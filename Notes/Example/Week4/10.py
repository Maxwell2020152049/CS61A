# Non-working implementation of mutable pairs using functions

def bad_pair(a, b):
    def pair_func(which, v=None):
        if which == 0:
            return a
        elif which == 1:
            return b
        elif which == 2:
            a = v
        else:
            b = v
    return pair_func

def left(p):
    return p(0)

def right(p):
    return p(1)

def set_left(p, v):
    p(2, v)

def set_right(p, v):
    p(3, v)

def test_bad_pair():
    aPair = bad_pair(3, 2)
    set_left(aPair, 5)
    print(left(aPair))

# Corrected version of pair

def pair(a, b):
    def pair_func(which, v=None):
        nonlocal a, b
        if which == 0:
            return a
        elif which == 1:
            return b
        elif which == 2:
            a = v
        else:
            b = v
    return pair_func

def test_good_pair():
    aPair = pair(3, 2)
    set_left(aPair, 5)
    print(left(aPair))

# Pairs of non-negative integers

def pair(a, b):
    """Return a value that represents the ordered pair of
    non-negative integer values (A, B)."""
    return 2**a * 3**b

def left(p):
    return multiplicity(2, p)

def right(p):
    return multiplicity(3, p)

def multiplicty(factor, n):
    """Assuming FACTOR and N are integers with FACTOR > 1, return
    the number of times N may be evenly divided by FACTOR."""
    r = 0
    while n % factor == 0:
        r += 1
        n //= factor
    return r

# String Literals

def string_literals():
    print('Single-quoted strings may contain "double-quoted strings"')
    print("Double-quoted strings may contain 'single-quoted strings'")
    print("""Triple double quotes allow 'this', "this", and ""this"",
as well as newline characters""")
    print('''Triple single quotes allow "this", 'this', and ''this'',
as well as newline characters''')
    print("A test of\nescapes\\.")
    print("Some unicode: \u0395\u1f55\u03c1\u03b7\u03ba\u03b1\u2764")
    print(r"In raw strings (starting with 'r'), \escapes are not replaced")

# Collection of sequence expressions

def print_sequences():
    t = (2, 0, 9, 10, 11)   # Tuple
    L = [2, 0, 9, 10, 11]   # List
    R = range(2, 13)        # Integers 2-12.
    E = range(2, 13, 2)     # Even integers 2-12.
    S = "Hello, world!"     # Strings (sequences of characters)

    print(f"t[2] == {t[2]}; L[2] == {L[2]}; R[2] == {R[2]}; E[2] == {E[2]}")
    print(f"t[-1] == {t[-1]}' t[len(t)-1] == {t[len(t)-1]}")
    print(f"S[1] == {S[1]}")

    print(f"t[1:4] == {t[1:4]}")
    print(f"t[2:] == {t[2:]}; t[2:len(t)] == {t[2:len(t)]}")
    print(f"t[::2] == {t[::2]}; t[0:len(t):2] == {t[0:len(t):2]}; ",
          f"t[::-1] == {t[::-1]}")
    print(f"S[0:5] == {S[0:5]}; S[0:5:2] == {S[0:5:2]}; S[4::-1] == {S[4::-1]}")
    print(f"S[1:2] == {S[1:2]}; S[1] == {S[1]}")
    
# Reversing a number using strings

def reverse_digits(n):
    """Assuming N >= 0 is an integer.  Return the number whose
    base-10 representation is the reverse of that of N.
    >>> reverse_digits(0)
    0
    >>> reverse_digits(1)
    1
    >>> reverse_digits(123)
    321
    >>> reverse_digits(10)
    1
    >>> reverse_digits(12321)
    12321
    >>> reverse_digits(2222222)
    2222222
    >>> reverse_digits(102)
    201
    """
    return int(str(n)[-1::-1])

