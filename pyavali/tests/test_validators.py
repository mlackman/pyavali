import unittest
from ..validators import empty, Not

class TestEmpty(unittest.TestCase):

  def test_it_returns_true_for_None(self):
    self.assertEquals(True, empty(None))

  def test_it_returns_false_for_non_empty_string(self):
    self.assertEquals(False, empty("text"))

  def test_it_returns_false_for_non_empty_array(self):
    self.assertEquals(False, empty([1]))

  def test_it_returns_true_for_empty_string(self):
    self.assertEquals(True, empty(""))


class TestNotCompositeValidtor(unittest.TestCase):

  def test_it_negates_composite(self):
    n = Not(lambda value: False)
    self.assertTrue(n(""))

if __name__ == '__main__':
  unittest.main()
