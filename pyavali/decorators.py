import pyavali

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
    self._argument_index = argument_index
    self._validator = validator
    self._message = message

  def __call__(self, func):
    def decorator_callable(*args, **kwargs):
      argument = self._get_argument(func, *args)
      if self._validate(argument) == False:
        self._raise_validation_failed(argument)
      return func(*args, **kwargs)

    return decorator_callable

  def _get_argument(self, func, *args):
    if len(args) <= self._argument_index:
      raise RuntimeError("Validated argument index %d not in decorated method '%s'" % (self._argument_index, func.__name__))
    return args[self._argument_index]

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


