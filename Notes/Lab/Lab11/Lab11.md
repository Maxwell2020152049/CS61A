[TOC]

# Lab 11: Interpreters

实验链接：[Lab 11: Interpreters](https://inst.eecs.berkeley.edu/~cs61a/sp21/lab/lab11/)

如何下载实验压缩包：

```shell
wget https://inst.eecs.berkeley.edu/~cs61a/sp21/lab/lab11/lab11.zip
```

## PyCombinator Interpreter

### Q1: Prologue

使用如下命令进行解锁测试：

```shell
python3 ok -q prologue_reader -u --local
```

```shell
python3 ok -q prologue_expr -u --local
```

测试结果如下：

```shell
=====================================================================
Assignment: Lab 11
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Prologue - Reader > Suite 1 > Case 1
(cases remaining: 10)

Q: What does REPL stand for?
Choose the number of the correct choice:
0) Really-Enormous-Purple-Llamas
1) Read-Eval-Parse-Lex
2) Read-Eval-Print-Loop
? 2
-- OK! --

---------------------------------------------------------------------
Prologue - Reader > Suite 1 > Case 2
(cases remaining: 9)

Q: What does the read component of the REPL loop do?
Choose the number of the correct choice:
0) Ensures a function has been defined before it is called
1) Turns input into a useful data structure
2) Turns input into tokens
3) Evaluates call expressions
? 1
-- OK! --

---------------------------------------------------------------------
Prologue - Reader > Suite 1 > Case 3
(cases remaining: 8)

Q: What does the tokenize function in reader.py return?
Choose the number of the correct choice:
0) Input expression represented as an instance of a subclass of Expr
1) Input expression represented as a list of tokens
2) Result of evaluating the input expression
3) Input expression with corrected number of parentheses
? 1
-- OK! --

---------------------------------------------------------------------
Prologue - Reader > Suite 1 > Case 4
(cases remaining: 7)

Q: What will tokenize('add(3, 4)') output?
Choose the number of the correct choice:
0) ['a', 'd', 'd', '(', '3', ',', '4', ')']
1) ['a', 'd', 'd', '(', 3, ',', 4, ')']
2) ['add', '(', 3, ',', 4, ')']
3) ['add', '(', '3', ',', '4', ')']
? 2
-- OK! --

---------------------------------------------------------------------
Prologue - Reader > Suite 1 > Case 5
(cases remaining: 6)

Q: What will tokenize('(lambda: 4)()') output?
Choose the number of the correct choice:
0) ['(', 'lambda', ':', 4, ')', '(', ')']
1) ['(', LambdaExpr, ':', 4, ')', '(', ')']
2) ['(', LambdaExpr, 4, ')', '(', ')']
3) ['lambda', 4, '(', ')']
? 0
-- OK! --

---------------------------------------------------------------------
Prologue - Reader > Suite 1 > Case 6
(cases remaining: 5)

Q: What does the read_expr function in reader.py accept as input and
return?  (looking at the read function may help answer this question)
Choose the number of the correct choice:
0) List of tokens and number of parentheses
1) List of tokens and an instance of a subclass of Expr
2) Input expression and an instance of a subclass of Expr
3) Input expression and list of tokens
? 1
-- OK! --

---------------------------------------------------------------------
Prologue - Reader > Suite 1 > Case 7
(cases remaining: 4)

Q: What does the read function in reader.py return?
Choose the number of the correct choice:
0) Result of evaluating the input expression
1) Input expression represented as an instance of a subclass of Expr
2) Input expression with corrected number of parentheses
3) Input expression represented as a list of tokens
? 1
-- OK! --

---------------------------------------------------------------------
Prologue - Reader > Suite 1 > Case 8
(cases remaining: 3)

Q: What will read('1') output?
Choose the number of the correct choice:
0) Name(1)
1) Number(1)
2) Literal(1)
3) Name('1')
? 1
-- Not quite. Try again! --

Choose the number of the correct choice:
0) Name(1)
1) Number(1)
2) Literal(1)
3) Name('1')
? 2
-- OK! --

---------------------------------------------------------------------
Prologue - Reader > Suite 1 > Case 9
(cases remaining: 2)

Q: What will read('x') output?
Choose the number of the correct choice:
0) Name('x')
1) Name(x)
2) x
3) Literal(x)
? 1
-- Not quite. Try again! --

Choose the number of the correct choice:
0) Name('x')
1) Name(x)
2) x
3) Literal(x)
? 0
-- OK! --

---------------------------------------------------------------------
Prologue - Reader > Suite 1 > Case 10
(cases remaining: 1)

Q: What will read('add(3, 4)') output?
Choose the number of the correct choice:
0) CallExpr(Literal('add'), Literal(3), Literal(4))
1) CallExpr(Name('add'), [Literal(3), Literal(4)])
2) CallExpr('add', [Literal(3), Literal(4)])
3) CallExpr(Name('add'), Literal(3), Literal(4))
? 1
-- OK! --

---------------------------------------------------------------------
OK! All cases for Prologue - Reader unlocked.

Cannot backup when running ok with --local.
```

```shell
=====================================================================
Assignment: Lab 11
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Prologue - Expr > Suite 1 > Case 1
(cases remaining: 6)

Q: What are all the types of expressions in PyCombinator?
Choose the number of the correct choice:
0) name, function, number, literal
1) number, lambda function, primitive function, string
2) literal, name, call expression, lambda expression
3) value, expression, function, number
? 2
-- OK! --

---------------------------------------------------------------------
Prologue - Expr > Suite 1 > Case 2
(cases remaining: 5)

Q: What are all the types of values in PyCombinator?
Choose the number of the correct choice:
0) number, lambda expression, primitive function
1) number, string, function
2) name, number, lambda function
3) number, lambda function, primitive function
? 3
-- OK! --

---------------------------------------------------------------------
Prologue - Expr > Suite 1 > Case 3
(cases remaining: 4)

Q: What does a Literal evaluate to?
Choose the number of the correct choice:
0) a Function
1) an Expression
2) a Number
3) a String
? 2
-- OK! --

---------------------------------------------------------------------
Prologue - Expr > Suite 1 > Case 4
(cases remaining: 3)

Q: What is the difference between a lambda expression and a lambda function?
Choose the number of the correct choice:
0) A lambda function is the result of evaluating a lambda expression
1) They are the same thing
2) A lambda expression is a call to a lambda function
3) A lambda expression is the result of evaluating a lambda function
? 0
-- OK! --

---------------------------------------------------------------------
Prologue - Expr > Suite 1 > Case 5
(cases remaining: 2)

Q: Which of the following describes the eval method?
Choose the number of the correct choice:
0) A method of Expr objects that evaluates a call expression and returns a Number
1) A method of Literal objects that returns a Name
2) A method of Expr objects that evaluates the Expr and returns a Value
3) A method of LambdaExpression objects that evaluates a function call
? 2
-- OK! --

---------------------------------------------------------------------
Prologue - Expr > Suite 1 > Case 6
(cases remaining: 1)

Q: How are environments represented in our interpreter?
Choose the number of the correct choice:
0) As dictionaries that map Name objects to Value objects
1) As sequences of Frame objects
2) As dictionaries that map variable names to Value objects
3) As linked lists containing dictionaries
? 1
-- Not quite. Try again! --

Choose the number of the correct choice:
0) As dictionaries that map Name objects to Value objects
1) As sequences of Frame objects
2) As dictionaries that map variable names to Value objects
3) As linked lists containing dictionaries
? 0
-- Not quite. Try again! --

Choose the number of the correct choice:
0) As dictionaries that map Name objects to Value objects
1) As sequences of Frame objects
2) As dictionaries that map variable names to Value objects
3) As linked lists containing dictionaries
? 3
-- Not quite. Try again! --

Choose the number of the correct choice:
0) As dictionaries that map Name objects to Value objects
1) As sequences of Frame objects
2) As dictionaries that map variable names to Value objects
3) As linked lists containing dictionaries
? 2
-- OK! --

---------------------------------------------------------------------
OK! All cases for Prologue - Expr unlocked.

Cannot backup when running ok with --local.
```

### Q2: Evaluating Names

实现如下：

```python
class Name(Expr):
    """A `Name` is a variable. When evaluated, we look up the value of the
    variable in the current environment.

    The `var_name` attribute contains the name of the variable (as a Python
    string).
    """
    def eval(self, env: dict[str, 'PrimitiveFunction']):
        """
        >>> env = {
        ...     'a': Number(1),
        ...     'b': LambdaFunction([], Literal(0), {})
        ... }
        >>> Name('a').eval(env)
        Number(1)
        >>> Name('b').eval(env)
        LambdaFunction([], Literal(0), {})
        >>> print(Name('c').eval(env))
        None
        """
        "*** YOUR CODE HERE ***"
        if self.var_name in env.keys():
            return env.get(self.var_name)

        return None
```

### Q3: Evaluating Call Expressions

实现如下：

```python
class CallExpr(Expr):
    """A call expression represents a function call.

    The `operator` attribute is an instance of `Expr`.
    The `operands` attribute is a list of `Expr` instances.

    For example, the call expression `add(3, 4)` is parsed as

    CallExpr(Name('add'), [Literal(3), Literal(4)])

    where `operator` is Name('add') and `operands` are [Literal(3), Literal(4)].
    """
    def eval(self, env: dict[str, 'PrimitiveFunction']):
        """
        >>> from reader import read
        >>> new_env = global_env.copy()
        >>> new_env.update({'a': Number(1), 'b': Number(2)})
        >>> add = CallExpr(Name('add'), [Literal(3), Name('a')])
        >>> add.eval(new_env)
        Number(4)
        >>> new_env['a'] = Number(5)
        >>> add.eval(new_env)
        Number(8)
        >>> read('max(b, a, 4, -1)').eval(new_env)
        Number(5)
        >>> read('add(mul(3, 4), b)').eval(new_env)
        Number(14)
        """
        "*** YOUR CODE HERE ***"
        operator: Expr = self.operator
        operands: list[Expr] = self.operands

        operator_eval: PrimitiveFunction = operator.eval(env)

        operands_eval: list[Value] = []
        for item in operands:
            operands_eval.append(item.eval(env))
        
        return operator_eval.apply(operands_eval)
```

## 必做题测试

使用如下命令进行测试：

```shell
python3 ok --score --local
```

测试结果如下：

```shell
=====================================================================
Assignment: Lab 11
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Scoring tests

---------------------------------------------------------------------
Prologue - Reader
    Passed: 0
    Failed: 0
[k..........] 0.0% passed

---------------------------------------------------------------------
Doctests for Name.eval

>>> from expr import *
>>> env = {
...     'a': Number(1),
...     'b': LambdaFunction([], Literal(0), {})
... }
>>> Name('a').eval(env)
Number(1)
>>> Name('b').eval(env)
LambdaFunction([], Literal(0), {})
>>> print(Name('c').eval(env))
None
Score: 1.0/1

---------------------------------------------------------------------
Doctests for CallExpr.eval

>>> from expr import *
>>> from reader import read
>>> new_env = global_env.copy()
>>> new_env.update({'a': Number(1), 'b': Number(2)})
>>> add = CallExpr(Name('add'), [Literal(3), Name('a')])
>>> add.eval(new_env)
Number(4)
>>> new_env['a'] = Number(5)
>>> add.eval(new_env)
Number(8)
>>> read('max(b, a, 4, -1)').eval(new_env)
Number(5)
>>> read('add(mul(3, 4), b)').eval(new_env)
Number(14)
Score: 1.0/1

---------------------------------------------------------------------
Point breakdown
    Prologue - Reader: 0.0/0
    Name.eval: 1.0/1
    CallExpr.eval: 1.0/1

Score:
    Total: 2.0

Cannot backup when running ok with --local.
```

## Optional Questions

### Q4: Applying Lambda Functions

实现如下：

```python
class LambdaFunction(Value):
    """A lambda function. Lambda functions are created in the LambdaExpr.eval
    method. A lambda function is a lambda expression that knows the
    environment in which it was evaluated in.

    The `parameters` attribute is a list of variable names (a list of strings).
    The `body` attribute is an instance of `Expr`, the body of the function.
    The `parent` attribute is an environment, a dictionary with variable names
        (strings) as keys and instances of the class Value as values.
    """
    def apply(self, arguments: list[Value]):
        """
        >>> from reader import read
        >>> add_lambda = read('lambda x, y: add(x, y)').eval(global_env)
        >>> add_lambda.apply([Number(1), Number(2)])
        Number(3)
        >>> add_lambda.apply([Number(3), Number(4)])
        Number(7)
        >>> sub_lambda = read('lambda add: sub(10, add)').eval(global_env)
        >>> sub_lambda.apply([Number(8)])
        Number(2)
        >>> add_lambda.apply([Number(8), Number(10)]) # Make sure you made a copy of env
        Number(18)
        >>> read('(lambda x: lambda y: add(x, y))(3)(4)').eval(global_env)
        Number(7)
        >>> read('(lambda x: x(x))(lambda y: 4)').eval(global_env)
        Number(4)
        """
        if len(self.parameters) != len(arguments):
            raise TypeError("Oof! Cannot apply number {} to arguments {}".format(
                comma_separated(self.parameters), comma_separated(arguments)))
        "*** YOUR CODE HERE ***"
        # 1. Make a copy of the parent environment.
        env: dict[Value] = self.parent.copy()

        # 2. Update the copy with the parameters of the LambdaFunction and the arguments passed into the method.
        env.update(dict(zip(self.parameters, arguments)))

        # 3. Evaluate the body using the newly created environment.
        return self.body.eval(env)
```

### Q5: Handling Exceptions

在`repl.py`中，添加对**`除0错误`**和**`属性错误`**的处理：

```python
# program start
if __name__ == '__main__':
    """Run a read-eval-print loop.
    `python3 repl.py` to start an interactive REPL.
    `python3 repl.py --read` to interactively read expressions and
      print their Python representations.
    """
    read_only = len(sys.argv) == 2 and sys.argv[1] == '--read'

    while True:
        try:
            # `input` prints the prompt, waits, and returns the user's input.
            user_input = input('> ')
            expr = read(user_input)
            if expr is not None:
                if read_only:
                    print(repr(expr))
                else:
                    print(expr.eval(global_env))
        except (
            SyntaxError, NameError, TypeError, 
            AttributeError, ZeroDivisionError
            ) as err:
            print(type(err).__name__ + ':', err)
        except (KeyboardInterrupt, EOFError):  # Ctrl-C, Ctrl-D
            print()  # blank line
            break  # exit while loop (and end program)
```

