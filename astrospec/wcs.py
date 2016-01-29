# Licensed under a 3-clause BSD style license - see LICENSE.rst
import numpy as np

from astropy.units.quantity import Quantity
from astropy.constants import c as c_light
import astropy.units as u

class WCSTable(Quantity):

    def between(x0, x1):
        '''
        Could be more clever.
        Currently, this is only a proof of concept.
        For now, it only works if the WCS table and the x0, x1 have
        compatible dimesiones, e.g. dimension of lengths.
        Using spectral equivalencies, we could have a WCS in nm,
        but pass x0, x1 in Hz or keV and it would work.
        '''
        return (self >= x0) & (self < x1)

    def shift_rv(self, rv):
        '''Shift spectrum by rv

        Parameters
        ----------
        rv : `~astropy.units.quantity.Quantity`
            radial velocity (positive value will red-shift the spectrum, negative
            value will blue-shift the spectrum)
        '''
        self[:] = (self.to(u.m, equivalencies=u.spectral()) * (
                1.*u.dimensionless_unscaled+rv/const.c)).to(
                self.unit, equivalencies=u.spectral())
