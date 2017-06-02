from sympy import *
import random

from qaflow import *
from qaflow.question_answer import *

# A few examples relating to dot product of two vectors (both 2-d and 3-d cases)


def example1():
    # Two vectors dot product (two-dimensional)
    # Find the dot product of the the 2-d vectors v = (a, b) and u = (c, d)

    a, b, c, d = symbols('a b c d')
    question = seqg('Find the dot product of the 2-d two vectors: (', a, ',', b, ') and (', c, ',', d, ')')
    replacements = {}
    replacements[a] = [random.randint(-10, 10)]
    replacements[b] = [random.randint(-10, 10)]
    replacements[c] = [random.randint(-10, 10)]
    replacements[d] = [random.randint(-10, 10)]
    answer = choiceg(a * c + b * d)
    q, a = make_qa_pair(question, answer, replacements, seed=5)
    print('Question: %s \nAnswer: %s' % (q, a))


def example2():
    # Angle between two 2-d vectors
    # Find the angle between the 2-d vectors v = (a, b) and u = (c, d)

    a, b, c, d = symbols('a b c d')
    question = seqg('Find the angle between the 2-d vectors: (', a, ',', b, ') and (', c, ',', d, ')')
    replacements = {}
    replacements[a] = [random.randint(-10, 10)]
    replacements[b] = [random.randint(-10, 10)]
    replacements[c] = [random.randint(-10, 10)]
    replacements[d] = [random.randint(-10, 10)]

    mag_v, mag_u = (a**2 + b**2)**.5, (c**2 + d**2)**.5
    cos_angle = (a * c + b * d)/(mag_v * mag_u)
    angle = acos(cos_angle)

    answer = choiceg(angle)
    q, a = make_qa_pair(question, answer, replacements, seed=6)
    print('Question: %s \nAnswer: %s rad' % (q, a))


def example3():
    # Determine if two 2-d vectors are perpendicular or not
    # Are the 2-d vectors v = (a, b) and u = (c, d) perpendicular to each other?

    a, b, c, d = symbols('a b c d')
    question = seqg('Are the 2-d vectors (', a, ',', b, ') and (', c, ',', d, ') perpendicular to each other?')
    replacements = {}
    replacements[a] = [random.randint(-5, 5)]
    replacements[b] = [random.randint(-5, 5)]
    replacements[c] = [random.randint(-5, 5)]
    replacements[d] = [random.randint(-5, 5)]

    dot = choiceg(a * c + b * d)
    ques, ans = make_qa_pair(question, dot, replacements, seed=5)
    answer = choiceg('Yes' if ans == 0 else 'No')
    q, a = make_qa_pair(question, answer, replacements, seed=4)
    print('Question: %s \nAnswer: %s' % (q, a))


def example4():
    # Two vectors dot product (three-dimensional)
    # Find the dot product of the 3-d vectors v = (a, b, c) and u = (d, e, f)

    a, b, c, d, e, f = symbols('a b c d e f')
    question = seqg('Find the dot product of the following 3-d vectors: (', a, ',', b, ',', c, ') and (', d, ',', e, ',', f, ')')
    replacements = {}
    replacements[a] = [random.randint(-10, 10)]
    replacements[b] = [random.randint(-10, 10)]
    replacements[c] = [random.randint(-10, 10)]
    replacements[d] = [random.randint(-10, 10)]
    replacements[e] = [random.randint(-10, 10)]
    replacements[f] = [random.randint(-10, 10)]

    answer = choiceg(a * d + b * e + c * f)
    q, a = make_qa_pair(question, answer, replacements, seed=5)
    print('Question: %s \nAnswer: %s' % (q, a))


def example5():
    # Determine angle between 3-d vectors
    # Find the angle between the 3-d vectors v = (a, b, c) and u = (d, e, f)

    a, b, c, d, e, f = symbols('a b c d e f')
    question = seqg('Find the angle between the 3-d vectors: (', a, ',', b, ',', c, ') and (', d, ',', e, ',', f, ')')
    replacements = {}
    replacements[a] = [random.randint(-10, 10)]
    replacements[b] = [random.randint(-10, 10)]
    replacements[c] = [random.randint(-10, 10)]
    replacements[d] = [random.randint(-10, 10)]
    replacements[e] = [random.randint(-10, 10)]
    replacements[f] = [random.randint(-10, 10)]

    mag_v, mag_u = (a**2 + b**2 + c**2)**.5, (d**2 + e**2 + f**2)**.5
    cos_angle = (a * d + b * e + c * f)/(mag_v * mag_u)
    angle = acos(cos_angle)

    answer = choiceg(angle)
    q, a = make_qa_pair(question, answer, replacements, seed=6)
    print('Question: %s \nAnswer: %s rad' % (q, a))


def example6():
    # Determine if two 3-d vectors are perpendicular or not
    # Are the 3-d vectors v = (a, b, c) and u = (d, e, f) perpendicular to each other?

    a, b, c, d, e, f = symbols('a b c d e f')
    question = seqg('Are the 3-d vectors (', a, ',', b, ',', c, ') and (', d, ',', e, ',', f, ') perpendicular to each other?')
    replacements = {}
    replacements[a] = [random.randint(-5, 5)]
    replacements[b] = [random.randint(-5, 5)]
    replacements[c] = [random.randint(-5, 5)]
    replacements[d] = [random.randint(-5, 5)]
    replacements[e] = [random.randint(-5, 5)]
    replacements[f] = [random.randint(-5, 5)]

    dot = choiceg(a * d + b * e + c * f)
    ques, ans = make_qa_pair(question, dot, replacements, seed=5)
    answer = choiceg('Yes' if ans == 0 else 'No')
    q, a = make_qa_pair(question, answer, replacements, seed=4)
    print('Question: %s \nAnswer: %s' % (q, a))


if __name__ == '__main__':
    # example1()
    # example2()
    # example3()
    # example4()
    # example5()
    example6()