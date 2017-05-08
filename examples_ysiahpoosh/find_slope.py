from sympy import * 
import random

from qaflow import * 
from qaflow.question_answer import *

x,y,a,b = symbols('x y a b')

def example1():
	#What is the slope of the line through two points 
	question = seqg('What is the slope of the line through the following points: ', perg(seqg('(', 1, ',', 2, ')'),seqg('(', 3, ',', 4, ')') ), '?')

	#possible assignments for numbers
	assignments = {}
	for i in range(1,5):
		assignments[i] = [random.randint(-10,10) for j in range(100)]

	def find_slope(a,b,c,d):
		if c-a == 0:
			return 0
		return (d-b)/(c-a)

	#ans1 = DelayedExecution(lambda a,b,c,d: str(d-b) + '/' + str(c-a), 1,2,3,4) 
	ans2 = DelayedExecution(lambda a,b,c,d: find_slope(a,b,c,d), 1,2,3,4)
	answer = choiceg(ans2)
	q,a = make_qa_pair(question, answer, assignments, seed=3)
	print('question: %s \nanswer: %s'%(q,a))


def example2():
	#What is the slope of the line through two points 
	question = seqg('What is the slope of the line through the following points: ', perg(seqg('(', 1, ',', 2, ')'),seqg('(', 3, ',', 4, ')') ), '?')

	#possible assignments for numbers
	assignments = {}
	for i in range(1,5):
		assignments[i] = [random.randint(-10,10) for j in range(100)]

	@func_flow
	def find_slope(a,b,c,d):
		if c-a == 0:
			return "undefined"
		return (d-b)/(c-a)

	@func_flow
	def slope_as_frac(a,b,c,d):
		if c-a == 0:
			return "undefined"
		return Rational(d-b, c-a)

	ans1 = find_slope(1,2,3,4)
	ans2 = slope_as_frac(1,2,3,4)
	answer = choiceg(ans1, ans2)
	q,a = make_qa_pair(question, answer, assignments, seed=3)
	print('question: %s \nanswer: %s'%(q,a))

if __name__=='__main__':
	#example1()
	example2()

