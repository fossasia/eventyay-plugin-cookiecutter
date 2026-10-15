from django.utils.translation import gettext_lazy as _
from eventyay.base.plugins import PluginConfig

from . import __version__


class PluginApp(PluginConfig):
    default = True
    name = "{{cookiecutter.module_name}}"
    verbose_name = _("{{cookiecutter.human_name}}")

    class EventyayPluginMeta:
        name = _("{{cookiecutter.human_name}}")
        author = "{{cookiecutter.author_name}}"
        description = _("{{cookiecutter.short_description}}")
        visible = True
        version = __version__
        category = "{{cookiecutter.category}}"

    def ready(self):
        from . import signals  # NOQA
