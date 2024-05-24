# Lab 6: Nonlocal, Mutability, Iterators and Generators

实验链接：[Lab 6: Nonlocal, Mutability, Iterators and Generators](https://inst.eecs.berkeley.edu/~cs61a/sp21/lab/lab06/#nonlocal-wwpd)

如何下载实验压缩包：

```shell
wget https://inst.eecs.berkeley.edu/~cs61a/sp21/lab/lab06/lab06.zip
```

## Nonlocal WWPD

### Q1: WWPD: Nonlocal Quiz

使用以下命令进行解锁测试：

```shell
python3 ok -q nonlocal_quiz -u --local
```

过程如下：

```shell
=====================================================================
Assignment: Lab 6
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
nonlocal_quiz > Suite 1 > Case 1
(cases remaining: 4)

Q: What is the value returned by the function call ba(3)?
>>> def ba(by):
...     def yo(da):
...         by += 2
...         return by
...     return yo(2)
...
>>> ba(3)
Choose the number of the correct choice:
0) This code will error
1) 2
2) 5
3) 3
? 0
-- OK! --

---------------------------------------------------------------------
nonlocal_quiz > Suite 1 > Case 2
(cases remaining: 3)

Q: What is the value returned by the function call ba(3)?
>>> def ba(by):
...     def yo(da):
...         nonlocal by
...         by += 2
...         return by
...     return yo(3)
...
>>> ba(3)
Choose the number of the correct choice:
0) This code will error
1) 2
2) 3
3) 5
? 3
-- OK! --

---------------------------------------------------------------------
nonlocal_quiz > Suite 1 > Case 3
(cases remaining: 2)

Q: What is the value returned by the function call ba([1, 2, 3])?
>>> def ba(by):
...     def yo(da):
...         by.append(da)
...         return by
...     return yo(5)
...
>>> ba([1, 2, 3])
Choose the number of the correct choice:
0) None
1) This code will error
2) [1, 2, 3, 5]
3) [1, 2, 3]
? 2
-- OK! --

---------------------------------------------------------------------
nonlocal_quiz > Suite 1 > Case 4
(cases remaining: 1)

Q: What is the value returned by the function call ba(5)?
>>> def ba(by):
...     def yo(da):
...         yoda = by + da
...         return yoda
...     return yo(5)
...
>>> ba(5)
Choose the number of the correct choice:
0) 15
1) 5
2) This code will error
3) 10
? 3
-- OK! --

---------------------------------------------------------------------
OK! All cases for nonlocal_quiz unlocked.

Cannot backup when running ok with --local.
```

## Mutability

### Q2: List-Mutation

使用以下命令进行解锁测试：

> Note: if nothing would be output by Python, type `Nothing`. If the code would error, type `Error`.

```shell
python3 ok -q list-mutation -u --local
```

过程如下：

```shell
=====================================================================
Assignment: Lab 6
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
List Mutation > Suite 1 > Case 1
(cases remaining: 1)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> # If nothing would be output by Python, type Nothing
>>> # If the code would error, type Error
>>> lst = [5, 6, 7, 8]
>>> lst.append(6)
? [5, 6, 7, 8, 6]
-- Not quite. Try again! --

? Nothing
-- OK! --

>>> lst
? [5, 6, 7, 8, 6]
-- OK! --

>>> lst.insert(0, 9)
>>> lst
? [9, 5, 6, 7, 8, 6]
-- OK! --

>>> x = lst.pop(2)
>>> lst
? [9, 5, 7, 8, 6]
-- OK! --

>>> lst.remove(x)
>>> lst
? [9, 5, 7, 8]
-- OK! --

>>> a, b = lst, lst[:]
>>> a is lst
? False
-- Not quite. Try again! --

? True
-- OK! --

>>> b == lst
? True
-- OK! --

>>> b is lst
? False
-- OK! --

---------------------------------------------------------------------
OK! All cases for List Mutation unlocked.

Cannot backup when running ok with --local.
```

### Q3: Insert Items

实现代码如下：

```python
def insert_items(lst, entry, elem):
    """Inserts elem into lst after each occurence of entry and then returns lst.
    
    >>> test_lst = [1, 5, 8, 5, 2, 3]
    >>> new_lst = insert_items(test_lst, 5, 7)
    >>> new_lst
    [1, 5, 7, 8, 5, 7, 2, 3]
    >>> large_lst = [1, 4, 8]
    >>> large_lst2 = insert_items(large_lst, 4, 4)
    >>> large_lst2
    [1, 4, 4, 8]
    >>> large_lst3 = insert_items(large_lst2, 4, 6)
    >>> large_lst3
    [1, 4, 6, 4, 6, 8]
    >>> large_lst3 is large_lst
    True
    """
    "*** YOUR CODE HERE ***"
    tmp = 0
    while True:
        try:
            idx = lst.index(entry, tmp)
        except:
            break

        lst.insert(idx + 1, elem)
        tmp = idx + 2

    return lst
```

## Iterators and Generators

### Q4: Scale

实现代码如下：

```python
def scale(it, multiplier):
    """Yield elements of the iterable it multiplied by a number multiplier.

    >>> m = scale([1, 5, 2], 5)
    >>> type(m)
    <class 'generator'>
    >>> list(m)
    [5, 25, 10]

    >>> m = scale(naturals(), 2)
    >>> [next(m) for _ in range(5)]
    [2, 4, 6, 8, 10]
    """
    "*** YOUR CODE HERE ***"
    for i in it:
        yield i * multiplier
```

### Q5: Hailstone

实现代码如下：

```python
def hailstone(n):
    """Yields the elements of the hailstone sequence starting at n.
    
    >>> for num in hailstone(10):
    ...     print(num)
    ...
    10
    5
    16
    8
    4
    2
    1
    """
    "*** YOUR CODE HERE ***"
    while n != 1:
        yield n
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
    yield n
```

递归解法：

```python
    if n == 1:
        yield 1
    else:
        yield n
        if n % 2 == 0:
            yield from hailstone(n // 2)
        else:
            yield from hailstone(n * 3 + 1)
```

