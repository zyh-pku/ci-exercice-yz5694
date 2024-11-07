# src/unc/__init__.py
from __future__ import annotations

import math
import sys
from typing import Any

if sys.version_info < (3, 11):
    from typing_extensions import Self
else:
    from typing import Self


class LabUnc:
    @staticmethod
    def combine(a: float, b: float) -> float:
        return a + b

    rounding_rule = 1.0
    "This is the number to round at for display, lab rule is 1, particle physics uses 3.54"

    def __init__(self, number: float, uncertainty: float = 0.0) -> None:
        self.n = number
        self.s = abs(uncertainty)

    @property
    def ndigits(self) -> int:
        v = math.ceil(-math.log10(self.s) + math.log10(self.rounding_rule))
        return v if v > 0 else 0

    @property
    def max(self) -> float:
        return self.n + self.s

    @property
    def min(self) -> float:
        return self.n - self.s

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.n}, {self.s})"

    def __str__(self) -> str:
        return f"{self.n:0.{self.ndigits}f} ± {self.s:0.{self.ndigits}f}"

    def __eq__(self, other: Any) -> bool:
        return abs(self.n - other.n) < 0.0000001 and abs(self.s - other.s) < 0.0000001

    def __add__(self: Self, other: LabUnc) -> Self:
        return self.__class__(self.n + other.n, self.combine(self.s, other.s))

    def __sub__(self: Self, other: LabUnc) -> Self:
        return self.__class__(self.n - other.n, self.combine(self.s, other.s))

    def __mul__(self: Self, other: LabUnc) -> Self:
        C = self.n * other.n
        δC = C * self.combine(self.s / self.n, other.s / other.n)
        return type(self)(C, δC)

    def __truediv__(self: Self, other: LabUnc) -> Self:
        C = self.n / other.n
        δC = C * self.combine(self.s / self.n, other.s / other.n)
        return self.__class__(C, δC)

    def __pow__(self: Self, power: float) -> Self:
        C = self.n**power
        δC = C * (power * self.s / self.n)
        return self.__class__(C, δC)


class StdUnc(LabUnc):
    @staticmethod
    def combine(a: float, b: float) -> float:
        return math.sqrt(a**2 + b**2)
