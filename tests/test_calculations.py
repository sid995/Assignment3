'''Calculations test'''
from calculator.operations import add, multiply, subtract, divide

def test_addition():
  assert add(2, 2) == 4

def test_subtract():
  assert subtract(4, 2) == 2

def test_multiply():
  assert multiply(4, 2) == 8

def test_divide():
  assert divide(4, 2) == 2
  