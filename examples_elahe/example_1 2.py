from sympy import *
import random

from qaflow import *
from qaflow.question_answer import *

def example_1():
    # In this example we try to find a velocity of an object by having its coordination in two different times
    x0, x1, t0, t1 = symbols('x0 x1 t0 t1')
    question = seqg('Find velocity of the object that moves from,',perg( Eq(x0,0) ), 'to ', perg(Eq(x1 , 1), '(m) in time frame of ', perg(Eq(t0,0), ' to ', perg(Eq(t1 ,1),'.')
    answer = (x1-x0)/(t1-t0)
    q,a = make_qa_pair(question, answer, seed = 1))
    print('question: %s \n answer: %s' %(q,a)))



if __name__ == '__main__':
    example_1()
