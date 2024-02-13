from typing import List
from calculator.calculation import Calculation

class Calculations:
  history: List[Calculation] = []

  @classmethod
  def get_history(cls) -> List[Calculation]:
    return cls.history
  
  @classmethod
  def add_calculation(cls, calculation: Calculation) -> List[Calculation]:
    return cls.history.append(calculation)
  
  @classmethod
  def clear_history(cls):
    cls.history.clear()

  @classmethod
  def get_latest(cls) ->Calculation:
    if cls.history:
      return cls.history[-1]
    return None
  
  @classmethod
  def find_by_operation(cls, operation_name: str) -> List[Calculation]:
    return [calc for calc in cls.history if calc.operation.__name__ == operation_name]