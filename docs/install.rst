************
Installation
************

Requirements
============

Astrospec has the following requirements:

- `Astropy`_ v1.1 or later
- `Numpy <http://www.numpy.org/>`_
- `SciPy <http://www.scipy.org/>`_

One easy way to get these dependencies is to install a python distribution like `anaconda <http://continuum.io/>`_.

Installing astrospec
====================

.. comment NOT on PIPY yet

   Using pip
   -------------

   To install astrospec with `pip <http://www.pip-installer.org/en/latest/>`_, simply run::

       pip install --no-deps astrospec

   .. note::

       The ``--no-deps`` flag is optional, but highly recommended if you already
       have Numpy installed, since otherwise pip will sometimes try to "help" you
       by upgrading your Numpy installation, which may not always be desired.

Building from source
====================

Obtaining the source packages
-----------------------------

Source packages
^^^^^^^^^^^^^^^

At this early stage of development not source packages are available.

.. comment Not on PiPy yet
   The latest stable source package for astrospec can be `downloaded here
   <https://pypi.python.org/pypi/astrospec>`_.

Development repository
^^^^^^^^^^^^^^^^^^^^^^

The latest development version of astrospec can be cloned from github
using this command::

   git clone git://github.com/hamogu/astrospec.git

Building and Installing
-----------------------

To build astrospec (from the root of the source tree)::

    python setup.py build

To install astrospec (from the root of the source tree)::

    python setup.py install

Testing a source code build of astrospec
----------------------------------------

The easiest way to test that your astrospec built correctly (without
installing it) is to run this from the root of the source tree::

    python setup.py test
