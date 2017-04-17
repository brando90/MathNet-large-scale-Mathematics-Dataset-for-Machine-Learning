#from require import require
import unittest
from sympy import *
import numpy as np
import random

from qaflow import *
from qaflow.question_answer import *

class Test_problem(unittest.TestCase):

    def ans_with_sympy(self,x,two,eight):
        ans = seqg(x, ' = ', two*eight )
        return ans

    def ans_with_delayed_multiplication(self,x):
        ##
        @func_flow
        def my_mult(a,b):
            return a*b
        ans = seqg(x, ' = ', seqg( my_mult(2,8) ) )
        return ans

    def ans_with_string(self,x):
        ans = seqg(x,' = ',2,'*',8)
        return ans

    def ans_with_delayed_and_straight_mult(self,x):
        explicit_mul = self.ans_with_string(x)
        @func_flow
        def my_mult(a,b):
            return a*b
        evaluated_mul = seqg( my_mult(2,8) )
        ans = seqg( explicit_mul,' = ', evaluated_mul )
        return ans

    ##

    def test_ans_with_sympy(self):
        x,y,a,b, X = symbols('x y a b X')
        e,f,g,h = symbols('e f g h')
        two, eight = symbols('2 8')
        ## solve x,  a = b,  x = 2*b, a = 8, can you do it?
        question = seqg(seqg('solve ',x,', '), seqg( seqg(Eq(a,b),', ') , seqg(Eq(x,two*b),', ') , seqg(Eq(a,eight),', ') ), 'can you do it?')
        ## pssible alternative assignments for symbols
        assignments = {}
        assignments[a] = [a,e,f,g,h]
        assignments[x] = [x,X]
        assignments[eight] = [1,2,3,4,5,6,7,8]
        ## possible answer(s)
        ans1 = self.ans_with_sympy(two,eight)
        ## generator for a choice of answer
        answer = choiceg( ans1 )
        q,a = make_qa_pair(question,answer,assignments)
        print('question: %s \n answer %s \n'%(q,a))

    def test_example_subs_seq_mutliple_choices(self):
        x,y,a,b, X = symbols('x y a b X')
        e,f,g,h = symbols('e f g h')
        ## solve x,  a = b,  x = 2*b, a = 8, can you do it?
        question = seqg(seqg('solve ',x,', '), seqg( seqg(Eq(a,b),', ') , seqg(Eq(x,2*b),', ') , seqg(Eq(a,8),', ') ), 'can you do it?')
        ## pssible alternative assignments for symbols
        assignments = {}
        assignments[a] = [a,e,f,g,h]
        assignments[x] = [x,X]
        assignments[8] = [random.randint(0,200) for i in range(100)]
        ## possible answer(s)
        ans1 = self.ans_with_string(x)
        ans2 = self.ans_with_delayed_multiplication(x)
        ans3 = self.ans_with_delayed_and_straight_mult(x)
        ## generator for a choice of answer
        answer = choiceg( ans1,ans2,ans3 )
        q,a = make_qa_pair(question,answer,assignments)
        print('question: %s \nanswer %s'%(q,a))

if __name__ == '__main__':
    unit_test = Test_problem()
    #unittest.main()
    unit_test.test_example_subs_seq_mutliple_choices()
