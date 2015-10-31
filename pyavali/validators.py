"""Common validators"""
from string import Template

class Not(object):
  """Composite validator callable
  Not(empty) - returns False when empty
  """

  def __init__(self, validator):
    self._validator = validator

  def __call__(self, value):
    return not self._validator(value)

class And(object):
  """Composite of validators.
  And(validators) - returns True when all validators are true
  """

  def __init__(self, *args):
    self._validators = args

  def message(self, value):
    validator = self._failing_validator(value)
    if hasattr(validator, 'message'):
      return validator.message(value)

  def __call__(self, value):
    return self._failing_validator(value) == None

  def _failing_validator(self, value):
     for validator in self._validators:
       if not validator(value):
         return validator

class Range(object):
  "Range validation min <= validated value <= max"

  def __init__(self, min, max, message=None):
    """Creates Range instance.
    min - minimum value the validated values must be at least
    max - maximum value the validated value can be.
    message - custom message. for example "must be in range [$min, $max]"
    """
    self._min = min
    self._max = max
    self._template= Template(message or "must be in range [$min, $max], got $value")

  def __call__(self, value):
    return self._min <= value <= self._max

  def message(self, value):
    return self._template.safe_substitute(min=self._min, max=self._max, value=str(value))

class Validate(object):
  """Custom validator which takes callable like lambda and has a message for validation"""

  def __init__(self, validator:callable, message:str):
    if message == None:
      raise ValueError("Message cannot be None")
    self._validator = validator
    self._message = message

  def __call__(self, value):
    return self._validator(value)

  def message(self, value):
    return self._message

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


