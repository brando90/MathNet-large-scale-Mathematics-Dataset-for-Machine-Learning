# -*- coding: utf-8 -*-
"""
Created on Mon May 15 22:15:13 2017

@author: Brando is cool
"""

from sympy import *
import random

from qaflow import *
from qaflow.question_answer import *

def example1():
    x,a,b,c,d,e,f,g= symbols('x a b c d e f g')
    expression_q = log(x)**2
    # Can you integrate this:  log(x)**2 expression?
    question = seqg('Can you integrate this: ' , expression_q,' ?')

    assignments = {}
    assignments[x] = [x,a,b,c,d,e,f,g]

    expression_ans = Eq(Integral(log(x)**2, x), Integral(log(x)**2, x).doit() )
    answer = seqg(  expression_ans ) # x⋅log (x) - 2⋅x⋅log(x) + 2⋅x
    q,a = make_qa_pair(question,answer,assignments)
    print('question: %s \nanswer: %s'%(q,a))

if __name__ == '__main__':
    example1()
