# On code.cs61a.org, the "from __main__ import fib" line does not work,
# so here is a different way to do the same thing:

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 2) + fib(n - 1)

from timeit import repeat

def fib_time():
    print(repeat('fib(10)', globals=globals(), number=5))
    print(repeat('fib(20)', globals=globals(), number=5))
    print(repeat('fib(30)', globals=globals(), number=5))
