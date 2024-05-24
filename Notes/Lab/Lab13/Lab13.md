[TOC]

# Lab 13: Regular Expressions, BNF

实验链接：[Lab 13: Regular Expressions, BNF](https://inst.eecs.berkeley.edu/~cs61a/sp21/lab/lab13/)

如何下载实验压缩包：

```shell
wget https://inst.eecs.berkeley.edu/~cs61a/sp21/lab/lab13/lab13.zip
```

## Q1: EBNF Grammar

使用如下命令进行解锁测试：

```shell
python3 ok -q ebnf-grammar-wwpd -u --local
```

过程如下：

```shell
=====================================================================
Assignment: Lab 13
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
ebnf-grammar > Suite 1 > Case 1
(cases remaining: 4)

Q: Which aspects of the Calculator language are supported by this grammar?
Choose the number of the correct choice:
0) Variables can be defined and used as operands.
1) The division operator requires at least two arguments.
2) The subtraction operator requires at least one argument.
3) Each of the operands can itself be a Calculator expression.
? 3
-- OK! --

---------------------------------------------------------------------
ebnf-grammar > Suite 1 > Case 2
(cases remaining: 3)

Q: Which of the following expressions would NOT be parsable according to that BNF?
Choose the number of the correct choice:
0) (1 + 2)
1) (+ 1)
2) (+ 1 (+ 2 3))
3) (+)
4) (+ 1 2 3)
5) (+ 1 2)
? 0
-- OK! --

---------------------------------------------------------------------
ebnf-grammar > Suite 1 > Case 3
(cases remaining: 2)

Q: Which line of the BNF should we modify to add support for calculations using a modulus operator, like (% 15 5)?
Choose the number of the correct choice:
0) ?calc_expr: NUMBER | calc_op
1) calc_op: "(" OPERATOR calc_expr* ")"
2) start: calc_expr
3) OPERATOR: "+" | "-" | "*" | "/"
? 3
-- OK! --

---------------------------------------------------------------------
ebnf-grammar > Suite 1 > Case 4
(cases remaining: 1)

Q: Does the EBNF grammar provide enough information to create a working interpreter for this version of the Calculator language?
Choose the number of the correct choice:
0) Yes, but only if we feed this grammar into a program that was written in the Calculator language itself.
1) Yes, if we feed this grammar into a program that understands EBNF grammars, it will be able to parse Calculator expressions and output the result.
2) No, this grammar does not provide enough information for the parsing or evaluation step, it is useful mostly as documentation.
3) No, this grammar gives enough information for parsing a Calculator expression, but it does not provide enough information to evaluate it.
? 3
-- OK! --

---------------------------------------------------------------------
OK! All cases for ebnf-grammar unlocked.

Cannot backup when running ok with --local.
```

## Q2: Roman Numerals

实现如下：

```python
def roman_numerals(text):
    """
    Finds any string of letters that could be a Roman numeral
    (made up of the letters I, V, X, L, C, D, M).

    >>> roman_numerals("Sir Richard IIV, can you tell Richard VI that Richard IV is on the phone?")
    ['IIV', 'VI', 'IV']
    >>> roman_numerals("My TODOs: I. Groceries II. Learn how to count in Roman IV. Profit")
    ['I', 'II', 'IV']
    >>> roman_numerals("I. Act 1 II. Act 2 III. Act 3 IV. Act 4 V. Act 5")
    ['I', 'II', 'III', 'IV', 'V']
    >>> roman_numerals("Let's play Civ VII")
    ['VII']
    >>> roman_numerals("i love vi so much more than emacs.")
    []
    >>> roman_numerals("she loves ALL editors equally.")
    []
    """
    return re.findall(r"\b([IVXLCDM]+)\b", text)
```

## Q3: Calculator Ops

实现如下：

```python
def calculator_ops(calc_str):
    """
    Finds expressions from the Calculator language that have two
    numeric operands and returns the expression without the parentheses.

    >>> calculator_ops("(* 2 4)")
    ['* 2 4']
    >>> calculator_ops("(+ (* 3 (+ (* 2 4) (+ 3 5))) (+ (- 10 7) 6))")
    ['* 2 4', '+ 3 5', '- 10 7']
    >>> calculator_ops("(* 2)")
    []
    """
    return re.findall(r"\(([+*-/]{1}\s\d+\s\d+)\)", calc_str)
```

## Q4: CS Classes

实现如下：

```python
def cs_classes(post):
    """
    Returns strings that look like a Berkeley CS class,
    starting with "CS", followed by a number, optionally ending with A, B, or C.
    Case insensitive.

    >>> cs_classes("Is it unreasonable to take CS61A, CS61B, CS70, and EE16A in the summer?")
    True
    >>> cs_classes("how do I become a TA for cs61a? that job sounds so fun")
    True
    >>> cs_classes("Can I take ECON101 as a CS major?")
    False
    >>> cs_classes("Should I do the lab lites or regular labs in EE16A?")
    False
    """
    return bool(re.search(r"(CS|cs)\d+[a-cA-C]{1}", post))
```

## 最终测试

使用如下命令进行最终测试：

```shell
python3 ok --score --local
```

结果如下：

```shell
=====================================================================
Assignment: Lab 13
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Scoring tests

---------------------------------------------------------------------
ebnf-grammar
    Passed: 0
    Failed: 0
[k..........] 0.0% passed

---------------------------------------------------------------------
Doctests for roman_numerals

>>> from lab13 import *
>>> roman_numerals("Sir Richard IIV, can you tell Richard VI that Richard IV is on the phone?")
['IIV', 'VI', 'IV']
>>> roman_numerals("My TODOs: I. Groceries II. Learn how to count in Roman IV. Profit")
['I', 'II', 'IV']
>>> roman_numerals("I. Act 1 II. Act 2 III. Act 3 IV. Act 4 V. Act 5")
['I', 'II', 'III', 'IV', 'V']
>>> roman_numerals("Let's play Civ VII")
['VII']
>>> roman_numerals("i love vi so much more than emacs.")
[]
>>> roman_numerals("she loves ALL editors equally.")
[]
Score: 1.0/1

---------------------------------------------------------------------
Doctests for calculator_ops

>>> from lab13 import *
>>> calculator_ops("(* 2 4)")
['* 2 4']
>>> calculator_ops("(+ (* 3 (+ (* 2 4) (+ 3 5))) (+ (- 10 7) 6))")
['* 2 4', '+ 3 5', '- 10 7']
>>> calculator_ops("(* 2)")
[]
Score: 1.0/1

---------------------------------------------------------------------
Doctests for cs_classes

>>> from lab13 import *
>>> cs_classes("Is it unreasonable to take CS61A, CS61B, CS70, and EE16A in the summer?")
True
>>> cs_classes("how do I become a TA for cs61a? that job sounds so fun")
True
>>> cs_classes("Can I take ECON101 as a CS major?")
False
>>> cs_classes("Should I do the lab lites or regular labs in EE16A?")
False
Score: 1.0/1

---------------------------------------------------------------------
Point breakdown
    ebnf-grammar: 0.0/0
    roman_numerals: 1.0/1
    calculator_ops: 1.0/1
    cs_classes: 1.0/1

Score:
    Total: 3.0

Cannot backup when running ok with --local.
```

