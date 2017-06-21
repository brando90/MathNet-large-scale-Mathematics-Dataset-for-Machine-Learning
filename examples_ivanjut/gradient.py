from sympy import *
import random

from qaflow import *
from qaflow.question_answer import *


# Ivan Jutamulia


def example1():
    # Find the gradient vector for the function x**3 * y**2 + x**-1 * y**5

    x, y, a, b, c, d = symbols('x y a b c d')
    expression = x**3 * y**2 + 1/x * y**5
    question = seqg('Find the gradient vector for the function ', expression, '.')

    replacements = {}
    replacements[x] = [x, a, b]
    replacements[y] = [y, c, d]

    partial_x = diff(expression, x)
    partial_y = diff(expression, y)
    answer = choiceg((partial_x, partial_y))

    q, a = make_qa_pair(question, answer, replacements, seed=1)
    print('Question: %s \nAnswer: %s' % (q, a))


if __name__ == '__main__':
    example1()
