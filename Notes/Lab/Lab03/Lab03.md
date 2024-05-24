# Lab 3: Recursion, Tree Recursion

实验链接：[Lab 3: Recursion, Tree Recursion](https://inst.eecs.berkeley.edu/~cs61a/sp21/lab/lab03/)

如何下载实验压缩包：

```shell
wget https://inst.eecs.berkeley.edu/~cs61a/sp21/lab/lab03/lab03.zip
```

## What Would Python Display?

### Q1: WWPD: Recursion

使用如下命令进行测试：

如果结果是函数，就输入`Function`，如果是错误就输入`Error`，如果没有输出就输入`Nothing`，如果出现无限循环或者无限递归，输出`Infinite`。

```shell
python3 ok -q recursion-wwpd -u --local
```

结果如下：

```shell
=====================================================================
Assignment: Lab 3
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Recursion > Suite 1 > Case 1
(cases remaining: 1)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> def f(a, b):
...     if a > b:
...         return f(a - 3, 2 * b)
...     elif a < b:
...         return f(b // 2, a)
...     else:
...         return b
>>> f(2, 2)
? 2
-- OK! --

>>> f(7, 4)
? 4
-- OK! --

>>> f(2, 28)
? 2
-- Not quite. Try again! --

? 8
-- OK! --

>>> f(-1, -3)
? Error
-- Not quite. Try again! --

? Infinite
-- OK! --

---------------------------------------------------------------------
OK! All cases for Recursion unlocked.

Cannot backup when running ok with --local.
```

### Q2: WWPD: Journey to the Center of the Earth

使用如下命令进行测试：

如果结果是函数，就输入`Function`，如果是错误就输入`Error`，如果没有输出就输入`Nothing`。

```shell
python3 ok -q sr-wwpd -u --local
```

结果如下：

```shell
=====================================================================
Assignment: Lab 3
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Self-Reference > Suite 1 > Case 1
(cases remaining: 1)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> def crust():
...   print("70km")
...   def mantle():
...       print("2900km")
...       def core():
...           print("5300km")
...           return mantle()
...       return core
...   return mantle
>>> drill = crust
>>> drill = drill()
? 70km
-- OK! --

>>> drill = drill()
? 2900km
-- OK! --

>>> drill = drill()
(line 1)? 5300km
(line 2)? 2900km
-- OK! --

>>> drill()
(line 1)? 5300km
(line 2)? 2900km
(line 3)? Function
-- OK! --

---------------------------------------------------------------------
OK! All cases for Self-Reference unlocked.

Cannot backup when running ok with --local.
```

## Coding Practice

### Q3: Summation

实现一个函数`summation(n, term)`，`n`是正整数，`term`是一个函数，接收一个参数并返回值，`summation`计算`term(1) + term(2) + ... + trem(n)`，并返回结果。

不允许使用循环语句。

实现代码如下：

```python
def summation(n, term):
    """Return the sum of numbers 1 through n (including n) wíth term applied to each number.
    Implement using recursion!

    >>> summation(5, lambda x: x * x * x) # 1^3 + 2^3 + 3^3 + 4^3 + 5^3
    225
    >>> summation(9, lambda x: x + 1) # 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
    54
    >>> summation(5, lambda x: 2**x) # 2^1 + 2^2 + 2^3 + 2^4 + 2^5
    62
    >>> # Do not use while/for loops!
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'summation',
    ...       ['While', 'For'])
    True
    """
    assert n >= 1
    "*** YOUR CODE HERE ***"
    if n == 1:
        return term(1)
    return term(n) + summation(n - 1, term)
```

### Q4: Pascal's Triangle

实现一个`pascal(row, column)`，求解`Pascal`三角第`row`行，第`column`列的值，其实就是杨辉三角。

注意：行、列都是从`0`开始索引的；越界的`Pascal`函数返回`0`。

实现代码如下：

```python
def pascal(row, column):
    """Returns the value of the item in Pascal's Triangle 
    whose position is specified by row and column.
    >>> pascal(0, 0)
    1
    >>> pascal(0, 5)	# Empty entry; outside of Pascal's Triangle
    0
    >>> pascal(3, 2)	# Row 3 (1 3 3 1), Column 2
    3
    >>> pascal(4, 2)     # Row 4 (1 4 6 4 1), Column 2
    6
    """
    "*** YOUR CODE HERE ***"
    if row < 0 or column < 0 or column > row:
        return 0
    if row == 0 and column == 0:
        return 1
    return pascal(row - 1, column - 1) + pascal(row - 1, column)
```

### Q5: Repeated, repeated

实现递归函数`repeated(f, n)`，返回`lambda x: f(f(f(...f(x)))`，调用`n`次`f`。

实现代码如下：

```python
def repeated(f, n):
    """Returns a function that takes in an integer and computes 
    the nth application of f on that integer.
    Implement using recursion!

    >>> add_three = repeated(lambda x: x + 1, 3)
    >>> add_three(5)
    8
    >>> square = lambda x: x ** 2
    >>> repeated(square, 2)(5) # square(square(5))
    625
    >>> repeated(square, 4)(5) # square(square(square(square(5))))
    152587890625
    >>> repeated(square, 0)(5)
    5
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'repeated',
    ...       ['For', 'While'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n == 0:
        return lambda x: x
    return compose1(f, repeated(f, n - 1))
```

使用如下代码进行测试：

```shell
python3 ok --local
```

结果如下：

```shell
=====================================================================
Assignment: Lab 3
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running tests

---------------------------------------------------------------------
Test summary
    5 test cases passed! No cases failed.

Cannot backup when running ok with --local.
```

