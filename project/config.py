class DefaultConfig(object):
    DEFAULT_APP_NAME = 'CovidYaar'
    SECRET_KEY = "OAx3Qghf0x8G^q^^dt#mNabd6*EF7U"
    MODULES = [
        "user",
        "main",
    ]
    DEBUG = False
    TEMPLATE_DIR = 'templates'
    TEMPLATE_NAME = 'Simple'
    SITE_NAME = u'کووید یار ایران'

class DevelopmentConfig(DefaultConfig):
    DEBUG = True
    TESTING = True