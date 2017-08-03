from sympy import * 
import random

from qaflow import * 
from qaflow.question_answer import *

number, side = symbols('number side')

def example1():
	#Probability of getting all heads or all tails
	question = seqg('A coin is tossed', number, 'times. What is the probability of getting', number, side)

	#possible assignments for numbers
	assignments = {}
	assignments[number] = [random.randint(2, 10)]
	assignments[side] = ['heads', 'tails']

	ans1 = DelayedExecution(lambda a: 1/2**a, number)
	ans2 = DelayedExecution(lambda a: Rational(1, 2**a), number)

	answer = choiceg(ans1, ans2)
	q,a = make_qa_pair(question, answer, assignments)
	print('question: %s \nanswer: %s'%(q,a))

if __name__ == "__main__":
	example1()