"""
Command to run:
python AreAllLowercaseTests.py -v
"""

import doctest
import unittest
from AreAllLowercase import IsLowercaseWithWhitespace

class AreAllLowercaseTests(unittest.TestCase):
  def test_correct(self):
    result = IsLowercaseWithWhitespace("laba diena")
    self.assertEqual(result, True)

  def test_with_upper(self):
    result = IsLowercaseWithWhitespace("Laba Diena")
    self.assertEqual(result, False)

  def test_with_digit(self):
    result = IsLowercaseWithWhitespace("laba 0 diena")
    self.assertEqual(result, False)

  def test_with_symbol(self):
    result = IsLowercaseWithWhitespace("laba & diena")
    self.assertEqual(result, False)

def load(loader, tests, ignore):
  tests.addTests(doctest.DocFileSuite("doctest.txt"))
  return tests

if __name__ == '__main__':
  unittest.main()