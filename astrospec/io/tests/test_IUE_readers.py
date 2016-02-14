import os
import pytest

import astropy.units as u

from ..IUE import ApertureException
from ...spectrum1d import Spectrum1D
from . import data_path


def test_mxlo():
    spec1 = Spectrum1D.read(data_path('lwp11854.mxlo'))
    assert spec1.meta['LDATEOBS'] == '11/10/87'


    spec3 = Spectrum1D.read(data_path('swp02283.mxlo'), aperture='SMALL')
    # specifying the format by hand should also work
    spec4 = Spectrum1D.read(data_path('swp02283.mxlo'), format='IUE-mxlo', aperture='LARGE')
    assert spec3.wcs[0].value == 1050.
    assert abs(spec3.wcs[1] - (1050. + 1.676338) * u.Angstrom) < 1e-4 * u.Angstrom


def test_multiple_apertures_exception():
    pytest.raises(ApertureException, Spectrum1D.read, data_path('swp02283.mxlo'))
    pytest.raises(ApertureException, Spectrum1D.read, data_path('swp02283.mxlo'), aperture = 'XXX')
