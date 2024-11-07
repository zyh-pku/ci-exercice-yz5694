import itertools

import pytest
from uncertainties import ufloat

from unc import StdUnc

CASES = ((10, 1), (10, 2), (20, 0.1), (10, 0.1), (0.1234, 0.02))
pairs = pytest.mark.parametrize("a,b", list(itertools.permutations(CASES, 2)))


@pairs
def test_add(a, b):
    assert StdUnc(*a) + StdUnc(*b) == ufloat(*a) + ufloat(*b)


@pairs
def test_sub(a, b):
    assert StdUnc(*a) - StdUnc(*b) == ufloat(*a) - ufloat(*b)


@pairs
def test_mul(a, b):
    assert StdUnc(*a) * StdUnc(*b) == ufloat(*a) * ufloat(*b)


@pairs
def test_div(a, b):
    assert StdUnc(*a) / StdUnc(*b) == ufloat(*a) / ufloat(*b)
