class ValidationFailed(Exception):
  def __init__(self, argument, argument_index, message):
    self.argument_index = argument_index
    self.message = message
    self.argument = argument

  def __str__(self):
    return "argument %s, index %d validation failed: %s" \
      % (repr(self.argument), self.argument_index, self.message)

