import logging
import os

from olympia.lib.settings_base import *  # noqa


ENGAGE_ROBOTS = True

EMAIL_URL = env.email_url('EMAIL_URL')
EMAIL_HOST = EMAIL_URL['EMAIL_HOST']
EMAIL_PORT = EMAIL_URL['EMAIL_PORT']
EMAIL_BACKEND = EMAIL_URL['EMAIL_BACKEND']
EMAIL_HOST_USER = EMAIL_URL['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = EMAIL_URL['EMAIL_HOST_PASSWORD']

SEND_REAL_EMAIL = True

ENV = env('ENV')

API_THROTTLE = False

CDN_HOST = 'https://addons.cdn.mozilla.net'
DOMAIN = env('DOMAIN', default='addons.mozilla.org')
SERVER_EMAIL = 'zprod@addons.mozilla.org'
SITE_URL = 'https://' + DOMAIN
SERVICES_URL = env('SERVICES_URL',
                   default='https://services.addons.mozilla.org')
STATIC_URL = '%s/static/' % CDN_HOST
MEDIA_URL = '%s/user-media/' % CDN_HOST

SESSION_COOKIE_DOMAIN = ".%s" % DOMAIN

# Domain emails should be sent to.
INBOUND_EMAIL_DOMAIN = env('INBOUND_EMAIL_DOMAIN',
                           default='addons.mozilla.org')

NETAPP_STORAGE_ROOT = env('NETAPP_STORAGE_ROOT')
NETAPP_STORAGE = NETAPP_STORAGE_ROOT + '/shared_storage'
GUARDED_ADDONS_PATH = NETAPP_STORAGE_ROOT + '/guarded-addons'
MEDIA_ROOT = NETAPP_STORAGE + '/uploads'

TMP_PATH = os.path.join(NETAPP_STORAGE, 'tmp')
PACKAGER_PATH = os.path.join(TMP_PATH, 'packager')

ADDONS_PATH = NETAPP_STORAGE_ROOT + '/files'

REVIEWER_ATTACHMENTS_PATH = MEDIA_ROOT + '/reviewer_attachment'

DATABASES = {
    'default': get_db_config('DATABASES_DEFAULT_URL'),
    'slave': get_db_config('DATABASES_SLAVE_URL'),
}

SERVICES_DATABASE = get_db_config('SERVICES_DATABASE_URL')

SLAVE_DATABASES = ['slave']

CACHE_MIDDLEWARE_KEY_PREFIX = CACHE_PREFIX

CACHES = {}
CACHES['default'] = env.cache('CACHES_DEFAULT')
CACHES['default']['TIMEOUT'] = 500
CACHES['default']['BACKEND'] = 'django.core.cache.backends.memcached.MemcachedCache'  # noqa
CACHES['default']['KEY_PREFIX'] = CACHE_PREFIX

# Celery
CELERY_BROKER_CONNECTION_TIMEOUT = 0.5

LOGGING['loggers'].update({
    'adi.updatecounts': {'level': logging.INFO},
    'amqp': {'level': logging.WARNING},
    'raven': {'level': logging.WARNING},
    'requests': {'level': logging.WARNING},
    'z.addons': {'level': logging.INFO},
    'z.task': {'level': logging.DEBUG},
    'z.pool': {'level': logging.ERROR},
})

ES_TIMEOUT = 60
ES_HOSTS = env('ES_HOSTS')
ES_URLS = ['http://%s' % h for h in ES_HOSTS]
ES_INDEXES = dict((k, '%s_%s' % (v, ENV)) for k, v in ES_INDEXES.items())


CEF_PRODUCT = STATSD_PREFIX

NEW_FEATURES = True

ADDONS_LINTER_BIN = 'node_modules/.bin/addons-linter'

XSENDFILE_HEADER = 'X-Accel-Redirect'

NEWRELIC_ENABLE = env.bool('NEWRELIC_ENABLE', default=False)

if NEWRELIC_ENABLE:
    NEWRELIC_INI = '/etc/newrelic.d/%s.ini' % DOMAIN

FXA_CONFIG = {
    'default': {
        'client_id': env('FXA_CLIENT_ID'),
        'client_secret': env('FXA_CLIENT_SECRET'),
        'content_host': 'https://accounts.firefox.com',
        'oauth_host': 'https://oauth.accounts.firefox.com/v1',
        'profile_host': 'https://profile.accounts.firefox.com/v1',
        'redirect_url':
            'https://%s/api/v3/accounts/authenticate/' % DOMAIN,
        'scope': 'profile',
    },
    'amo': {
        'client_id': env('AMO_FXA_CLIENT_ID'),
        'client_secret': env('AMO_FXA_CLIENT_SECRET'),
        'content_host': 'https://accounts.firefox.com',
        'oauth_host': 'https://oauth.accounts.firefox.com/v1',
        'profile_host': 'https://profile.accounts.firefox.com/v1',
        'redirect_url':
            'https://addons.mozilla.org/api/v3/accounts/authenticate/',
        'scope': 'profile',
        'skip_register_redirect': True,
    },
}
DEFAULT_FXA_CONFIG_NAME = 'default'
ALLOWED_FXA_CONFIGS = ['default', 'amo']

VALIDATOR_TIMEOUT = 360

ES_DEFAULT_NUM_SHARDS = 10

RAVEN_JS_DSN = (
    'https://8c1c5936578948a9a0614cbbafccf049@sentry.prod.mozaws.net/78')
RAVEN_JS_ALLOW_LIST = ['addons.mozilla.org', 'addons.cdn.mozilla.net']


RECOMMENDATION_ENGINE_URL = env(
    'RECOMMENDATION_ENGINE_URL',
    default='https://taar.prod.mozaws.net/api/recommendations/')

TAAR_LITE_RECOMMENDATION_ENGINE_URL = env(
    'TAAR_LITE_RECOMMENDATION_ENGINE_URL',
    default=('https://taarlite.prod.mozaws.net/taarlite/api/v1/'
             'addon_recommendations/'))

FXA_SQS_AWS_QUEUE_URL = (
    'https://sqs.us-west-2.amazonaws.com/361527076523/'
    'amo-account-change-prod')

DRF_API_VERSIONS = ['v3', 'v4']
DRF_API_REGEX = r'^/?api/(?:v3|v4)/'
