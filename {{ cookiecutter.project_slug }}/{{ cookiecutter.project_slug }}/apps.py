from django.apps import AppConfig


class {{ cookiecutter.project_slug.split('_')|map('capitalize')|join }}Config(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "{{ cookiecutter.project_slug }}"
