import sys
from importlib.metadata import entry_points

from django.apps import apps
from eventyay.base.plugins import PluginConfig, get_all_plugins

from {{cookiecutter.module_name}} import __version__


def test_plugin_entry_point():
    entries = [
        entry
        for entry in entry_points(group="pretix.plugin")
        if entry.name == "{{cookiecutter.module_name}}"
    ]
    assert len(entries) == 1
    assert entries[0].module == "{{cookiecutter.module_name}}"
    assert entries[0].load().__version__ == __version__


def test_plugin_discovery():
    config = apps.get_app_config("{{cookiecutter.module_name}}")
    assert isinstance(config, PluginConfig)
    assert config.name == "{{cookiecutter.module_name}}"
    assert config.EventyayPluginMeta.version == __version__
    assert config.EventyayPluginMeta.category == "{{cookiecutter.category}}"
    assert "{{cookiecutter.module_name}}.signals" in sys.modules
    assert config.EventyayPluginMeta in get_all_plugins(include_inactive=True)
