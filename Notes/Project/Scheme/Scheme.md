[TOC]

# Project 4: Scheme Interpreter

截止`2024/6/1`，`CS61A`的往年的网站都需要UCB的校园网账号认证，所以使用`2023 Spring`的版本完成。

本项目在`Windows`系统上完成，使用`python`表示`python3`。

## Part 1: The Evaluator

测试对基础知识的理解：

```shell
python ok -q eval_apply -u --local
```

结果如下：

```shell
=====================================================================
Assignment: Project 4: Scheme Interpreter
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Understanding Eval/Apply > Suite 1 > Case 1
(cases remaining: 5)

Q: What types of expressions are represented as Pairs?
Choose the number of the correct choice:
0) All expressions are represented as Pairs
1) Only call expressions
2) Call expressions and special forms
3) Only special forms
? 0
-- Not quite. Try again! --

Choose the number of the correct choice:
0) All expressions are represented as Pairs
1) Only call expressions
2) Call expressions and special forms
3) Only special forms
? 2
-- OK! --

---------------------------------------------------------------------
Understanding Eval/Apply > Suite 1 > Case 2
(cases remaining: 4)

Q: What expression in the body of scheme_eval finds the value of a name?
Choose the number of the correct choice:
0) scheme_forms.SPECIAL_FORMS[first](rest, env)
1) scheme_symbolp(expr)
2) env.lookup(expr)
3) env.find(name)
? 2
-- OK! --

---------------------------------------------------------------------
Understanding Eval/Apply > Suite 1 > Case 3
(cases remaining: 3)

Q: How do we know if a given combination is a special form?
Choose the number of the correct choice:
0) Check if the first element in the list is a symbol
1) Check if the first element in the list is a symbol and that the
   symbol is in the dictionary SPECIAL_FORMS
2) Check if the expression is in the dictionary SPECIAL_FORMS
? 1
-- OK! --

---------------------------------------------------------------------
Understanding Eval/Apply > Suite 1 > Case 4
(cases remaining: 2)

Q: What is the difference between applying builtins and applying user-defined procedures?
(Choose all that apply)

I.   User-defined procedures open a new frame; builtins do not
II.  Builtins simply execute a predefined Python function; user-defined
     procedures must evaluate additional expressions in the body
III. Builtins have a fixed number of arguments; user-defined procedures do not

---
Choose the number of the correct choice:
0) III only
1) II only
2) I only
3) I, II and III
4) I and II
5) I and III
6) II and III
? 4
-- OK! --

---------------------------------------------------------------------
Understanding Eval/Apply > Suite 1 > Case 5
(cases remaining: 1)

Q: What exception should be raised for the expression (1)?
Choose the number of the correct choice:
0) SchemeError("malformed list: (1)")
1) AssertionError
2) SchemeError("unknown identifier: 1")
3) SchemeError("1 is not callable")
? 0
-- Not quite. Try again! --

Choose the number of the correct choice:
0) SchemeError("malformed list: (1)")
1) AssertionError
2) SchemeError("unknown identifier: 1")
3) SchemeError("1 is not callable")
? 2
-- Not quite. Try again! --

Choose the number of the correct choice:
0) SchemeError("malformed list: (1)")
1) AssertionError
2) SchemeError("unknown identifier: 1")
3) SchemeError("1 is not callable")
? 3
-- OK! --

---------------------------------------------------------------------
OK! All cases for Understanding Eval/Apply unlocked.

Cannot backup when running ok with --local.
```

### Problem 1 (1 pt)

Frame类是将值绑定到scheme变量上的类，实现该类的两个成员函数。

使用如下命令进行解锁测试：

```shell
python ok -q 01 -u --local
```

结果如下：

```shell
$ python ok -q 01 -u --local
=====================================================================
Assignment: Project 4: Scheme Interpreter
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 1 > Suite 1 > Case 1
(cases remaining: 5)

>>> from scheme import *
>>> global_frame = create_global_frame()
>>> global_frame.define("x", 3)
>>> global_frame.parent is None
? True
-- OK! --

>>> global_frame.lookup("x")
? 3
-- OK! --

>>> global_frame.define("x", 2)
>>> global_frame.lookup("x")
? 2
-- OK! --

>>> global_frame.lookup("foo")
Choose the number of the correct choice:
0) SchemeError
1) 3
2) None
? 0
-- OK! --

---------------------------------------------------------------------
Problem 1 > Suite 1 > Case 2
(cases remaining: 4)

>>> from scheme import *
>>> first_frame = create_global_frame()
>>> first_frame.define("x", 3)
>>> second_frame = Frame(first_frame)
>>> second_frame.parent == first_frame
? True
-- OK! --

>>> second_frame.define("y", False)
>>> second_frame.lookup("x")
? 3
-- OK! --

>>> second_frame.lookup("y")
? False
-- OK! --

---------------------------------------------------------------------
Problem 1 > Suite 1 > Case 3
(cases remaining: 3)

-- Already unlocked --

---------------------------------------------------------------------
Problem 1 > Suite 1 > Case 4
(cases remaining: 2)

-- Already unlocked --

---------------------------------------------------------------------
Problem 1 > Suite 2 > Case 1
(cases remaining: 1)

-- Already unlocked --

---------------------------------------------------------------------
OK! All cases for Problem 1 unlocked.

Cannot backup when running ok with --local.
```

实现代码如下：

```python
class Frame:
    """An environment frame binds Scheme symbols to Scheme values."""
    def define(self, symbol: str, value):
        """Define Scheme SYMBOL to have VALUE."""
        # BEGIN PROBLEM 1
        "*** YOUR CODE HERE ***"
        self.bindings[symbol] = value
        # END PROBLEM 1

    def lookup(self, symbol: str):
        """Return the value bound to SYMBOL. Errors if SYMBOL is not found."""
        # BEGIN PROBLEM 1
        "*** YOUR CODE HERE ***"
        frame: Frame = self
        while frame is not None:
            if frame.bindings.get(symbol) is not None:
                return frame.bindings.get(symbol)
            frame = frame.parent
        # END PROBLEM 1
        raise SchemeError('unknown identifier: {0}'.format(symbol))
```

进行代码测试：

```shell
python ok -q 01 --local
```

结果如下：

```shell
=====================================================================
Assignment: Project 4: Scheme Interpreter
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running tests

---------------------------------------------------------------------
Test summary
    5 test cases passed! No cases failed.

Cannot backup when running ok with --local.
```

### Problem 2 (2 pt)

实现scheme_apply函数中计算内置过程的部分。

进行解锁测试：

```shell
python ok -q 02 -u --local
```

结果如下：

```shell
=====================================================================
Assignment: Project 4: Scheme Interpreter
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 2 > Suite 1 > Case 1
(cases remaining: 11)

>>> from scheme import *
>>> env = create_global_frame()
>>> twos = Pair(2, Pair(2, nil))
>>> plus = BuiltinProcedure(scheme_add) # + procedure
>>> scheme_apply(plus, twos, env) # Type SchemeError if you think this errors
? 4
-- OK! --

---------------------------------------------------------------------
Problem 2 > Suite 1 > Case 2
(cases remaining: 10)

>>> from scheme import *
>>> env = create_global_frame()
>>> plus = BuiltinProcedure(scheme_add) # + procedure
>>> scheme_apply(plus, nil, env) # Remember what (+) evaluates to in scheme
? 0
-- OK! --

---------------------------------------------------------------------
Problem 2 > Suite 1 > Case 3
(cases remaining: 9)

>>> from scheme import *
>>> env = create_global_frame()
>>> twos = Pair(2, Pair(2, nil))
>>> oddp = BuiltinProcedure(scheme_oddp) # odd? procedure
>>> scheme_apply(oddp, twos, env) # Type SchemeError if you think this errors
? False
-- Not quite. Try again! --

? SchemeError
-- OK! --

---------------------------------------------------------------------
Problem 2 > Suite 1 > Case 4
(cases remaining: 8)

-- Already unlocked --

---------------------------------------------------------------------
Problem 2 > Suite 1 > Case 5
(cases remaining: 7)

-- Already unlocked --

---------------------------------------------------------------------
Problem 2 > Suite 1 > Case 6
(cases remaining: 6)

-- Already unlocked --

---------------------------------------------------------------------
Problem 2 > Suite 1 > Case 7
(cases remaining: 5)

-- Already unlocked --

---------------------------------------------------------------------
Problem 2 > Suite 1 > Case 8
(cases remaining: 4)

-- Already unlocked --

---------------------------------------------------------------------
Problem 2 > Suite 1 > Case 9
(cases remaining: 3)

-- Already unlocked --

---------------------------------------------------------------------
Problem 2 > Suite 1 > Case 10
(cases remaining: 2)

-- Already unlocked --

---------------------------------------------------------------------
Problem 2 > Suite 1 > Case 11
(cases remaining: 1)

-- Already unlocked --

---------------------------------------------------------------------
OK! All cases for Problem 2 unlocked.

Cannot backup when running ok with --local.
```

实现代码如下：

```python
def scheme_apply(procedure: Procedure, args: Pair, env: Frame):
    """Apply Scheme PROCEDURE to argument values ARGS (a Scheme list) in
    Frame ENV, the current environment."""
    validate_procedure(procedure)
    if not isinstance(env, Frame):
       assert False, "Not a Frame: {}".format(env)
    if isinstance(procedure, BuiltinProcedure):
        # BEGIN PROBLEM 2
        "*** YOUR CODE HERE ***"
        # 将 args 从 Pair 转换为 列表
        args_list: list = []
        while isinstance(args, Pair):
            args_list.append(args.first)
            args = args.rest
        if procedure.need_env:
            args_list.append(env)
        # END PROBLEM 2
        try:
            # BEGIN PROBLEM 2
            "*** YOUR CODE HERE ***"
            return procedure.py_func(*args_list)
            # END PROBLEM 2
        except TypeError as err:
            raise SchemeError('incorrect number of arguments: {0}'.format(procedure))
    ......
```

进行代码测试：

```shell
python ok -q 02 --local
```

结果如下：

```shell
=====================================================================
Assignment: Project 4: Scheme Interpreter
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running tests

---------------------------------------------------------------------
Test summary
    11 test cases passed! No cases failed.

Cannot backup when running ok with --local.
```

### Problem 3 (2 pt)

实现scheme对内置过程的计算。

进行解锁测试：

```shell
python ok -q 03 -u --local
```

结果如下：

```shell
=====================================================================
Assignment: Project 4: Scheme Interpreter
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 3 > Suite 1 > Case 1
(cases remaining: 5)

>>> from scheme_reader import *
>>> from scheme import *
>>> expr = read_line('(+ 2 2)')
>>> scheme_eval(expr, create_global_frame()) # Type SchemeError if you think this errors
? 4
-- OK! --

>>> scheme_eval(Pair('+', Pair(2, Pair(2, nil))), create_global_frame()) # Type SchemeError if you think this errors
? 4
-- OK! --

>>> expr = read_line('(+ (+ 2 2) (+ 1 3) (* 1 4))')
>>> scheme_eval(expr, create_global_frame()) # Type SchemeError if you think this errors
? 12
-- OK! --

>>> expr = read_line('(yolo)')
>>> scheme_eval(expr, create_global_frame()) # Type SchemeError if you think this errors
? SchemeError
-- OK! --

---------------------------------------------------------------------
Problem 3 > Suite 2 > Case 1
(cases remaining: 4)


scm> (* (+ 3 2) (+ 1 7)) ; Type SchemeError if you think this errors
? 35
-- Not quite. Try again! --

? 40
-- OK! --

scm> (1 2) ; Type SchemeError if you think this errors
? SchemeError
-- OK! --

---------------------------------------------------------------------
Problem 3 > Suite 2 > Case 2
(cases remaining: 3)

-- Already unlocked --

---------------------------------------------------------------------
Problem 3 > Suite 2 > Case 3
(cases remaining: 2)

-- Already unlocked --

---------------------------------------------------------------------
Problem 3 > Suite 2 > Case 4
(cases remaining: 1)

-- Already unlocked --

---------------------------------------------------------------------
OK! All cases for Problem 3 unlocked.

Cannot backup when running ok with --local.
```

实现代码如下：

```python
def scheme_eval(expr: Pair, env: Frame, _=None):  # Optional third argument is ignored
    def eval(_expr):
        return scheme_eval(_expr, env)
    """Evaluate Scheme expression EXPR in Frame ENV.

    >>> expr = read_line('(+ 2 2)')
    >>> expr
    Pair('+', Pair(2, Pair(2, nil)))
    >>> scheme_eval(expr, create_global_frame())
    4
    """
    # Evaluate atoms
    if scheme_symbolp(expr):
        return env.lookup(expr)
    elif self_evaluating(expr):
        return expr

    # All non-atomic expressions are lists (combinations)
    if not scheme_listp(expr):
        raise SchemeError('malformed list: {0}'.format(repl_str(expr)))
    first, rest = expr.first, expr.rest
    if scheme_symbolp(first) and first in scheme_forms.SPECIAL_FORMS:
        return scheme_forms.SPECIAL_FORMS[first](rest, env)
    else:
        # BEGIN PROBLEM 3
        "*** YOUR CODE HERE ***"
        procedure: Procedure = scheme_eval(first, env) if isinstance(first, Pair) else env.lookup(first)
        args: Pair = rest.map(eval)
        return scheme_apply(procedure, args, env)
        # END PROBLEM 3
```

进行代码测试：

```shell
python ok -q 03 --local
```

结果如下：

```shell
=====================================================================
Assignment: Project 4: Scheme Interpreter
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running tests

---------------------------------------------------------------------
Test summary
    5 test cases passed! No cases failed.

Cannot backup when running ok with --local.
```

### Problem 4 (2 pt)

实现define过程，使其能够定义一个符号。

进行解锁测试：

```shell
python ok -q 04 -u --local
```

结果如下：

```shell
=====================================================================
Assignment: Project 4: Scheme Interpreter
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 4 > Suite 1 > Case 1
(cases remaining: 9)

Q: What is the structure of the expressions argument to do_define_form?
Choose the number of the correct choice:
0) Pair(A, B), where:
       A is the symbol being bound,
       B is an expression whose value should be evaluated and bound to A
1) Pair('define', Pair(A, Pair(B, nil))), where:
       A is the symbol being bound,
       B is an expression whose value should be evaluated and bound to A
2) Pair(A, Pair(B, nil)), where:
       A is the symbol being bound,
       B is an expression whose value should be evaluated and bound to A
3) Pair(A, Pair(B, nil)), where:
       A is the symbol being bound,
       B is the value that should be bound to A
4) Pair(A, B), where:
       A is the symbol being bound,
       B is the value that should be bound to A
? 1
-- Not quite. Try again! --

Choose the number of the correct choice:
0) Pair(A, B), where:
       A is the symbol being bound,
       B is an expression whose value should be evaluated and bound to A
1) Pair('define', Pair(A, Pair(B, nil))), where:
       A is the symbol being bound,
       B is an expression whose value should be evaluated and bound to A
2) Pair(A, Pair(B, nil)), where:
       A is the symbol being bound,
       B is an expression whose value should be evaluated and bound to A
3) Pair(A, Pair(B, nil)), where:
       A is the symbol being bound,
       B is the value that should be bound to A
4) Pair(A, B), where:
       A is the symbol being bound,
       B is the value that should be bound to A
? 0
-- Not quite. Try again! --

Choose the number of the correct choice:
0) Pair(A, B), where:
       A is the symbol being bound,
       B is an expression whose value should be evaluated and bound to A
1) Pair('define', Pair(A, Pair(B, nil))), where:
       A is the symbol being bound,
       B is an expression whose value should be evaluated and bound to A
2) Pair(A, Pair(B, nil)), where:
       A is the symbol being bound,
       B is an expression whose value should be evaluated and bound to A
3) Pair(A, Pair(B, nil)), where:
       A is the symbol being bound,
       B is the value that should be bound to A
4) Pair(A, B), where:
       A is the symbol being bound,
       B is the value that should be bound to A
? 2
-- OK! --

---------------------------------------------------------------------
Problem 4 > Suite 1 > Case 2
(cases remaining: 8)

Q: What method of a Frame instance will bind
a value to a symbol in that frame?
Choose the number of the correct choice:
0) bindings
1) define
2) lookup
3) make_child_frame
? 1
-- OK! --

---------------------------------------------------------------------
Problem 4 > Suite 2 > Case 1
(cases remaining: 7)


scm> (define size 2)
? size
-- OK! --

scm> size
? 2
-- OK! --

scm> (define x (+ 7 3))
? x
-- OK! --

scm> x
? 10
-- OK! --

---------------------------------------------------------------------
Problem 4 > Suite 2 > Case 2
(cases remaining: 6)

-- Already unlocked --

---------------------------------------------------------------------
Problem 4 > Suite 2 > Case 3
(cases remaining: 5)

-- Already unlocked --

---------------------------------------------------------------------
Problem 4 > Suite 2 > Case 4
(cases remaining: 4)

-- Already unlocked --

---------------------------------------------------------------------
Problem 4 > Suite 2 > Case 5
(cases remaining: 3)

-- Already unlocked --

---------------------------------------------------------------------
Problem 4 > Suite 2 > Case 6
(cases remaining: 2)

-- Already unlocked --

---------------------------------------------------------------------
Problem 4 > Suite 2 > Case 7
(cases remaining: 1)

-- Already unlocked --

---------------------------------------------------------------------
OK! All cases for Problem 4 unlocked.

Cannot backup when running ok with --local.
```

实现代码如下：

```python
def do_define_form(expressions: Pair, env: Frame):
    validate_form(expressions, 2)  # Checks that expressions is a list of length at least 2
    signature = expressions.first
    if scheme_symbolp(signature):
        # assigning a name to a value e.g. (define x (+ 1 2))
        validate_form(expressions, 2, 2)  # Checks that expressions is a list of length exactly 2
        # BEGIN PROBLEM 4
        "*** YOUR CODE HERE ***"
        first, rest = expressions.first, expressions.rest
        value = scheme_eval(rest.first, env)
        env.define(first, value)
        return first
        # END PROBLEM 4
    elif isinstance(signature, Pair) and scheme_symbolp(signature.first):
        # defining a named procedure e.g. (define (f x y) (+ x y))
        # BEGIN PROBLEM 10
        "*** YOUR CODE HERE ***"
        # END PROBLEM 10
    else:
        bad_signature = signature.first if isinstance(signature, Pair) else signature
        raise SchemeError('non-symbol: {0}'.format(bad_signature))
```

进行代码测试：

```shell
python ok -q 04 --local
```

结果如下：

```shell
=====================================================================
Assignment: Project 4: Scheme Interpreter
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running tests

---------------------------------------------------------------------
Test summary
    9 test cases passed! No cases failed.

Cannot backup when running ok with --local.
```

### Problem 5 (1 pt)

进行解锁测试：

```shell

```

结果如下：

```shell

```

实现代码如下：

```python

```

进行代码测试：

```shell

```

结果如下：

```shell

```

