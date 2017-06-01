from sympy import *
import random

from qaflow import *
from qaflow.question_answer import *

# A few examples relating to dot product of multiple vectors


def example1():
    # Two vectors dot product (two-dimensional)
    # Find the dot product of the the vectors v = (a, b) and u = (c, d)

    a, b, c, d = symbols('a b c d')
    question = seqg('Find the dot product of the following two vectors: (', a, ',', b, ') and (', c, ',', d, ')')
    replacements = {}
    replacements[a] = [random.randint(-10, 10)]
    replacements[b] = [random.randint(-10, 10)]
    replacements[c] = [random.randint(-10, 10)]
    replacements[d] = [random.randint(-10, 10)]
    answer = choiceg(a * c + b * d)
    q, a = make_qa_pair(question, answer, replacements, seed=5)
    print('Question: %s \nAnswer: %s' % (q, a))


def example2():
    # Angle between two vectors
    # Find the angle between the vectors v = (a, b) and u = (c, d)

    a, b, c, d = symbols('a b c d')
    question = seqg('Find the angle between the vectors: (', a, ',', b, ') and (', c, ',', d, ')')
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
    # Determine if two vectors are perpendicular or not
    pass
    # will work on this later


def example4():
    # Find the area of a parallelogram spanned by two vectors
    pass
    # will work on this later

if __name__ == '__main__':
    # example1()
    example2()
    # example3()
    # example4()