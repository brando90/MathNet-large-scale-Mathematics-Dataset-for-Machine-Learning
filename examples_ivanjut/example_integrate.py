from sympy import *
import random

from qaflow import *
from qaflow.question_answer import *


def example1():

    # integrate the following expression x**2 + x + 1 with respect to x.
    # integrate x**2 + x + 1 with respect to x.

    x,y,a,b, X = symbols('x y a b X')
    e,f,g,h = symbols('e f g h')
    expression = x**2 + x + 1
    question = seqg('integrate the following expression ', expression, 'with respect to ', x)
    replacements = {}
    replacements[x] = [x,y,a,b,X, e,f,g,h]
    #
    answer = choiceg( integrate(expression) )
    q,a = make_qa_pair(question,answer,replacements,seed=1)
    print('question: %s \nanswer: %s'%(q,a))


def example2():

    # integrate the following expression x**2 + x + 1 with respect to x.
    # integrate perm(x**2 + x + 1) with respect to x.

    x, y, a, b, X = symbols('x y a b X')
    e, f, g, h = symbols('e f g h')
    expression = perg(x**2, '+', x, '+', 1)
    question = seqg('integrate the following expression ', expression, )
    replacements = {}
    replacements[x] = [x,y,a,b,X, e,f,g,h]
    answer = choiceg( integrate(x**2 + x + 1) )
    q,a = make_qa_pair(question,answer,replacements,seed=1)
    print('question: %s \nanswer: %s'%(q,a))


def example3():

    # integrate the following expression x**3 + x**2 + x + 1 with respect to x.
    # integrate perm(x**3 + x**2 + x + 1) with respect to x.

    x,y,a,b, X = symbols('x y a b X')
    e,f,g,h = symbols('e f g h')
    expression = perg(x**3, '+', x**2, '+', x, '+', 1)
    question = seqg('integrate the following expression ', expression, )
    replacements = {}
    replacements[x] = [x,y,a,b,X, e,f,g,h]
    answer = choiceg( integrate(x**3+x**2 + x + 1) )
    q,a = make_qa_pair(question,answer,replacements,seed=1)
    print('question: %s \nanswer: %s'%(q,a))


if __name__ == '__main__':
    # example1()
    # example2()
    example3()
