import unittest
from ..validators import Validate

class TestValidate(unittest.TestCase):

  def setUp(self):
    self.validate = Validate(lambda x: x == 0, "must be 0")

  def test_it_returns_false_when_validation_fails(self):
    self.assertFalse(self.validate(1))

  def test_it_returns_true_when_validation_is_ok(self):
    self.assertTrue(self.validate(0))

  def test_it_raises_exception_if_message_is_none(self):
    with self.assertRaises(ValueError):
      Validate(lambda x: x == 0, None)


