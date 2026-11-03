#!/usr/bin/env python3
"""Examples of how terrible these functions are."""

from is_even import is_even
from is_prime import is_prime
from add import add
from math_ops import multiply, factorial, maximum
from is_palindrome import is_palindrome

print("=== is_even ===")
for i in range(0, 75):
    print(f"{i:3d}: {is_even(i)}")

print("\n=== is_prime (first 30) ===")
for i in range(1, 31):
    print(f"{i:3d}: {is_prime(i)}")

print("\n=== add (recursive) ===")
print("5 + 3 =", add(5, 3))
print("10 + 20 =", add(10, 20))

print("\n=== multiply ===")
print("6 * 7 =", multiply(6, 7))

print("\n=== factorial ===")
print("5! =", factorial(5))
print("7! =", factorial(7))

print("\n=== maximum ===")
print("max(42, 17) =", maximum(42, 17))

print("\n=== is_palindrome ===")
print("121:", is_palindrome(121))
print("123:", is_palindrome(123))
print("'racecar':", is_palindrome("racecar"))
