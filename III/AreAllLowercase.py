from string import ascii_letters, whitespace

def IsLowercaseWithWhitespace(string):
  if set(string).difference(ascii_letters + whitespace):
    return False
  return string.islower()
