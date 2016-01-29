# Licensed under a 3-clause BSD style license - see LICENSE.rst
import numpy as np

from astropy.nddata import support_nddata
from astropy.utils.metadata import MetaData
from astropy.units.quantity import Quantity

from warnings import warn

from .wcs import WCSTable

class Spectrum1D(object):
    meta = MetaData()

    @support_nddata
    def __init__(self, data, dispersion=None, dispersion_unit=None,
                 uncertainty=None, mask=None, meta=None, unit=None,
                 flags=None):

    self.meta = meta

    data = Quantity(data, unit)

    if mask is None:
        self.data = data
    else:
        self.data = np.ma.asanyarray(data)
        self.data[mask] = np.ma.masked

    if wcs is None:
        if dispersion is None:
            raise ValueError('Specify dispersion or WCS, but not both.')
        else:
            if len(self.data) != len(self.dispersion):
                raise ValueError('Data and dispersion need to have same number of elements.')

            self.wcs = WCSTable(dispersion, dispersion_unit)
    else:
        self.wcs = wcs


    # For now, just save it. We can do stuff with that later.
    self.uncertainty = uncertainty
    self.flags = flags

    # Two examples how we can interact with a WCS
    # If we do this, we have to specify that all WCS are slicable and have a shift_rv.
    def shift_rv(self, rv):
        '''Shift spectrum by rv

        Parameters
        ----------
        rv : `~astropy.units.quantity.Quantity`
            radial velocity (positive value will red-shift the spectrum, negative
            value will blue-shift the spectrum)
        '''
        self.wcs.shift_rv(rv)

    def slice_dispersion(self, x0, x1):
        ind = self.wcs.between(x0, x1)
        flags = None if self.flags is None else self.flags[ind]
        uncertainty = None if self.uncertainty is None else self.uncertainty[ind]

        return self.__class__(self.data[ind], self.wcs[ind], meta=self.meta,
                              flags=flags, uncertainty=uncertainty)
