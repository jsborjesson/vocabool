#
# Insert your credentials here, and rename this file to `credentials.py`.
#

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Use this as headers in all outgoing api-requests
USER_AGENT = {
    'User-Agent': 'MyCoolApp (http://myurl.com; myemail@example.com)'
}

YANDEX_TRANSLATE_API_KEY = 'YOUR_YANDEX_TRANSLATE_KEY'
