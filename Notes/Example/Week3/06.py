# Procedures are renamed num_squares1, num_squares2, etc., to allow them
# to be executed and tested together.

# Simple linear recursions.

def sum_squares1(N):
    """Return The sum of K**2 for K from 1 to N (inclusive).
    >>> sum_squares1(-1)
    0
    >>> sum_squares1(0)
    0
    >>> sum_squares1(1)
    1
    >>> sum_squares1(4)
    30
    """

    if N < 1:
        return 0
    else:
        return sum_squares1(N - 1) + N**2

# Tail-recursive sum_squares
def sum_squares2(N):
    """Return the sum of K**2 for 1 <= K <= N.
    >>> sum_squares2(-1)
    0
    >>> sum_squares2(0)
    0
    >>> sum_squares2(1)
    1
    >>> sum_squares2(4)
    30
    """

    def part_sum(accum, k):
        """Return the sum of ACCUM + K**2 + (K+1)**2 + ... + N**2."""
        if k > N:
            return accum
        else:
            return part_sum(accum + k**2, k + 1)
    return part_sum(0, 1)

# Iterattive version
def sum_squares3(N):
    """Return the sum of K**2 for 1 <= K <= N.
    >>> sum_squares3(-1)
    0
    >>> sum_squares3(0)
    0
    >>> sum_squares3(1)
    1
    >>> sum_squares3(4)
    30
    """

    accum = 0
    k = 1
    while k <= N:
        accum = accum + k**2
        k = k + 1
    return accum

import sys
from math import sqrt
from subprocess import Popen, DEVNULL, PIPE

sin60 = sqrt(3) / 2

# To use interactively:  Download 06.py from the cs61a.org website.
# Install gs (ghostscript) and put it in your path.  Then, run the command
#     python3 -i 06.py
# (or equivalent) on your local machine, at which point you can run
# >>> d = make_displayer()
# >>> draw_gasket(3, d.stdin)
# >>> draw_gasket(6, d.stdin)
# ...
# >>> stop_displayer(d)   # To clean up.

def make_gasket(n, x, y, s, output):
    """Write Postscript commands to OUTPUT that draw an Nth-order
    Sierpinski's gasket, with lower-left corner at (X,Y), and
    size S X S (units of points: 1/72 in)."""
    if n == 0:
        draw_solid_triangle(x, y, s, output)
    else:
        make_gasket(n - 1, x, y, s/2, output)
        make_gasket(n - 1, x + s/2, y, s/2, output)
        make_gasket(n - 1, x + s/4, y + sin60*s/2, s/2, output)

def draw_solid_triangle(x, y, s, output):
    """Draw a solid triangle lower-left corner at (X, Y)
    and side S on OUTPUT."""
    print(f"{x:.2f} {y:.2f} moveto "
          f"{s:.2f} 0 rlineto "
          f"-{s/2:.2f} {s*sin60:.2f} rlineto "
          "closepath fill", file=output)

def draw_gasket(n, output=sys.stdout, x=10, y=10, s=400):
    """Create a complete Postscript file for the gasket created by
    make_gasket(N, X, Y, S, OUTPUT)."""
    print("%!", file=output)
    make_gasket(n, x, y, s, output=output)
    print("showpage", file=output)
    output.flush()
    
def make_displayer():
    """Create a Ghostscript process that displays its input (sent in through
    .stdin)."""
    # Adjust the -gWIDTHxHEIGHT option to change drawing area.  Units are
    # pixels.
    return Popen(["gs", "-g1300x1000"],
                  universal_newlines=True, stdin=PIPE, stdout=DEVNULL)

def stop_displayer(d):
    """Terminate execution of displayer D (created by make_displayer)."""
    d.stdin.close()
    d.wait()
