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

def example3():
    a,b,c,x = symbols('a b c x')
    wrt = perg('wrt','w.r.t.','with respect to ')
    expr = a**2+b**2+c**2
    question = seqg('Do derivative of ',expr,wrt,x)
    assignments = {}
    assignments[x] = [a,b,c]
    def my_derivative(expr,x):
        return diff(expr,x)
    derivative_ans = DelayedExecution(my_derivative,expr,x)
    answer = choiceg(derivative_ans)
    q,a = make_qa_pair(question,answer,assignments)
    print('question: %s \nanswer: %s'%(q,a))

if __name__ == '__main__':
    example3()
