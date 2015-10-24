import pyavali
from .argumentpickers import ArgumentByIndexPicker

class validate_param(object):
  """Validates a function argument by calling validator with the argument.

  @validate_param(0, int)
  def foo(param):
    ...

  argument_index - Index of the arguments in args array.
  validator - Callable, which takes the param
  message - Message set to the raised exception

  Raises ValidatorException if validator returned false or raised error
  """

  def __init__(self, argument_index, validator, message=None):
    self._argument_picker = ArgumentByIndexPicker(argument_index)
    self._validator = Validator(validator, message)
    self._message = message

  def __call__(self, func):
    def decorator_callable(*args, **kwargs):
      argument = self._argument_picker.argument(func, *args)
      self._validator.validate(argument)
      return func(*args, **kwargs)

    return decorator_callable

class validate(object):
  """Validates a function argument by calling validator with the argument.

  @validate("width", int, "must be int")
  def foo(width):
    ...

  argument_name - Name of the argument to be validated
  validator - Callable, which takes the argument.
  message - Message used in exception if validation fails
  """
  def __init__(self, argument_name, validator, message=None):
    pass

  def __call__(self, func):
    pass

class Validator(object):

  def __init__(self, validator, message=None):
    self._validator = validator
    self._message = message
    self._argument_index = 0

  def validate(self, argument):
    if self._validate(argument) == False:
      self._raise_validation_failed(argument)

  def _validate(self, argument):
    try:
      return self._validator(argument)
    except:
      return False

  def _raise_validation_failed(self, argument):
    message = None
    if self._message:
      message = self._message.format(argument)
    raise pyavali.ValidationFailed(argument, self._argument_index, message)


