# Week12

`CS 61A 2021 Fall`官网：[CS 61A: Structure and Interpretation of Computer Programs](https://inst.eecs.berkeley.edu/~cs61a/sp21/)

`翻译视频`：[【计算机程序的构造和解释】精译【UC Berkeley 公开课-CS61A (Spring 2021)】-中英双语字幕](https://www.bilibili.com/video/BV1v64y1Q78o/?spm_id_from=444.41.top_right_bar_window_default_collection.content.click&vd_source=249a8ad55bb26717dd55ec3dd295f644)

`github`:[Maxwell2020152049/CS61A](https://github.com/Maxwell2020152049/CS61A)

## Lecture 27: Interpretating Scheme

`Slide`：[27-Interpreters_full.pdf](https://inst.eecs.berkeley.edu/~cs61a/sp21/assets/slides/27-Interpreters_full.pdf)

`Lab`：[Lab 11: Interpreters](https://inst.eecs.berkeley.edu/~cs61a/sp21/lab/lab11/)

## Lecture #28: The Halting Problem and Incompleteness

`Slide`：[28-Undecidability_full.pdf](https://inst.eecs.berkeley.edu/~cs61a/sp21/assets/slides/28-Undecidability_full.pdf)

`Project`：[Project 4: Scheme Interpreter](https://inst.eecs.berkeley.edu/~cs61a/sp21/proj/scheme/)

##  Lecture #29: Defining Syntax—Macros

`Slide`：[29-Macros_full.pdf](https://inst.eecs.berkeley.edu/~cs61a/sp21/assets/slides/29-Macros_full.pdf)

`Homework`：[Homework 8: More Scheme](https://inst.eecs.berkeley.edu/~cs61a/sp21/hw/hw08/)

### Macros in Scheme

```scheme
scm> (define L '(1 2 3))
l
```

```scheme
scm> L
(1 2 3)
```

逗号表达式`,`和`Python`中`f-string`的`{}`一样，可以计算名称的值。

```scheme
scm> `(a b ,L)
(a b (1 2 3))
```

`@`可以把一个列表插入另一个列表。

```scheme
scm> `(a b ,@L)
(a b 1 2 3)
```

```scheme
scm> `(a b ,@(cdr L) d)
(a b 2 3 d)
```

