### Solutions to problems in last slide.

import re


## Match a hexadecimal number in Python (starts with 0x).

for m in re.finditer(r'0[xX][0-9a-fA-F]+',
                     "This is in hex: 0x1aBc.  This is not: 12.  This is: 0X33a"):
    print(m.group(0))

## Match a list of words separated by commas and whitespace (such
## as "cat, dog,   gnu, zebra".

print(re.search(r'\b(\w+,\s+)+\w+',
                "I own a cat, dog, gnu, zebra among others").group(0))

# In the above, I assume that a list must contain more than one item.

## Match text in parentheses.
# This can't be done while ensuring proper nesting, but we can at least 
# guarantee that we start and end with a parenthesis:

print(re.search(r'\(.*\)',
                "Here is a parenthesized expression: (1 + (2 * 3) + 6))")
          .group(0))

# The above will match 
#    (1 + (2 * 3) + 6))
# even though it is unbalanced (as long as it's all one one line).


## Match text in parentheses that are not nested.

print(re.search(r'\([^()]*\)', "Text (with (some) parentheses)").group(0))

# The above will match just "(some)")
