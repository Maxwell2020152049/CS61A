# Create nested environment
x = 1
y = 12
def g1(x):
    def g2(x):
        # Stop here
        print(x)
    g2(x + 1)
g1(2)

# Illustrate chain of calls.
def square(x): return x*x 
def sum_square(x, y):
    return square(x)+square(y) 
z = sum_square(3, 4)

# Functions taking and returning functions
def id(x):
    return x
print(id(id)(id(13)))

# Illustration of returing a nested function.
def incr(n):
    def f(x):
        return n + x
    return f

incr(5)(6)

# Illustrations of conditional statements
                        
def signum(x):          
    if x > 0:           
        return 1        
    elif x == 0:        
        return 0        
    else:               
        return -1       
                        
def max(x, y):          
    if x > y:           
        return x        
    else:               
        return y        
                        
def min(x, y):          
    if x < y:            
        return x        
    return y


# Illustrations of conditional expressions

def signum(x):                                           
    return 1 if x > 0 else 0 if x == 0 else -1           
                                                         
def max(x, y):                                           
    return x if x > y else y                             
                                                         
def min(x, y):                                           
    return x if x < y else y                             


# Illustrations of how indentation groups statements

x = 0                               
if x > 1:                       
    print(">1")                 
    if x < 6:                   
        print("<6")             
    print("x =", x)             
# Prints nothing                

x = 0                
if x > 1:            
    print(">1")      
    if x < 6:        
        print("<6")  
print("x =", x)     
 # Prints "x = 0"    


# Iteration via recursion (preview) 

def add_sq(accum, k, n):
    """Return ACCUM + K ** 2 + (K+1)**2 + ... + N**2."""
    if k > n:
        return accum
    else:
        return add_sq(accum + k ** 2, k + 1, n)
print(add_sq(0, 1, 100))


# Iteration via while loop (indefinite repetition)

accum = 0
k = 1
n = 100
while k <= n:
    accum = accum + k ** 2
    k += 1    # Another way to write k = k + 1
print(accum)

#  Prime numbers

def is_prime(n):
    """Return True iff N is prime.
    >>> is_prime(1)
    False
    >>> is_prime(2)
    True
    >>> is_prime(8)
    False
    >>> is_prime(21)
    False
    >>> is_prime(23)
    True
    """
    if (n == 1):    return False

    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    
    return True

def smallest_factor(n):
    """Returns the smallest value k>1 that evenly divides N."""
    i = 2
    while i <= n:
        if n % i == 0:
            return i
        i += 1


def print_factors(n):
    """Print the prime factors of N.
    >>> print_factors(180)
    2
    2
    3
    3
    5
    """
    while n != 1:
        i = 2
        while i <= n:
            if n % i == 0:
                print(i)
                n //= i
                break
            i += 1
