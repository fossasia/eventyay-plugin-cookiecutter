pretix-plugin-cookiecutter
==========================

A simple `cookiecutter`_ template to bootstrap a `pretix`_ plugin.

Usage
-----

Let's pretend you want to create a pretix plugin called "superplugin".
First, create a virtual environment and install the ``cookiecutter``
package using pip. Next, use it to bootstrap your project folder::

    $ cd <your-project-folder-parent>
    $ cookiecutter https://github.com/pretix/pretix-plugin-cookiecutter


You'll be prompted for some questions. Answer them, and you will find a
project folder created for you::

    repo_name [pretix-superplugin]: pretix-superplugin
    repo_url [GitHub repository URL]: https://github.com/myuser/pretix-superplugin
    module_name [pretix_superplugin]: pretix_superplugin
    human_name [The pretix super plugin]: Super Plugin
    author_name [Your name]: J Random Developer
    author_email [Your email]: jrandom@example.org
    short_description [Short description]: The best plugin
    Select license:
    1 - Apache
    2 - pretix Enterprise
    Choose from 1, 2 [1]: 1
    min_basever [2.7.0]: 2.7.0
    Select category:
    1 - FEATURE
    2 - PAYMENT
    3 - INTEGRATION
    4 - CUSTOMIZATION
    5 - FORMAT
    6 - API
    Choose from 1, 2, 3, 4, 5, 6 [1]: 1


Now, change to the newly created directory::

    $ cd pretix-superplugin

Voilà, there's your plugin structure! See pretix' `documentation`_ for more info.

.. _pretix: https://github.com/pretix/pretix
.. _cookiecutter: https://github.com/audreyr/cookiecutter
.. _documentation: https://docs.pretix.eu/en/latest/development/api/plugins.html#pluginsetup
