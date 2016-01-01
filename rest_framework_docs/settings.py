from django.conf import settings


class DRFSettings(object):

    def __init__(self):
        self.drf_settings = {
            "SHOW_DOCS": self.get_setting("SHOW_DOCS") or True
        }

    def get_setting(self, name):
        try:
            return settings.REST_FRAMEWORK_DOCS[name]
        except:
            return None

    @property
    def settings(self):
        return self.drf_settings
