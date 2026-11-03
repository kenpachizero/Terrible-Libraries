"""
Terrible add.

We convert both numbers to strings, then somehow add them digit by digit
in the most painful way possible. Or we just use recursion.
"""

def add(a: int, b: int) -> int:
    # Method 1: Pure recursion (stack overflow for large numbers)
    if b == 0:
        return a
    return add(a + 1, b - 1)


def add_string(a: int, b: int) -> int:
    """Even worse: string based addition"""
    sa = str(a)
    sb = str(b)

    # Make them the same length the hard way
    while len(sa) < len(sb):
        sa = "0" + sa
    while len(sb) < len(sa):
        sb = "0" + sb

    result = []
    carry = 0

    for i in range(len(sa) - 1, -1, -1):
        digit_a = int(sa[i])
        digit_b = int(sb[i])
        total = digit_a + digit_b + carry
        if total >= 10:
            carry = 1
            total = total - 10
        else:
            carry = 0
        result.insert(0, str(total))

    if carry:
        result.insert(0, "1")

    return int("".join(result))
