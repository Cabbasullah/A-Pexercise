#Write a Python program to get the least common multiple (LCM) of two positive integers
from math import gcd
def least_common_multiples(a,b):
  return (a*b/(gcd(a,b)))
print (least_common_multiples(2,8))
