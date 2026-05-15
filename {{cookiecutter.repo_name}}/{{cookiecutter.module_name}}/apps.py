from django.utils.translation import gettext_lazy as _

from . import __version__

try:
    from eventyay.base.plugins import PluginConfig
except ImportError:
    raise RuntimeError("Please use a later version of eventyay-tickets")


class PluginApp(PluginConfig):
    default = True
    name = "{{cookiecutter.module_name}}"
    verbose_name = _("{{cookiecutter.human_name}}")

    class PretixPluginMeta:
        name = _("{{cookiecutter.human_name}}")
        author = "{{cookiecutter.author_name}}"
        description = _("{{cookiecutter.short_description}}")
        visible = True
        version = __version__
        category = "{{cookiecutter.category}}"

    def ready(self):
        from . import signals  # NOQA
