from string import ascii_letters, whitespace

def IsLowercaseWithWhitespace(string):
  if set(string).difference(ascii_letters + whitespace):
    print("false")
  if (string.islower()):
    print("true")
  else:
    print("false")
