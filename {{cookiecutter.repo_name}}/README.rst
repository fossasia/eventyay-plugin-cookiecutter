{{cookiecutter.human_name}}
==========================

This is a plugin for `pretix`_. 

{{ cookiecutter.short_description }}

Development setup
-----------------

1. Make sure that you have a working `pretix development setup`_.

2. Clone this repository, eg to ``local/{{ cookiecutter.repo_name }}``.

3. Activate the virtual environment you use for pretix development.

4. Execute ``python setup.py develop`` within this directory to register this application with pretix's plugin registry.

5. Execute ``make`` within this directory to compile translations.

6. Restart your local pretix server. You can now use the plugin from this repository for your events by enabling it in
   the 'plugins' tab in the settings.


License
-------

{% if cookiecutter.license == "Apache" %}
Copyright {{cookiecutter.year}} {{cookiecutter.author_name}}

Released under the terms of the Apache License 2.0
{% elif cookiecutter.license == "pretix Enterprise" %}
Copyright {{cookiecutter.year}} Raphael Michel

Released under the terms of the proprietary pretix Enterprise license.
{% endif %}


.. _pretix: https://github.com/pretix/pretix
.. _pretix development setup: https://docs.pretix.eu/en/latest/development/setup.html
