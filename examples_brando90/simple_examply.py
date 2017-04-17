from sympy import *
import random

from qaflow import *
from qaflow.question_answer import *

x,y,a,b = symbols('x y a b')

def example1():
    ## solve x,  a = b,  x = 2*b, a = 8, can you do it?
    question = seqg('solve x ,', perg( 'a = b, ' , 'x = 2*b, ' , 'x = 8, ' ),'can you do it?')
    answer = choiceg( 'x = 2*8', 'x = 16', 'x = 2*8 = 16' )
    q,a = make_qa_pair(question,answer,seed=3)
    print('question: %s \nanswer: %s'%(q,a))

def example2():
    x,y,a,b, X = symbols('x y a b X')
    e,f,g,h = symbols('e f g h')
    ## solve x,  a = b,  x = 2*b, a = 8, can you do it?
    question = seqg(seqg('solve ',x,', '), seqg( seqg(Eq(a,b),', ') , seqg(Eq(x,2*b),', ') , seqg(Eq(a,8),', ') ), 'can you do it?')
    ## pssible alternative assignments for symbols
    assignments = {}
    assignments[a] = [a,e,f,g,h]
    assignments[x] = [x,X]
    assignments[8] = [random.randint(0,200) for i in range(100)]
    ## generator for a choice of answer
    ans1 = seqg(x,' = ',2,'*',8)
    ans2 = seqg(x,'=',2,'*',8)
    answer = choiceg( ans1,ans2 )
    q,a = make_qa_pair(question,answer,assignments,seed=4)
    print('question: %s \nanswer: %s'%(q,a))


def example3():
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
    ans1 = seqg(x,' = ',2,'*',8)
    ans2 = seqg(x,'=',2,'*',8)
    ans3 = DelayedExecution(lambda a,b: a*b,2,8)
    @func_flow
    def my_mult(a,b):
        return a*b
    ans4 = seqg(x, ' = ', seqg( my_mult(2,8) ) )
    ## generator for a choice of answer
    answer = choiceg( ans1,ans2,ans3,ans4 )
    q,a = make_qa_pair(question,answer,assignments,seed=5)
    print('question: %s \nanswer: %s'%(q,a))

if __name__ == '__main__':
    #example1()
    #example2()
    example3()
