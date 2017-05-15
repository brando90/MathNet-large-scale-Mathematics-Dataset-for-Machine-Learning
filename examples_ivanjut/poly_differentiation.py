from sympy import *
import random

from qaflow import *
from qaflow.question_answer import *


# GENERAL POLYNOMIAL DIFFERENTIATION

def example1():

    # Differentiate the following expression x**b with respect to x, where a is a constant.
    # Differentiate x**b with respect to x, where a is a constant.

    x, y, a, b, X = symbols('x y a b X')
    e, f, g, h = symbols('e f g h')
    expression = x**b
    question = seqg('differentiate the following expression ', expression, 'with respect to', x)
    replacements = {}
    replacements[x] = [x, y, a, X, e, f, g, h]
    replacements[b] = [i for i in range(100)]
    answer = choiceg(diff(x**b, x))
    q,a = make_qa_pair(question, answer, replacements, seed=3)
    print('question: %s \nanswer: %s' % (q, a))


def example2():

    # Differentiate the following expression x**b + x**c + d with respect to x, where b, c, d are constants.
    # Differentiate x**b + x**c + d with respect to x, where b, c, d are constants.

    x, y, a, b, X = symbols('x y a b X')
    e, f, g, h, c, d = symbols('e f g h c d')
    expression = x**b + x**c + d
    question = seqg('differentiate the following expression ', expression, 'with respect to', x)
    replacements = {}
    replacements[x] = [x, y, a, X, e, f, g, h]
    replacements[b] = [i for i in range(100)]
    replacements[c] = [j for j in range(50)]
    replacements[d] = [k for k in range(200)]
    answer = choiceg(diff((x**b + x**c + d), x))
    q,a = make_qa_pair(question, answer, replacements, seed=1)
    print('question: %s \nanswer: %s' % (q, a))


def example3():

    # Differentiate the following expression x**b + x**c + d with respect to x, where b, c, d are constants.
    # Differentiate perg(x**b + x**c + d) with respect to x, where b, c, d are constants.

    x, y, a, b, X = symbols('x y a b X')
    e, f, g, h, c, d = symbols('e f g h c d')
    expression = perg(x**b, '+', x**c, '+', d)
    question = seqg('differentiate the following expression ', expression, 'with respect to', x)
    replacements = {}
    replacements[x] = [x, y, a, X, e, f, g, h]
    replacements[b] = [i for i in range(100)]
    replacements[c] = [j for j in range(50)]
    replacements[d] = [k for k in range(200)]
    answer = choiceg(diff((x**b + x**c + d), x))
    q,a = make_qa_pair(question, answer, replacements, seed=1)
    print('question: %s \nanswer: %s' % (q, a))


if __name__ == '__main__':
    # example1()
    # example2()
    example3()