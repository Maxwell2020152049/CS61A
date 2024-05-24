# Creating a list from scratch:
a = []
b = [1, 2, 3, 4, 5]

# Creating a list from existing lists:
c = b + [20, 30]
d = c[:]
e = list(c)

# List Mutation
L = [1, 2, 3, 4, 5]
L[2] = 6

L[1:3] = [9, 8]

L[2:4] = []            # Deleting elements

L[1:1] = [2, 3, 4, 5]  # Inserting elements

L[len(L):] = [10, 11]  # Appending

L[0:0] = range(-3, 0)  # Prepending

# append() adds a single element to a list:
s = [2, 3]
t = [5, 6]
s.append(4)
s.append(t)
t = 0

# extend() adds all the elements in one list to a list:
s = [2, 3]
t = [5, 6]
# s.extend(4) # 🚫 Error: 4 is not an iterable!
s.extend(t)
t = 0

# pop() removes and returns the last element:
s = [2, 3]
t = [5, 6]
t = s.pop()

# remove() removes the first element equal to the argument:
s = [6, 2, 4, 8, 4]
s.remove(4)
# s.remove(9)

list1 = [1,2,3]
list2 = [1,2,3]
# evaluates to True if both exp0 and exp1 evaluate to objects containing equal values
are_equal = list1 == list2
# evaluates to True if both exp0 and exp1 evaluate to the same object
identical = list1 is list2

# Equality of contents vs. Identity of objects
a = ["apples", "bananas"]
b = ["apples", "bananas"]
c = a

if a == b == c:
    print("All equal!")

a[1] = "oranges"

if a is c and a == c:
    print("A and C are equal AND identical!")

if a == b:
    print("A and B are equal!") # Nope!

if b == c:
    print("B and C are equal!") # Nope!


# Test List's '+' and '+='
a = [1, 2, 3]
print(a, id(a))

b = a + [4, 5]
print(b, id(b))

a += [6, 7]
print(a, id(a))

a = a + [8, 9]
print(a, id(a))


# Try this in your local friendly Python interpreter:
a = "orange"
b = "orange"
c = "o" + "range"
print(a is b)
print(a is c)

a = 100
b = 100
print(a is b)
print(a is 10 * 10)
print(a == 10 * 10)

a = 100000000000000000
b = 100000000000000000
print(a is b)
print(100000000000000000 is 100000000000000000)

# access is allowed
attendees = []

def mark_attendance(name):
    attendees.append(name)
    print("In attendance:", attendees)

mark_attendance("Emily")
mark_attendance("Cristiano")
mark_attendance("Samantha")


# re-assign is not allowed
# UnboundLocalError: local variable 'current' referenced before assignment
current = 0

def count():
    # current = current + 1     # 🚫  Error!
    print("Count:", current)

count()
count()


# Re-assigning globals
current = 0

def count():
    global current
    current = current + 1
    print("Count:", current)

count()
count()

# UnboundLocalError: local variable 'current' referenced before assignment
def make_counter(start):
    current = start

    def count():
        # current = current + 1
        print("Count:", current)

    return count

counter = make_counter(30)
counter()
counter()
counter()

# The nonlocal declaration tells Python to look in the parent frame for the name lookup.
def make_counter(start):
    current = start

    def count():
        nonlocal current
        current = current + 1
        print("Count:", current)

    return count

counter = make_counter(30)
counter()
counter()
counter()