from sympy import *
import random

from qaflow import *
from qaflow.question_answer import *


def example1():

    # Differentiate the following expression x**2 + x + 1 with respect to x.
    # Differentiate x**2 + x + 1 with respect to x.

    x,y,a,b, X = symbols('x y a b X')
    e,f,g,h = symbols('e f g h')
    expression = x**2 + x + 1
    question = seqg('differentiate the following expression ', expression, 'with respect to ', x)
    replacements = {}
    replacements[x] = [x, y, a, b, X, e, f, g, h]

    answer = choiceg(diff(expression))
    q,a = make_qa_pair(question, answer, replacements, seed=2)
    print('question: %s \nanswer: %s'%(q,a))


def example2():

    # Differentiate the following expression x**2 + x + 1 with respect to x.
    # Differentiate perg(x**2 + x + 1) with respect to x.

    x, y, a, b, X = symbols('x y a b X')
    e, f, g, h = symbols('e f g h')
    expression = perg(x**2, '+', x, '+', 1)
    question = seqg('differentiate the following expression ', expression, 'with respect to ', x)
    replacements = {}
    replacements[x] = [x, y, a, b, X, e, f, g, h]

    answer = choiceg(diff(x**2 + x + 1))
    q,a = make_qa_pair(question, answer, replacements, seed=4)
    print('question: %s \nanswer: %s'%(q,a))


def example3():

    # differentiate the following expression x**3 + x**2 + x + 1 with respect to x.
    # differentiate perm(x**3 + x**2 + x + 1) with respect to x.

    x,y,a,b, X = symbols('x y a b X')
    e,f,g,h = symbols('e f g h')
    expression = perg(x**3, '+', x**2, '+', x, '+', 1)
    question = seqg('differentiate the following expression ', expression, 'with respect to', x)
    replacements = {}
    replacements[x] = [x, y, a, b, X, e, f, g, h]
    answer = choiceg(diff(x**3 + x**2 + x + 1))
    q,a = make_qa_pair(question, answer, replacements, seed=1)
    print('question: %s \nanswer: %s' % (q, a))


if __name__ == '__main__':
    # example1()
    # example2()
    example3()
