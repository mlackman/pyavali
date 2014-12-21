"""Common validators"""

class Not(object):
  """Composite validator callable
  Not(empty) - returns False when empty
  """

  def __init__(self, validator):
    self._validator = validator

  def __call__(self, value):
    return not self._validator(value)



def empty(value):
  value = value or []
  return len(value) == 0


