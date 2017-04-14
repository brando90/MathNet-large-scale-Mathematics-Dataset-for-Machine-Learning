import unittest
from sympy import *
import numpy as np
import random

from funcflow import *

def make_qa_pair(question,answer,assigments):
    new_assigments = { key: [random.sample(value,1)[0]] for key,value in assigments.items() }
    q = question.execute(new_assigments)
    a = answer.execute(new_assigments)
    print(q)
    print(a)

class Test_problem(unittest.TestCase):

    def test_example_subs_seq(self):
        x,y,a,b, X = symbols('x y a b X')
        e,f,g,h = symbols('e f g h')
        ## solve x,  a = b,  x = 2*b, a = 8, can you do it?
        question = seqg(seqg('solve ',x,', '), seqg( seqg(Eq(a,b),', ') , seqg(Eq(x,2*b),', ') , seqg(Eq(a,8),', ') ),'can you do it?')
        assigments = {a:[e,f,g,h],x:[x,X],8:[random.randint(0,200) for i in range(100)] }
        ##
        @func_flow
        def my_mult(a,b):
            return a*b
        ans1 = seqg(x, ' = ', 2,'*',8)
        ans2 = seqg(x, ' = ', seqg( my_mult(2,8) ) )
        #
        answer = choiceg( ans1 )
        make_qa_pair(question,answer,assigments)
        answer = choiceg( ans2 )
        make_qa_pair(question,answer,assigments)
        answer = choiceg( ans1,ans2 )
        make_qa_pair(question,answer,assigments)

if __name__ == '__main__':
    unit_test = Test_problem()
    #unittest.main()
    unit_test.test_example_subs_seq()
