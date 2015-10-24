import unittest
from ..argumentpickers import ArgumentByIndexPicker, ArgumentByIndexError


class TestArgumentByIndexPicker(unittest.TestCase):

  def test_it_picks_first_argument(self):
    picker = ArgumentByIndexPicker(0)
    args = (1,2,3,4)
    def func(a,b,c,d): pass
    self.assertEquals(1, picker.argument(func, *args))

  def test_it_picks_last_argument(self):
    picker = ArgumentByIndexPicker(3)
    args = (1,2,3,4)
    def func(a,b,c,d): pass
    self.assertEquals(4, picker.argument(func, *args))

  def test_it_raises_error_when_argument_index_out_of_bounds(self):
    picker = ArgumentByIndexPicker(0)
    def func(): pass
    args = ()
    with self.assertRaises(ArgumentByIndexError) as cm:
      picker.argument(func, *args)
    self.assertEquals(cm.exception.message, "Tried to pick argument with index 0 from 'func', but it takes 0 arguments")




