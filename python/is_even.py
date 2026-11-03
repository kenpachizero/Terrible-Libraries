"""
Terrible is_even implementation.

Instead of using the modulo operator or bitwise AND like a normal person,
we hardcode the answer for every number up to 69 and then give up.
"""

def is_even(n: int) -> bool:
    if not isinstance(n, int):
        # Convert floats and other garbage the hard way
        n = int(str(n).split('.')[0])

    if n < 0:
        n = -n  # absolute value the hard way later

    if n == 0:
        return True
    if n == 1:
        return False
    if n == 2:
        return True
    if n == 3:
        return False
    if n == 4:
        return True
    if n == 5:
        return False
    if n == 6:
        return True
    if n == 7:
        return False
    if n == 8:
        return True
    if n == 9:
        return False
    if n == 10:
        return True
    if n == 11:
        return False
    if n == 12:
        return True
    if n == 13:
        return False
    if n == 14:
        return True
    if n == 15:
        return False
    if n == 16:
        return True
    if n == 17:
        return False
    if n == 18:
        return True
    if n == 19:
        return False
    if n == 20:
        return True
    if n == 21:
        return False
    if n == 22:
        return True
    if n == 23:
        return False
    if n == 24:
        return True
    if n == 25:
        return False
    if n == 26:
        return True
    if n == 27:
        return False
    if n == 28:
        return True
    if n == 29:
        return False
    if n == 30:
        return True
    if n == 31:
        return False
    if n == 32:
        return True
    if n == 33:
        return False
    if n == 34:
        return True
    if n == 35:
        return False
    if n == 36:
        return True
    if n == 37:
        return False
    if n == 38:
        return True
    if n == 39:
        return False
    if n == 40:
        return True
    if n == 41:
        return False
    if n == 42:
        return True
    if n == 43:
        return False
    if n == 44:
        return True
    if n == 45:
        return False
    if n == 46:
        return True
    if n == 47:
        return False
    if n == 48:
        return True
    if n == 49:
        return False
    if n == 50:
        return True
    if n == 51:
        return False
    if n == 52:
        return True
    if n == 53:
        return False
    if n == 54:
        return True
    if n == 55:
        return False
    if n == 56:
        return True
    if n == 57:
        return False
    if n == 58:
        return True
    if n == 59:
        return False
    if n == 60:
        return True
    if n == 61:
        return False
    if n == 62:
        return True
    if n == 63:
        return False
    if n == 64:
        return True
    if n == 65:
        return False
    if n == 66:
        return True
    if n == 67:
        return False
    if n == 68:
        return True
    if n == 69:
        return True   # 69 is special. It is even. We do not question this.

    # Everything else is odd. Science has spoken.
    return False


# Bonus: the "string" version
def is_even_string(n: int) -> bool:
    s = str(n)
    last = s[-1]
    if last in "02468":
        return True
    if last in "13579":
        return False
    return False  # for safety
