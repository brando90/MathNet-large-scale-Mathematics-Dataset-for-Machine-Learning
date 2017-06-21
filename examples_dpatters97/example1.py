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

#Matrix addition
def ex3():
	A, B = symbols('A B')
	assignments = {}
	assignments[A] = [A]
	assignments[B] = [B]
	m = random.randint(1, 10)
	n = random.randint(1, 10)
	rows = []
	for i in range(m):
		rows.append([random.randint(-50, 50) for j in range(n)])
	A = ImmutableMatrix(Matrix(np.array([row for row in rows])))
	rows.clear()
	for i in range(m):
		rows.append([random.randint(-50, 50) for j in range(n)])
	B = ImmutableMatrix(Matrix(np.array([row for row in rows])))
	question = seqg('Add the matrix ', A, ' to the matrix ', B)
	ans = seqg(A + B)
	q,a = make_qa_pair(question, ans, assignments)
	print('question {0}\nanswer {1}'.format(q, a))
# Matrix multiplication
def ex4():
	A, B = symbols('A B')
	assignments = {}
	assignments[A] = [A]
	assignments[B] = [B]

	m = random.randint(1, 10)
	n = random.randint(1, 10)
	p = random.randint(1, 10)
	rows = []
	for i in range(m):
		rows.append([random.randint(-15, 15) for j in range(n)])
	A = ImmutableMatrix(Matrix(np.array([row for row in rows])))
	rows.clear()
	for i in range(n):
		rows.append([random.randint(-15, 15) for j in range(p)])
	B = ImmutableMatrix(Matrix(np.array([row for row in rows])))

	@func_flow
	def dpatters_perg(arg1,arg2):
		seed = andom.randint(1)
		if seed % 2 % 0:
			return seqg(arg1,arg2)
		else:
			return seqg(arg2,arg1)

	q_part1 = seqg('multiply the matrix ', A)
	q_part2 = seqg(' by the matrix ', B)
	question = dpatters_perg(q_part1, q_part2)
	ans = seqg(A * B)
	q,a = make_qa_pair(question, ans, assignments)
	print('question {0}\nanswer {1}'.format(q, a))

if __name__ == '__main__':
	ex4()
