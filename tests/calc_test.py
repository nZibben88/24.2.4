import pytest

from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_success(self):
        assert self.calc.multiply(self, 12, 4) == 48

    def test_division_success(self):
        assert self.calc.division(self, 12, 4) == 3

    def test_subtraction_success(self):
        assert self.calc.subtraction(self, 12, 4) == 8

    def test_adding_success(self):
        assert self.calc.adding(self, 12, 4) == 16