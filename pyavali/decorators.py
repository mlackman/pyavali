from functools import wraps
import pyavali
from .argumentpickers import create_argument_picker

class validate(object):
  """Validates a function argument by calling validator with the argument.

  @validate(0, int)
  def foo(param):
    ...

  or

  @validate("param", int, "must be int")
  def foo(param)
    ...

  argument_index_or_name - Index of the arguments in args array or name of the argument
  validator - Callable, which takes the param
  message - Message set to the raised exception

  Raises ValidatorException if validator returned false or raised error
  """

  def __init__(self, argument_index_or_name, validator, message=None):
    self._argument_name = str(argument_index_or_name)
    self._argument_picker = create_argument_picker(argument_index_or_name)
    self._validator = validator
    self._message = message

  def __call__(self, func):
    self._validator = Validator(self._validator, func.__name__, self._argument_name, self._message)

    @wraps(func)
    def decorator_callable(*args, **kwargs):
      argument = self._argument_picker.argument(func, *args, **kwargs)
      self._validator.validate(argument)
      return func(*args, **kwargs)

    return decorator_callable

class validate_param(validate):
  pass

class Validator(object):

  def __init__(self, validator, function_name, argument_name, message=None):
    self._validator = validator
    self._message = message
    self._argument_name = argument_name
    self._argument_index = 0
    self._function_name = function_name

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
    elif hasattr(self._validator, "message"):
      message = self._validator.message(argument)
      message = "validation failed for '%s': '%s' %s" % (self._function_name, self._argument_name, message)

    raise pyavali.ValidationFailed(argument, self._argument_index, message)


