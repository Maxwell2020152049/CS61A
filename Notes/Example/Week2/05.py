def eg1():
    def f():
        return 0

    def g():
        print(f())

    def h():
        def f():
            return 1
        g()

    h()

def eg2():    
    def f():
        return 0

    g = f

    def f():
        return 1

    print(g())

def eg3():
    def f():
        return 0

    def g():
        print(f())

    def f():
        return 1

    g()

def eg4():
    def g(x):
        print(x)

    def f(f):
        f(1)

    f(g)

def eg5():
    def f():
        return 0

    def g():
        return f()

    def h(k):
        def f():
            return 1
        p = k
        return p()

    print(h(g))

def eg6():
    def f(p, k):
        def g():
            print(k)
        if k == 0:
            f(g, 1)
        else:
            p()

    f(None, 0)

def eg7():
    def f(x):
        x = x + 1

    y = 4
    f(y)
    x = 2
    f(x)
    print(y, x)

def eg8():
    def f(x):
        def g(y):
            x = y
        g(4)
        return x

    print(f(3))
    
def eg9():
    def print_sums(n):
        print(n)
        def next_sum(k):
            return print_sums(n+k)
        return next_sum

    print_sums(1)(3)(5)


# Currying

from operator import add
def eg10():
    def curry2(f):
        return lambda x: lambda y: f(x, y)

    print(curry2(add)(30)(12))
    print(curry2(add)(30))

