from sympy import *
import numpy as np
import random

from qaflow import *
from qaflow.question_answer import *

def ex1():
	x, a, b = symbols('x a b')
	assignments = {}
	assignments[x] = [a, b, x]

	expr = x**2
	question = seqg('Find derivative of ', expr, 'with respect to ', x)
	@func_flow
	def solve_deriv(ex, resp):
		return diff(ex, resp)
	ans = choiceg(solve_deriv(expr, x))
	q,a = make_qa_pair(question, ans, assignments)
	print('question {0}\nanswer{1}'.format(q, a))
def ex2():
    A, B, C, D = symbols('A B C D')
    assignments = {}
    assignments[A] = [A, B, C, D]
    'for the matrix A, find a basis for the image and kernel'
    r1 = []
    r2 = []
    r3 = []
    for i in range(3):
        r1.append(random.randint(1, 10))
        r2.append(random.randint(1, 10))
        r3.append(random.randint(1, 10))
    #A = ImmutableMatrix([[1,3,6],[1,2,5],[1,1,4]])
    A = ImmutableMatrix(Matrix(np.array([r1, r2, r3])))
    question = perg(seqg('for the matrix A=', A), 'for the image')
    ans = choiceg(seqg('image =', A.columnspace()))
    q,a = make_qa_pair(question, ans, assignments)
    print('question {0}\nanswer {1}'.format(q, a))
    

if __name__ == '__main__':
	ex2()
