passwortpranger
===============

.. image:: https://secure.travis-ci.org/dbrgn/passwortpranger.png?branch=master
    :alt: Build status
    :target: http://travis-ci.org/dbrgn/passwortpranger


Eine Webplatform, um Firmen die unsorgfältig mit Passwörtern umgehen an den
virtuellen Pranger zu stellen.

Dev Setup
---------

Clone repository::

    git clone https://github.com/dbrgn/passwortpranger.git
    cd paswortpranger

Setup virtualenv::

    mkvirtualenv pranger

Install dependencies::

    pip install -r requirements/dev.txt

Set environment variables::

    POSTACTIVATE=$VIRTUAL_ENV/$VIRTUALENVWRAPPER_ENV_BIN_DIR/postactivate
    echo "export DJANGO_DEBUG=True" >> $POSTACTIVATE
    echo "export DATABASE_URL='postgres://localhost/pranger'" >> $POSTACTIVATE
    source $POSTACTIVATE

Initialize database::

    createdb pranger
    cd pranger
    ./manage.py migrate

Test setup::

    ./runtests.py
    ./manage.py runserver

There should be at least two passing test (and no fails).

Deployment
----------

.. image:: https://www.herokucdn.com/deploy/button.png
    :alt: Deploy to Heroku
    :target: https://heroku.com/deploy?template=https://github.com/dbrgn/passwortpranger

Testing
-------

- Testing is set up using pytest_.
- You can use the ``runtests.py`` script to run all tests and show coverage
  information afterwards.
- PEP8 violations in the project directory (excluding tests and migrations) are
  counted as errors. PEP8 errors E126, E127 and E128 are ignored. Max line
  length is set to 99 characters.
- Coverage configuration is at ``pranger/.coveragerc``.
- Pytest configuration is at ``pranger/pytest.ini``.
- To speed up tests, you can use the ``--reuse-db`` option to avoid destroying
  the database after a test run. Don't use this option after model changes,
  otherwise tests will fail.

License
-------

MIT, see ``LICENSE`` file.

.. _pytest: http://pytest.org/
