USE_I18N = False
SECRET_KEY = "test_secret_key"

LOGGING = {
    "version": 1,  # the dictConfig format version
    "disable_existing_loggers": False,  # retain the default loggers
    "handlers": {
        "console": {"class": "logging.StreamHandler", "level": "DEBUG"},
    },
    "loggers": {
        "django": {"level": "DEBUG", "handlers": ["console"]},
        "{{ cookiecutter.project_slug }}": {"level": "DEBUG", "handlers": ["console"]},
    },
}
