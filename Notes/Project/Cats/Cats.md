# Project 2: CS 61A Autocorrected Typing Software

`Project`地址：[Project 2: CS 61A Autocorrected Typing Software](https://inst.eecs.berkeley.edu/~cs61a/sp21/proj/cats/)

使用如下命令可以下载项目：

```shell
wget https://inst.eecs.berkeley.edu/~cs61a/sp21/proj/cats/cats.zip
```

项目的最终效果类似：[Final Product](https://cats.cs61a.org/)

## Phase 1: Typing

### Problem 1 (1 pt)

实现`choose(paragraphs, select, k)`函数：

- `paragraphs`：一个字符串列表
- `select`：选择函数，参数为字符串，若符合要求，返回`True`，否则返回`False`
- `k`：函数返回第`k`个符合要求的字符串

使用如下命令进行解锁测试：

```shell
python3 ok -q 01 -u --local
```

过程如下：

```shell
=====================================================================
Assignment: Project 2: Cats
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 1 > Suite 1 > Case 1
(cases remaining: 102)

>>> from cats import choose
>>> ps = ['short', 'really long', 'tiny']
>>> s = lambda p: len(p) <= 5
>>> choose(ps, s, 0)
? 'short'
-- OK! --

>>> choose(ps, s, 1)
? 'tiny'
-- OK! --

>>> choose(ps, s, 2)
? ''
-- OK! --

---------------------------------------------------------------------
OK! All cases for Problem 1 unlocked.

Cannot backup when running ok with --local.
```

实现代码如下：

```python
def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns True. If there are fewer than K such paragraphs, return
    the empty string.

    Arguments:
        paragraphs: a list of strings
        select: a function that returns True for paragraphs that can be selected
        k: an integer

    >>> ps = ['hi', 'how are you', 'fine']
    >>> s = lambda p: len(p) <= 4
    >>> choose(ps, s, 0)
    'hi'
    >>> choose(ps, s, 1)
    'fine'
    >>> choose(ps, s, 2)
    ''
    """
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    for str in paragraphs:
        if select(str):
            if k == 0:
                return str
            k -= 1
    return ''
    # END PROBLEM 1
```

### Problem 2 (2 pt)

实现`about(topic)`函数：

- `topic`：一个字符串列表，字符串都是小写单词

返回一个`select(str)`函数，若`str`包含`topic`中的某个单词，返回`True`，否则返回`False`。

注意：判断是否包含某个单词的时候，不区分大小写。

使用如下命令进行解锁测试：

```shell
python3 ok -q 02 -u --local
```

过程如下：

```shell
=====================================================================
Assignment: Project 2: Cats
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 2 > Suite 1 > Case 1
(cases remaining: 102)

>>> from cats import about
>>> from cats import choose
>>> dogs = about(['dogs', 'hounds'])
>>> dogs('A paragraph about cats.')
? False
-- OK! --

>>> dogs('A paragraph about dogs.')
? True
-- OK! --

>>> dogs('Release the Hounds!')
? True
-- OK! --

>>> dogs('"DOGS" stands for Department Of Geophysical Science.')
? True
-- OK! --

>>> dogs('Do gs and ho unds don\'t count')
? False
-- OK! --

>>> dogs("AdogsParagraph")
? False
-- OK! --

---------------------------------------------------------------------
OK! All cases for Problem 2 unlocked.

Cannot backup when running ok with --local.
```

实现思路：先使用`remove_punctuation`函数去掉`str`的标点符号，再使用`lower`函数把所有字母变成小写，再使用`split`将字符串分割成单词列表（分隔符为空格）。

实现代码如下：

```python
def about(topic):
    """Return a select function that returns whether
    a paragraph contains one of the words in TOPIC.

    Arguments:
        topic: a list of words related to a subject

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    def select(str):
        str_rm_punc = remove_punctuation(str)
        str_lower = lower(str_rm_punc)
        str_split = split(str_lower)

        for word in str_split:
            if word in topic:
                return True
        return False

    return select
    # END PROBLEM 2
```

### Problem 3 (1 pt)

实现一个`accuracy(typed, reference)`：

- `typed`：正在输入的字符串
- `reference`：打字软件给出的字符串

返回打字的正确率，即两个字符串中相同位置的单词相同的比例。

注意：要求返回值是浮点数，比例的分母是`typed`中单词的个数。

使用如下命令进行解锁测试：

```shell
python3 ok -q 03 -u --local
```

过程如下：

```shell
=====================================================================
Assignment: Project 2: Cats
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 3 > Suite 1 > Case 1
(cases remaining: 103)

>>> from cats import accuracy
>>> accuracy("12345", "12345") # This should return 100.0 (not the integer 100!)
? 100.0
-- OK! --

>>> accuracy("a b c", "a b c")
? 100.0
-- OK! --

>>> accuracy("a  b  c  d", "b  a  c  d")
? 50.0
-- OK! --

>>> accuracy("a b", "c d e")
? 0.0
-- OK! --

>>> accuracy("Cat", "cat") # the function is case-sensitive
? 0.0
-- OK! --

>>> accuracy("a b c d", " a d ")
? 25.0
-- OK! --

>>> accuracy("abc", " ")
? 0.0
-- OK! --

>>> accuracy(" a b \tc" , "a b c") # Tabs don't count as words
? 100.0
-- OK! --

>>> accuracy("abc", "")
? 0.0
-- OK! --

>>> accuracy("", "abc")
? 0.0
-- OK! --

>>> accuracy("cats.", "cats") # punctuation counts
? 0.0
-- OK! --

>>> accuracy("", "") # Returns 100.0
? 100.0
-- OK! --

---------------------------------------------------------------------
OK! All cases for Problem 3 unlocked.

Cannot backup when running ok with --local.
```

实现代码如下：

```python
def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    Arguments:
        typed: a string that may contain typos
        reference: a string without errors

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    >>> accuracy('', '')
    100.0
    """
    typed_words = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    len_typed = len(typed_words)
    len_ref = len(reference_words)

    if len_typed == 0 and len_ref == 0:
        return 100.0
    elif len_typed == 0 or len_ref == 0:
        return 0.0

    ans = sum([1 for x, y in zip(typed_words, reference_words) if x == y])
    ans /= len_typed

    return ans * 100.0

    # END PROBLEM 3
```

### Problem 4 (1 pt)

实现一个`wpm(typed, elapsed)`函数：

- `typed`：已经输入的字符串
- `elapsed`：已经经过的时间，单位是秒（`s`）

`wpm`即`words per minute`，不过单词的计数是5个字母算一个单词。

注意：返回结果是浮点数。

使用如下命令进行解锁测试：

```shell
python3 ok -q 04 -u --local
```

过程如下：

```shell
=====================================================================
Assignment: Project 2: Cats
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 4 > Suite 1 > Case 1
(cases remaining: 104)

>>> from cats import wpm
>>> wpm("12345", 3) # Note: wpm returns a float (with a decimal point)
? 20
-- Not quite. Try again! --

? 20.0
-- OK! --

>>> wpm("a b c", 20)
? 3.0
-- OK! --

>>> wpm("", 10)
? 0.0
-- OK! --

---------------------------------------------------------------------
OK! All cases for Problem 4 unlocked.

Cannot backup when running ok with --local.
```

实现代码如下：

```python
def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string.

    Arguments:
        typed: an entered string
        elapsed: an amount of time in seconds

    >>> wpm('hello friend hello buddy hello', 15)
    24.0
    >>> wpm('0123456789',60)
    2.0
    """
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    return (len(typed) / 5.0) / (elapsed / 60.0)
    # END PROBLEM 4
```

使用以下命令可以进行打字测试（测试的字符串的主题与`cats`和`kittens`有关）：

```shell
python3 cats.py -t cats kittens
```

使用以下命令可以运行项目的`GUI`界面：

```shell
python3 gui.py
```

## Phase 2: Autocorrect

实现一个自动纠错功能（`Autocorrect`），在网页`GUI`中，按空格可以把错误的单词换成词典中最接近的正确的单词。

### Problem 5 (2 pt)

实现`autocorrect(typed_word, valid_words, diff_function, limit)`函数：

- `typed_word`：正在输入的单词
- `valid_words`：合法的单词的列表
- `diff_function`：差别函数
- `limit`：最大限制

使用`diff_function`函数，返回`typed_word`和`valid_words`中的单词的差别值，返回差别最小的那个；如果最小的差别值都比`limit`大，就返回`typed_word`本身。

注意：如果`typed_word`已经在`valid_words`中，那么就返回`typed_word`；如果有不止一个差别最小的单词，返回最早进行检测的。

使用如下命令进行解锁测试：

```shell
python3 ok -q 05 -u --local
```

过程如下：

```shell
=====================================================================
Assignment: Project 2: Cats
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 5 > Suite 1 > Case 1
(cases remaining: 104)

>>> from cats import autocorrect, lines_from_file
>>> abs_diff = lambda w1, w2, limit: abs(len(w2) - len(w1))
>>> autocorrect("cul", ["culture", "cult", "cultivate"], abs_diff, 10)
? 'cult'
-- OK! --

>>> autocorrect("cul", ["culture", "cult", "cultivate"], abs_diff, 0)
? cul
-- Not quite. Try again! --

? 'cul'
-- OK! --

>>> autocorrect("wor", ["worry", "car", "part"], abs_diff, 10)
? 'car'
-- OK! --

>>> first_diff = lambda w1, w2, limit: 1 if w1[0] != w2[0] else 0
>>> autocorrect("wrod", ["word", "rod"], first_diff, 1)
? 'wrod'
-- Not quite. Try again! --

? 'rod'
-- Not quite. Try again! --

? 'word'
-- OK! --

>>> autocorrect("inside", ["idea", "inside"], first_diff, 0.5)
? 'idea'
-- Not quite. Try again! --

? 'inside'
-- OK! --

>>> autocorrect("inside", ["idea", "insider"], first_diff, 0.5)
? 'insider'
-- Not quite. Try again! --

? 'idea'
-- OK! --

>>> autocorrect("outside", ["idea", "insider"], first_diff, 0.5)
? 'outside'
-- OK! --

---------------------------------------------------------------------
OK! All cases for Problem 5 unlocked.

Cannot backup when running ok with --local.
```

实现代码如下：

```python
def autocorrect(typed_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from TYPED_WORD. Instead returns TYPED_WORD if that difference is greater
    than LIMIT.

    Arguments:
        typed_word: a string representing a word that may contain typos
        valid_words: a list of strings representing valid words
        diff_function: a function quantifying the difference between two words
        limit: a number

    >>> ten_diff = lambda w1, w2, limit: 10 # Always returns 10
    >>> autocorrect("hwllo", ["butter", "hello", "potato"], ten_diff, 20)
    'butter'
    >>> first_diff = lambda w1, w2, limit: (1 if w1[0] != w2[0] else 0) # Checks for matching first char
    >>> autocorrect("tosting", ["testing", "asking", "fasting"], first_diff, 10)
    'testing'
    """
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    if typed_word in valid_words:
        return typed_word
    
    diff = limit
    return_word = typed_word
    for word_valid in valid_words:
        tmp = diff_function(typed_word, word_valid, limit)
        if tmp < diff:
            diff = tmp
            return_word = word_valid
        elif tmp == diff and return_word == typed_word:
            return_word = word_valid
        
    return return_word
    # END PROBLEM 5
```

### Problem 6 (2 pts)

实现`sphinx_switches(start, goal, limit)`函数：

- `start`：起始单词
- `goal`：目标单词
- `limit`：最多允许修改的字母数

返回从`start`变成`goal`最少需要修改的字母数（逐位匹配）。

注意：不允许使用循环语句，要求使用递归实现，若发现需要修改的字面数大于`limit`，立即返回。

使用如下命令进行解锁测试：

```shell
python3 ok -q 06 -u --local
```

过程如下：

```shell
=====================================================================
Assignment: Project 2: Cats
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 6 > Suite 1 > Case 1
(cases remaining: 105)

>>> from cats import sphinx_switches, autocorrect
>>> import tests.construct_check as test
>>> big_limit = 10
>>> sphinx_switches("car", "cad", big_limit)
? 1
-- OK! --

>>> sphinx_switches("this", "that", big_limit)
? 2
-- OK! --

>>> sphinx_switches("one", "two", big_limit)
? 3
-- OK! --

>>> sphinx_switches("from", "form", big_limit)
? 2
-- OK! --

>>> sphinx_switches("awe", "awesome", big_limit)
? 4
-- OK! --

>>> sphinx_switches("someawe", "awesome", big_limit)
? 6
-- OK! --

>>> sphinx_switches("awful", "awesome", big_limit)
? 4
-- Not quite. Try again! --

? 5
-- OK! --

>>> sphinx_switches("awful", "awesome", 3) > 3
? False
-- Not quite. Try again! --

? True
-- OK! --

>>> sphinx_switches("awful", "awesome", 4) > 4
? True
-- OK! --

>>> sphinx_switches("awful", "awesome", 5) > 5
? False
-- OK! --

---------------------------------------------------------------------
OK! All cases for Problem 6 unlocked.

Cannot backup when running ok with --local.

```

实现代码如下：

```python
def sphinx_switches(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths and returns the result.

    Arguments:
        start: a starting word
        goal: a string representing a desired goal word
        limit: a number representing an upper bound on the number of chars that must change

    >>> big_limit = 10
    >>> sphinx_switches("nice", "rice", big_limit)    # Substitute: n -> r
    1
    >>> sphinx_switches("range", "rungs", big_limit)  # Substitute: a -> u, e -> s
    2
    >>> sphinx_switches("pill", "pillage", big_limit) # Don't substitute anything, length difference of 3.
    3
    >>> sphinx_switches("roses", "arose", big_limit)  # Substitute: r -> a, o -> r, s -> o, e -> s, s -> e
    5
    >>> sphinx_switches("rose", "hello", big_limit)   # Substitute: r->h, o->e, s->l, e->l, length difference of 1.
    5
    """
    # BEGIN PROBLEM 6
    def switch(start, goal, limit, change_cnt):
        if change_cnt > limit or len(start) == 0 or len(goal) == 0:
            return change_cnt

        return switch(start[1:], goal[1:], limit, 
            (1 if start[0] != goal[0] else 0) + change_cnt)

    return switch(start, goal, limit, abs(len(start) - len(goal)))
    # END PROBLEM 6
```

另一种解法，写完`Problem 7`才想到的，本题可以看作只支持替换操作（添加和删除操作只有不能替换时才考虑）：

```python
    if limit < 0:
        return 0
    
    elif not start or not goal:
        return abs(len(start) - len(goal))

    else:
        tmp = 0 if start[0] == goal[0] else 1
        return sphinx_switches(start[1:], goal[1:], limit - tmp) + tmp
```

### Problem 7 (3 pt)

实现`pawssible_patches(start, goal, limit)`函数：

- `start`：起始单词
- `goal`：目标单词
- `limit`：最多允许修改的字母数

允许以下操作：

- 删除`start`的一个字母
- 给`start`添加一个字母
- 替换`start`的一个字母

实现代码如下：

```python
def pawssible_patches(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL.
    This function takes in a string START, a string GOAL, and a number LIMIT.

    Arguments:
        start: a starting word
        goal: a goal word
        limit: a number representing an upper bound on the number of edits

    >>> big_limit = 10
    >>> pawssible_patches("cats", "scat", big_limit)       # cats -> scats -> scat
    2
    >>> pawssible_patches("purng", "purring", big_limit)   # purng -> purrng -> purring
    2
    >>> pawssible_patches("ckiteus", "kittens", big_limit) # ckiteus -> kiteus -> kitteus -> kittens
    3
    """
    if limit < 0:  # Fill in the condition
        # BEGIN
        "*** YOUR CODE HERE ***"
        return 0
        # END

    elif not start or not goal:  # Feel free to remove or add additional cases
        # BEGIN
        "*** YOUR CODE HERE ***"
        return abs(len(start) - len(goal))
        # END

    else:
        add = pawssible_patches(start, goal[1:], limit - 1) + 1  # Fill in these lines
        remove = pawssible_patches(start[1:], goal, limit - 1) + 1

        tmp = 0 if start[0] == goal[0] else 1

        substitute = pawssible_patches(start[1:], goal[1:], limit - tmp) + tmp
        # BEGIN
        "*** YOUR CODE HERE ***"
        return min(add, remove, substitute)
        # END
```

### (Optional) Extension: final diff (0pt)

本题是自行设计一个`diff`函数，返回尽可能小的差别值。

先挖个坑，以后再填。

使用以下命令可以测试`diff`函数的效率和准确率：

```shell
python3 score.py
```

测试`sphinx_switches`结果如下：

```shell
Correction Speed: 74436.21742690227 wpm
Correctly Corrected: 422 words
Incorrectly Corrected: 406 words
Uncorrected: 112 words
```

测试`pawssible_patches`结果如下：

```shell
Correction Speed: 198.3337695674132 wpm
Correctly Corrected: 124 words
Incorrectly Corrected: 15 words
Uncorrected: 12 words
```

## Phase 3: Multiplayer

### Problem 8 (2 pt)

实现`report_progress(typed, prompt, user_id, send)`函数：

- `typed`：已输入的单词列表
- `prompt`：需要完成的单词列表
- `user_id`：用户`id`
- `send`：发送函数，可以发送一个字典{'id': 1, 'progress': 0.6}给服务器，`id`键对应用户`id`，`progress`键对应当前进度。

使用如下命令进行解锁测试：

```shell
python3 ok -q 08 -u --local
```

过程如下：

```shell
=====================================================================
Assignment: Project 2: Cats
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 8 > Suite 1 > Case 1
(cases remaining: 102)

>>> from cats import report_progress
>>> print_progress = lambda d: print('ID:', d['id'], 'Progress:', d['progress'])
>>> typed = ['I', 'have', 'begun']
>>> prompt = ['I', 'have', 'begun', 'to', 'type']
>>> print_progress({'id': 1, 'progress': 0.6})
? {'id': 1, 'progress': 0.6}
-- Not quite. Try again! --

? 'id': 1, 'progress': 0.6
-- Not quite. Try again! --

? ID: 1 Progress: 0.6
-- OK! --

>>> report_progress(typed, prompt, 1, print_progress) # print_progress is called on the report
(line 1)? ID: 1 Progress: 0.6
(line 2)? 0.6
-- OK! --

>>> report_progress(['I', 'begun'], prompt, 2, print_progress)
(line 1)? ID: 2 Progress: 0.2
(line 2)? 0.2
-- OK! --

>>> report_progress(['I', 'hve', 'begun', 'to', 'type'], prompt, 3, print_progress)
(line 1)? ID: 3 Progress: 0.2
(line 2)? 0.2
-- OK! --

---------------------------------------------------------------------
OK! All cases for Problem 8 unlocked.

Cannot backup when running ok with --local.
```

实现代码如下：

```python
def report_progress(typed, prompt, user_id, send):
    """Send a report of your id and progress so far to the multiplayer server.
    Returns the progress so far.

    Arguments:
        typed: a list of the words typed so far
        prompt: a list of the words in the typing prompt
        user_id: a number representing the id of the current user
        send: a function used to send progress to the multiplayer server

    >>> print_progress = lambda d: print('ID:', d['id'], 'Progress:', d['progress'])
    >>> # The above function displays progress in the format ID: __, Progress: __
    >>> print_progress({'id': 1, 'progress': 0.6})
    ID: 1 Progress: 0.6
    >>> typed = ['how', 'are', 'you']
    >>> prompt = ['how', 'are', 'you', 'doing', 'today']
    >>> report_progress(typed, prompt, 2, print_progress)
    ID: 2 Progress: 0.6
    0.6
    >>> report_progress(['how', 'aree'], prompt, 3, print_progress)
    ID: 3 Progress: 0.2
    0.2
    """
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    ratio = 0
    for x, y in zip(typed, prompt):
        if x == y:
            ratio += 1.0
        else:
            break

    ratio /= len(prompt)
    send({'id': user_id, 'progress': ratio})
    return ratio 
    # END PROBLEM 8
```

### Problem 9 (1 pt)

实现`time_per_word(times_per_player, words)`函数：

- `time_per_player`：每个用户的完成每个单词的时刻，数据类型是以列表为元素的列表
- `words`：单词列表

返回抽象数据类型`game`:

```python
def game(words, times):
    """A data abstraction containing all words typed and their times."""
    assert all([type(w) == str for w in words]), 'words should be a list of strings'
    assert all([type(t) == list for t in times]), 'times should be a list of lists'
    assert all([isinstance(i, (int, float)) for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]), 'There should be one word per time.'
    return [words, times]


def word_at(game, word_index):
    """A selector function that gets the word with index word_index"""
    assert 0 <= word_index < len(game[0]), "word_index out of range of words"
    return game[0][word_index]


def all_words(game):
    """A selector function for all the words in the game"""
    return game[0]


def all_times(game):
    """A selector function for all typing times for all players"""
    return game[1]


def time(game, player_num, word_index):
    """A selector function for the time it took player_num to type the word at word_index"""
    assert word_index < len(game[0]), "word_index out of range of words"
    assert player_num < len(game[1]), "player_num out of range of players"
    return game[1][player_num][word_index]


def game_string(game):
    """A helper function that takes in a game object and returns a string representation of it"""
    return "game(%s, %s)" % (game[0], game[1])
```

使用如下命令进行解锁测试：

```shell
python3 ok -q 09 -u --local
```

过程如下：

```shell
=====================================================================
Assignment: Project 2: Cats
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 9 > Suite 1 > Case 1
(cases remaining: 103)

>>> from cats import game, game_string, time_per_word, all_words, all_times, word_at, time
>>> p = [[1, 4, 6, 7], [0, 4, 6, 9]]
>>> words = ['This', 'is', 'fun']
>>> game = time_per_word(p, words)
>>> all_words(game)
? ['This', 'is', 'fun']
-- OK! --

>>> all_times(game)
? [[1, 4, 6, 7], [0, 4, 6, 9]]
-- Not quite. Try again! --

? [[1, 4, 6], [0, 4, 6]]
-- Not quite. Try again! --

? [[3, 2, 1], [4, 2, 3]]
-- OK! --

>>> p = [[0, 2, 3], [2, 4, 7]]
>>> game = time_per_word(p, ['hello', 'world'])
>>> word_at(game, word_index=1)
? 'world'
-- OK! --

>>> all_times(game)
? [[2, 1], [2, 3]]
-- OK! --

>>> time(game, player_num=0, word_index=1)
? 1
-- OK! --

---------------------------------------------------------------------
OK! All cases for Problem 9 unlocked.

Cannot backup when running ok with --local.
```

实现代码如下：

```python
def time_per_word(times_per_player, words):
    """Given timing data, return a game data abstraction, which contains a list
    of words and the amount of time each player took to type each word.

    Arguments:
        times_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.
        words: a list of words, in the order they are typed.

    >>> p = [[75, 81, 84, 90, 92], [19, 29, 35, 36, 38]]
    >>> game = time_per_word(p, ['collar', 'plush', 'blush', 'repute'])
    >>> all_words(game)
    ['collar', 'plush', 'blush', 'repute']
    >>> all_times(game)
    [[6, 3, 6, 2], [10, 6, 1, 2]]
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    times = []
    for i in range (0, len(times_per_player)):
        times.append([])
        for j in range(1, len(times_per_player[0])):
            times[i].append(times_per_player[i][j] - times_per_player[i][j - 1])

    return game(words, times)
    # END PROBLEM 9
```

### Problem 10 (2 pt)

实现`fastest_words(game)`函数：

- `game`：抽象数据类型`game`的实例对象

返回一个列表，列表的元素是每个玩家完成最快的单词列表。

使用如下命令进行解锁测试：

```shell
python3 ok -q 10 -u --local
```

过程如下：

```shell
=====================================================================
Assignment: Project 2: Cats
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 10 > Suite 1 > Case 1
(cases remaining: 103)

>>> from cats import game, fastest_words
>>> p0 = [2, 2, 3]
>>> p1 = [6, 1, 2]
>>> fastest_words(game(['What', 'great', 'luck'], [p0, p1]))
? [['What'], ['great', 'luck']]
-- OK! --

>>> p0 = [2, 2, 3]
>>> p1 = [6, 1, 3]
>>> fastest_words(game(['What', 'great', 'luck'], [p0, p1]))  # with a tie, choose the first player
? [['What', 'luck'], ['great']]
-- OK! --

>>> p2 = [4, 3, 1]
>>> fastest_words(game(['What', 'great', 'luck'], [p0, p1, p2]))
? [['What'], ['great'], ['luck']]
-- OK! --

---------------------------------------------------------------------
OK! All cases for Problem 10 unlocked.

Cannot backup when running ok with --local.
```

实现代码如下：

```python
def fastest_words(game):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        game: a game data abstraction as returned by time_per_word.

    >>> p0 = [5, 1, 3]
    >>> p1 = [4, 1, 6]
    >>> fastest_words(game(['Just', 'have', 'fun'], [p0, p1]))
    [['have', 'fun'], ['Just']]
    """
    player_indices = range(len(all_times(game)))  # contains an *index* for each player
    word_indices = range(len(all_words(game)))    # contains an *index* for each word
    # BEGIN PROBLEM 10
    "*** YOUR CODE HERE ***"
    word_fastest = [[] for i in player_indices]

    for i in word_indices:
        min_index = 0 # fastest player index
        for j in player_indices:
            if time(game, j, i) < time(game, min_index, i):
                min_index = j
        word_fastest[min_index].append(word_at(game, i))

    return word_fastest

    # END PROBLEM 10
```

## 最终测试

使用以下命令可以进行测试：

```shell
python3 ok --local
```

结果如下：

```sh
=====================================================================
Assignment: Project 2: Cats
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running tests

---------------------------------------------------------------------
Test summary
    1032 test cases passed! No cases failed.

Cannot backup when running ok with --local.
```

