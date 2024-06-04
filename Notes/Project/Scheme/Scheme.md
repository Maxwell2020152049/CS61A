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

实现`quote`过程，返回字面值。

进行解锁测试：

```shell
python ok -q 05 -u --local
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
Problem 5 > Suite 1 > Case 1
(cases remaining: 4)

Q: What is the structure of the expressions argument to do_quote_form?
Choose the number of the correct choice:
0) A, where:
       A is the quoted expression
1) [A], where:
       A is the quoted expression
2) Pair('quote', Pair(A, nil)), where:
       A is the quoted expression
3) Pair(A, nil), where:
       A is the quoted expression
? 3
-- OK! --

---------------------------------------------------------------------
Problem 5 > Suite 2 > Case 1
(cases remaining: 3)

>>> from scheme import *
>>> global_frame = create_global_frame()
>>> do_quote_form(Pair(3, nil), global_frame)
? Pair(3, nil)
-- Not quite. Try again! --

? 3
-- OK! --

>>> do_quote_form(Pair('hi', nil), global_frame)
? 'hi'
-- OK! --

>>> expr = Pair(Pair('+', Pair('x', Pair(2, nil))), nil)
>>> do_quote_form(expr, global_frame) # Make sure to use Pair notation
? Pair('+', Pair('x', Pair(2, nil)))
-- OK! --

---------------------------------------------------------------------
Problem 5 > Suite 3 > Case 1
(cases remaining: 2)

-- Already unlocked --

---------------------------------------------------------------------
Problem 5 > Suite 4 > Case 1
(cases remaining: 1)

-- Already unlocked --

---------------------------------------------------------------------
OK! All cases for Problem 5 unlocked.

Cannot backup when running ok with --local.
```

实现代码如下：

```python
def do_quote_form(expressions: Pair, env: Frame):
    """Evaluate a quote form.

    >>> env = create_global_frame()
    >>> do_quote_form(read_line("((+ x 2))"), env) # evaluating (quote (+ x 2))
    Pair('+', Pair('x', Pair(2, nil)))
    """
    validate_form(expressions, 1, 1)
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    return expressions.first
    # END PROBLEM 5
```

进行代码测试：

```shell
python ok -q 05 --local
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
    4 test cases passed! No cases failed.

Cannot backup when running ok with --local.
```

## Part 2: Procedures

### Problem 6 (1 pt)

实现begin过程，依次计算子表达式，返回最后一个子表达式的结果。

进行解锁测试：

```shell
python ok -q 06 -u --local
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
Problem 6 > Suite 1 > Case 1
(cases remaining: 7)

>>> from scheme import *
>>> env = create_global_frame()
>>> eval_all(Pair(2, nil), env)
Choose the number of the correct choice:
0) SchemeError
1) 2
? 2
-- OK! --

>>> eval_all(Pair(4, Pair(5, nil)), env)
Choose the number of the correct choice:
0) 4
1) 5
2) (4 5)
3) SchemeError
? 5
-- OK! --

>>> eval_all(nil, env) # return None (meaning undefined)
---------------------------------------------------------------------
Problem 6 > Suite 1 > Case 2
(cases remaining: 6)

-- Already unlocked --

---------------------------------------------------------------------
Problem 6 > Suite 2 > Case 1
(cases remaining: 5)


scm> (begin (+ 2 3) (+ 5 6))
? 11
-- OK! --

scm> (begin (define x 3) x)
? 3
-- OK! --

---------------------------------------------------------------------
Problem 6 > Suite 2 > Case 2
(cases remaining: 4)


scm> (begin 30 '(+ 2 2))
Choose the number of the correct choice:
0) 4
1) '(+ 2 2)
2) 30
3) (+ 2 2)
? 1
-- Not quite. Try again! --

Choose the number of the correct choice:
0) 4
1) '(+ 2 2)
2) 30
3) (+ 2 2)
? 3
-- OK! --

scm> (define x 0)
? x
-- OK! --

scm> (begin (define x (+ x 1)) 42 (define y (+ x 1)))
? y
-- OK! --

scm> x
? 1
-- OK! --

scm> y
? 2
-- OK! --

---------------------------------------------------------------------
Problem 6 > Suite 2 > Case 3
(cases remaining: 3)

-- Already unlocked --

---------------------------------------------------------------------
Problem 6 > Suite 2 > Case 4
(cases remaining: 2)

-- Already unlocked --

---------------------------------------------------------------------
Problem 6 > Suite 2 > Case 5
(cases remaining: 1)

-- Already unlocked --

---------------------------------------------------------------------
OK! All cases for Problem 6 unlocked.

Cannot backup when running ok with --local.
```

实现代码如下：

```python
def eval_all(expressions: Pair, env: Frame):
    """Evaluate each expression in the Scheme list EXPRESSIONS in
    Frame ENV (the current environment) and return the value of the last.

    >>> eval_all(read_line("(1)"), create_global_frame())
    1
    >>> eval_all(read_line("(1 2)"), create_global_frame())
    2
    >>> x = eval_all(read_line("((print 1) 2)"), create_global_frame())
    1
    >>> x
    2
    >>> eval_all(read_line("((define x 2) x)"), create_global_frame())
    2
    """
    # BEGIN PROBLEM 6
    value = None
    expr: Pair = expressions
    while isinstance(expr, Pair):
        value = scheme_eval(expr.first, env)
        expr = expr.rest
    return value
    # END PROBLEM 6
```

进行代码测试：

```shell
python ok -q 06 --local
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
    7 test cases passed! No cases failed.

Cannot backup when running ok with --local.
```

### Problem 7 (2 pt)

进行解锁测试：

```shell
python ok -q 07 -u --local
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
Problem 7 > Suite 1 > Case 1
(cases remaining: 5)


scm> (lambda (x y) (+ x y))
? (lambda (x y) (+ x y))
-- OK! --

scm> (lambda (x)) ; type SchemeError if you think this causes an error
? SchemeError
-- OK! --

---------------------------------------------------------------------
Problem 7 > Suite 1 > Case 2
(cases remaining: 4)

-- Already unlocked --

---------------------------------------------------------------------
Problem 7 > Suite 1 > Case 3
(cases remaining: 3)

-- Already unlocked --

---------------------------------------------------------------------
Problem 7 > Suite 2 > Case 1
(cases remaining: 2)

>>> from scheme_reader import *
>>> from scheme import *
>>> env = create_global_frame()
>>> lambda_line = read_line("(lambda (a b c) (+ a b c))")
>>> lambda_proc = do_lambda_form(lambda_line.rest, env)
>>> lambda_proc.formals # use single quotes ' around strings in your answer
? Pair('a', Pair('b', Pair('c', nil)))
-- OK! --

>>> lambda_proc.body # the body is a *Scheme list* of expressions! Make sure your answer is a properly nested Pair.
? Pair(Pair('+', Pair('a', Pair('b', Pair('c', nil)))), nil)
-- OK! --

---------------------------------------------------------------------
Problem 7 > Suite 2 > Case 2
(cases remaining: 1)

-- Already unlocked --

---------------------------------------------------------------------
OK! All cases for Problem 7 unlocked.

Cannot backup when running ok with --local.
```

实现代码如下：

```python
def do_lambda_form(expressions: Pair, env: Frame):
    """Evaluate a lambda form.

    >>> env = create_global_frame()
    >>> do_lambda_form(read_line("((x) (+ x 2))"), env) # evaluating (lambda (x) (+ x 2))
    LambdaProcedure(Pair('x', nil), Pair(Pair('+', Pair('x', Pair(2, nil))), nil), <Global Frame>)
    """
    validate_form(expressions, 2)
    formals = expressions.first
    validate_formals(formals)
    # BEGIN PROBLEM 7
    "*** YOUR CODE HERE ***"
    return LambdaProcedure(formals=formals, body=expressions.rest, env=env)
    # END PROBLEM 7
```

进行代码测试：

```shell
python ok -q 07 --local
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

### Problem 8 (2 pt)

进行解锁测试：

```shell
python ok -q 08 -u --local
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
Problem 8 > Suite 1 > Case 1
(cases remaining: 6)

>>> from scheme import *
>>> global_frame = create_global_frame()
>>> formals = Pair('a', Pair('b', Pair('c', nil)))
>>> vals = Pair(1, Pair(2, Pair(3, nil)))
>>> frame = global_frame.make_child_frame(formals, vals)
>>> global_frame.lookup('a') # Type SchemeError if you think this errors
? 1
-- Not quite. Try again! --

? SchemeError
-- OK! --

>>> frame.lookup('a')        # Type SchemeError if you think this errors
? 1
-- OK! --

>>> frame.lookup('b')        # Type SchemeError if you think this errors
? 2
-- OK! --

>>> frame.lookup('c')        # Type SchemeError if you think this errors
? 3
-- OK! --

---------------------------------------------------------------------
Problem 8 > Suite 1 > Case 2
(cases remaining: 5)

>>> from scheme import *
>>> global_frame = create_global_frame()
>>> frame = global_frame.make_child_frame(nil, nil)
>>> frame.parent is global_frame
? True
-- OK! --

---------------------------------------------------------------------
Problem 8 > Suite 1 > Case 3
(cases remaining: 4)

-- Already unlocked --

---------------------------------------------------------------------
Problem 8 > Suite 2 > Case 1
(cases remaining: 3)

-- Already unlocked --

---------------------------------------------------------------------
Problem 8 > Suite 2 > Case 2
(cases remaining: 2)

-- Already unlocked --

---------------------------------------------------------------------
Problem 8 > Suite 2 > Case 3
(cases remaining: 1)

-- Already unlocked --

---------------------------------------------------------------------
OK! All cases for Problem 8 unlocked.

Cannot backup when running ok with --local.
```

实现代码如下：

```python
def make_child_frame(self, formals: Pair, vals: Pair):
        """Return a new local frame whose parent is SELF, in which the symbols
        in a Scheme list of formal parameters FORMALS are bound to the Scheme
        values in the Scheme list VALS. Both FORMALS and VALS are represented
        as Pairs. Raise an error if too many or too few vals are given.

        >>> env = create_global_frame()
        >>> formals, expressions = read_line('(a b c)'), read_line('(1 2 3)')
        >>> env.make_child_frame(formals, expressions)
        <{a: 1, b: 2, c: 3} -> <Global Frame>>
        """
        if len(formals) != len(vals):
            raise SchemeError('Incorrect number of arguments to function call')
        # BEGIN PROBLEM 8
        frame = Frame(self)
        while isinstance(formals, Pair):
            frame.define(formals.first, vals.first)
            formals = formals.rest
            vals = vals.rest
        return frame
        "*** YOUR CODE HERE ***"
        # END PROBLEM 8
```

进行代码测试：

```shell
python ok -q 08 --local
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
    6 test cases passed! No cases failed.

Cannot backup when running ok with --local.
```

### Problem 9 (2 pt)

进行解锁测试：

```shell
python ok -q 09 -u --local
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
Problem 9 > Suite 1 > Case 1
(cases remaining: 6)

-- Already unlocked --

---------------------------------------------------------------------
Problem 9 > Suite 1 > Case 2
(cases remaining: 5)

-- Already unlocked --

---------------------------------------------------------------------
Problem 9 > Suite 2 > Case 1
(cases remaining: 4)

-- Already unlocked --

---------------------------------------------------------------------
Problem 9 > Suite 2 > Case 2
(cases remaining: 3)

-- Already unlocked --

---------------------------------------------------------------------
Problem 9 > Suite 3 > Case 1
(cases remaining: 2)


scm> (define outer (lambda (x y)
....   (define inner (lambda (z x)
....     (+ x (* y 2) (* z 3))))
....   (inner x 10)))
? outer
-- OK! --

scm> (outer 1 2)
? 17
-- OK! --

scm> (define outer-func (lambda (x y)
....   (define inner (lambda (z x)
....     (+ x (* y 2) (* z 3))))
....   inner))
? outer-func
-- OK! --

scm> ((outer-func 1 2) 1 10)
? 17
-- OK! --

---------------------------------------------------------------------
Problem 9 > Suite 3 > Case 2
(cases remaining: 1)

-- Already unlocked --

---------------------------------------------------------------------
OK! All cases for Problem 9 unlocked.

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
        ......
    elif isinstance(procedure, LambdaProcedure):
        # BEGIN PROBLEM 9
        "*** YOUR CODE HERE ***"
        frame: Frame = procedure.env.make_child_frame(formals=procedure.formals, vals=args)
        return eval_all(expressions=procedure.body, env=frame)
        # END PROBLEM 9
    elif isinstance(procedure, MuProcedure):
        ......
    else:
        assert False, "Unexpected procedure: {}".format(procedure)
```

进行代码测试：

```shell
python ok -q 09 --local
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
    6 test cases passed! No cases failed.

Cannot backup when running ok with --local.
```

### Problem 10 (1 pt)

进行解锁测试：

```shell
python ok -q 10 -u --local
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
Problem 10 > Suite 1 > Case 1
(cases remaining: 7)


scm> (define (f x y) (+ x y))
? f
-- OK! --

scm> f
Choose the number of the correct choice:
0) (define f (lambda (x y) (+ x y)))
1) (lambda (f x y) (+ x y))
2) (lambda (x y) (+ x y))
3) (f (x y) (+ x y))
? 0
-- Not quite. Try again! --

Choose the number of the correct choice:
0) (define f (lambda (x y) (+ x y)))
1) (lambda (f x y) (+ x y))
2) (lambda (x y) (+ x y))
3) (f (x y) (+ x y))
? 2
-- OK! --

---------------------------------------------------------------------
Problem 10 > Suite 1 > Case 2
(cases remaining: 6)

-- Already unlocked --

---------------------------------------------------------------------
Problem 10 > Suite 1 > Case 3
(cases remaining: 5)

-- Already unlocked --

---------------------------------------------------------------------
Problem 10 > Suite 1 > Case 4
(cases remaining: 4)

-- Already unlocked --

---------------------------------------------------------------------
Problem 10 > Suite 1 > Case 5
(cases remaining: 3)

-- Already unlocked --

---------------------------------------------------------------------
Problem 10 > Suite 1 > Case 6
(cases remaining: 2)

-- Already unlocked --

---------------------------------------------------------------------
Problem 10 > Suite 2 > Case 1
(cases remaining: 1)

-- Already unlocked --

---------------------------------------------------------------------
OK! All cases for Problem 10 unlocked.

Cannot backup when running ok with --local.
```

实现代码如下：

```python
def do_define_form(expressions: Pair, env: Frame):
    ......
    validate_form(expressions, 2)  # Checks that expressions is a list of length at least 2
    signature = expressions.first
    if scheme_symbolp(signature):
        ......
    elif isinstance(signature, Pair) and scheme_symbolp(signature.first):
        # defining a named procedure e.g. (define (f x y) (+ x y))
        # BEGIN PROBLEM 10
        "*** YOUR CODE HERE ***"
        symbol: str = signature.first
        formals: Pair = signature.rest
        body: Pair = expressions.rest
        lambda_procedure: LambdaProcedure = do_lambda_form(expressions=Pair(formals, body), env=env)
        env.define(symbol, lambda_procedure)
        return symbol
        # END PROBLEM 10
    else:
        bad_signature = signature.first if isinstance(signature, Pair) else signature
        raise SchemeError('non-symbol: {0}'.format(bad_signature))
```

进行代码测试：

```shell
python ok -q 10 --local
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
    7 test cases passed! No cases failed.

Cannot backup when running ok with --local.
```

### Problem 11 (1 pt)

进行解锁测试：

```shell
python ok -q 11 -u --local
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
Problem 11 > Suite 1 > Case 1
(cases remaining: 2)


scm> (define y 1)
? y
-- OK! --

scm> (define f (mu (x) (+ x y)))
? f
-- OK! --

scm> (define g (lambda (x y) (f (+ x x))))
? g
-- OK! --

scm> (g 3 7)
? 13
-- OK! --

---------------------------------------------------------------------
Problem 11 > Suite 2 > Case 1
(cases remaining: 1)

-- Already unlocked --

---------------------------------------------------------------------
OK! All cases for Problem 11 unlocked.

Cannot backup when running ok with --local.
```

实现代码如下：

```python
# in scheme_forms.py
def do_mu_form(expressions: Pair, env: Frame):
    """Evaluate a mu form."""
    validate_form(expressions, 2)
    formals: Pair = expressions.first
    validate_formals(formals)
    # BEGIN PROBLEM 11
    "*** YOUR CODE HERE ***"
    mu_procedure: MuProcedure = MuProcedure(formals, expressions.rest)
    return mu_procedure
    # END PROBLEM 11

# in scheme_eval_apply.py
def scheme_apply(procedure: Procedure, args: Pair, env: Frame):
    """Apply Scheme PROCEDURE to argument values ARGS (a Scheme list) in
    Frame ENV, the current environment."""
    validate_procedure(procedure)
    if not isinstance(env, Frame):
       assert False, "Not a Frame: {}".format(env)
    if isinstance(procedure, BuiltinProcedure):
        ......
    elif isinstance(procedure, LambdaProcedure):
        ......
    elif isinstance(procedure, MuProcedure):
        # BEGIN PROBLEM 11
        "*** YOUR CODE HERE ***"
        frame: Frame = env.make_child_frame(formals=procedure.formals, vals=args)
        return eval_all(expressions=procedure.body, env=frame)
        # END PROBLEM 11
    else:
        assert False, "Unexpected procedure: {}".format(procedure)
```

进行代码测试：

```shell
python ok -q 11 --local
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
    2 test cases passed! No cases failed.

Cannot backup when running ok with --local.
```

## Part 3: Special Forms

### Problem 12 (2 pt)

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



### Problem 13 (2 pt)

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



### Problem 14 (2 pt)

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



### Additional Scheme Tests (1 pt)



## Part 4: Write Some Scheme

### Problem 15 (2 pt)

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



### Problem 16 (2 pt)

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



## Optional Problems

### Optional Problem (0 pt)



