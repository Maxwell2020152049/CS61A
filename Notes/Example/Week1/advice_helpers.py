# There are helper functions,
# just so that we can avoid calling object methods for demo 1
def read_file(file):
    return file.read()

def count(str, text):
    return str.count(text)

def lower(str):
    return str.lower()

def split(str):
    return str.split()

# These helper functions identify top words

# A not that helpful function that we soon abandon!
def find_top_word(words):
    word_counts = {}
    for word in words:
        if not word in word_counts:
            word_counts[word] = 0
        word_counts[word] += 1
    
    top_word_count = 1
    top_word = ""
    for word, count in word_counts.items():
        if count > top_word_count:
            top_word = word
            top_word_count = count
    return top_word

# Returns a list of words by frequency
def rank_words(words):
    word_counts = {}
    for word in words:
        if not word in word_counts:
            word_counts[word] = 0
        word_counts[word] += 1
    return sorted(word_counts, key=word_counts.get, reverse=True)

def text_extractor(str, starter, stopper="\n"):
    found_at = 0
    while found_at > -1:
        found_at = str.find(starter + " ")
        end_at = str.find(stopper, found_at)
        yield str[found_at:end_at]
        str = str[end_at:]
