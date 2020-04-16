import math
def is_prime(n):
    """Determines if a non-negative integer is prime."""
    if n < 2:
        return False
    for i in range (2, int(math.sqrt(n)+ 1)):
        if n % i == 0:
                return False
        return True

from prime import is_prime

def test_prime(n, expected):
  if is_prime(n) != expected:
      print(f"ERROR on is_prime({n}), expected {expected}")

import unittest

from prime import is_prime


class Tests(unittest.TestCase):

      def test_1(self):
          """Check that 1 is not prime."""
          self.assertFalse(is_prime(1))

      def test_2(self):
          """Check that 2 is prime."""
          self.assertTrue(is_prime(2))

      def test_8(self):
          """Check that 8 is not prime."""
          self.assertFalse(is_prime(8))

      def test_11(self):
          """Check that 11 is prime."""
          self.assertTrue(is_prime(11))

      def test_25(self):
          """Check that 25 is not prime."""
          self.assertFalse(is_prime(25))

      def test_28(self):
          """Check that 28 is not prime."""
          self.assertFalse(is_prime(28))


if __name__ == "__main__":
      unittest.main()
