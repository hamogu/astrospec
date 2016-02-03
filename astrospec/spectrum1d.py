# Licensed under a 3-clause BSD style license - see LICENSE.rst
import numpy as np
from scipy inport interpolate

from astropy.nddata import NDData, NDIOMixin, NDSlicingMixin
from astropy.utils.metadata import MetaData
from astropy import units as u

from warnings import warn


class Spectrum1D(NDSlicingMixin, NDIOMixin, NDData):
    """A 1 dimensionan spectrum.
    
    See `astropy.nddata.NDData` for a description of the parameters.
    """

    def shift_rv(self, rv):
        '''Shift spectrum by rv

        Parameters
        ----------
        rv : :class:`~astropy.quantity.Quantity`
            radial velocity (positive value will red-shift the spectrum, negative
            value will blue-shift the spectrum)
        '''
        self.wcs.shift_rv(rv)

    def interpol(self, new_dispersion,  **kwargs):
        '''Interpolate a spectrum onto a new dispersion axis.

        Parameters
        ----------
        new_dispersion : :class:`~astropy.quantity.Quantity`
           The new dispersion axis.

        All other keywords are passed directly to scipy.interpolate.interp1d.

        Returns
        -------
        spec : :class:`~astrospec.Spectrum1d`
            A new spectrum.
        '''
        new_disp = new_dispersion.to(self.wcs.unit, equivalencies=u.spectral())

        f_flux = interpolate.interp1d(self.wcs.data, self.data, **kwargs)
        newflux = f_flux(new_disp)

        new_wcs=WCSTable(new_dispersion)

        if self.uncertainty is not None:
            warnings.warn('The uncertainty column is interpolated.' +
                         'Bins are no longer independent and might require scaling.' +
                         'It is up to the user the decide if the uncertainties are still meaningful.')
            f_uncert = interpolate.interp1d(self.wcs.data, self.uncertainty, **kwargs)

        return self.__class__(data=newflux, unit=self.unit, meta=self.meta,
                              wcs=new_wcs, uncertainty=f_uncert, 
                              uncertainty=self.uncertainty)

