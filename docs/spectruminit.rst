Initializing a `~astrospec.spectrum1d.Spectum1D` object
=======================================================

.. _spectrumfromnumpy:

Initialize a spectrum from numpy arrays
---------------------------------------

The `~astrospec.spectrum1d.Spectum1D` class takes the same initialization parameters
as `astropy.nddata.NDData`, for a detailed description see the astropy documentation.
The one important difference is the world coordiante system, see below for details.

Here is an exmaple::

    import numpy as np
    import astropy.units as u
    from astrospec import Spectrum1D
    from astrospec.wcs import WCSTable

    # some random data as an example
    wave = np.arange(1000., 1100.)
    wcs = WCSTable(wave, u.Angstroem)

    flux = np.random.rand(100.)
    my_spec = Spectrum1D(data=flux, unit=u.erg/u.s/u.Angstrom, wcs=wcs)

World Coordinate System (WCS)
-----------------------------
The world coordinate system maps bin number in the spectrum to a dispersion coordiante, e.g. a wavelength or frequency.

.. automodapi:: astrospec.wcs
