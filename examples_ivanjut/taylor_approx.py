from sympy import *
import random

from qaflow import *
from qaflow.question_answer import *

# Finds second-order Taylor approximation for a function


def example1():
    # Second-order Taylor approx of a function
    # Find the second-order Taylor series of the function x**3 * y**4 around the point (1, 1)

    x, y, a, b, e, f, g, h, z, i, j, h, k = symbols('x y a b e f g h z i j h k')
    expression = x**i * y**j
    question = seqg('Find the second-order Taylor series of the function', expression, 'around the point (', x, ',', y, ').')
    replacements = {}
    replacements[x] = [a, b, e, f]
    replacements[y] = [g, h, z]
    replacements[i] = [random.randint(1, 10)]
    replacements[j] = [random.randint(1, 10)]
    replacements[h] = [h]
    replacements[k] = [k]

    partial_x = diff(expression, x)
    partial_y = diff(expression, y)
    partial_xx = diff(partial_x, x)
    partial_xy = diff(partial_x, y)
    partial_yy = diff(partial_y, y)

    solution = expression + partial_x * h + partial_y * k + .5 * partial_xx * h**2 + partial_xy * h * k + .5 * partial_yy * k**2

    answer = choiceg(solution)
    q, a = make_qa_pair(question, answer, replacements, seed=3)
    print('Question: %s \nAnswer: %s' % (q, a))


if __name__ == '__main__':
    example1()

