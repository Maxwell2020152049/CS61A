

def iterating_over_pairs():
    """
    >>> L = [ (1, 9), (2, 2), (5, 6), (3, 3) ]
    >>> same = 0
    >>> for x, y in L:
    ...    if x == y:
    ...        same += 1
    >>> same
    2
    """
    pass

def using_zip():
    """Examples of zip() function and multiple assignment in a loop.

    >>> list(zip([1, 2, 5, 3], [9, 2, 6, 3, 10]))
    [(1, 9), (2, 2), (5, 6), (3, 3)]
    >>> # Length of result is that of shortest sequence
    >>> list(zip([1, 4, 7, 10], [2, 5, 8, 11], [3, 6, 9, 12, 15]))
    [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12)]
    >>> beasts = ["aardvark", "axolotl", "gnu", "hartebeest"]
    >>> for n, animal in zip(range(1, 5), beasts):
    ...     print(n, animal)
    1 aardvark
    2 axolotl
    3 gnu
    4 hartebeest
    """
    pass

def list_setting():
    """Various examples of mutating a list.

    >>> L = [1, 2, 3, 4, 5]
    >>> L[2] = 6
    >>> L
    [1, 2, 6, 4, 5]
    >>> L[1:3] = [9, 8]
    >>> L
    [1, 9, 8, 4, 5]
    >>> L[2:4] = []            # Deleting elements
    >>> L
    [1, 9, 5]
    >>> L[1:1] = [2, 3, 4, 5]  # Inserting elements
    >>> L
    [1, 2, 3, 4, 5, 9, 5]
    >>> L[len(L):] = [10, 11]  # Appending
    >>> L
    [1, 2, 3, 4, 5, 9, 5, 10, 11]
    >>> L[0:0] = range(-3, 0)  # Prepending
    >>> L
    [-3, -2, -1, 1, 2, 3, 4, 5, 9, 5, 10, 11]
    """
    pass

def multiplying_lists():
    """Examples of the * operators on sequences.
    >>> [0] * 3
    [0, 0, 0]
    >>> (1, 2) * 3
    (1, 2, 1, 2, 1, 2)
    >>> "a" * 5
    'aaaaa'
    >>> 5 * 'a'
    'aaaaa'
    """

def matches(a, b):
    """Return the number of values k such that A[k] == B[k].
    >>> matches([1, 2, 3, 4, 5], [3, 2, 3, 0, 5])
    3
    >>> matches("abdomens", "indolence")
    4
    >>> matches("abcd", "dcba")
    0
    >>> matches("abcde", "edcba")
    1
    >>> matches("abcdefg", "edcba")
    1
    """
    return sum([1 for x, y in zip(a, b) if x==y])

def triangle(n):
    """Assuming N >= 0, return the list consisting of N lists:
    [1], [1, 2], [1, 2, 3], ... [1, 2, ... N].
    >>> triangle(0)
    []
    >>> triangle(1)
    [[1]]
    >>> triangle(5)
    [[1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 5]]
    """
    return [list(range(1, i + 1)) for i in range(1, n+1)]

# Rationals

from math import gcd

def make_rat(n, d):
    """The rational number N/D, assuming N, D are integers, D!=0"""
    g = gcd(n, d)
    n //= g; d //= g
    return (n, d)

def numer(r):
    """The numerator of rational number R in lowest terms."""
    return r[0]

def denom(r):
    """The denominator of rational number R in lowest terms.
       Always positive."""
    return r[1]

def add_rat(x, y):
    return make_rat(numer(x) * denom(y) + numer(y) * denom(x),
                    denom(x) * denom(y))

def mul_rat(x, y):
    return make_rat(numer(x) * numer(y), denom(x) * denom(y))

def str_rat(r):  # (For fun: a little new Python string magic)
    return str(numer(r)) if denom(r) == 1 else f"{numer(r)}/{denom(r)}" 

def equal_rat(x, y):
    return numer(x) * denom(y) == numer(y) * denom(x)


def exact_harmonic_number(n):
    """Return 1 + 1/2 + 1/3 + ... + 1/N as a rational number.
    >>> str_rat(exact_harmonic_number(1))
    '1'
    >>> str_rat(exact_harmonic_number(3))
    '11/6'
    >>> str_rat(exact_harmonic_number(10))
    '7381/2520'
    """
    s = make_rat(0, 1)
    for k in range(1, n + 1):
        s = add_rat(s, make_rat(1, k))
    return s
