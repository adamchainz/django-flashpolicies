.. _install:


Installation guide
==================

Before installing django-flashpolicies, you'll need to have a copy of
`Django <https://www.djangoproject.com>`_ already installed. For
information on obtaining and installing Django, consult the `Django
download page <https://www.djangoproject.com/download/>`_, which offers
convenient packaged downloads and installation instructions.

The |version| release of django-flashpolicies supports Django 1.8 and
1.9, on any Python version supported by those versions of Django:

* Django 1.8 suports Python 2.7, 3.2, 3.3, 3.4 and 3.5.

* Django 1.9 supports Python 2.7, 3.4 and 3.5.

.. important:: **Python 3.2**

   Although Django 1.8 supports Python 3.2, and django-flashpolicies
   |version| supports it, many Python libraries supporting Python 3
   impose a minimum requirement of Python 3.3 (due to conveniences
   added in Python 3.3 which make supporting Python 2 and 3 in the
   same codebase much simpler).

   As a result, use of Python 3.2 is discouraged; Django 1.9 has
   already dropped support for it, and a future release of
   django-flashpolicies will likely drop Python 3.2 support as well.


Normal installation
-------------------

The preferred method of installing django-flashpolicies is via
``pip``, the standard Python package-installation tool. If you don't
have ``pip``, instructions are available for `how to obtain and
install it <https://pip.pypa.io/en/latest/installing.html>`_.

Once you have ``pip``, simply type::

    pip install django-flashpolicies


Manual installation
-------------------

It's also possible to install django-flashpolicies manually. To do
so, obtain the latest packaged version from `the listing on the Python
Package Index
<https://pypi.python.org/pypi/django-flashpolicies/>`_. Unpack the
``.tar.gz`` file, and run::

    python setup.py install

Once you've installed django-flashpolicies, you can verify successful
installation by opening a Python interpreter and typing ``import
flashpolicies``.

If the installation was successful, you'll simply get a fresh Python
prompt. If you instead see an ``ImportError``, check the configuration
of your install tools and your Python import path to ensure
django-flashpolicies installed into a location Python can import from.


Installing from a source checkout
---------------------------------

The development repository for ``django-flashpolicies`` is at
<https://github.com/ubernostrum/django-flashpolicies>. Presuming you have `git
<http://git-scm.com/>`_ installed, you can obtain a copy of the
repository by typing::

    git clone https://github.com/ubernostrum/django-flashpolicies.git

From there, you can use normal git commands to check out the specific
revision you want, and install it using ``python setup.py install``.

