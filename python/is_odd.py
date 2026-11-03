"""
Terrible is_odd.

We just invert is_even. But we do it the long way.
"""

from is_even import is_even

def is_odd(n: int) -> bool:
    # Call is_even and then manually invert the result with a giant if
    result = is_even(n)
    if result is True:
        return False
    elif result is False:
        return True
    else:
        # Should never happen, but just in case
        return not result
