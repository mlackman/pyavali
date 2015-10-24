
class ArgumentByIndexPicker(object):

  def __init__(self, index):
    """Creates ArgumentIndexPicker
    index - Index of the argument, which this picker picks
    """
    self._index = index

  def argument(self, func, *args):
    """
    func - function, which argument is checked
    *args - arguments for the func
    Returns the argument by index
    """
    if self._index + 1 > len(args):
      raise ArgumentByIndexError(self._index, func.__name__)

    return args[self._index]

class ArgumentByIndexError(Exception):

  def __init__(self, index, function_name):
    super().__init__()
    self.message = \
      "Tried to pick argument with index %d from '%s', but it takes 0 arguments" % (index, function_name)

  def __str__(self):
    return self.message

