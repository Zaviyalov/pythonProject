import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_multyply_calculate_faled(self):
        assert self.calc.multiply(self, 6, 2) == 6

    def test_division_calculate_correctry(self):
        assert self.calc.division(self, 4, 2) == 2

    def test_subtraction_calculate_correctre(self):
        assert self.calc.subtraction(self, 8, 6) == 2

    def test_adding_calculate_correctry(self):
        assert self.calc.adding(self, 4, 8) == 12