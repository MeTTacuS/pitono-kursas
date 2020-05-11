from string import ascii_letters, digits, whitespace

def IsLowercaseWithWhitespace(string):
  if set(string).difference(ascii_letters + whitespace):
    return False
  return string.islower()
