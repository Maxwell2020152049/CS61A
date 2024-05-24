# Lab 5: Python Lists, Data Abstraction, Trees

实验链接：[Lab 5: Python Lists, Data Abstraction, Trees](https://inst.eecs.berkeley.edu/~cs61a/sp21/lab/lab05/)

如何下载实验压缩包：

```shell
wget https://inst.eecs.berkeley.edu/~cs61a/sp21/lab/lab05/lab05.zip
```

## Required Questions

### List Comprehensions

#### Q1: Couple

实现函数`couple(s, t)`，`s`和`t`是两个长度相同的列表，返回一个列表，第`i`个元素是`[s[i], t[i]]`。

实现代码如下：

```python
def couple(s, t):
    """Return a list of two-element lists in which the i-th element is [s[i], t[i]].

    >>> a = [1, 2, 3]
    >>> b = [4, 5, 6]
    >>> couple(a, b)
    [[1, 4], [2, 5], [3, 6]]
    >>> c = ['c', 6]
    >>> d = ['s', '1']
    >>> couple(c, d)
    [['c', 's'], [6, '1']]
    """
    assert len(s) == len(t)
    "*** YOUR CODE HERE ***"
    return [[x, y] for x, y in zip(s, t)]
```

### Data Abstraction

本实验提供了一个`城市`的抽象数据类型（`ADT`），用法如下：

```python
>>> berkeley = make_city('Berkeley', 122, 37)
>>> get_name(berkeley)
'Berkeley'
>>> get_lat(berkeley)
122
>>> new_york = make_city('New York City', 74, 40)
>>> get_lon(new_york)
40
```

实现方式如下（理论上，用户不该知道这些信息）：

```python
# Treat all the following code as being behind an abstraction layer, you shouldn't need to look at it!

def make_city(name, lat, lon):
    """
    >>> city = make_city('Berkeley', 0, 1)
    >>> get_name(city)
    'Berkeley'
    >>> get_lat(city)
    0
    >>> get_lon(city)
    1
    """
    if change_abstraction.changed:
        return {"name": name, "lat": lat, "lon": lon}
    else:
        return [name, lat, lon]


def get_name(city):
    """
    >>> city = make_city('Berkeley', 0, 1)
    >>> get_name(city)
    'Berkeley'
    """
    if change_abstraction.changed:
        return city["name"]
    else:
        return city[0]


def get_lat(city):
    """
    >>> city = make_city('Berkeley', 0, 1)
    >>> get_lat(city)
    0
    """
    if change_abstraction.changed:
        return city["lat"]
    else:
        return city[1]


def get_lon(city):
    """
    >>> city = make_city('Berkeley', 0, 1)
    >>> get_lon(city)
    1
    """
    if change_abstraction.changed:
        return city["lon"]
    else:
        return city[2]
```

#### Q2: Distance

实现`distance(city_a, city_b)`函数，`city_a`和`city_b`是两个城市对象，返回它们之间的距离，用`(latitude， longitude)`表示坐标，距离为[欧几里得距离](https://zh.wikipedia.org/zh-hans/%E6%AC%A7%E5%87%A0%E9%87%8C%E5%BE%97%E8%B7%9D%E7%A6%BB)。

实现代码如下：

```python
def distance(city_a, city_b):
    """
    >>> city_a = make_city('city_a', 0, 1)
    >>> city_b = make_city('city_b', 0, 2)
    >>> distance(city_a, city_b)
    1.0
    >>> city_c = make_city('city_c', 6.5, 12)
    >>> city_d = make_city('city_d', 2.5, 15)
    >>> distance(city_c, city_d)
    5.0
    """
    "*** YOUR CODE HERE ***"
    x1 = get_lat(city_a)
    y1 = get_lon(city_a)
    x2 = get_lat(city_b)
    y2 = get_lon(city_b)

    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
```

#### Q3: Closer city

实现`closer_city(lat, lon, city_a, city_b)`函数：

- `lat`、`lon`：目标城市的纬度、经度
- `city_a`、`city_b`：两个城市对象

返回两个城市中距离`(lat, lon)`较近的一个，若一样近，返回`city_b`。

实现代码如下：

```python
def closer_city(lat, lon, city_a, city_b):
    """
    Returns the name of either city_a or city_b, whichever is closest to
    coordinate (lat, lon). If the two cities are the same distance away
    from the coordinate, consider city_b to be the closer city.

    >>> berkeley = make_city('Berkeley', 37.87, 112.26)
    >>> stanford = make_city('Stanford', 34.05, 118.25)
    >>> closer_city(38.33, 121.44, berkeley, stanford)
    'Stanford'
    >>> bucharest = make_city('Bucharest', 44.43, 26.10)
    >>> vienna = make_city('Vienna', 48.20, 16.37)
    >>> closer_city(41.29, 174.78, bucharest, vienna)
    'Bucharest'
    """
    "*** YOUR CODE HERE ***"
    city_c = make_city("Target", lat, lon)
    return get_name(city_a)\
        if distance(city_a, city_c) < distance(city_b, city_c)\
            else get_name(city_b)
```

#### Q4: Don't violate the abstraction barrier!

没有代码的实现，本题是让你检查在之前两题的实现中，是否违反了抽象的隔离，没有使用`ADT`的构造器和选择器，而是之间访问其数据，直接用列表构造`城市`，这些行为会导致无法通过本题测试。

### Trees

本实验的`树`的`ADT`如下：

```python
# Tree ADT

def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    if change_abstraction.changed:
        for branch in branches:
            assert is_tree(branch), 'branches must be trees'
        return {'label': label, 'branches': list(branches)}
    else:
        for branch in branches:
            assert is_tree(branch), 'branches must be trees'
        return [label] + list(branches)


def label(tree):
    """Return the label value of a tree."""
    if change_abstraction.changed:
        return tree['label']
    else:
        return tree[0]


def branches(tree):
    """Return the list of branches of the given tree."""
    if change_abstraction.changed:
        return tree['branches']
    else:
        return tree[1:]


def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if change_abstraction.changed:
        if type(tree) != dict or len(tree) != 2:
            return False
        for branch in branches(tree):
            if not is_tree(branch):
                return False
        return True
    else:
        if type(tree) != list or len(tree) < 1:
            return False
        for branch in branches(tree):
            if not is_tree(branch):
                return False
        return True


def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)
```

#### 	Q5: Finding Berries!

实现一个`berry_finder(t)`，`t`是一棵树，如果树中某个节点包含`'berry'`，返回`True`，否则返回`False`。

实现代码如下：

```python
def berry_finder(t):
    """Returns True if t contains a node with the value 'berry' and 
    False otherwise.

    >>> scrat = tree('berry')
    >>> berry_finder(scrat)
    True
    >>> sproul = tree('roots', [tree('branch1', [tree('leaf'), tree('berry')]), tree('branch2')])
    >>> berry_finder(sproul)
    True
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> berry_finder(numbers)
    False
    >>> t = tree(1, [tree('berry',[tree('not berry')])])
    >>> berry_finder(t)
    True
    """
    "*** YOUR CODE HERE ***"
    if is_leaf(t):
        return label(t) == 'berry'
    
    if label(t) == 'berry':
        return True

    child = branches(t)

    for b in child:
        if berry_finder(b):
            return True
    
    return False
```

#### Q6: Sprout leaves

实现`sprout_leaves(t, leaves)`函数：

- `t`：一棵树
- `leaves`：值的列表

返回一棵新的树，是在`t`的叶子上加上`leaves`得到的。

`eg`：

有这样一棵树`t = tree(1, [tree(2), tree(3, [tree(4)])])`：

```python
  1
 / \
2   3
    |
    4
```

调用`sprout_leaves(t, [5, 6])`之后：

```python
       1
     /   \
    2     3
   / \    |
  5   6   4
         / \
        5   6
```

实现代码如下：

```python
def sprout_leaves(t, leaves):
    """Sprout new leaves containing the data in leaves at each leaf in
    the original tree t and return the resulting tree.

    >>> t1 = tree(1, [tree(2), tree(3)])
    >>> print_tree(t1)
    1
      2
      3
    >>> new1 = sprout_leaves(t1, [4, 5])
    >>> print_tree(new1)
    1
      2
        4
        5
      3
        4
        5

    >>> t2 = tree(1, [tree(2, [tree(3)])])
    >>> print_tree(t2)
    1
      2
        3
    >>> new2 = sprout_leaves(t2, [6, 1, 2])
    >>> print_tree(new2)
    1
      2
        3
          6
          1
          2
    """
    "*** YOUR CODE HERE ***"
    if is_leaf(t):
        return tree(label(t), [tree(leave) for leave in leaves])
    
    child = branches(t)

    return tree(label(t), [sprout_leaves(b, leaves) for b in child])
```

#### Q7: Don't violate the abstraction barrier!

和`Q4`一样，不再多加赘述。

使用如下命令测试上述题目：

```shell
python3 ok --local
```

结果如下：

```shell
=====================================================================
Assignment: Lab 5
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running tests

---------------------------------------------------------------------
Test summary
    7 test cases passed! No cases failed.
```

## Optional Questions

### Q8: Coordinates

实现`coords(fn, seq, lower, upper)`函数：

- `fn`：计算函数
- `seq`：自变量的序列
- `lower`、`upper`：因变量`fn(x)`的最小值和最大值

实现代码如下：

```python
def coords(fn, seq, lower, upper):
    """
    >>> seq = [-4, -2, 0, 1, 3]
    >>> fn = lambda x: x**2
    >>> coords(fn, seq, 1, 9)
    [[-2, 4], [1, 1], [3, 9]]
    """
    "*** YOUR CODE HERE ***"
    return [[x, fn(x)] for x in seq if lower <= fn(x) <= upper]
```

### Q9: Riffle Shuffle

实现`riffle(deck)`函数：

- `deck`：值的序列

返回一个列表，值是序列的第一个元素，中间一个元素，循环往复。

实现代码如下：

```python
def riffle(deck):
    """Produces a single, perfect riffle shuffle of DECK, consisting of
    DECK[0], DECK[M], DECK[1], DECK[M+1], ... where M is position of the
    second half of the deck.  Assume that len(DECK) is even.
    >>> riffle([3, 4, 5, 6])
    [3, 5, 4, 6]
    >>> riffle(range(20))
    [0, 10, 1, 11, 2, 12, 3, 13, 4, 14, 5, 15, 6, 16, 7, 17, 8, 18, 9, 19]
    """
    "*** YOUR CODE HERE ***"

    deck = list(deck)
    return deck if len(deck) == 2 else\
        [deck[0], deck[len(deck) // 2]] +\
            riffle(deck[1 : len(deck) // 2] + deck[len(deck) // 2 + 1 : ])
```

### Q10: Add trees

实现`add_trees(t1, t2)`函数，返回两棵树相加的结果树，如果有的节点只有一棵树有，就创建新的节点。

实现代码如下：

```python
def add_trees(t1, t2):
    """
    >>> numbers = tree(1,
    ...                [tree(2,
    ...                      [tree(3),
    ...                       tree(4)]),
    ...                 tree(5,
    ...                      [tree(6,
    ...                            [tree(7)]),
    ...                       tree(8)])])
    >>> print_tree(add_trees(numbers, numbers))
    2
      4
        6
        8
      10
        12
          14
        16
    >>> print_tree(add_trees(tree(2), tree(3, [tree(4), tree(5)])))
    5
      4
      5
    >>> print_tree(add_trees(tree(2, [tree(3)]), tree(2, [tree(3), tree(4)])))
    4
      6
      4
    >>> print_tree(add_trees(tree(2, [tree(3, [tree(4), tree(5)])]), \
    tree(2, [tree(3, [tree(4)]), tree(5)])))
    4
      6
        8
        5
      5
    """
    "*** YOUR CODE HERE ***"
    if not t1:
        return t2
    if not t2:
        return t1

    child1 = branches(t1)
    child2 = branches(t2)
    
    return tree(label(t1) + label(t2),\
            [ add_trees(child1[i] if i < len(child1) else [],\
                child2[i] if i < len(child2) else []) \
                    for i in range(max(len(child1), len(child2)))])
```

### Fun Question!

### Shakespeare and Dictionaries

> We will use dictionaries to approximate the entire works of Shakespeare! We're going to use a bigram language model. Here's the idea: We start with some word -- we'll use "The" as an example. Then we look through all of the texts of Shakespeare and for every instance of "The" we record the word that follows "The" and add it to a list, known as the *successors* of "The". Now suppose we've done this for every word Shakespeare has used, ever.
>
> Let's go back to "The". Now, we randomly choose a word from this list, say "cat". Then we look up the successors of "cat" and randomly choose a word from that list, and we continue this process. This eventually will terminate in a period (".") and we will have generated a Shakespearean sentence!
>
> The object that we'll be looking things up in is called a "successor table", although really it's just a dictionary. The keys in this dictionary are words, and the values are lists of successors to those words.

#### Q11: Successor Tables

实现`build_successors_table(tokens)`函数，返回`tokens`中的单词的后续字典。

实现代码如下：

```python
def build_successors_table(tokens):
    """Return a dictionary: keys are words; values are lists of successors.

    >>> text = ['We', 'came', 'to', 'investigate', ',', 'catch', 'bad', 'guys', 'and', 'to', 'eat', 'pie', '.']
    >>> table = build_successors_table(text)
    >>> sorted(table)
    [',', '.', 'We', 'and', 'bad', 'came', 'catch', 'eat', 'guys', 'investigate', 'pie', 'to']
    >>> table['to']
    ['investigate', 'eat']
    >>> table['pie']
    ['.']
    >>> table['.']
    ['We']
    """
    table = {}
    prev = '.'
    for word in tokens:
        if prev not in table:
            "*** YOUR CODE HERE ***"
            table[prev] = [word]
        else:
            table[prev] += [word]
        "*** YOUR CODE HERE ***"
        prev = word
    return table
```

#### Q12: Construct the Sentence

实现`construct_sent(word, table)`，根据`table`字典，返回一个以`word`开头的句子。

实现代码如下：

```python
def construct_sent(word, table):
    """Prints a random sentence starting with word, sampling from
    table.

    >>> table = {'Wow': ['!'], 'Sentences': ['are'], 'are': ['cool'], 'cool': ['.']}
    >>> construct_sent('Wow', table)
    'Wow!'
    >>> construct_sent('Sentences', table)
    'Sentences are cool.'
    """
    import random
    result = ''
    while word not in ['.', '!', '?']:
        "*** YOUR CODE HERE ***"
        result += word + ' '
        word = random.choice(table[word])
    return result.strip() + word
```

#### Putting it all together

给予`Q11`和`Q12`更多真实的数据，我跑的时候一直报`urllib.error.HTTPError: HTTP Error 502: Bad Gateway`，就不做了。
