from django.utils.translation import gettext_lazy

try:
    from pretix.base.plugins import PluginConfig
except ImportError:
    raise RuntimeError("Please use pretix 2.7 or above to run this plugin!")

__version__ = '1.0.0'


class PluginApp(PluginConfig):
    name = '{{cookiecutter.module_name}}'
    verbose_name = '{{cookiecutter.human_name}}'

    class PretixPluginMeta:
        name = gettext_lazy('{{cookiecutter.human_name}}')
        author = '{{cookiecutter.author_name}}'
        description = gettext_lazy('{{cookiecutter.short_description}}')
        visible = True
        version = __version__
        category = '{{cookiecutter.category}}'
        compatibility = "pretix>={{cookiecutter.min_basever}}"

    def ready(self):
        from . import signals  # NOQA


default_app_config = '{{cookiecutter.module_name}}.PluginApp'
