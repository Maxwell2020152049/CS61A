[TOC]

# Lab 8: Midterm Review

实验链接：[Lab 8: Midterm Review](https://inst.eecs.berkeley.edu/~cs61a/sp21/lab/lab08/)

如何下载实验压缩包：

```shell
wget https://inst.eecs.berkeley.edu/~cs61a/sp21/lab/lab08/lab08.zip
```

## Q1: All Questions Are Optional

> The questions in this assignment are not graded, but they are highly recommended to help you prepare for the upcoming midterm. You will receive credit for this lab even if you do not complete these questions.
>
> This question has no Ok tests.

## Recursion and Tree Recursion

### Q2: `Subsequences`

使用如下命令进行测试：

```shell
python3 ok -q subseqs --local
```

结果如下：

```shell
=====================================================================
Assignment: Lab 8
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running tests

---------------------------------------------------------------------
Test summary
    1 test cases passed! No cases failed.

Cannot backup when running ok with --local.
```

实现如下：

```py
def insert_into_all(item, nested_list: list[list]):
    """Return a new list consisting of all the lists in nested_list,
    but with item added to the front of each. You can assuming that
     nested_list is a list of lists.

    >>> nl = [[], [1, 2], [3]]
    >>> insert_into_all(0, nl)
    [[0], [0, 1, 2], [0, 3]]
    """
    "*** YOUR CODE HERE ***"
    new_list: list[list] = []
    for x in nested_list:
        new_list.append([item] + x)

    return new_list


def subseqs(s: list):
    """Return a nested list (a list of lists) of all subsequences of S.
    The subsequences can appear in any order. You can assume S is a list.

    >>> seqs = subseqs([1, 2, 3])
    >>> sorted(seqs)
    [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
    >>> subseqs([])
    [[]]
    """
    if len(s) == 0:
        return [[]]
    else:
        lst = subseqs(s[1:])
        return lst + insert_into_all(s[0], lst)
```

### Q3: Non-Decreasing Subsequences

使用如下命令进行测试：

```shell
python3 ok -q non_decrease_subseqs --local
```

结果如下：

```shell
=====================================================================
Assignment: Lab 8
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running tests

---------------------------------------------------------------------
Test summary
    1 test cases passed! No cases failed.

Cannot backup when running ok with --local.
```

实现如下：

```py
def non_decrease_subseqs(s):
    """Assuming that S is a list, return a nested list of all subsequences
    of S (a list of lists) for which the elements of the subsequence
    are strictly nondecreasing. The subsequences can appear in any order.

    >>> seqs = non_decrease_subseqs([1, 3, 2])
    >>> sorted(seqs)
    [[], [1], [1, 2], [1, 3], [2], [3]]
    >>> non_decrease_subseqs([])
    [[]]
    >>> seqs2 = non_decrease_subseqs([1, 1, 2])
    >>> sorted(seqs2)
    [[], [1], [1], [1, 1], [1, 1, 2], [1, 2], [1, 2], [2]]
    """
    def subseq_helper(s: list, prev: int):
        if not s:
            return [[]]
        elif s[0] < prev:
            # s[0]不能选
            return subseq_helper(s[1:], prev)
        else:
            a = subseq_helper(s[1:], s[0])      # 选s[0]
            b = subseq_helper(s[1:], prev)      # 不选s[0]
            return insert_into_all(s[0], a) + b
    return subseq_helper(s, -100)
```

### Q4: Number of Trees

数学题，参考：[Catalan number](https://en.wikipedia.org/wiki/Catalan_number)

使用如下命令进行测试：

```shell
python3 ok -q subseqs --local
```

结果如下：

```shell
=====================================================================
Assignment: Lab 8
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running tests

---------------------------------------------------------------------
Test summary
    1 test cases passed! No cases failed.

Cannot backup when running ok with --local.
```

实现如下：

```py
def combination(n: int, m: int):
    """
    计算组合数 C(n, m)的值

    参数:
    n(int): 组合数上标
    m(int): 组合数下标
    """
    ans: int = 1
    for i in range(m):
        ans *= n - i

    for i in range(m):
        ans //= i + 1

    return ans


def catalan(n: int):
    """
    计算卡特兰数

    参数：
    n(int): 第n个卡特兰数
    """
    return combination(2 * n, n) - combination(2 * n, n + 1)


def num_trees(n):
    """Returns the number of unique full binary trees with exactly n leaves. E.g.,

    1   2        3       3    ...
    *   *        *       *
       / \      / \     / \
      *   *    *   *   *   *
              / \         / \
             *   *       *   *

    >>> num_trees(1)
    1
    >>> num_trees(2)
    1
    >>> num_trees(3)
    2
    >>> num_trees(8)
    429

    """
    "*** YOUR CODE HERE ***"
    return catalan(n - 1)
```

## Generators

### Q5: Merge

合并两个迭代器，返回一个生成器，注意递归写法很容易有坑(生成器和迭代器混在一起写)。

和[HW05-Q7: Generate Preorder](https://inst.eecs.berkeley.edu/~cs61a/sp21/hw/hw05/#q7)很像，但生成前序遍历是非破坏性操作，本题是破坏性操作。

使用如下命令进行测试：

```python
python3 ok -q merge --local
```

结果如下：

```shell
=====================================================================
Assignment: Lab 8
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running tests

---------------------------------------------------------------------
Test summary
    1 test cases passed! No cases failed.

Cannot backup when running ok with --local.
```


实现如下：

```python
def merge(incr_a, incr_b):
    """Yield the elements of strictly increasing iterables incr_a and incr_b, removing
    repeats. Assume that incr_a and incr_b have no repeats. incr_a or incr_b may or may not
    be infinite sequences.

    >>> m = merge([0, 2, 4, 6, 8, 10, 12, 14], [0, 3, 6, 9, 12, 15])
    >>> type(m)
    <class 'generator'>
    >>> list(m)
    [0, 2, 3, 4, 6, 8, 9, 10, 12, 14, 15]
    >>> def big(n):
    ...    k = 0
    ...    while True: yield k; k += n
    >>> m = merge(big(2), big(3))
    >>> [next(m) for _ in range(11)]
    [0, 2, 3, 4, 6, 8, 9, 10, 12, 14, 15]
    """
    iter_a, iter_b = iter(incr_a), iter(incr_b)
    next_a, next_b = next(iter_a, None), next(iter_b, None)
    "*** YOUR CODE HERE ***"
    while next_a is not None and next_b is not None:
        if next_a == next_b:
            yield next_a
            next_a = next(iter_a, None)
            next_b = next(iter_b, None)
        elif next_a < next_b:
            yield next_a
            next_a = next(iter_a, None)
        else:
            yield next_b
            next_b = next(iter_b, None)

    if next_a is None:
        yield next_b
        yield from iter_b
    else:
        yield next_a
        yield from iter_a  
```

## Objects

### Q6: Keyboard

使用如下命令进行测试：

```shell
python3 ok -q Keyboard --local
```

结果如下：

```shell
=====================================================================
Assignment: Lab 8
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running tests

---------------------------------------------------------------------
Test summary
    1 test cases passed! No cases failed.

Cannot backup when running ok with --local.
```

实现如下：

```python
class Keyboard:
    """A Keyboard takes in an arbitrary amount of buttons, and has a
    dictionary of positions as keys, and values as Buttons.

    >>> b1 = Button(0, "H")
    >>> b2 = Button(1, "I")
    >>> k = Keyboard(b1, b2)
    >>> k.buttons[0].key
    'H'
    >>> k.press(1)
    'I'
    >>> k.press(2) #No button at this position
    ''
    >>> k.typing([0, 1])
    'HI'
    >>> k.typing([1, 0])
    'IH'
    >>> b1.times_pressed
    2
    >>> b2.times_pressed
    3
    """

    def __init__(self, *args):
        self.buttons: dict[int, Button] = {}
        for b in args:
            self.buttons[b.pos] = b

    def press(self, info: int) -> str:
        """Takes in a position of the button pressed, and
        returns that button's output"""
        if info in self.buttons.keys():
            button: Button = self.buttons[info]
            button.times_pressed += 1
            return button.key
        return ""

    def typing(self, typing_input) -> str:
        """Takes in a list of positions of buttons pressed, and
        returns the total output"""
        ans: str = ""
        for info in typing_input:
            ans += self.press(info)
        return ans
```

### Q7: Bank Account

使用如下命令进行测试：

```shell
python3 ok -q Account --local
```

结果如下：

```shell
=====================================================================
Assignment: Lab 8
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running tests

---------------------------------------------------------------------
Test summary
    1 test cases passed! No cases failed.

Cannot backup when running ok with --local.
```

实现如下：

```python
class Account:
    """A bank account that allows deposits and withdrawals.
    It tracks the current account balance and a transaction
    history of deposits and withdrawals.

    >>> eric_account = Account('Eric')
    >>> eric_account.deposit(1000000)   # depositing paycheck for the week
    1000000
    >>> eric_account.transactions
    [('deposit', 1000000)]
    >>> eric_account.withdraw(100)      # make a withdrawal to buy dinner
    999900
    >>> eric_account.transactions
    [('deposit', 1000000), ('withdraw', 100)]
    >>> print(eric_account) #call to __str__
    Eric's Balance: $999900
    >>> eric_account.deposit(10)
    999910
    >>> eric_account #call to __repr__
    Accountholder: Eric, Deposits: 2, Withdraws: 1
    """

    interest = 0.02

    def __init__(self, account_holder: str):
        self.balance = 0
        self.holder = account_holder
        "*** YOUR CODE HERE ***"
        self.transactions: list[tuple[str, int]] = []

    def deposit(self, amount: int):
        """Increase the account balance by amount, add the deposit
        to the transaction history, and return the new balance.
        """
        "*** YOUR CODE HERE ***"
        self.balance += amount
        self.transactions.append(('deposit', amount))
        return self.balance

    def withdraw(self, amount: int):
        """Decrease the account balance by amount, add the withdraw
        to the transaction history, and return the new balance.
        """
        "*** YOUR CODE HERE ***"
        if self.balance < amount:
            pass
        self.balance -= amount
        self.transactions.append(('withdraw', amount))
        return self.balance

    def __str__(self):
        "*** YOUR CODE HERE ***"
        return f"{self.holder}'s Balance: ${self.balance}"

    def __repr__(self):
        "*** YOUR CODE HERE ***"
        deposit_num = sum([1 for x in self.transactions if x[0] == "deposit"])
        withdraw_num = len(self.transactions) - deposit_num
        return f"Accountholder: {self.holder}, Deposits: {deposit_num}, Withdraws: {withdraw_num}"
```

## Mutable Lists

### Q8: Trade

使用如下命令进行测试：

```shell
python3 ok -q trade --local
```

结果如下：

```shell
=====================================================================
Assignment: Lab 8
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running tests

---------------------------------------------------------------------
Test summary
    1 test cases passed! No cases failed.

Cannot backup when running ok with --local.
```

实现如下：

```python
def trade(first, second):
    """Exchange the smallest prefixes of first and second that have equal sum.

    >>> a = [1, 1, 3, 2, 1, 1, 4]
    >>> b = [4, 3, 2, 7]
    >>> trade(a, b) # Trades 1+1+3+2=7 for 4+3=7
    'Deal!'
    >>> a
    [4, 3, 1, 1, 4]
    >>> b
    [1, 1, 3, 2, 2, 7]
    >>> c = [3, 3, 2, 4, 1]
    >>> trade(b, c)
    'No deal!'
    >>> b
    [1, 1, 3, 2, 2, 7]
    >>> c
    [3, 3, 2, 4, 1]
    >>> trade(a, c)
    'Deal!'
    >>> a
    [3, 3, 2, 1, 4]
    >>> b
    [1, 1, 3, 2, 2, 7]
    >>> c
    [4, 3, 1, 4, 1]
    """
    m, n = 1, 1

    equal_prefix = lambda: sum(first[: m]) == sum(second[: n])
    while m < len(first) and n < len(second) and not equal_prefix():
        if sum(first[: m]) < sum(second[: n]):
            m += 1
        else:
            n += 1

    if equal_prefix():
        first[:m], second[:n] = second[:n], first[:m]
        return 'Deal!'
    else:
        return 'No deal!'
```

### Q9: Shuffle

使用如下命令进行测试：

```shell
python3 ok -q shuffle --local
```

结果如下：

```shell
=====================================================================
Assignment: Lab 8
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running tests

---------------------------------------------------------------------
Test summary
    1 test cases passed! No cases failed.

Cannot backup when running ok with --local.
```

实现如下：

```python
def shuffle(cards: list):
    """Return a shuffled list that interleaves the two halves of cards.

    >>> shuffle(range(6))
    [0, 3, 1, 4, 2, 5]
    >>> suits = ['♡', '♢', '♤', '♧']
    >>> cards = [card(n) + suit for n in range(1,14) for suit in suits]
    >>> cards[:12]
    ['A♡', 'A♢', 'A♤', 'A♧', '2♡', '2♢', '2♤', '2♧', '3♡', '3♢', '3♤', '3♧']
    >>> cards[26:30]
    ['7♤', '7♧', '8♡', '8♢']
    >>> shuffle(cards)[:12]
    ['A♡', '7♤', 'A♢', '7♧', 'A♤', '8♡', 'A♧', '8♢', '2♡', '8♤', '2♢', '8♧']
    >>> shuffle(shuffle(cards))[:12]
    ['A♡', '4♢', '7♤', '10♧', 'A♢', '4♤', '7♧', 'J♡', 'A♤', '4♧', '8♡', 'J♢']
    >>> cards[:12]  # Should not be changed
    ['A♡', 'A♢', 'A♤', 'A♧', '2♡', '2♢', '2♤', '2♧', '3♡', '3♢', '3♤', '3♧']
    """
    assert len(cards) % 2 == 0, 'len(cards) must be even'
    half = len(cards) // 2
    shuffled = []
    for i in range(half):
        shuffled.append(cards[i])
        shuffled.append(cards[i + half])
    return shuffled
```

## Linked Lists

### Q10: Insert

使用如下命令进行测试：

```shell
 python3 ok -q insert --local
```

结果如下：

```shell
 =====================================================================
Assignment: Lab 8
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running tests

---------------------------------------------------------------------
Test summary
    1 test cases passed! No cases failed.

Cannot backup when running ok with --local.
```

实现如下：

```python
 def insert(link: 'Link', value, index: int):
    """Insert a value into a Link at the given index.

    >>> link = Link(1, Link(2, Link(3)))
    >>> print(link)
    <1 2 3>
    >>> other_link = link
    >>> insert(link, 9001, 0)
    >>> print(link)
    <9001 1 2 3>
    >>> link is other_link # Make sure you are using mutation! Don't create a new linked list.
    True
    >>> insert(link, 100, 2)
    >>> print(link)
    <9001 1 100 2 3>
    >>> insert(link, 4, 5)
    Traceback (most recent call last):
        ...
    IndexError: Out of bounds!
    """
    "*** YOUR CODE HERE ***"
    lnk: 'Link' = link
    for i in range(index):
        lnk = lnk.rest
        if lnk is Link.empty:
            raise IndexError('Out of bounds!')
    lnk.rest = Link(lnk.first, lnk.rest)
    lnk.first = value
```

### Q11: Deep Linked List Length

使用如下命令进行测试：

```shell
 python3 ok -q deep_len --local
```

结果如下：

```shell
 =====================================================================
Assignment: Lab 8
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running tests

---------------------------------------------------------------------
Test summary
    1 test cases passed! No cases failed.

Cannot backup when running ok with --local.
```

实现如下：

```python
 def deep_len(lnk: 'Link'):
    """ Returns the deep length of a possibly deep linked list.

    >>> deep_len(Link(1, Link(2, Link(3))))
    3
    >>> deep_len(Link(Link(1, Link(2)), Link(3, Link(4))))
    4
    >>> levels = Link(Link(Link(1, Link(2)), \
            Link(3)), Link(Link(4), Link(5)))
    >>> print(levels)
    <<<1 2> 3> <4> 5>
    >>> deep_len(levels)
    5
    """
    if lnk is Link.empty:
        return 0
    elif not isinstance(lnk.first, Link):
        return 1 + deep_len(lnk.rest)
    else:
        return deep_len(lnk.first) + deep_len(lnk.rest)
```

### Q12: Linked Lists as Strings

使用如下命令进行测试：

```shell
python3 ok -q make_to_string --local 
```

结果如下：

```shell
 =====================================================================
Assignment: Lab 8
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running tests

---------------------------------------------------------------------
Test summary
    1 test cases passed! No cases failed.

Cannot backup when running ok with --local.
```

实现如下：

```python
 def make_to_string(front: str, mid: str, back: str, empty_repr: str):
    """ Returns a function that turns linked lists to strings.

    >>> kevins_to_string = make_to_string("[", "|-]-->", "", "[]")
    >>> jerrys_to_string = make_to_string("(", " . ", ")", "()")
    >>> lst = Link(1, Link(2, Link(3, Link(4))))
    >>> kevins_to_string(lst)
    '[1|-]-->[2|-]-->[3|-]-->[4|-]-->[]'
    >>> kevins_to_string(Link.empty)
    '[]'
    >>> jerrys_to_string(lst)
    '(1 . (2 . (3 . (4 . ()))))'
    >>> jerrys_to_string(Link.empty)
    '()'
    """
    def printer(lnk: Link):
        if lnk is Link.empty:
            return empty_repr
        else:
            return front + str(lnk.first) + mid + printer(lnk.rest) + back
    return printer
```

## Trees

### Q13: Prune Small

使用如下命令进行测试：

```shell
python3 ok -q prune_small --local 
```

结果如下：

```shell
 =====================================================================
Assignment: Lab 8
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running tests

---------------------------------------------------------------------
Test summary
    1 test cases passed! No cases failed.

Cannot backup when running ok with --local.
```

实现如下：

```python
 def prune_small(t: 'Tree', n: int):
    """Prune the tree mutatively, keeping only the n branches
    of each node with the smallest label.

    >>> t1 = Tree(6)
    >>> prune_small(t1, 2)
    >>> t1
    Tree(6)
    >>> t2 = Tree(6, [Tree(3), Tree(4)])
    >>> prune_small(t2, 1)
    >>> t2
    Tree(6, [Tree(3)])
    >>> t3 = Tree(6, [Tree(1), Tree(3, [Tree(1), Tree(2), Tree(3)]), Tree(5, [Tree(3), Tree(4)])])
    >>> prune_small(t3, 2)
    >>> t3
    Tree(6, [Tree(1), Tree(3, [Tree(1), Tree(2)])])
    """
    while len(t.branches) > n:
        largest = max(t.branches, key=lambda x: x.label)
        t.branches.remove(largest)
    for cld in t.branches:
        prune_small(cld, n)
```

### Q14: Long Paths

注意：filter函数返回一个迭代器，需要用list函数转换为列表。

> 在 Python 中，`filter()` 函数用于过滤序列（例如，列表、元组等）中的元素，根据指定的条件筛选出符合条件的元素，并返回一个新的迭代器或可迭代对象。`filter()` 函数的基本语法如下：
>
> ```python
> filter(function, iterable)
> ```
>
> 其中，`function` 是一个用于筛选的函数，`iterable` 是一个可迭代对象，表示待筛选的序列。
>
> 下面是一个示例，演示如何使用 `filter()` 函数：
>
> ```python
> # 定义一个函数，用于筛选偶数
> def is_even(num):
>     return num % 2 == 0
> 
> # 创建一个列表
> numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
> 
> # 使用 filter() 函数筛选偶数
> even_numbers = list(filter(is_even, numbers))
> 
> # 输出结果
> print(even_numbers)  # [2, 4, 6, 8, 10]
> ```
>
> 在上述示例中，我们首先定义了一个函数 `is_even()`，用于判断一个数字是否为偶数。然后，我们创建了一个包含整数的列表 `numbers`。通过调用 `filter(is_even, numbers)`，我们使用 `is_even()` 函数过滤出所有的偶数，并得到一个新的迭代器。最后，通过 `list()` 函数将迭代器转换为列表，并将结果赋值给变量 `even_numbers`。最后，我们打印 `even_numbers`，输出筛选出的偶数列表。
>
> 需要注意的是，`filter()` 函数返回的是一个迭代器（在 Python 3 中），因此如果需要保存结果，可以将其转换为列表或其他类型的序列。

使用如下命令进行测试：

```shell
 python3 ok -q long_paths --local
```

结果如下：

```shell
 =====================================================================
Assignment: Lab 8
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running tests

---------------------------------------------------------------------
Test summary
    1 test cases passed! No cases failed.

Cannot backup when running ok with --local.
```

实现如下：

```python
 def long_paths(t: 'Tree', n) -> list[list]:
    """Return a list of all paths in t with length at least n.

    >>> long_paths(Tree(1), 0)
    [[1]]
    >>> long_paths(Tree(1), 1)
    []
    >>> t = Tree(3, [Tree(4), Tree(4), Tree(5)])
    >>> left = Tree(1, [Tree(2), t])
    >>> mid = Tree(6, [Tree(7, [Tree(8)]), Tree(9)])
    >>> right = Tree(11, [Tree(12, [Tree(13, [Tree(14)])])])
    >>> whole = Tree(0, [left, Tree(13), mid, right])
    >>> print(whole)
    0
      1
        2
        3
          4
          4
          5
      13
      6
        7
          8
        9
      11
        12
          13
            14
    >>> for path in long_paths(whole, 2):
    ...     print(path)
    ...
    [0, 1, 2]
    [0, 1, 3, 4]
    [0, 1, 3, 4]
    [0, 1, 3, 5]
    [0, 6, 7, 8]
    [0, 6, 9]
    [0, 11, 12, 13, 14]
    >>> for path in long_paths(whole, 3):
    ...     print(path)
    ...
    [0, 1, 3, 4]
    [0, 1, 3, 4]
    [0, 1, 3, 5]
    [0, 6, 7, 8]
    [0, 11, 12, 13, 14]
    >>> long_paths(whole, 4)
    [[0, 11, 12, 13, 14]]
    """
    "*** YOUR CODE HERE ***"
    def all_paths(t: 'Tree'):
        if t.is_leaf():
            return [[t.label]]
        paths = []
        for cld in t.branches:
            paths.extend(all_paths(cld))
        return insert_into_all(t.label, paths)

    return  list(filter(lambda x: len(x) > n, all_paths(t)))
```

## Complexity

### Q15: Determining Complexity

使用如下命令进行测试：

```shell
 python3 ok -q wwpd-complexity -u --local
```

过程如下：

```shell
  =====================================================================
Assignment: Lab 8
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Orders of Growth > Suite 1 > Case 1
(cases remaining: 2)

Q: What is the order of growth of `is_prime` in terms of `n`?

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
Choose the number of the correct choice:
0) Exponential - Θ(2^n)
1) Linear - Θ(n)
2) Logarithmic - Θ(log(n))
3) Quadratic - Θ(n^2)
? 1
-- OK! --

---------------------------------------------------------------------
Orders of Growth > Suite 1 > Case 2
(cases remaining: 1)

Q: What is the order of growth of `bar` in terms of `n`?

def bar(n):
    i, sum = 1, 0
    while i <= n:
        sum += biz(n)
        i += 1
    return sum

def biz(n):
    i, sum = 1, 0
    while i <= n:
        sum += i**3
        i += 1
    return sum
Choose the number of the correct choice:
0) Exponential - Θ(2^n)
1) Linear - Θ(n)
2) Quadratic - Θ(n^2)
3) Logarithmic - Θ(log(n))
? 2
-- OK! --

---------------------------------------------------------------------
OK! All cases for Orders of Growth unlocked.

Cannot backup when running ok with --local.
```
