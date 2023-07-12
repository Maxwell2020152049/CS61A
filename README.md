# CS61A

## 关于`.gitignore`

```
**/*.zip
**/__pycache__
```

`git`不需要维护 **`压缩包`** 和 **`缓存文件`**

## Lab 0: Getting Started

实验链接：[Lab 0: Getting Started](https://inst.eecs.berkeley.edu/~cs61a/sp21/lab/lab00/)

关于实验测评：[Using Ok](https://inst.eecs.berkeley.edu/~cs61a/sp21/articles/using-ok/)

### 实验环境配置

`CS 61A`的实验需要：

- `Terminal（终端）`
- `Python3`

- `Text Editor（代码编辑器）`

### 命令行工具的使用

实验会可能用到的命令：

- `ls`
- `cd`
- `mkdir`
- `unzip`
- `mv`

### Python Basic

#### Primitive Expressions（原始表达式）

**`原始表达式`** 只进行一步计算：

```python
>>> 3
3
>>> 12.5
12.5
>>> True
True
```

#### Arithmetic Expressions（算术表达式）

算术表达式由以下运算符组成：

- 加法：`+`
- 减法：`-`
- 乘法：`*`
- 乘方：`**`
- 浮点数除法：`/`
- 下取整除法：`//`
- 取余：`%`

```python
>>> 7 / 4
1.75
>>> (2 + 6) / 4	  # Floating point division
2.0
>>> 7 // 4        # Floor division (rounding down)
1
>>> 7 % 4         # Modulus (remainder of 7 // 4)
3
```

#### Assignment statements（赋值语句）

```python
>>> a = (100 + 50) // 2
```

```python
>>> a
75
```

### Doing the assignment（实验任务）

#### Unlocking tests（解锁测试）

完成正式实验前要进行一次测试，检测学生对`python`的基础知识的掌握程度，使用如下命令（`--local`参数使得测评在本地运行）：

```shell
python3 ok -q python-basics -u --local
```

测试过程如下：

```shell
=====================================================================
Assignment: Lab 0
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Python Basics > Suite 1 > Case 1
(cases remaining: 2)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> 10 + 2
? 12
-- OK! --

>>> 7 / 2
? 3.5
-- OK! --

>>> 7 // 2
? 3
-- OK! --

>>> 7 % 2                       # 7 modulo 2, the remainder when dividing 7 by 2.
? 1
-- OK! --

---------------------------------------------------------------------
Python Basics > Suite 2 > Case 1
(cases remaining: 1)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> x = 20
>>> x + 2
? 22
-- OK! --

>>> x
? 20
-- OK! --

>>> y = 5
>>> y = y + 3
>>> y * 2
? 16
-- OK! --

>>> y = y // 4
>>> y + x
? 22
-- OK! --

---------------------------------------------------------------------
OK! All cases for Python Basics unlocked.

Cannot backup when running ok with --local.
```

#### Understanding problems（了解问题）

> In `twenty_twenty_one`,
>
> - The docstring tells you to "come up with the most creative expression that evaluates to 2021," but that you can only use numbers and arithmetic operators `+` (add), `*` (multiply), and `-` (subtract).
> - The `doctest` checks that the function call `twenty_twenty_one()` should return the number 2021.

代码如下：

```python
def twenty_twenty_one():
    """Come up with the most creative expression that evaluates to 2021,
    using only numbers and the +, *, and - operators.

    >>> twenty_twenty_one()
    2021
    """
    return 20 * 100 + 21
```

#### Running tests（运行测试）

使用如下命令测评代码：

```shell
python3 ok --local
```

测评结果如下：

```shell
=====================================================================
Assignment: Lab 0
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running tests

---------------------------------------------------------------------
Test summary
    3 test cases passed! No cases failed.

Cannot backup when running ok with --local.
```

### Appendix: Useful Python command line options（有用的Python命令行选项）

> - **`-i`**: The `-i` option runs your Python script, then opens an interactive session. In an interactive session, you run Python code line by line and get immediate feedback instead of running an entire file all at once. To exit, type `exit()` into the interpreter prompt. You can also use the keyboard shortcut `Ctrl-D` on Linux/Mac machines or `Ctrl-Z Enter` on Windows.
>
>   If you edit the Python file while running it interactively, you will need to exit and restart the interpreter in order for those changes to take effect.
>
>   ```
>   python3 -i 
>   ```



> - **`-m doctest`**: Runs doctests in a particular file. Doctests are surrounded by triple quotes (`"""`) within functions.
>
>   Each test in the file consists of `>>>` followed by some Python code and the expected output (though the `>>>` are not seen in the output of the doctest command).
>
>   ```python
>    python3 -m doctest 
>   ```

<hr>

## Homework 1: Variables & Functions, Control

作业链接：[Homework 1: Variables & Functions, Control](https://inst.eecs.berkeley.edu/~cs61a/sp21/hw/hw01/)

### Q1: Syllabus Quiz

教学大纲和课程政策，详见[Syllabus Quiz](https://docs.google.com/forms/d/e/1FAIpQLSfCH090Wp9dmmstwizj5MEXDDmb9J55G8L8Wjqczmwz1NLW_w/viewform)和[Syllabus & Course Policies](https://inst.eecs.berkeley.edu/~cs61a/sp21/articles/about/)。

### Q2: A Plus Abs B

> Fill in the blanks in the following function for adding `a` to the absolute value of `b`, without calling `abs`. You may **not** modify any of the provided code other than the two blanks.

题意就是实现如下函数`f`：
$$
f(a, b) = a + \lvert b \rvert
$$

实现代码如下：

```python
def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    >>> # a check that you didn't change the return statement!
    >>> import inspect, re
    >>> re.findall(r'^\s*(return .*)', inspect.getsource(a_plus_abs_b), re.M)
    ['return f(a, b)']
    """
    if b < 0:
        f = lambda x, y : x - y
    else:
        f = lambda x, y : x + y
    return f(a, b)
```

另一种实现（使用`lambda`表达式）：

```python
def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    >>> # a check that you didn't change the return statement!
    >>> import inspect, re
    >>> re.findall(r'^\s*(return .*)', inspect.getsource(a_plus_abs_b), re.M)
    ['return f(a, b)']
    """
    
    if b < 0:
        f = sub
    else:
        f = add
    return f(a, b)
```

### Q3: Two of Three

> Write a function that takes three *positive* numbers as arguments and returns the sum of the squares of the two smallest numbers. **Use only a single line for the body of the function.**

> **Hint:** Consider using the `max` or `min` function:
>
> ```python
> >>> max(1, 2, 3)
> 3
> >>> min(-1, -2, -3)
> -3
> ```
>



思路：最小的数可以用`min()`函数得到，次小的数可以用`x`、`y`、`z`三个数的和减掉最小值和最大值（`max()`）。

实现代码如下：

```python
def two_of_three(x, y, z):
    """Return a*a + b*b, where a and b are the two smallest members of the
    positive numbers x, y, and z.

    >>> two_of_three(1, 2, 3)
    5
    >>> two_of_three(5, 3, 1)
    10
    >>> two_of_three(10, 2, 8)
    68
    >>> two_of_three(5, 5, 5)
    50
    >>> # check that your code consists of nothing but an expression (this docstring)
    >>> # a return statement
    >>> import inspect, ast
    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(two_of_three)).body[0].body]
    ['Expr', 'Return']
    """
    return min(x, y, z) ** 2 + (x + y + z - min(x, y, z) - max(x, y, z)) ** 2
```

### Q4: Largest Factor

> Write a function that takes an integer `n` that is **greater than 1** and returns the largest integer that is smaller than `n` and evenly divides `n`.
>
> **Hint:** To check if `b` evenly divides `a`, you can use the expression `a % b == 0`, which can be read as, "the remainder of dividing `a` by `b` is 0."

思路：找一个数`n`的最大因子，用循环把`1~n-1`都检查一遍就行了。

实现代码：

```python
def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    "*** YOUR CODE HERE ***"
    ans = 1
    for i in range(1, n):
        if n % i == 0:
            ans = i

    return ans
```

### Q5: If Function vs Statement

> Let's try to write a function that does the same thing as an `if` statement.

```python
def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 'equal', 'not equal')
    'not equal'
    >>> if_function(3>2, 'bigger', 'smaller')
    'bigger'
    """
    if condition:
        return true_result
    else:
        return false_result
```

> Despite the doctests above, this function actually does *not* do the same thing as an `if` statement in all cases. To prove this fact, write functions `cond`, `true_func`, and `false_func` such that `with_if_statement` prints `61A`, but `with_if_function` prints both `Welcome to` and `61A` on separate lines.

```python
def with_if_statement():
    """
    >>> result = with_if_statement()
    61A
    >>> print(result)
    None
    """
    if cond():
        return true_func()
    else:
        return false_func()

def with_if_function():
    """
    >>> result = with_if_function()
    Welcome to
    61A
    >>> print(result)
    None
    """
    return if_function(cond(), true_func(), false_func())

def cond():
    "*** YOUR CODE HERE ***"

def true_func():
    "*** YOUR CODE HERE ***"

def false_func():
    "*** YOUR CODE HERE ***"
```

思路：这个题主要是考查对`if`语句的理解和对函数传递参数的理解，观察`with_if_statement()`和`with_if_function()`两个函数，不难发现，要实现的三个函数有以下特点：

- cond()：返回`True`或者`False`。
- `true_func()`和`false_func()`：调用输出函数，没有返回值，一个输出`"Welcome to"`，一个输出`"61A"`。

综合下来，实现代码如下：

```python
def cond():
    "*** YOUR CODE HERE ***"
    return False


def true_func():
    "*** YOUR CODE HERE ***"
    print("Welcome to")


def false_func():
    "*** YOUR CODE HERE ***"
    print("61A")
```

### Q6: Hailstone

> Douglas Hofstadter's Pulitzer-prize-winning book, *Gödel, Escher, Bach*, poses the following mathematical puzzle.
>
> 1. Pick a positive integer `n` as the start.
> 2. If `n` is even, divide it by 2.
> 3. If `n` is odd, multiply it by 3 and add 1.
> 4. Continue this process until `n` is 1.
>
> The number `n` will travel up and down but eventually end at 1 (at least for all numbers that have ever been tried -- nobody has ever proved that the sequence will terminate). Analogously, a hailstone travels up and down in the atmosphere before eventually landing on earth.
>
> This sequence of values of `n` is often called a Hailstone sequence. Write a function that takes a single argument with formal parameter name `n`, prints out the hailstone sequence starting at `n`, and returns the number of steps in the sequence:

思路：经典的`3*n+1`问题，注意最开始的`n`就算作一步。

实现代码如下：

```python
def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"
    step = 1
    print(n)
    while True:
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
        print(n)
        step += 1
        if n == 1:
            break
        
    return step
```

### 测评结果

运行测评代码：

```shell
python ok --local
```

测评结果如下：

```shell
=====================================================================
Assignment: Homework 1
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running tests

---------------------------------------------------------------------
Test summary
    6 test cases passed! No cases failed.

Cannot backup when running ok with --local.
```

<hr>

## Lab 1: Variables & Functions, Control

实验链接：[Lab 1: Variables & Functions, Control](https://inst.eecs.berkeley.edu/~cs61a/sp21/lab/lab01/)

如何下载实验压缩包：

```shell
wget https://inst.eecs.berkeley.edu/~cs61a/sp21/lab/lab01/lab01.zip
```

### What Would Python Display(WWPD)? (Part 1)

#### Q1: WWPD: Control

使用如下命令进行测试：

```shell
python3 ok -q control -u --local
```

需要注意：

- 若用整型或浮点型做控制语句的判断条件，`0`会被当作`False`，`非0`会被当作`True`

测试过程如下：

```shell
=====================================================================
Assignment: Lab 1
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Control > Suite 1 > Case 1
(cases remaining: 5)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> def xk(c, d):
...     if c == 4:
...         return 6
...     elif d >= 4:
...         return 6 + 7 + c
...     else:
...         return 25
>>> xk(10, 10)
? 23
-- OK! --

>>> xk(10, 6)
? 19
-- Not quite. Try again! --

? 23
-- OK! --

>>> xk(4, 6)
? 6
-- OK! --

>>> xk(0, 0)
? 25
-- OK! --

---------------------------------------------------------------------
Control > Suite 1 > Case 2
(cases remaining: 4)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> def how_big(x):
...     if x > 10:
...         print('huge')
...     elif x > 5:
...         return 'big'
...     elif x > 0:
...         print('small')
...     else:
...         print("nothin")
>>> how_big(7)
? big
-- Not quite. Try again! --

? 'big'
-- OK! --

>>> how_big(12)
? 'huge'
-- Not quite. Try again! --

? huge
-- OK! --

>>> how_big(1)
? small
-- OK! --

>>> how_big(-1)
? nothin
-- OK! --

---------------------------------------------------------------------
Control > Suite 2 > Case 1
(cases remaining: 3)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> n = 3
>>> while n >= 0:  # If this loops forever, just type Infinite Loop
...     n -= 1
...     print(n)
(line 1)? 2
(line 2)? 1
(line 3)? 0
(line 4)? -1
-- OK! --

---------------------------------------------------------------------
Control > Suite 2 > Case 2
(cases remaining: 2)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> positive = 28
>>> while positive: # If this loops forever, just type Infinite Loop
...    print("positive?")
...    positive -= 3
? positive
-- Not quite. Try again! --

? positive?
-- Not quite. Try again! --

? Infinite Loop
-- OK! --

---------------------------------------------------------------------
Control > Suite 2 > Case 3
(cases remaining: 1)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> positive = -9
>>> negative = -12
>>> while negative: # If this loops forever, just type Infinite Loop
...    if positive:
...        print(negative)
...    positive += 3
...    negative += 3
(line 1)? Infinite Loop
-- Not quite. Try again! --

(line 1)? -12
(line 2)? -9
(line 3)? -6
-- OK! --

---------------------------------------------------------------------
OK! All cases for Control unlocked.
```

#### Q2: WWPD: Veritasiness

使用如下命令进行测试：

```shell
python3 ok -q short-circuit -u --local
```

需要注意：

- `and`和`or`运算符有`短路性`

测试过程如下：

```shell
=====================================================================
Assignment: Lab 1
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Veritasiness > Suite 1 > Case 1
(cases remaining: 3)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> True and 13
? 13
-- OK! --

>>> False or 0
? 0
-- OK! --

>>> not 10
? False
-- OK! --

>>> not None
? True
-- OK! --

---------------------------------------------------------------------
Veritasiness > Suite 1 > Case 2
(cases remaining: 2)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> True and 1 / 0 and False  # If this errors, just type Error.
? Error
-- OK! --

>>> True or 1 / 0 or False  # If this errors, just type Error.
? True
-- OK! --

>>> True and 0  # If this errors, just type Error.
? 0
-- OK! --

>>> False or 1  # If this errors, just type Error.
? 1
-- OK! --

>>> 1 and 3 and 6 and 10 and 15  # If this errors, just type Error.
? 15
-- OK! --

>>> -1 and 1 > 0 # If this errors, just type Error.
? True
-- OK! --

>>> 0 or False or 2 or 1 / 0  # If this errors, just type Error.
? 2
-- OK! --

---------------------------------------------------------------------
Veritasiness > Suite 2 > Case 1
(cases remaining: 1)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> not 0
? True
-- OK! --

>>> (1 + 1) and 1  # If this errors, just type Error. If this is blank, just type Nothing.
? 1
-- OK! --

>>> 1/0 or True  # If this errors, just type Error. If this is blank, just type Nothing.
? Error
-- OK! --

>>> (True or False) and False  # If this errors, just type Error. If this is blank, just type Nothing.
? False
-- OK! --

---------------------------------------------------------------------
OK! All cases for Veritasiness unlocked.

Cannot backup when running ok with --local.
```

#### Q3: Debugging Quiz!

报错信息汇总与调试方法：[Debugging](https://inst.eecs.berkeley.edu/~cs61a/sp21/articles/debugging/)

使用如下命令进行测试：

```shell
python3 ok -q debugging-quiz -u --local
```

需要注意：

- `Traceback`中，越后打印的函数就是越晚调用的
- 在输出的内容前加上`"DEBUG: "`，`ok`测评器会忽略改行输出
- 在程序运行出错时，中止程序，抛出异常，好过打印错误信息

测试过程如下：

```shell
=====================================================================
Assignment: Lab 1
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
debugging-quiz > Suite 1 > Case 1
(cases remaining: 12)

Q: In the following traceback, what is the most recent function call?
Traceback (most recent call last):
    File "temp.py", line 10, in <module>
      f("hi")
    File "temp.py", line 2, in f
      return g(x + x, x)
    File "temp.py", line 5, in g
      return h(x + y * 5)
    File "temp.py", line 8, in h
      return x + 0
  TypeError: must be str, not int
Choose the number of the correct choice:
0) g(x + x, x)
1) h(x + y * 5)
2) f("hi")
? 1
-- OK! --

---------------------------------------------------------------------
debugging-quiz > Suite 1 > Case 2
(cases remaining: 11)

Q: In the following traceback, what is the cause of this error?
Traceback (most recent call last):
    File "temp.py", line 10, in <module>
      f("hi")
    File "temp.py", line 2, in f
      return g(x + x, x)
    File "temp.py", line 5, in g
      return h(x + y * 5)
    File "temp.py", line 8, in h
      return x + 0
  TypeError: must be str, not int
Choose the number of the correct choice:
0) the code looped infinitely
1) there was a missing return statement
2) the code attempted to add a string to an integer
? 2
-- OK! --

---------------------------------------------------------------------
debugging-quiz > Suite 1 > Case 3
(cases remaining: 10)

Q: How do you write a doctest asserting that square(2) == 4?
Choose the number of the correct choice:
0) def square(x):
       '''
       square(2)
       4
       '''
       return x * x
1) def square(x):
       '''
       input: 2
       output: 4
       '''
       return x * x
2) def square(x):
       '''
       >>> square(2)
       4
       '''
       return x * x
3) def square(x):
       '''
       doctest: (2, 4)
       '''
       return x * x
? 2
-- OK! --

---------------------------------------------------------------------
debugging-quiz > Suite 1 > Case 4
(cases remaining: 9)

Q: When should you use print statements?
Choose the number of the correct choice:
0) To investigate the values of variables at certain points in your code
1) For permanant debugging so you can have long term confidence in your code
2) To ensure that certain conditions are true at certain points in your code
? 0
-- OK! --

---------------------------------------------------------------------
debugging-quiz > Suite 1 > Case 5
(cases remaining: 8)

Q: How do you prevent the ok autograder from interpreting print statements as output?
Choose the number of the correct choice:
0) You don't need to do anything, ok only looks at returned values, not printed values
1) Print with # at the front of the outputted line
2) Print with 'DEBUG:' at the front of the outputted line
? 0
-- Not quite. Try again! --

Choose the number of the correct choice:
0) You don't need to do anything, ok only looks at returned values, not printed values
1) Print with # at the front of the outputted line
2) Print with 'DEBUG:' at the front of the outputted line
? 1
-- Not quite. Try again! --

Choose the number of the correct choice:
0) You don't need to do anything, ok only looks at returned values, not printed values
1) Print with # at the front of the outputted line
2) Print with 'DEBUG:' at the front of the outputted line
? 2
-- OK! --

---------------------------------------------------------------------
debugging-quiz > Suite 1 > Case 6
(cases remaining: 7)

Q: What is the best way to open an interactive terminal to investigate a failing test for question sum_digits in assignment lab01?
Choose the number of the correct choice:
0) python3 ok -q sum_digits --trace
1) python3 -i lab01.py
2) python3 ok -q sum_digits -i
3) python3 ok -q sum_digits
? 1
-- Not quite. Try again! --

Choose the number of the correct choice:
0) python3 ok -q sum_digits --trace
1) python3 -i lab01.py
2) python3 ok -q sum_digits -i
3) python3 ok -q sum_digits
? 2
-- OK! --

---------------------------------------------------------------------
debugging-quiz > Suite 1 > Case 7
(cases remaining: 6)

Q: What is the best way to look at an environment diagram to investigate a failing test for question sum_digits in assignment lab01?
Choose the number of the correct choice:
0) python3 ok -q sum_digits
1) python3 ok -q sum_digits --trace
2) python3 ok -q sum_digits -i
3) python3 -i lab01.py
? 1
-- OK! --

---------------------------------------------------------------------
debugging-quiz > Suite 1 > Case 8
(cases remaining: 5)

Q: Which of the following is NOT true?
Choose the number of the correct choice:
0) It is generally bad practice to release code with debugging print statements left in
1) Debugging is not a substitute for testing
2) It is generally good practice to release code with assertion statements left in
3) Code that returns a wrong answer instead of crashing is generally better as it at least works fine
4) Testing is very important to ensure robust code
? 0
-- Not quite. Try again! --

Choose the number of the correct choice:
0) It is generally bad practice to release code with debugging print statements left in
1) Debugging is not a substitute for testing
2) It is generally good practice to release code with assertion statements left in
3) Code that returns a wrong answer instead of crashing is generally better as it at least works fine
4) Testing is very important to ensure robust code
? 3
-- OK! --

---------------------------------------------------------------------
debugging-quiz > Suite 1 > Case 9
(cases remaining: 4)

Q: You get a SyntaxError. What is most likely to have happened?
Choose the number of the correct choice:
0) You typed a variable name incorrectly
1) You forgot a return statement
2) Your indentation mixed tabs and spaces
3) You had an unmatched parenthesis
? 3
-- OK! --

---------------------------------------------------------------------
debugging-quiz > Suite 1 > Case 10
(cases remaining: 3)

Q: You get a IndentationError. What is most likely to have happened?
Choose the number of the correct choice:
0) You had an unmatched parenthesis
1) You typed a variable name incorrectly
2) Your indentation mixed tabs and spaces
3) You forgot a return statement
? 2
-- OK! --

---------------------------------------------------------------------
debugging-quiz > Suite 1 > Case 11
(cases remaining: 2)

Q: You get a TypeError: ... 'NoneType' object is not ... . What is most likely to have happened?
Choose the number of the correct choice:
0) You typed a variable name incorrectly
1) Your indentation mixed tabs and spaces
2) You had an unmatched parenthesis
3) You forgot a return statement
? 3
-- OK! --

---------------------------------------------------------------------
debugging-quiz > Suite 1 > Case 12
(cases remaining: 1)

Q: You get a NameError. What is most likely to have happened?
Choose the number of the correct choice:
0) You had an unmatched parenthesis
1) You typed a variable name incorrectly
2) You forgot a return statement
3) Your indentation mixed tabs and spaces
? 1
-- OK! --

---------------------------------------------------------------------
OK! All cases for debugging-quiz unlocked.

Cannot backup when running ok with --local.
```

### Coding Practice

#### Q4: Falling Factorial

> Let's write a function `falling`, which is a "falling" factorial that takes two arguments, `n` and `k`, and returns the product of `k` consecutive numbers, starting from `n` and working downwards. When `k` is 0, the function should return 1.

思路：简单的循环语法题，记得给`ans`赋初值

实现代码如下：

```python
def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    ans = 1
    while k > 0:
        ans *= n
        n -= 1
        k -= 1
    return ans
```

#### Q5: Sum Digits

> Write a function that takes in a nonnegative integer and sums its digits. (Using floor division and modulo might be helpful here!)

思路：简单的循环语法题，把每位的数加在一起，得到答案

实现代码如下：

```python
def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    sum = 0
    while y > 0:
        sum += y % 10
        y //= 10

    return sum
```

### Extra Practice

> These questions are optional and will not affect your score on this assignment. However, they are **great practice** for future assignments, projects, and exams. Attempting these questions is valuable in helping cement your knowledge of course concepts, and it's fun!

#### Q6: WWPD: What If?

使用如下命令进行测试：

```shell
python3 ok -q if-statements -u --local
```

需要注意：

`print()`打印字符串不会有`"`或`'`，但字符串做返回值会有`"`或`'`。

测试过程如下：

```shell
=====================================================================
Assignment: Lab 1
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
What If? > Suite 1 > Case 1
(cases remaining: 2)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> def ab(c, d):
...     if c > 5:
...         print(c)
...     elif c > 7:
...         print(d)
...     print('foo')
>>> ab(10, 20)
(line 1)? 10
(line 2)? foo
-- OK! --

---------------------------------------------------------------------
What If? > Suite 1 > Case 2
(cases remaining: 1)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> def bake(cake, make):
...    if cake == 0:
...        cake = cake + 1
...        print(cake)
...    if cake == 1:
...        print(make)
...    else:
...        return cake
...    return make
>>> bake(0, 29)
(line 1)? 1
(line 2)? 29
(line 3)? 29
-- OK! --

>>> bake(1, "mashed potatoes")
(line 1)? mashed potatoes
(line 2)? "mashed potatoes"
-- OK! --

---------------------------------------------------------------------
OK! All cases for What If? unlocked.

Cannot backup when running ok with --local.
```

#### Q7: Double Eights

> Write a function that takes in a number and determines if the digits contain two adjacent 8s.

思路：检查`n`的低2位是否是`88`，然后除`10`，直到`n`变成个位数。

实现代码如下：

```shell
def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    while n >= 10:
        if n % 100 == 88:
            return True
        n //= 10
    return False
```

使用如下命令测试：

```shell
python3 ok -q double_eights --local
```
```shell
=====================================================================
Assignment: Lab 1
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running tests

---------------------------------------------------------------------
Test summary
    1 test cases passed! No cases failed.

Cannot backup when running ok with --local.
```

### 最终测试（不包括`Extra Practice`）

使用如下命令测试：

```shell
python ok --local
```

测试结果如下：

```python
=====================================================================
Assignment: Lab 1
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running tests

---------------------------------------------------------------------
Test summary
    22 test cases passed! No cases failed.

Cannot backup when running ok with --local.
```

