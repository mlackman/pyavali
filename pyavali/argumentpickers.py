import inspect

class ArgumentByIndexPicker(object):

  def __init__(self, index:int):
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

class ArgumentByNamePicker(object):

  def __init__(self, argument_name:str):
    """Creates ArgumentByNamePicker.
    argument_name - Name of the argument, which this picker picks
    """
    self._argument_name = argument_name

  def argument(self, func, *args, **kwargs):
    argument_index = self._argument_index(func)
    if argument_index != -1 and argument_index < len(args):
      return args[argument_index]
    if self._argument_name in kwargs.keys():
      return kwargs[self._argument_name]
    raise ArgumentByNameError(self._argument_name, func.__name__)

  def _argument_index(self, func):
    argument_names, _, _, _  = inspect.getargspec(func)
    if self._argument_name in argument_names:
      return argument_names.index(self._argument_name)
    else:
      return -1

class ArgumentByIndexError(Exception):

  def __init__(self, index:int, function_name:str):
    super().__init__()
    self.message = \
      "Tried to pick argument with index %d from '%s', but it takes 0 arguments" % (index, function_name)

  def __str__(self):
    return self.message

class ArgumentByNameError(Exception):
  def __init__(self, name:str, function_name:str):
    super().__init__()
    self.message = \
      "Tried to pick argument with name '%s' from '%s', but it was not found" % (name, function_name)

  def __str__(self):
    return self.message


