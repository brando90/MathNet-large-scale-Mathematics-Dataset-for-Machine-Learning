from sympy import *
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

if __name__ == '__main__':
	ex1()
