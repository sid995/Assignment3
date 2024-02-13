from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

class Calculator:
  @staticmethod
  def add(a, b):
    calculation = Calculation(a, b, add)
    return calculation.perform()
  
  @staticmethod
  def subtract(a, b):
    calculation = Calculation(a, b, subtract)
    return calculation.perform()
  
  @staticmethod
  def multiply(a, b):
    calculation = Calculation(a, b, multiply)
    return calculation.perform()
  
  @staticmethod
  def divide(a, b):
    calculation = Calculation(a, b, divide)
    return calculation.perform()