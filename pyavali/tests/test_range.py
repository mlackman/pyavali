import unittest
from ..validators import Range


class TestRange(unittest.TestCase):

  def setUp(self):
    self.range = Range(-1, 1)

  def test_it_returns_false_when_value_below_min(self):
    self.assertFalse(self.range(-2))

  def test_it_returns_true_when_value_equals_min(self):
    self.assertTrue(self.range(-1))

  def test_it_returns_true_when_value_equals_max(self):
    self.assertTrue(self.range(1))

  def test_it_returns_false_when_value_more_than_max(self):
    self.assertFalse(self.range(2))

  def test_it_has_default_message(self):
    self.assertEquals("must be in range [-1, 1]", self.range.message)
