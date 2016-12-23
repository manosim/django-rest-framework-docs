from django.conf import settings


class DRFSettings(object):

    def __init__(self):
        self.drf_settings = {
            "HIDE_DOCS": self.get_setting("HIDE_DOCS") or False,
            "MODULE_ROUTERS": self.get_setting("MODULE_ROUTERS"),
            "DEFAULT_MODULE_ROUTER": self.get_setting("DEFAULT_MODULE_ROUTER"),
            "DEFAULT_ROUTER": self.get_setting("DEFAULT_ROUTER")
        }

    def get_setting(self, name):
        try:
            return settings.REST_FRAMEWORK_DOCS[name]
        except:
            return None

    @property
    def settings(self):
        return self.drf_settings
