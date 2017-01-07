from django.apps import AppConfig


class PluginApp(AppConfig):
    name = '{{cookiecutter.module_name}}'
    verbose_name = '{{cookiecutter.human_name}}'

    class PretixPluginMeta:
        name = '{{cookiecutter.human_name}}'
        author = '{{cookiecutter.author_name}}'
        description = '{{cookiecutter.short_description}}'
        visible = True
        version = '1.0.0'

    def ready(self):
        from . import signals  # NOQA


default_app_config = '{{cookiecutter.module_name}}.PluginApp'
