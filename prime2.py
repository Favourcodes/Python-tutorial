import math

def is_prime(n):
  return n > 1 and all(n % i for i in range(2, int(math.sqrt(n)) + 1))