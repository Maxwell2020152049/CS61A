### Linked Lists

class Link:
    """A linked list node."""
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'
 
    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'

# Useful utility for testing
def toLinked(L):
    """Returns a linked-list representation of the Python iterable L."""
    if len(L) == 0:
        return Link.empty
    result = last = Link(L[0], Link.empty)
    for item in L[1:]:
        last.rest = Link(item)
        last = last.rest
    return result

def split(L):
    """Returns (Mid, Last, Length), where Last is the last node in
    linked list L, Mid is the node at or (for even length) just before
    the middle, and Length is the length.
    If L is empty, returns (empty, empty, 0).
    >>> split(toLinked([1, 2, 3, 4, 5]))
    (Link(3, Link(4, Link(5))), Link(5), 5)
    >>> split(toLinked([1, 2, 3, 4]))
    (Link(2, Link(3, Link(4))), Link(4), 4)
"""    

    if L is Link.empty:
        return (Link.empty, Link.empty, 0)
    else:
        M = L
        N = 1
        while L.rest is not Link.empty:
            L = L.rest
            N += 1
            if N % 2 == 1:
                M = M.rest
        return M, L, N

def intersperse(L, pred, inserts):
    """Returns a copy of linked list L in which the items whose
    values satisfy PRED (a one-argument, boolean function) are
    followed by successive values from linked list INSERTS, until
    INSERTS is exhausted. The function is non-destructive.
    >>> data = toLinked([1, 2, 3, 4, 5])
    >>> alt = toLinked([10, 11, 12, 13])
    >>> print(intersperse(data, lambda x: x % 2 == 1, alt))
    <1 10 2 3 11 4 5 12>
    >>> print(intersperse(data, lambda x: True, alt))
    <1 10 2 11 3 12 4 13 5>
    """
    if L is Link.empty or inserts is Link.empty:
        return L
    elif pred(L.first):
        return Link(L.first,
                    Link(inserts.first,
                         intersperse(L.rest, pred, inserts.rest)))
    else:
        return Link(L.first,
                    intersperse(L.rest, pred, inserts))

def intersperse2(L, pred, inserts):
    """Returns a copy of linked list L in which the items whose
    values satisfy PRED (a one-argument, boolean function) are
    followed by successive values from linked list INSERTS, until
    INSERTS is exhausted. The function is non-destructive.
    >>> data = toLinked([1, 2, 3, 4, 5])
    >>> alt = toLinked([10, 11, 12, 13])
    >>> print(intersperse2(data, lambda x: x % 2 == 1, alt))
    <1 10 2 3 11 4 5 12>
    >>> print(intersperse2(data, lambda x: True, alt))
    <1 10 2 11 3 12 4 13 5>
    """
    sentinel = Link(None)

    last = sentinel
    while L is not Link.empty and inserts is not Link.empty:
        if pred(L.first):
            last.rest = Link(L.first, Link(inserts.first))
            inserts = inserts.rest
            last = last.rest.rest
        else:
            last.rest = Link(L.first)
            last = last.rest
        L = L.rest
    last.rest = L

    return sentinel.rest

def dintersperse(L, pred, inserts):
    """Returns a copy of linked list L in which the items whose
    values satisfy PRED (a one-argument, boolean function) are
    followed by successive values from linked list INSERTS, until
    INSERTS is exhausted. The function is destructive and creates no
    new Link nodes.
    >>> data = toLinked([1, 2, 3, 4, 5])
    >>> alt = toLinked([10, 11, 12, 13])
    >>> print(dintersperse(data, lambda x: x % 2 == 1, alt))
    <1 10 2 3 11 4 5 12>
    >>> data = toLinked([1, 2, 3, 4, 5])
    >>> alt = toLinked([10, 11, 12, 13])
    >>> final = dintersperse(data, lambda x: True, alt)
    >>> print(final)
    <1 10 2 11 3 12 4 13 5>
    >>> final is data
    True
"""
    result = L
    if L is Link.empty or inserts is Link.empty:
        return result
    elif pred(L.first):
        L = L.rest
        result.rest = inserts
        inserts = inserts.rest
        result.rest.rest = dintersperse(L, pred, inserts)
    else:
        L = L.rest
        result.rest = dintersperse(L, pred, inserts)
    return result


### Binary Trees

class BTree:
    """A tree with exactly two branches, which may be empty."""
    empty = None   # Placeholder

    def __init__(self, label, left=None, right=None):
        self.label = label
        self.left = left or BTree.empty
        self.right = right or BTree.empty

    def __repr__(self):
        if self.left == self.right == BTree.empty:
            return f'BTree({repr(self.label)})'
        elif self.right is BTree.empty:
            return f'BTree({repr(self.label)}, {repr(self.left)})'
        elif self.left is BTree.empty:
            return f'BTree({repr(self.label)}, BTree.empty, {repr(self.right)})'
        else:
            return f'BTree({repr(self.label)}, {repr(self.left)}, {repr(self.right)})'

BTree.empty = BTree(None)

def isIn(T, target):
    """Return True iff T contains the label TARGET.
    >>> animals = BTree('cow', 
    ...                 BTree('bear', BTree('axolotl', right=BTree('bat'))),
    ...                 BTree('platypus', BTree('lion'), BTree('viper')))
    >>> isIn(animals, 'viper')
    True
    >>> isIn(animals, 'elephant')
    False
"""
    if T is BTree.empty:
        return False
    elif target == T.label:
        return True
    elif target < T.label:
        return isIn(T.left, target)
    else:
        return isIn(T.right, target)

def add(T, target):
    """Destructively modify T to add the label TARGET, if it is not already
    present.  Return the resulting tree.
    >>> animals = BTree('cow', 
    ...                 BTree('bear', BTree('axolotl', right=BTree('bat'))),
    ...                 BTree('platypus', BTree('lion'), BTree('viper')))
    >>> add(animals, 'dog')
    BTree('cow', BTree('bear', BTree('axolotl', BTree.empty, BTree('bat'))), BTree('platypus', BTree('lion', BTree('dog')), BTree('viper')))
    >>> add(animals, 'bear')
    BTree('cow', BTree('bear', BTree('axolotl', BTree.empty, BTree('bat'))), BTree('platypus', BTree('lion', BTree('dog')), BTree('viper')))
"""
    if T is BTree.empty:
        return BTree(target)
    elif target < T.label:
        T.left = add(T.left, target)
    elif target > T.label:
        T.right = add(T.right, target)
    return T
