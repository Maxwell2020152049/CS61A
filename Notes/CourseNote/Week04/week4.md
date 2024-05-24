## Week4

`CS 61A 2021 Fall`官网：[CS 61A: Structure and Interpretation of Computer Programs](https://inst.eecs.berkeley.edu/~cs61a/sp21/)

`翻译视频`：[【计算机程序的构造和解释】精译【UC Berkeley 公开课-CS61A (Spring 2021)】-中英双语字幕](https://www.bilibili.com/video/BV1v64y1Q78o/?spm_id_from=444.41.top_right_bar_window_default_collection.content.click&vd_source=249a8ad55bb26717dd55ec3dd295f644)

`github`:[Maxwell2020152049/CS61A](https://github.com/Maxwell2020152049/CS61A)

### Lecture #9: Still More on Functions

`Lab`：[Lab 3: Recursion, Tree Recursion](https://inst.eecs.berkeley.edu/~cs61a/sp21/lab/lab03/)

`Slide`：[09-Function_Examples_full.pdf](https://inst.eecs.berkeley.edu/~cs61a/sp21/assets/slides/09-Function_Examples_full.pdf)

#### 练习：翻转数字（`Exercise: Reversing Digits`）

实现一个`reverse digits(n)`函数，返回翻转的`n`：

```python
def reverse_digits(n):
    """Assuming N >= 0 is an integer.  Return the number whose
    base-10 representation is the reverse of that of N.
    >>> reverse_digits(0)
    0
    >>> reverse_digits(1)
    1
    >>> reverse_digits(123)
    321
    >>> reverse_digits(10)
    1
    >>> reverse_digits(12321)
    12321
    >>> reverse_digits(2222222)
    2222222
    >>> reverse_digits(102)
    201
    """
    assert type(n) is int and n >= 0
    if n < 10:
        return n
    return reverse_digits(n // 10) + (n % 10) * 10 ** (num_digits(n) - 1)

def num_digits(x):
    """Return the number of decimal digits in the positive integer X."""
    x_count = 1
    while x >= 10:
        x_count += 1
        x //= 10
    return x_count
```

#### 练习：交错数字（`Exercise: Interleaving Digits`）

实现一个`interleave(a, b)`函数，返回`a`、`b`交错的值：

```python
# Interleaving digits (spoiler alert!)

def interleave(a, b):
    """Assuming A and B are non-negative integers with the same 
    number of base-10 digits, return the number whose base-10 
    representation is the interleaving of A's and B's digits,
    starting with A.
    >>> interleave(1, 2)
    12
    >>> interleave(0, 1)
    1
    >>> interleave(1, 0)
    10
    >>> interleave(123,456)
    142536
    >>> interleave(111111, 222222)
    121212121212
    """
    if a <= 9:
        return a * 10 + b
    return interleave(a // 10, b // 10) * 100 + interleave(a % 10, b %10)
```

#### 环境图填空题（`Environment Detective`）

根据右侧的环境框架，给左边的程序代码填空：

![](./Resources/image1.png)

答案如下：

![](./Resources/image2.png)

[在PythonTutor中可以看到效果](https://pythontutor.com/cp/composingprograms.html#code=def%20flip%28flop%29%3A%0A%20%20%20%20if%20flop%20%3D%3D%203%3A%0A%20%20%20%20%20%20%20%20return%20None%0A%20%20%20%20flip%20%3D%20lambda%20flip%3A%203%0A%20%20%20%20return%20flip%0A%0Adef%20flop%28flip%29%3A%0A%20%20%20%20return%20flop%0A%0Aflip,%20flop%20%3D%20flop,%20flip%0A%0Aflip%28flop%281%29%282%29%29%283%29&cumulative=true&curInstr=19&mode=display&origin=composingprograms.js&py=3&rawInputLstJSON=%5B%5D)

### Lecture #10: Containers and Sequences

`Slide`：[10-Containers_full.pdf](https://inst.eecs.berkeley.edu/~cs61a/sp21/assets/slides/10-Containers_full.pdf)

#### Decorators

在`python`中，可以使用如下语法设置追踪函数，设置之后，每次调用`square`函数都会调用`trace1`函数：

```python
# Tracing

def trace1(f):
    """Return a function that takes a single argument, x, prints it,
    computes and prints F(x), and returns the computed value."""
    def traced(x):
        print("->", x)
        r = f(x)
        print("<-", r)
        return r
    return traced

@trace1
def square(x):
    return x * x

@trace1
def traced_reverse(n):
    assert type(n) is int and n >= 0
    if n < 10:
        return n
    return traced_reverse(n // 10) + (n % 10) * 10 ** (num_digits(n) - 1)
```

#### Pairs

在`python`中，如何使用已学知识实现一种含有两个元素的数据类型。

若两个元素都是非负数，可以使用如下方法实现：

```python
# Pairs of non-negative integers

def pair(a, b):
    """Return a value that represents the ordered pair of
    non-negative integer values (A, B)."""
    return 2**a * 3**b

def left(p):
    return multiplicity(2, p)

def right(p):
    return multiplicity(3, p)

def multiplicty(factor, n):
    """Assuming FACTOR and N are integers with FACTOR > 1, return
    the number of times N may be evenly divided by FACTOR."""
    r = 0
    while n % factor == 0:
        r += 1
        n //= factor
    return r
```

进一步泛化，可以使用如下方法实现能够修改的`pair`：

注意：在内部函数直接给`a`、`b`复制会创建新的变量，不会达到预期的效果，可以用`nolocal`修饰符从父环境中引入环境变量。

> - Assignment in Python usually creates or sets a `local variable` in the currently executing environment frame. 
>
> - But that’s useless in the attempted implementation (see the test bad pair function in 10.py). 
>
> - We need instead to indicate that we actually want to set the variables a and b introduced `outside` the pair func function in the enclosing (parent) function’s (pair’s) frame. 
>
> - The declaration
>
>   `nonlocal` var1, var2, . . . 
>
>   means “assignment to any of the variables vari in the current frame actually assigns to those variables in its parent’s frame, grandparent’s frame, etc. (not including the global frame).”
>
> - Furthermore, those variables must already exists in one of these ancestor frames.

```python
def pair(a, b):
    def pair_func(which, v=None):
        nonlocal a, b
        if which == 0:
            return a
        elif which == 1:
            return b
        elif which == 2:
            a = v
        else:
            b = v
    return pair_func

def test_good_pair():
    aPair = pair(3, 2)
    set_left(aPair, 5)
    print(left(aPair))
```

#### 序列（`Sequences`）

序列有以下属性（不同序列可能有不同属性）：

- 有限性（`finite`）
- 可修改性（`mutable`）
- 可索引性（`indexable`）
- 可迭代性（`iterable`）

> - The term `sequence` refers generally to a data structure consisting of an `indexed collection of values`, which we'll generally call elements. 
> - That is, there is a first, second, third value (which CS types call #0, #1, #2, etc.) 
> - A sequence may be `finite` (with a length) or `infinite`. 
> - It may be `mutable` (elements can change) or `immutable`. 
> - It may be `indexable`: its elements may be accessed via `selection` by their indices. 
> - It may be `iterable`: its values may be accessed `sequentially` from first to last.

在`python`中，有以下几种序列：

![](./Resources/image3.png)

#### 字符串字面量（`String Literals`）

以下代码说明了字符串字面量的特性：

```python
# String Literals

def string_literals():
    print('Single-quoted strings may contain "double-quoted strings"')
    print("Double-quoted strings may contain 'single-quoted strings'")
    print("""Triple double quotes allow 'this', "this", and ""this"",
as well as newline characters""")
    print('''Triple single quotes allow "this", 'this', and ''this'',
as well as newline characters''')
    print("A test of\nescapes\\.")
    print("Some unicode: \u0395\u1f55\u03c1\u03b7\u03ba\u03b1\u2764")
    print(r"In raw strings (starting with 'r'), \escapes are not replaced")
```

#### 选择和切片

列表可以通过索引得到元素，通过区间切片的到部分列表：

```python
# Collection of sequence expressions

def print_sequences():
    t = (2, 0, 9, 10, 11)   # Tuple
    L = [2, 0, 9, 10, 11]   # List
    R = range(2, 13)        # Integers 2-12.
    E = range(2, 13, 2)     # Even integers 2-12.
    S = "Hello, world!"     # Strings (sequences of characters)

    print(f"t[2] == {t[2]}; L[2] == {L[2]}; R[2] == {R[2]}; E[2] == {E[2]}")
    print(f"t[-1] == {t[-1]}' t[len(t)-1] == {t[len(t)-1]}")
    print(f"S[1] == {S[1]}")

    print(f"t[1:4] == {t[1:4]}")
    print(f"t[2:] == {t[2:]}; t[2:len(t)] == {t[2:len(t)]}")
    print(f"t[::2] == {t[::2]}; t[0:len(t):2] == {t[0:len(t):2]}; ",
          f"t[::-1] == {t[::-1]}")
    print(f"S[0:5] == {S[0:5]}; S[0:5:2] == {S[0:5:2]}; S[4::-1] == {S[4::-1]}")
    print(f"S[1:2] == {S[1:2]}; S[1] == {S[1]}")
```

用切片的特性很容易实现上节课的`reverse_digits`函数：

```python
def reverse_digits(n):
    """Assuming N >= 0 is an integer.  Return the number whose
    base-10 representation is the reverse of that of N.
    >>> reverse_digits(0)
    0
    >>> reverse_digits(1)
    1
    >>> reverse_digits(123)
    321
    >>> reverse_digits(10)
    1
    >>> reverse_digits(12321)
    12321
    >>> reverse_digits(2222222)
    2222222
    >>> reverse_digits(102)
    201
    """
    return int(str(n)[-1::-1])
```

#### 序列的结合与转化（`Sequence Combination and Conversion`）

使用`list()`、`tuple()`、`str()`函数，可以实现不同序列的转化。

#### 序列的循环迭代器（`Sequence Iteration: For Loops`）

可以使用如下形式，遍历列表中的元素

```python
for x in L:
    ···
```

#### 一个有意思的点

元组（`tuple`）是不可被修改的，列表（`list`）是可以被修改的，但是元组中的列表的元素可以被修改。原因是，元组中保存的是列表的引用，该引用不可以被修改，但引用的对象是列表，可以被修改。

`eg`：

```python
>>> T = (2020, [1, 5], 2049)
>>> T[1][0] = 3 
>>> T
(2020, [3, 5], 2049)
>>> T[1] = [3, 5]
Traceback (most recent call last):       
  File "<stdin>", line 1, in <module>    
TypeError: 'tuple' object does not support item assignment
```

### Lecture #11: Sequences (II) and Data Abstraction

`Lab`：[Lab 4: Midterm Review](https://inst.eecs.berkeley.edu/~cs61a/sp21/lab/lab04/)

`Slide`：[11-Data_Abstraction_full.pdf](https://inst.eecs.berkeley.edu/~cs61a/sp21/assets/slides/11-Data_Abstraction_full.pdf)

#### 多变量（`Multiple Variables`）

序列的循环迭代器可以支持多变量的迭代：

```python
>>> L = [ (1, 9), (2, 2), (5, 6), (3, 3) ]
>>> same = 0
>>> for x, y in L:
...    if x == y:
...        same += 1
>>> same
2
```

#### zip

`zip`函数可以将多个序列组合在一起：

注意，`zip`函数的返回值是`生成器`，可能需要类型转换函数进行转换。

```python
# Examples of zip() function and multiple assignment in a loop.
>>> list(zip([1, 2, 5, 3], [9, 2, 6, 3, 10]))
[(1, 9), (2, 2), (5, 6), (3, 3)]
>>> # Length of result is that of shortest sequence
>>> list(zip([1, 4, 7, 10], [2, 5, 8, 11], [3, 6, 9, 12, 15]))
[(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12)]
>>> beasts = ["aardvark", "axolotl", "gnu", "hartebeest"]
>>> for n, animal in zip(range(1, 5), beasts):
...     print(n, animal)
1 aardvark
2 axolotl
3 gnu
4 hartebeest
```

#### 列表的修改（`Modifying Lists`）

列表是可以修改的，可以通过其元素的引用修改其内容，也可以通过切片修改：

```python
# Various examples of mutating a list.
>>> L = [1, 2, 3, 4, 5]
>>> L[2] = 6
>>> L
[1, 2, 6, 4, 5]
>>> L[1:3] = [9, 8]
>>> L
[1, 9, 8, 4, 5]
>>> L[2:4] = []            # Deleting elements
>>> L
[1, 9, 5]
>>> L[1:1] = [2, 3, 4, 5]  # Inserting elements
>>> L
[1, 2, 3, 4, 5, 9, 5]
>>> L[len(L):] = [10, 11]  # Appending
>>> L
[1, 2, 3, 4, 5, 9, 5, 10, 11]
>>> L[0:0] = range(-3, 0)  # Prepending
>>> L
[-3, -2, -1, 1, 2, 3, 4, 5, 9, 5, 10, 11]
```

列表支持乘法运算符`*`：

```python
# Examples of the * operators on sequences.
>>> [0] * 3
[0, 0, 0]
>>> (1, 2) * 3
(1, 2, 1, 2, 1, 2)
>>> "a" * 5
'aaaaa'
>>> 5 * 'a'
'aaaaa'
```

#### 列表推导式（`List Comprehensions`）

在`python`中，使用以下形式的语句可以推导出一个列表，推导式中的变量都是局部的：

```python
[ <expression> for <var> in <sequence expression> if <boolean expression> ]
```

使用如下代码可以生成一个列表，包含[0, 100]中的素数的平方：

```python
[ x*x for x in range(101) if isprime(x) ]
```

可以在`for`语句中嵌套`for`语句：

```python
>>> [ (a, b) for a in range(10, 13) for b in range(2) ]
[(10, 0), (10, 1), (11, 0), (11, 1), (12, 0), (12, 1)]
```

`eg`：

```py
>>> [ (a, b) for a in range(0, 3) for b in range(a, 4) ]  
[(0, 0), (0, 1), (0, 2), (0, 3), (1, 1), (1, 2), (1, 3), (2, 2), (2, 3)]
```

`eg`：

如果一个变量不重要，可以使用`_`作为其变量名。

```python
>>> [ 0 for x in range(5)]  
[0, 0, 0, 0, 0]
>>> [ 0 for _ in range(5)] 
[0, 0, 0, 0, 0]
```

#### 练习1（`Exercise I`）

实现一个`match(a, b)`函数，返回`a`、`b`两个序列中相同索引的元素相等的个数：

```python
def matches(a, b):
    """Return the number of values k such that A[k] == B[k].
    >>> matches([1, 2, 3, 4, 5], [3, 2, 3, 0, 5])
    3
    >>> matches("abdomens", "indolence")
    4
    >>> matches("abcd", "dcba")
    0
    >>> matches("abcde", "edcba")
    1
    """
    cnt = 0
    for x, y in zip(a, b):
        if x == y:
            cnt += 1
    return cnt
```

等价的，更简洁的实现：

`sum`可以对列表求值，`True`和`False`支持加法运算符，结果是整数，`True`被视为`1`，`False`被视为`0`。

```python
return sum([ 1 for x, y in zip(a, b) if x == y ])
```

#### 练习2（`Exercise II`）

实现`triangle(n)`函数，输出形如`[[0], ..., [n]]`的内容：

```python
def triangle(n):
    """Assuming N >= 0, return the list consisting of N lists:
    [1], [1, 2], [1, 2, 3], ... [1, 2, ... N].
    >>> triangle(0)
    []
    >>> triangle(1)
    [[1]]
    >>> triangle(5)
    [[1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 5]]
    """
    return [ [ x for x in range(1, i + 1) ] for i in range(1, n + 1) ]
```

等价的，更简洁的实现：

```python
return [ list(range(1, i + 1)) for i in range(1, n + 1) ]
```

#### 数据抽象（`Data Abstraction`）

几个重要的概念：

- 抽象数据类型（`abstract data type (ADT)`）

- 应用程序员接口（`Application Programmer’s Interface (API)`）

抽象数据类型需要：

- 构造器（`Constructors`）
- 访问器（`Accessors`）
- 修改器（`Mutators`）

#### 有理数（`Rational Numbers`）

本节课介绍了如何实现有理数的`ADT`，详见`Slide`的`P13~P21`，抽象层次图如下：

![](./Resources/image4.png)

实现代码如下：

```python
# Rationals

from math import gcd

def make_rat(n, d):
    """The rational number N/D, assuming N, D are integers, D!=0"""
    g = gcd(n, d)
    n //= g; d //= g
    return (n, d)

def numer(r):
    """The numerator of rational number R in lowest terms."""
    return r[0]

def denom(r):
    """The denominator of rational number R in lowest terms.
       Always positive."""
    return r[1]

def add_rat(x, y):
    return make_rat(numer(x) * denom(y) + numer(y) * denom(x),
                    denom(x) * denom(y))

def mul_rat(x, y):
    return make_rat(numer(x) * numer(y), denom(x) * denom(y))

def str_rat(r):  # (For fun: a little new Python string magic)
    return str(numer(r)) if denom(r) == 1 else f"{numer(r)}/{denom(r)}" 

def equal_rat(x, y):
    return numer(x) * denom(y) == numer(y) * denom(x)


def exact_harmonic_number(n):
    """Return 1 + 1/2 + 1/3 + ... + 1/N as a rational number.
    >>> str_rat(exact_harmonic_number(1))
    '1'
    >>> str_rat(exact_harmonic_number(3))
    '11/6'
    >>> str_rat(exact_harmonic_number(10))
    '7381/2520'
    """
    s = make_rat(0, 1)
    for k in range(1, n + 1):
        s = add_rat(s, make_rat(1, k))
    return s
```

