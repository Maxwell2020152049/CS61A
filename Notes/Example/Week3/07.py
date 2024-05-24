def find_zero(lowest, highest, func):
    """Return a value v such that LOWEST <= v <= HIGHEST and 
    FUNC(v) == 0, or None if there is no such value.
    Assumes that FUNC is a non-descending function from integers
    to integers (that is, if a < b, then FUNC(a) <= FUNC(b).
    >>> find_zero(0, 10, lambda x: x - 4)
    4
    >>> find_zero(0, 100, lambda x: x**2 - 36)
    6
    >>> find_zero(0, 100, lambda x: x**2 - 37)
    """

    if lowest > highest:
         return None
    middle = (lowest + highest) // 2
    if func(middle) == 0:
        return middle
    elif func(middle) < 0:
        return find_zero(middle + 1, highest, func)
    else: 
        return find_zero(lowest, middle -1, func)
    

# Maze configuration from lecture

BLOCKS1 = { (0, 0), (0, 3), (0, 4), (0, 5), (0, 6), (1, 0), (1, 2), (1, 3),
            (1, 4), (1, 5), (2, 0), (2, 1), (2, 3), (2, 4), (2, 6), (3, 0),
            (3, 1), (3, 3), (3, 5), (3, 6), (4, 0), (4, 1), (4, 2), (4, 3),
            (4, 4), (4, 6), (5, 0), (5, 2), (5, 3), (5, 4), (5, 5), (6, 1),
            (6, 3), (6, 6), (7, 1), (7, 2), (7, 4), (7, 5), (8, 0), (8, 1),
            (8, 3), (8, 4), (8, 6), (9, 0), (9, 3), (9, 6) }

def maze1(x, y):
    return not 0 <= x < 10 or (x, y) in BLOCKS1

# Missing block at (7, 1)
BLOCKS2 = { (0, 0), (0, 3), (0, 4), (0, 5), (0, 6), (1, 0), (1, 2), (1, 3),
            (1, 4), (1, 5), (2, 0), (2, 1), (2, 3), (2, 4), (2, 6), (3, 0),
            (3, 1), (3, 3), (3, 5), (3, 6), (4, 0), (4, 1), (4, 2), (4, 3),
            (4, 4), (4, 6), (5, 0), (5, 2), (5, 3), (5, 4), (5, 5), (6, 1),
            (6, 3), (6, 6), (7, 2), (7, 4), (7, 5), (8, 0), (8, 1),
            (8, 3), (8, 4), (8, 6), (9, 0), (9, 3), (9, 6) }

def maze2(x, y):
    return not 0 <= x < 10 or (x, y) in BLOCKS2



def is_path(blocked, x0, y0):
   """True iff there is a path of squares from (X0, Y0) to some 
   square (x1, 0) such that all squares on the path (including first and
   last) are unoccupied.  BLOCKED is a predicate such that BLOCKED(x, y) 
   is true iff the grid square at (x, y) is occupied or off the edge.
   Each step of a path goes down one row and 1 or 0 columns left or right."""

   if blocked(x0, y0):
       return False
   elif y0 == 0:
       return True
   else:
       return (is_path(blocked, x0-1, y0-1) 
              or is_path(blocked, x0, y0-1) 
              or is_path(blocked, x0+1, y0-1))

def num_paths(blocked, x0, y0):
   """Return the number of unoccupied paths that run from (X0, Y0)
   to some square (x1, 0). BLOCKED is a predicate such that BLOCKED(x, y) 
   is true iff the grid square at (x, y) is occupied or off the edge. """

   if blocked(x0, y0):
       return 0
   elif y0 == 0:
       return 1
   else:
       return num_paths(blocked, x0, y0-1) \
            + num_paths(blocked, x0-1, y0-1) \
            + num_paths(blocked, x0+1, y0-1)
# OR (looking ahead a bit)
#      return sum( (num_paths(blocked, x0+k, y0-1)
#                   for k in range(-1, 2))
#                )

def num_partitions(n, k):
    """Return number of distinct ways to express N as a sum of 
    positive integers each of which is <= K, where K > 0."""
    if n < 0:
        return 0
    elif k == 1:
        return 1
    else:
        return num_partitions(n-k, k) + num_partitions(n, k-1)
