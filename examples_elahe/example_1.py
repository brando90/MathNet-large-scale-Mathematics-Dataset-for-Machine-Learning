from sympy import *
import random

from qaflow import *
from qaflow.question_answer import *

def example1():
    # 'Find velocity of the object that moves from, x0=0 to x1=1 (m) in time frame of t0 = 0 to t1=1.
    x0, x1, t0, t1 = symbols('x0 x1 t0 t1')
    # addition of matrices'
    question = seqg('Find velocity of the object that moves from ,', Eq(x0,3), 'to ', Eq(x1 , 4), '(m) in time frame of ', Eq(t0,1), ' to ', Eq(t1 ,2),'.')

    # @func_flow
    # def vel(x1,x0,t1,t0):
    #     if t1-t0 == 0:
    #         return "Undefined"
    #     else:
    #         return (x1-x0)/(t1-t0)
    @func_flow
    def vel(x1,x0,t1,t0):
        return (x1-x0)/(t1-t0)

    #answer = seqg( (x1-x0)/(t1-t0) )
    #answer = vel(3,4,1,2)
    answer = vel(x1,x0,t1,t0)
    replacements = {}
    #pdb.set_trace()
    replacements[1] = [random.randint(0,200) for i in range(100)]
    replacements[2] = [random.randint(0,200) for i in range(100)]
    replacements[3] = [random.randint(0,200) for i in range(100)]
    replacements[4] = [random.randint(0,200) for i in range(100)]
    #answer = seqg( 'rubush' )
    #q,a = make_qa_pair(question, answer, seed=1)
    q,a = make_qa_pair(question,answer,replacements)
    print('question: %s \n answer: %s' %(q,a))

def example2():
    #source activate eit_env
    pass

if __name__ == '__main__':
    example1()
