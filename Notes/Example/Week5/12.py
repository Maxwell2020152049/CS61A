# Dictionaries

states = {
	"CA": "California",
	"DE": "Delaware",
	"NY": "New York",
	"TX": "Texas",
	"WY": "Wyoming"
}

print(len(states))
print("CA" in states)
print("ZZ" in states)

# Dictionary selection

words = {
	"mÃ¡s": "more",
	"otro": "other",
	"agua": "water"
}

print(words["otro"])
first_word = "agua"
print(words[first_word])
# words["pavo"] - error!
print(words.get("pavo", "ðŸ¤”"))

# Dictionary - mutating
users = {}
users["profpamela"] = "b3stp@ssEvErDontHackMe"
users["profpamela"] += "itsLongerSoItsMoreSecure!!"
print(users["profpamela"])

# Dict of dicts
spiders = {
  "smeringopus": {
	  "name": "Pale Daddy Long-leg",
	  "length": 7
  },
  "holocnemus pluchei": {
	  "name": "Marbled cellar spider",
	  "length": (5, 7)
  }
}

# Dictionary iteration
insects = {"spiders": 8, "centipedes": 100, "bees": 6}
for name in insects:
    print(insects[name])

# Matrix- Implementation A
def matrix(rows, cols):
    return [ [0 for col in range(cols)] for row in range(rows) ]

def value(matrix, row, col):
    return matrix[row][col]

def set_value(matrix, row, col, val):
    matrix[row][col] = val

# Matrix- Implementation B
def matrix(rows, cols):
    return [ [0 for row in range(rows)] for col in range(cols) ]

def value(matrix, row, col):
    return matrix[col][row]

def set_value(matrix, row, col, val):
    matrix[col][row] = val

# Matrix- Implementation C
def matrix(rows, cols):
    return tuple( [0 for col in range(cols)] for row in range(rows) )

def value(matrix, row, col):
    return matrix[row][col]

def set_value(matrix, row, col, val):
    matrix[row][col] = val

# Matrix- Implementation D2
def matrix(rows, cols):
    return [ tuple(0 for col in range(cols))
        for row in range(rows) ]

def value(matrix, row, col):
    return matrix[row][col]

def set_value(matrix, row, col, val):
    matrix[row] = matrix[row][:col] + (val,) + matrix[row][col+1:]

m = matrix(3, 4)
set_value(m, 0, 0, 1)
set_value(m, 0, 1, 2)
set_value(m, 0, 3, 4)

# Tree - Implementation A
def tree(label, children=[]):
    return [label] + children

def label(tree):
    return tree[0]

def children(tree):
    return tree[1:]

def is_leaf(tree):
    return len(children(tree)) == 0

# Tree- Implementation B
def tree(label, children=[]):
    return (label, children)

def label(tree):
    return tree[0]

def children(tree):
    return tree[1]

# Tree - Implementation C
def tree(label, children=[]):
    return {"l": label, "c": children}

def label(tree):
    return tree["l"]

def children(tree):
    return tree["c"]

t = tree(20, [tree(12,
               [tree(9,
                  [tree(7), tree(2)]),
                tree(3)]),
              tree(8,
                [tree(4), tree(4)])])

# Tree processing

def count_leaves(t):
    """Returns the number of leaf nodes in T."""
    if is_leaf(t):
        return 1
    else:
        children_leaves = 0
        for c in children(t):
            children_leaves += count_leaves(c)
        return children_leaves

def count_leaves(t):
    """Returns the number of leaf nodes in T."""
    if is_leaf(t):
        return 1
    else:
        return sum([count_leaves(c) for c in children(t)])

def double(t):
    """Returns a tree identical to T, but with all labels doubled."""
    if is_leaf(t):
        return tree(label(t) * 2)
    else:
        return tree(label(t) * 2,
            [double(c) for c in children(t)])

def double(t):
    """Returns a tree identical to T, but with all labels doubled."""
    if is_leaf(t):
        return tree(label(t) * 2)
    else:
        doubled_children = []
        for c in children(t):
            doubled_children.append(double(c))
        return tree(label(t) * 2, doubled_children)

def double(t):
    """Returns the number of leaf nodes in T."""
    return tree(label(t) * 2,
            [double(c) for c in children(t)])