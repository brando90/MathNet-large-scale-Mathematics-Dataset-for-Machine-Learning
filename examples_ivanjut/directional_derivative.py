from sympy import *
import random

from qaflow import *
from qaflow.question_answer import *

# Compute the directional derivative


def example1():
    # Let f = x**2 + x*y + y**2. Let u = (-3/5, 4/5).
    # Find the directional derivative of f in the u direction at the point (x, y).

    x, y, a, b, c, d, u, v, w = symbols('x y a b c d u v w')

    expression = x**2 + x*y + y**2
    function = seqg('Let f = ', expression, '.')
    vector = seqg('Let ', u, '= (-3/5, 4/5).')
    compute = seqg('Find the directional derivative of f in the ', u, 'direction at the point (', x, ',', y, ').')
    givens = perg(function, vector)

    question = seqg(givens, compute)

    replacements = {}
    replacements[x] = [a, b]
    replacements[y] = [c, d]
    replacements[u] = [v, w]

    partial_x = diff(expression, x)
    partial_y = diff(expression, y)
    ans = partial_x * -3/5 + partial_y * 4/5

    answer = choiceg(ans)
    q, a = make_qa_pair(question, answer, replacements, seed=3)
    print('Question: %s \nAnswer: %s' % (q, a))


def example2():
    # Let f(x, y) = x**a + x*y + y**b. Let u = (c, d).
    # Compute the directional derivative of f in the u direction at the point (x, y).

    x, y, a, b, c, d, u = symbols('x y a b c d u')

    expression = x**a + x*y + y**b
    function = seqg('Let f(x, y) = ', expression, '.')
    vector = seqg('Let u = (', c, ',', d, ').')
    compute = seqg('Find the directional derivative of f in the u direction at the point (x, y).')
    givens = perg(function, vector)

    question = seqg(givens, compute)

    replacements = {}
    replacements[a] = [random.randint(1, 10)]
    replacements[b] = [random.randint(1, 10)]
    replacements[c] = [random.randint(-5, 5)]
    replacements[d] = [random.randint(-5, 5)]

    partial_x = diff(expression, x)
    partial_y = diff(expression, y)
    magnitude = (c**2 + d**2) ** 0.5
    unit = (c/magnitude, d/magnitude)
    ans = partial_x * unit[0] + partial_y * unit[1]

    answer = choiceg(ans)
    q, a = make_qa_pair(question, answer, replacements, seed=3)
    print('Question: %s \nAnswer: %s' % (q, a))

if __name__ == '__main__':
    # example1()
    example2()