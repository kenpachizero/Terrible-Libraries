"""
Terrible is_palindrome for numbers and strings.
"""

def is_palindrome(value) -> bool:
    s = str(value)

    # Reverse the string the slowest way possible
    reversed_s = ""
    for i in range(len(s) - 1, -1, -1):
        reversed_s = reversed_s + s[i]

    # Compare character by character instead of just ==
    if len(s) != len(reversed_s):
        return False

    for i in range(len(s)):
        if s[i] != reversed_s[i]:
            return False

    return True
