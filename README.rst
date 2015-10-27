kotti_compass
*************

This is an extension to Kotti that allows to add foo to your site.

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

Database upgrade
================

If you are upgrading from a previous version you might have to migrate your
database.  The migration is performed with `alembic`_ and Kotti's console script
``kotti-migrate``. To migrate, run
``kotti-migrate upgrade --scripts=kotti_compass:alembic``.

For integration of alembic in your environment please refer to the
`alembic documentation`_. If you have problems with the upgrade,
please create a new issue in the `tracker`_.

Development
===========

Contributions to kotti_compass are highly welcome.
Just clone its `Github repository`_ and submit your contributions as pull requests.

.. _alembic: http://pypi.python.org/pypi/alembic
.. _alembic documentation: http://alembic.readthedocs.org/en/latest/index.html
.. _tracker: https://github.com/umeboshi2/kotti_compass/issues
.. _Github repository: https://github.com/umeboshi2/kotti_compass
