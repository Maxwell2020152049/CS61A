# Import helper functions
from advice_helpers import *

# Open the file 
filename = "advice.txt"
advice_file = open(filename, encoding="utf8")
advice = read_file(advice_file)
# Or in one line:
advice = read_file(open(filename))
# Also lowercase it in that one line!
advice = lower(read_file(open(filename, encoding="utf8")))

# Begin analyzing the advice:
len(advice)
"exams" in advice
"study for exams" in advice
"eat exams" in advice 

count(advice, "exams")
154 / 1100 * 100

# Start a word-level analysis:
advice_words = advice.split()

max(advice_words)

min(advice_words)

find_top_word(advice_words)

ranked = rank_words(advice_words)

ranked[0:10]

ranked[10:20]

# Extract advice starting with a phrase:
extractor = text_extractor(advice, "practice")

next(extractor)
next(extractor)
next(extractor)

for text in extractor:
    print(text)
