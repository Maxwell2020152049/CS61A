# Lists, tuples, dictionaries, and strings are all iterable objects.
my_order = ["Yuca Shepherds Pie", "Pão de queijo", "Guaraná"]

ranked_chocolates = ("Dark", "Milk", "White")

prices = {"pineapple": 9.99, "pen": 2.99, "pineapple-pen": 19.99}

best_topping = "pineapple"


# We can iterate over iterable objects:
my_order = ["Yuca Shepherds Pie", "Pão de queijo", "Guaraná"]
for item in my_order:
    print(item)
lowered = [item.lower() for item in my_order]

ranked_chocolates = ("Dark", "Milk", "White")
for chocolate in ranked_chocolates:
    print(chocolate)

prices = {"pineapple": 9.99, "pen": 2.99, "pineapple-pen": 19.99}
for product in prices:
    print(product, " costs ", prices[product])
discounted = { item: prices[item] * 0.75 for item in prices }

best_topping = "pineapple"
for letter in best_topping:
    print(letter)
    

# An iterator is an object that provides sequential access to values, one by one.
# iter(iterable) returns an iterator over the elements of an iterable.
# next(iterator) returns the next element in an iterator.
toppings = ["pineapple", "pepper", "mushroom", "roasted red pepper"]

topperator = iter(toppings)
next(topperator) # 'pineapple'
next(topperator) # 'pepper'
next(topperator) # 'mushroom'
next(topperator) # 'roasted red pepper'
# next(topperator) # ❌ StopIteration exception


# An unhandled exception will immediately stop a program.
# Use try/except to handle an exception:
ranked_chocolates = ("Dark", "Milk", "White")

chocolaterator = iter(ranked_chocolates)
print(next(chocolaterator))
print(next(chocolaterator))
print(next(chocolaterator))

try:
    print(next(chocolaterator))
except StopIteration:
    print("No more left!")


# We can use a while loop to process iterators of arbitrary length:
ranked_chocolates = ("Dark", "Milk", "White")
chocolaterator = iter(ranked_chocolates)

try:
    while True:
        choco = next(chocolaterator)
        print(choco)
except StopIteration:
    print("No more left!")


# use for loops
ranked_chocolates = ("Dark", "Milk", "White")
for chocolate in ranked_chocolates:
    print(chocolate)


# When the iter() function is passed an iterable object, it calls the __iter__() method on it:
ranked_chocolates = ("Dark", "Milk", "White")
chocorator1 = iter(ranked_chocolates)
chocorator2 = ranked_chocolates.__iter__()


# When the next() function is passed an iterator, it calls the __next__() method on it:
ranked_chocolates = ("Dark", "Milk", "White")
chocolate1 = next(chocorator1)
chocolate2 = chocorator2.__next__()


# Iterate over item in sequence in reverse order
chocolate_bars = ("90%", "70%", "55%")

worst_first = reversed(chocolate_bars)

for chocolate in worst_first:
    print(chocolate)


# Iterate over co-indexed tuples with elements from each of the iterables
eng_nums = ["one", "two", "three"]
esp_nums = ["uno", "dos", "tres"]

zip_iter = zip(eng_nums, esp_nums)
eng, esp = next(zip_iter)
print(eng, esp)

for eng, esp in zip(eng_nums, esp_nums):
    print(eng, esp)
    
    
# Iterate over func(x) for x in iterable
# Same as [func(x) for x in iterable]
nums = [1, 2, 3, 4, 5]

# Map returns an iterator
squares1 = map(lambda num: num ** 2, nums)

# Create a list of all the elements from the iterator
squares1 = list(squares1)

# Compare to...
squares2 = [num**2 for num in nums]


# Iterate over x in iterable if func(x)
# Same as [x for x in iterable if func(x)]
nums = [1, 2, 3, 4, 5]

# Filter returns an iterator
even1 = filter(lambda num: num % 2 == 0, nums)

# Create a list of all the elements from the iterator
even1 = list(even1)

# Compare to...
even2 = [num for num in nums if num % 2 == 0]


# A generator is a type of iterator that yields results from a generator function.
# A generator function uses yield instead of return:
def evens():
    num = 0
    while num < 10:
        yield num
        num += 2
        
evengen = evens()

next(evengen)  # 0
next(evengen)  # 2
next(evengen)  # 4
next(evengen)  # 6
next(evengen)  # 8
# next(evengen)  # ❌ StopIteration exception


# We can use for loops on generators, since generators are just special types of iterators.
def evens(start, end):
    num = start + (start % 2)
    while num < end:
        yield num
        num += 2

for num in evens(12, 60):
   print(num)


# Looks a lot like...
evens = [num for num in range(12, 60) if num % 2 == 0]
# Or  = filter(lambda x: x % 2 == 0, range(12, 60))
for num in evens:
    print(num)
    
    
# Generators are lazy: they only generate the next item when needed.
# Why generate the whole sequence...
def find_matches(filename, match):
    matched = []
    for line in open(filename):
        if line.find(match) > -1:
            matched.append(line)
    return matched

# matched_lines = find_matches('frankenstein.txt', "!")
# matched_lines[0]
# matched_lines[1]


# ...if you only want some elements?
def find_matches(filename, match):
    for line in open(filename):
        if line.find(match) > -1:
            yield line

# line_iter = find_matches('frankenstein.txt', "!")
# next(line_iter)
# next(line_iter)


# A yield from statement yields the values from an iterator one at a time. 🍬
# Instead of...
def a_then_b(a, b):
    for item in a:
        yield item
    for item in b:
        yield item

list(a_then_b(["Apples", "Aardvarks"], ["Bananas", "BEARS"]))


# We can write...
def a_then_b(a, b):
    yield from a
    yield from b

list(a_then_b(["Apples", "Aardvarks"], ["Bananas", "BEARS"]))


# A yield from can also yield the results of a generator function.
# Instead of...
def factorial(n, accum):
    if n == 0:
        yield accum
    else:
        for result in factorial(n - 1, n * accum):
            yield result

for num in factorial(3, 1):
    print(num)
    
# We can write...
def factorial(n, accum):
    if n == 0:
        yield accum
    else:
        yield from factorial(n - 1, n * accum)

for num in factorial(3, 1):
    print(num)
    

# A pre-order traversal of the tree leaves:
def leaves(t):
    yield label(t)
    for c in branches(t):
        yield from leaves(c)

t = tree(20, [tree(12,
               [tree(9,
                  [tree(7), tree(2)]),
                tree(3)]),
              tree(8,
               [tree(4), tree(4)])])

leave_gen = leaves(t)
next(leave_gen)





