from sympy import *
import random

from qaflow import *
from qaflow.question_answer import *

def example1():
    ## Make x the subject, expr
    a,b,c = symbols('a b c')
    expr = Eq(a + b, c)
    question = seqg('Make ', c, ' the subject in the following expression: ', expr)
    @func_flow
    def solve_this(expr,b):
        return solve(expr,b)[0]
    answer = choiceg( solve_this(expr,b) )
    q,a = make_qa_pair(question,answer,seed=3)
    print('question: %s \nanswer: %s'%(q,a))

def example2():
    ## Make x the subject, expr
    a,b,c = symbols('a b c')
    expr = Eq(a + b, c)
    question = seqg('Make ', c, ' the subject in the following expression: ', expr)
    solve_this = DelayedExecution(lambda expr, b: solve(expr,b)[0],expr,b)
    ans1 = solve_this
    ans2 = seqg(b,' = ',solve_this)
    answer = choiceg( ans1, ans2 )
    q,a = make_qa_pair(question,answer,seed=3)
    print('question: %s \nanswer: %s'%(q,a))

if __name__ == '__main__':
    example2()
