"""
Daily Coding Problem - Day 447

This problem was asked by Google.

Implement integer exponentiation. That is, implement the pow(x, y) function, where x and y are integers and returns x^y.

Do this faster than the naive method of repeated multiplication.

For example, pow(2, 10) should return 1024.
"""

def ipow(base, exp):
    result = 1
    while exp:
        # If exp is odd
        if exp & 1:
            result = result * base
        # Divide exp by 2
        exp = exp >> 1
        base = base * base
    return result

print(ipow(8, 5))
print(ipow(2, 10))
print(ipow(6, 1))
print(ipow(3, 2))