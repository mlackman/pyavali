import unittest

from ..decorators import validate_param, validate
from ..validators import And, Range, Validate
import pyavali


class Callable(object):
  def __init__(self, returns=None, raises=None):
    self.returns = returns
    self.raises = raises

  def __call__(self, param):
    if self.raises: raise self.raises;
    self.parameter_received = param
    return self.returns

def call(func, param):
  try:
    func(param)
  except Exception as e:
    return e


class TestPyavali(unittest.TestCase):

  def setUp(self):
    self.callable = Callable()

  def test_it_calls_callable_with_argument_given(self):
    @validate(0, self.callable)
    def method(first_param): pass;

    method("parameter")

    self.assertEquals("parameter", self.callable.parameter_received)

  def test_it_returns_decorated_function_return_value(self):
    @validate(0, self.callable)
    def method(param): return 5;

    self.assertEquals(5, method(""))

  def test_validating_with_parameter_name(self):
    @validate("param", self.callable)
    def method(param): return 5;

    self.assertEquals(5, method(""))

  def test_it_raises_validation_failed_exception(self):
    callable_which_returns_false = Callable(returns=False)
    @validate(0, callable_which_returns_false)
    def method(first_param): pass;

    self.assertRaises(pyavali.ValidationFailed, method, "")

  def test_it_sets_message_to_exception_if_set(self):
    callable_which_returns_false = Callable(returns=False)
    @validate(0, callable_which_returns_false, "Message")
    def method(first_param): pass;

    exception = call(method, "")

    self.assertEquals("Message", exception.message)

  def test_it_raises_validation_failed_when_validator_raises_exception(self):
    callable_which_raises_error = Callable(raises=Exception())
    @validate_param(0, callable_which_raises_error)
    def method(first_param): pass;

    self.assertRaises(pyavali.ValidationFailed, method, "")

  def test_it_raises_error_when_validator_tries_to_validate_non_existing_argument(self):
    @validate(0, self.callable)
    def method(): pass;

    self.assertRaises(Exception, method)


class TestComplexValidation(unittest.TestCase):

  @validate("width", And(Validate(lambda value: isinstance(value, int), "must be integer"), Range(min=5, max=10)))
  def validated_func(self, width): pass

  @validate(1, Validate(lambda value: isinstance(value, int), "must be integer"))
  def other_validated_func(self, width): pass

  def test_it_raises_error_when_not_integer(self):
    with self.assertRaises(pyavali.ValidationFailed) as cm:
      self.validated_func("a")
    self.assertEquals(cm.exception.message, "validation failed for 'validated_func': 'width' must be integer")

  def test_it_raises_error_with_message_when_argument_validated_by_index(self):
    with self.assertRaises(pyavali.ValidationFailed) as cm:
      self.other_validated_func("2")
    self.assertEquals(cm.exception.message, "validation failed for 'validated_func': argument at 1 must be integer")

if __name__ == '__main__':
  unittest.main()
