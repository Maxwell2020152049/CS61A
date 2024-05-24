# Towers of Hanoi

def move_tower(n, start_peg, end_peg):
    """Perform moves that transfer an ordered tower of N>0 disks in the
    Towers of Hanoi puzzle from peg START_PEG to peg END_PEG, where 
    1 <= START_PEG, END_PEG <= 3, and START_PEG != END_PEG. Assumes
    the disks to be moved are all smaller than those on the other pegs."""

    if n == 1:
        move_disk(start_peg, end_peg)
    else:
        spare_peg = 6 - start_peg - end_peg
        move_tower(n - 1, start_peg, spare_peg)
        move_disk(start_peg, end_peg)
        move_tower(n - 1, spare_peg, end_peg)


## Extra fancy stuff for showing the moves, setting up, and solving the puzzle.

import time

PAUSE = 1.0

pegs = [0, [], [], []]

def solve_puzzle(n):
    """Show the moves to solve a Towers of Hanoi problem for a tower
    of N>0 disks."""
    set_up_puzzle(n)
    print_puzzle()
    time.sleep(PAUSE)
    move_tower(n, 1, 3)

def set_up_puzzle(n):
    """Set up Towers of Hanoi puzzle with N disks on peg 1, and
    other pegs empty."""
    pegs[:] = [n, [ k for k in range(n, 0, -1) ], [], []]

def move_disk(peg0, peg1):
    """Move disk from PEG0 and PEG1, printing the result."""
    pegs[peg1].append(pegs[peg0].pop())
    print_puzzle()
    time.sleep(PAUSE)
    
def print_puzzle():
    """Print current configuration of puzzle (stored in pegs)."""
    n = pegs[0]
    for k in range(n, 0, -1):
        for j in range(1, 4):
            print(" ", end="")
            if len(pegs[j]) >= k:
                c = pegs[j][k-1]
                print(" " + " " * (n - c) + "##" * c + " " * (n - c) + " ", end="")
            else:
                print(" " * (2 * n + 2), end="")
        print()
    print("=" * (6*n + 9))
    print(" " * (n+2) + "1" + " " * (2 * n + 2) + "2" + " " * (2 * n + 2) + "3")
    print()
            

# Deleting digits (spoiler alert!)

def remove_digit(n, digit):
    """Assuming N>=0, 0 <= DIGIT <= 9, return a number whose
    base-10 representation is the same as N, but with all instances of
    DIGIT removed.  If all digits removed, return 0.
    >>> remove_digit(123, 3)
    12
    >>> remove_digit(1234, 5)
    1234
    >>> remove_digit(1234, 1)
    234
    >>> remove_digit(111111, 1)
    0
    """
    if n == 0:
        return 0
    if n % 10 == digit:
        return remove_digit(n // 10, digit)
    return n % 10 + remove_digit(n // 10, digit) * 10
