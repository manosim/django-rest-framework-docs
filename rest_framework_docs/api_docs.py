from importlib import import_module
from types import ModuleType
from django.conf import settings
from django.core.urlresolvers import RegexURLResolver, RegexURLPattern
from django.utils.module_loading import import_string
from rest_framework.views import APIView
from rest_framework.routers import BaseRouter
from rest_framework_docs.api_endpoint import ApiNode, ApiEndpoint
from rest_framework_docs.settings import DRFSettings


drf_settings = DRFSettings().settings


class ApiDocumentation(object):

    def __init__(self, drf_router=None):
        self.endpoints = []
        self.drf_router = drf_router

        try:
            root_urlconf = import_string(settings.ROOT_URLCONF)
        except ImportError:
            # Handle a case when there's no dot in ROOT_URLCONF
            root_urlconf = import_module(settings.ROOT_URLCONF)
        if hasattr(root_urlconf, 'urls'):
            self.get_all_view_names(root_urlconf.urls.urlpatterns)
        else:
            self.get_all_view_names(root_urlconf.urlpatterns)

    def get_all_view_names(self, urlpatterns, parent_api_node=None):
        for pattern in urlpatterns:
            if isinstance(pattern, RegexURLResolver):
                # Try to get router from settings, if no router is found,
                # Use the instance drf_router property.
                router = get_router(pattern)
                if router is None:
                    parent_router = None
                    if parent_api_node is not None:
                        parent_router = parent_api_node.drf_router
                    if parent_router is not None:
                        router = parent_router
                    else:
                        router = self.drf_router
                if pattern._regex == "^":
                    parent = parent_api_node
                else:
                    parent = ApiNode(
                        pattern,
                        parent_node=parent_api_node,
                        drf_router=router
                    )
                self.get_all_view_names(urlpatterns=pattern.url_patterns, parent_api_node=parent)
            elif isinstance(pattern, RegexURLPattern) and _is_drf_view(pattern) and not _is_format_endpoint(pattern):
                router = self.drf_router
                if parent_api_node is not None:
                    if parent_api_node.drf_router is not None:
                        router = parent_api_node.drf_router
                api_endpoint = ApiEndpoint(pattern, parent_api_node, router)
                self.endpoints.append(api_endpoint)

    def get_endpoints(self):
        return self.endpoints


def _is_drf_view(pattern):
    """
    Should check whether a pattern inherits from DRF's APIView
    """
    return hasattr(pattern.callback, 'cls') and issubclass(pattern.callback.cls,
                                                           APIView)


def _is_format_endpoint(pattern):
    """
    Exclude endpoints with a "format" parameter
    """
    return '?P<format>' in pattern._regex


def get_router(pattern):
    urlconf = pattern.urlconf_name
    router = None
    if isinstance(urlconf, ModuleType):
        # First: try MODULE_ROUTERS setting - Don't ignore errors
        router = get_module_router(urlconf)
        if router is not None:
            return router
        # Second: try DEFAULT_MODULE_ROUTER setting - Ignore errors
        try:
            router = get_default_module_router(urlconf)
            if router is not None:
                return router
        except:
            pass
        # Third: try DEFAULT_ROUTER setting - Don't ignore errors
        router = get_default_router()
        if router is not None:
            return router
    return router


def get_module_router(module):
    routers = drf_settings['MODULE_ROUTERS']
    if routers is None:
        return None
    if module.__name__ in routers:
        router_name = routers[module.__name__]
        router = getattr(module, router_name)
        assert isinstance(router, BaseRouter), \
            """
            drfdocs 'ROUTERS' setting does not correspond to
            a router instance for module {}.
            """.format(module.__name__)
        return router
    return None


def get_default_module_router(module):
    default_module_router = drf_settings['DEFAULT_MODULE_ROUTER']
    if default_module_router is None:
        return None
    router = getattr(module, default_module_router)
    assert isinstance(router, BaseRouter), \
        """
        drfdocs 'DEFAULT_MODULE_ROUTER' setting does not correspond to
        a router instance for module {}.
        """.format(module.__name__)
    return router


def get_default_router():
    default_router_path = drf_settings['DEFAULT_ROUTER']
    if default_router_path is None:
        return None
    router = import_string(default_router_path)
    assert isinstance(router, BaseRouter), \
        """
        drfdocs 'DEFAULT_ROUTER_NAME' setting does not correspond to
        a router instance {}.
        """.format(router.__name__)
    return router
