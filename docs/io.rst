.. _readingfiles:

Reading a spectrum from a file
==============================

Unfortunately, there is a no single common format to store spectra in astronomy. Instead a number of different conventions are used by different communities and different observatories. For example, HST data is distributed as a fits table with columns for wavelenght and flux (and some others); in contrast, IRAF users often work with spetra where the flux data is encoded in the primary fits data unit (like an image) and the wavelength is given through header keywords.

This package supplies routines to read many common file formats, but it will never be complete (we welcome contributions!). If the format you need is not in the list you have two options:

- Read in the data by hand into numpy arrays by whatever means necessary and :ref:`spectrumfromnumpy`.
- Write a method and register it with `astropy.io.registry`. See the code of the existing
  readers in the ``astrospec/io/`` directory of the source code.

The following formats are implemented at this time:

============= ======== ================================================================
format name   identify description
============= ======== ================================================================
``IUE-mxlo``  yes      IUE data downloaded from https://archive.stsci.edu/iue/
============= ======== ================================================================

Reading a file with a know format is simple:

    # Get the path to a file that's included in astrospec as an example
    from astropec.io.tests import data_path
    filename = data_path('lwp11854.mxlo')

    from astrospec import Spectrum1D
    my_spec = Spectum1D.read(filename, format='IUE-mxlo')

For convenience, some formats can be automatically identified from the file name or file format - those are marked with "yes" in the identify column of the table above. In this case, you can just pass in the filename (however, this is slower than specifying the format directly):

        my_spec = Spectum1D.read(filename)
