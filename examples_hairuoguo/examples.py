# examples for hairuoguo
from sympy import *
import random

from qaflow import *
from qaflow.question_answer import *


#word problem 1

def example():

    assignments = {}
    x, y, a, b, X = symbols('x y a b X')
    Ve,f,g,h = symbols('e f g h')
    ## solve x,  a = b,  x = 2*b, a = 8, can you do it?
    #first possible syntax using + for seqg
    question = seqg() + 'solve' + x +  Eq(a,b)/Eq(x,2*b)/Eq(a,8) + ' can you do it?'
    #question = seqg(Eq(a,b)) 
    #second possible syntax for using >
    '''
    question = solve > x >  Eq(a,b)/Eq(x,2*b)/Eq(a,8) >'can you do it?'
    #third possible syntax using + for seqg
    question = solve + x +  perg( Eq(a,b),Eq(x,2*b),Eq(a,8)) + 'can you do it?'
    '''
    print(question.execute(assignments= {x: [g]}))
if __name__ == '__main__':
    example()
