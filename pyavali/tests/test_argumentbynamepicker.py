import unittest
from ..argumentpickers import ArgumentByNamePicker, ArgumentByNameError


class TestArgumentByNamePicker(unittest.TestCase):

  def test_it_can_pick_argument_by_name(self):
    picker = ArgumentByNamePicker("b")
    args = (1,2,3,4)
    kwargs = {}
    def func(a,b,c,d): pass
    self.assertEquals(2, picker.argument(func, *args, **kwargs))

  def test_it_can_pick_argument_by_name_2(self):
    picker = ArgumentByNamePicker("d")
    args = (1,2,3,4)
    kwargs = {}
    def func(a,b,c,d): pass
    self.assertEquals(4, picker.argument(func, *args, **kwargs))

  def test_it_can_pick_argument_from_kwargs(self):
    picker = ArgumentByNamePicker("d")
    args = (1,2,)
    kwargs = {'c':3, 'd':4}
    def func(a,b,c,d): pass
    self.assertEquals(4, picker.argument(func, *args, **kwargs))

  def test_it_raises_exception_when_argument_not_found(self):
    picker = ArgumentByNamePicker("e")
    args = (1,2,)
    kwargs = {'c':3, 'd':4}
    def func(a,b,c,d): pass
    with self.assertRaises(ArgumentByNameError) as cm:
      picker.argument(func, *args, **kwargs)
    self.assertEquals(cm.exception.message, "Tried to pick argument with name 'e' from 'func', but it was not found")







