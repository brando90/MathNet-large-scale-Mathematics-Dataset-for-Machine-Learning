from sympy import *
import random

from qaflow import *
from qaflow.question_answer import *


# GENERAL POLYNOMIAL DIFFERENTIATION

def example_replacements(seed=1):
    # Differentiate the following expression sum^n_{i=1} a_i x^i with respect to x^i where a_i are constant coefficients
    n = random.randint(1,10)
    x, y, X, e, f, g, h = symbols('x y X e f g h')
    a = [ symbols( 'a'+str(i) ) for i in range(n+1)]
    poly = 0
    for i in range(n+1): #from 0 to n inclusive
        #poly = poly + a[i]*power(x,i)
        poly = poly + a[i]*(x**i)
    # Question
    question = seqg('differentiate the following expression ', poly, 'with respect to', x)
    # Replacements
    replacements = {}
    replacements[x] = [x, y, a, X, e, f, g, h]
    #replacements[b] = [i for i in range(100)]
    # Answer
    answer = choiceg(diff(poly,x))
    q,a = make_qa_pair(question, answer, replacements, seed=seed)
    print('question: %s \nanswer: %s' % (q, a))


if __name__ == '__main__':
    seed = random.randint(1,10)
    print('seed = ', seed)
    example_replacements(seed)
