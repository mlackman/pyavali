"""Common validators"""

class Not(object):
  """Composite validator callable
  Not(empty) - returns False when empty
  """

  def __init__(self, validator):
    self._validator = validator

  def __call__(self, value):
    return not self._validator(value)

def noneValue(value):
  """None value validator

  NoneValue(None) returns True
  NoneValue(1) returns False
  Not(NoneValue(None)) return False
  """
  return value == None

def empty(value):
  value = value or []
  return len(value) == 0


