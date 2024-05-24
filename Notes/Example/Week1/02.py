# Some simple snippets you might want to try out in the Python Tutor.
# (See the Tutor link on the class web page.

# Snippet 1

def saxb(a, x, b):
    return a * x + b

a = 3
b = 2

z = 0
z = saxb(3, z, 2)
z = saxb(3, z, 2)
print(z)

####

# Snippet 2

# Another way to accomplish the same thing:

saxb = lambda a, x, b: a * x + b

a = 3
b = 2

z = 0
z = saxb(3, z, 2)
z = saxb(3, z, 2)
print(z)

####

# Snippet 3

# Random number generators (evidence of side effects).

from random import randint
randint(0, 100)   # Random number in 0--100.
randint(0, 100)   # Different result: Something must have changed!

####

# Snippet 4

# Functions returning nested functions

def incr(n):
    def f(x):
        return n + x
    return f

incr(5)(6)

####

# Hiding of names

# Snippet 5

def hmmmm(x):           
    def f(x):
        return x
    return f
hmmmm(5)(6)

####

# Another simple example of nested call.

# Snippet 6

from operator import mul
def square(x):
   return mul(x,x)
x = -2

