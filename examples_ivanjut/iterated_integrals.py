from sympy import *
import random

from qaflow import *
from qaflow.question_answer import *


# Examples involving 2 or 3 iterated integrals.


def example1():
    # Let R be the rectangle [1, 2] x [3, 5] in x y coordinates.
    # Calculate the integral over the region R of the function x*y**2.

    x, y, a, b, c, d, e, f, g, h = symbols('x y a b c d e f g h')
    expression = x * y**2
    region = seqg('Let R be the rectangle [1, 2] x [3, 5] in', x, y, 'coordinates.')
    compute = seqg('Calculate the integral over the region R of the function ', expression, '.')
    question = perg(region, compute)

    replacements = {}
    replacements[x] = [x, a, b, c, d]
    replacements[y] = [y, e, f, g, h]

    answer = choiceg(integrate(expression, (x, 1, 2), (y, 3, 5)))

    q, a = make_qa_pair(question, answer, replacements, seed=1)
    print('Question: %s \nAnswer: %s' % (q, a))


def example2():
    # Let R be the rectangle [a, b] x [c, d] in x, y coordinates.
    # Calculate the integral over the region R of the function x**2 * y**3.

    x, y, a, b, c, d = symbols('x y a b c d')
    expression = x**2 * y**3
    region = seqg('Let R be the rectangle [', a, ',', b, '] x [', c, ',', d, '] in x, y coordinates.')
    compute = seqg('Calculate the integral over the region R of the function ', expression, '.')
    question = perg(region, compute)

    replacements = {}
    replacements[a] = [random.randint(-5, 5)]
    replacements[b] = [random.randint(-5, 5)]
    replacements[c] = [random.randint(-5, 5)]
    replacements[d] = [random.randint(-5, 5)]

    answer = choiceg(integrate(expression, (x, a, b), (y, c, d)))

    q, a = make_qa_pair(question, answer, replacements, seed=5)
    print('Question: %s \nAnswer: %s' % (q, a))


def example3():
    # Compute the integral over [0, 2] x [0, 1] of the function e**(x+y).

    x, y, a, b, c, d = symbols('x y a b c d')
    expression = exp(x + y)
    question = seqg('Compute the integral over [0, 2] x [0, 1] of the function ', expression, '.')

    replacements = {}
    replacements[x] = [x, a, b]
    replacements[y] = [y, c, d]

    answer = choiceg(integrate(expression, (x, 0, 2), (y, 0, 1)))

    q, a = make_qa_pair(question, answer, replacements, seed=1)
    print('Question: %s \nAnswer: %s' % (q, a))


def example4():
    # Let V be the volume defined by [1, 5] x [2, 3] x [0, 4] in x, y, z coordinates.
    # Compute the integral over the volume V of the function x**2 + y**2 + z**2.

    x, y, z, a, b, c, d, e, f = symbols('x y z a b c d e f')
    expression = x**2 + y**2 + z**2
    volume = seqg('Let V be the volume defined by [1, 5] x [2, 3] x [0, 4] in ', x, ',', y, ',', z, 'coordinates.')
    compute = seqg('Compute the integral over the volume V of the function ', expression, '.')
    question = perg(volume, compute)

    replacements = {}
    replacements[x] = [x, a, b]
    replacements[y] = [y, c, d]
    replacements[z] = [z, e, f]

    answer = choiceg(integrate(expression, (x, 1, 5), (y, 2, 3), (z, 0, 4)))

    q, a = make_qa_pair(question, answer, replacements, seed=4)
    print('Question: %s \nAnswer: %s' % (q, a))


def example5():
    # Let V be the volume [a, b] x [c, d] x [e, f] in xyz coordinates.
    # Calculate the integral over the volume V of the function x**2 + y**2 + z**2.

    x, y, z, a, b, c, d, e, f = symbols('x y z a b c d e f')
    expression = x**2 + y**2 + z**2
    region = seqg('Let V be the volume [', a, ',', b, '] x [', c, ',', d, '] x [', e, ',', f, '] in xyz coordinates.')
    compute = seqg('Calculate the integral over the volume V of the function ', expression, '.')
    question = perg(region, compute)

    replacements = {}
    replacements[a] = [random.randint(-5, 5)]
    replacements[b] = [random.randint(-5, 5)]
    replacements[c] = [random.randint(-5, 5)]
    replacements[d] = [random.randint(-5, 5)]
    replacements[e] = [random.randint(-5, 5)]
    replacements[f] = [random.randint(-5, 5)]

    answer = choiceg(integrate(expression, (x, a, b), (y, c, d), (z, e, f)))

    q, a = make_qa_pair(question, answer, replacements, seed=5)
    print('Question: %s \nAnswer: %s' % (q, a))


if __name__ == '__main__':
    # example1()
    # example2()
    # example3()
    # example4()
    example5()
