from sympy import *
import random

from qaflow import *
from qaflow.question_answer import *


def example1():

    # Differentiate the following expression x**2 + y + 1 with respect to x.
    # Differentiate x**2 + y + 1 with respect to x.

    x, y, a,b, X = symbols('x y a b X')
    e,f,g,h = symbols('e f g h')
    expression = x**2 + y + 1
    question = seqg('Differentiate the following expression ', expression, 'with respect to ', x)
    replacements = {}
    replacements[x] = [x, a, b, X]
    replacements[y] = [e, f, g, h]
    answer = choiceg(diff(expression, x))
    q,a = make_qa_pair(question, answer, replacements, seed=4)
    print('question: %s \nanswer: %s'%(q,a))


def example2():

    # Differentiate a complicated function with respect to y.
    # Differentiate x**3*y**4 + x*y + y**(1/2)*x*z + z**2 with respect to y.

    x, y, a, b, e, f, g, h, z = symbols('x y a b e f g h z')
    expression = x**3*y**4 + x*y + y**(1/2)*x*z + z**2
    question = seqg('Differentiate the following expression ', expression, 'with respect to ', y)
    replacements = {}
    replacements[x] = [x, a, b]
    replacements[y] = [y, g, h]
    replacements[z] = [z, e, f]
    answer = choiceg(diff(expression, y))
    q, a = make_qa_pair(question, answer, replacements, seed=3)
    print('Question: %s \nAnswer: %s' % (q, a))


if __name__ == '__main__':
    # example1()
    example2()
