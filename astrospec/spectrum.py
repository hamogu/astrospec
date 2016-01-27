# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""Module for the Spectrum object and related functionality."""

from astropy.nddata import NDData


class SpectrumError(Exception):
    """Primary exception specific to the Spectrum object."""


class Spectrum1D:
    """A spectrum object wraps an Astropy NDData array plus metadata."""

    def __init__(self, data=None, wcs=None, filepath=None, **kwargs):
        """Initialize via either an already existing data array or from a file."""
