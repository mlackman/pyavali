import unittest
from ..validators import And


class TestAnd(unittest.TestCase):

  def test_it_returns_true_when_all_validators_are_true(self):
    and_validator = And(lambda a: True, lambda b: True, lambda c: True)
    self.assertTrue(and_validator(1))

  def test_it_returns_false_when_one_validator_returns_false(self):
    ok_validator = lambda value: value == 1
    fail_validator = lambda value: value != 1

    and_validator = And(ok_validator, fail_validator)
    self.assertFalse(and_validator(1))
