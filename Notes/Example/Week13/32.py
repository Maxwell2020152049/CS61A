# A Simple Calculator Using Scheme Syntax.

# Implemented using the Lark package in Python.

import sys
from lark import Lark, Transformer


grammar = """
    start: calc_expr
    ?calc_expr : NUMBER | calc_op
    calc_op: "(" OPERATOR calc_expr* ")"
    OPERATOR: "+" | "-" | "*" | "/"

    %ignore /\s+/
    %import common.NUMBER
"""

parser = Lark(grammar)


from functools import reduce
from operator import mul, truediv

# The Transformer class defines the .transform method, which produces a
# transformed tree by applying its methods to each node of the tree, bottom
# up, replacing each node with the value returned by applying to it the method
# whose name is the type of node (the .data field of a Tree node and the
# .type field of a (leaf) Token node.)  Any node whose type is not among the
# method names is left unchanged.  The .transform method is non-destructive:
# the tree is essntially reconstructed with new values for transformed nodes.

class Eval(Transformer):
    def start(self, args):
        return args[0]

    def calc_op(self, args):
        op = args[0]
        operands = args[1:]
        if op == '+':
            return sum(operands)
        elif op == '-':
            if len(operands) == 1:
                return -operands[0]
            else:
                return operands[0] - sum(operands[1:])
        elif op == '*':
            return reduce(mul, operands)
        elif op == '/':
            return reduce(truediv, operands)

    def NUMBER(self, num):
        return float(num)
    
evaluator = Eval()

def read_eval_print():
    while True:
        try:
            line = input("calc> ")
            if line.lower() == 'exit' or line.lower() == 'quit':
                return
            tree = parser.parse(line)
            print(evaluator.transform(tree))
        except EOFError:
            sys.exit(0)
        except:
            print(f"Bad input: {line}", file=sys.stderr)

if __name__ == "__main__":
    read_eval_print()
