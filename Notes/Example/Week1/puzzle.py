# Example: program to solve Spelling Bee puzzles from the New York Times

import sys
from re import split

def find_words(word_list, must_contain, may_also_contain, min_length):
    """Return a list of all words in the list of strings WORD_LIST 
    that are at least MIN_LENGTH letters long, contain all the letters in 
    the string MUST_CONTAIN at least once, and consist only of letters 
    in MUST_CONTAIN and the string MAY_ALSO_CONTAIN."""

    must_contain_set = set(must_contain)
    may_contain_set = set(must_contain + may_also_contain)

    return [ word for word in word_list
                 if len(word) >= min_length and
                    must_contain_set <= set(word) <= may_contain_set ]

# Read in dictionary, and split it up into a list of words.
words = split(r'\s+', open('words01.txt').read().strip())

# Example from first lecture, corresponding to the puzzle
#                   B
#                O     C
#                   T
#                L     E
#                   I

print(find_words(words, "t", "bceilo", 5))

# Same puzzle, but look for words that use all the letters at least once.

print(find_words(words, "tbceilo", "", 5))
