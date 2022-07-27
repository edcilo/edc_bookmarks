import os


app_config = {
    'APP_NAME': os.getenv('APP_NAME', 'ms'),
    'APP_VERSION': os.getenv('APP_VERSION', '0.0.0'),
    'SECRET_KEY': os.getenv('APP_SECRET_KEY', None),
    'TIMEZONE': os.getenv('APP_TIMEZONE', 'UTC')
}
