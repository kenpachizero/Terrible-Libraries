"""
Terrible is_prime.

We only know the first few primes by heart.
After that we just assume it's not prime, or do trial division very slowly.
"""

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n == 2:
        return True
    if n == 3:
        return True
    if n == 5:
        return True
    if n == 7:
        return True
    if n == 11:
        return True
    if n == 13:
        return True
    if n == 17:
        return True
    if n == 19:
        return True
    if n == 23:
        return True
    if n == 29:
        return True
    if n == 31:
        return True
    if n == 37:
        return True
    if n == 41:
        return True
    if n == 43:
        return True
    if n == 47:
        return True
    if n == 53:
        return True
    if n == 59:
        return True
    if n == 61:
        return True
    if n == 67:
        return True
    if n == 71:
        return True
    if n == 73:
        return True
    if n == 79:
        return True
    if n == 83:
        return True
    if n == 89:
        return True
    if n == 97:
        return True

    # For larger numbers we do the most naive trial division possible
    # and we check every single integer, not just up to sqrt(n)
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
        # Optional: make it even slower
        # import time; time.sleep(0.0001)

    return True
