
# Designing Functions

def same_length(a, b):
    """Return true iff positive integers A and B have the same
    number of digits when written in decimal.

    >>> same_length(50, 70)
    True
    >>> same_length(50, 100)
    False
    >>> same_length(1000, 100000)
    False
    """
    a_count = 1
    while a >= 10:
        a_count += 1
        a //= 10

    # The next section looks the same as the first. Yuch!
    b_count = 1
    while b >= 10:
        b_count += 1
        b //= 10
    
    return a_count == b_count

# So, we refactor into two functions
def same_length2(a, b):
    """Return true iff positive integers A and B have the same
    number of digits when written in decimal.

    >>> same_length2(50, 70)
    True
    >>> same_length2(50, 100)
    False
    >>> same_length2(1000, 100000)
    False
    """
    return digits2(a) == digits2(b)

def digits2(x):
    """Return the number of decimal digits in the positive integer X."""
    x_count = 1
    while x >= 10:
        x_count += 1
        x //= 10
    return x_count

# Now let's generalize even further!

def same_length3(a, b, base=10):
    """Return true iff positive integers A and B have the same
    number of digits when written in radix BASE.

    >>> same_length3(50, 70)
    True
    >>> same_length3(20, 100)
    False
    >>> same_length3(50, 100)
    False
    >>> same_length3(1000, 100000)
    False
    >>> same_length3(50, 100, 16)
    True
    """
    return digits3(a, base) == digits3(b, base)

def digits3(x, base=10):
    """Return the number of radix BASE digits in the positive integer X."""
    x_count = 1
    while x >= base:
        x_count += 1
        x //= base
    return x_count

# Functions on functions

from operator import add, neg

def summation(N, term):
    k = 1
    sum = 0
    while k <= N:
        sum += term(k)
        k += 1
    return sum

def sum_squares(N):
    def square(x):
        return x*x
    return summation(N, square)

# or

def sum_squares(N):
    return summation(N, lambda x: x*x)

def summations():
    print(summation(10, lambda x: x**3))      # Sum of cubes
    print(summation(10, lambda x: 1 / x))     # Harmonic series
    print(summation(10, lambda k: x**(k-1) / factorial(k-1)))
                                       # Approximate e**x
    
# Functions that return functions

def add_func(f, g):
    """Return function that returns F(x)+G(x) for argument x."""
    def adder(x):           #
        return f(x) + g(x)  # or return lambda x: f(x) + g(x)
    return adder            # 

h = add_func(abs, neg)
print(h(-5))

# Generalizing still more:

def combine_funcs(op):
    def combined(f, g):
        def val(x):
            return op(f(x), g(x))
        return val
    return combined

# Now, can define instead

add_func = combine_funcs(add)

h = add_func(abs, neg)
print(h(-5))

# Conditional function

def bad_if_func(then_expr, condition, else_expr):
    return then_expr if condition else else_expr

def bad_inverse(x):
    return bad_if_func(1/x, x > 0, 0)

def if_func(then_expr, condition, else_expr):
    return then_expr() if condition else else_expr()

def good_inverse(x):
    return if_func(lambda: 1/x, x > 0, lambda: 0)

