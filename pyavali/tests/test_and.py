import unittest
from ..validators import And, Validate


class TestAnd(unittest.TestCase):

  def test_it_returns_true_when_all_validators_are_true(self):
    and_validator = And(lambda a: True, lambda b: True, lambda c: True)
    self.assertTrue(and_validator(1))

  def test_it_returns_false_when_one_validator_returns_false(self):
    ok_validator = lambda value: value == 1
    fail_validator = lambda value: value != 1

    and_validator = And(ok_validator, fail_validator)
    self.assertFalse(and_validator(1))

  def test_it_returns_the_message_of_the_failed_validator(self):
    ok_validator = Validate(lambda x: True, "message of the ok validator")
    fail_validator = Validate(lambda x: False, "message of the fail validator")

    and_validator = And(ok_validator, fail_validator)
    self.assertEquals("message of the fail validator", and_validator.message(5))

  def test_it_returns_none_message_when_composite_validator_does_not_have_message(self):
    and_validator = And(lambda x: False, lambda x: True)
    self.assertEquals(None, and_validator.message(5))
