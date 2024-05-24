def tree(label, children=None):
    """ Creates a tree whose root node is labeled LABEL and
        optionally has CHILDREN, a list of trees."""
    return (label, list(children or []))

def label(tree):
    """ Returns the label of the root node of TREE. """
    return tree[0]

def children(tree):
    """ Returns a list of children of TREE. """
    return tree[1]

def double(t):
    """Returns a tree identical to T, but with all labels doubled."""
    child = children(t)
    return tree(label(t) * 2, 
            [double(t) for t in child])

t = tree(20, [tree(12, [tree(9, [tree(7), tree(2)])]), tree(8, [tree(4), tree(4)])])


# a_tuple = (1, 2)
# a_tuple[0] = 3                  # 🚫 Error! Tuple items cannot be set.
# a_string = "Hi y'all"
# a_string[1] = "I"               # 🚫 Error! String elements cannot be set.
# a_string += ", how you doing?"  # 🤔 How does this work?
# an_int = 20
# an_int += 2                     # 🤔 And this?


grades = [90, 70, 85]
grades_copy = grades
grades[1] = 100
words = {"agua": "water"}
words["pavo"] = "turkey"


def tree(label, children=None):
    return [label] + list(children or [])

def label(tree):
    return tree[0]

def children(tree):
    return tree[1:]

def set_label(tree, label):
    tree[0] = label

def set_children(tree, children):
    tree[1] = children

def double(t):
    """Doubles every label in T, mutating T."""
    set_label(t, label(t) * 2)
    if not is_leaf(t):
        for c in children(t):
            double(c)


listA = [2, 3]
listB = listA

listC = listA[:]
listA[0] = 4
listB[1] = 5


listA = [2, 3]
listB = listA

listC = list(listA)
listA[0] = 4
listB[1] = 5


L = [1, 2, 3, 4, 5]

L[2] = 6

L[1:3] = [9, 8]

L[2:4] = []            # Deleting elements

L[1:1] = [2, 3, 4, 5]  # Inserting elements

L[len(L):] = [10, 11]  # Appending

L = L + [20, 30]

L[0:0] = range(-3, 0)  # Prepending


s = [2, 3]
t = [5, 6]
s.append(4)
s.append(t)
t = 0


s = [2, 3]
t = [5, 6]
# s.extend(4) # 🚫 Error: 4 is not an iterable!
s.extend(t)
t = 0


s = [2, 3]
t = [5, 6]
t = s.pop()


s = [6, 2, 4, 8, 4]
s.remove(4)


list1 = [1,2,3]
list2 = [1,2,3]
identical = list1 is list2
are_equal = list1 == list2
