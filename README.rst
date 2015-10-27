kotti_compass
*************

This is an extension to Kotti that allows to add custom
stylesheets to your site.  This project uses compass_ to
help build the stylesheets and places them in a python package
subdirectory where these assets can be served through pyramid or
fanstatic.

This project includes scss versions of:
  - bootstrap
  - jquery-ui
  - font-awesome

This project is meant to be cloned so you can make stylesheets more
easily for any python project where an http server can serve static
assets from a python package.



|build status|_

`Find out more about Kotti`_

Development happens at https://github.com/umeboshi2/kotti_compass

.. |build status| image:: https://secure.travis-ci.org/umeboshi2/kotti_compass.png?branch=master
.. _build status: http://travis-ci.org/umeboshi2/kotti_compass
.. _Find out more about Kotti: http://pypi.python.org/pypi/Kotti

Setup
=====

To enable the extension in your Kotti site, activate the configurator::

    kotti.configurators =
        kotti_compass.kotti_configure

Development
===========

- todo: describe this

  - bundle install

  - compass compile

Contributions to kotti_compass are highly welcome.
Just clone its `Github repository`_ and submit your contributions as pull requests.

.. _alembic: http://pypi.python.org/pypi/alembic
.. _alembic documentation: http://alembic.readthedocs.org/en/latest/index.html
.. _tracker: https://github.com/umeboshi2/kotti_compass/issues
.. _Github repository: https://github.com/umeboshi2/kotti_compass
