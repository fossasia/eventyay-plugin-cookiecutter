eventyay-plugin-cookiecutter
==========================

A simple `cookiecutter`_ template to bootstrap a `eventyay`_ plugin.

Usage
-----

Let's pretend you want to create a eventyay plugin called "superplugin".
First, create a virtual environment and install the ``cookiecutter``
package using pip. Next, use it to bootstrap your project folder::

    $ cd <your-project-folder-parent>
    $ cookiecutter https://github.com/fossasia/eventyay-plugin-cookiecutter


You'll be prompted for some questions. Answer them, and you will find a
project folder created for you::

    repo_name [eventyay-superplugin]: eventyay-superplugin
    repo_url [GitHub repository URL]: https://github.com/myuser/eventyay-superplugin
    module_name [eventyay_superplugin]: eventyay_superplugin
    human_name [The eventyay super plugin]: Super Plugin
    author_name [Your name]: J Random Developer
    author_email [Your email]: jrandom@example.org
    short_description [Short description]: The best plugin
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

    $ cd eventyay-superplugin

Voilà, there's your plugin structure! See eventyay' `documentation`_ for more info.

.. _eventyay: https://github.com/eventyay/eventyay
.. _cookiecutter: https://github.com/audreyr/cookiecutter
.. _documentation: https://docs.eventyay.eu/en/latest/development/api/plugins.html#pluginsetup
