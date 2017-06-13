'''
The first three terms of a geometric sequence are 27, -9, and 3. 
Find the sum to infinity of the sequence.
'''
from qaflow import *
from qaflow.question_answer import *
from sympy import *

def example(seed=None):
	random.seed(seed)
	a1 = random.randint(-1000,1000)
	r = random.randint(-999,999)/1000
	a2 = a1*r
	a3 = a2*r

	first_sentence = "The first three terms of a geometric sequence are {0}, {1}, and {2}.".format(a1,a2,a3)
	second_sentence = "Find the sum to infinity of the sequence."
	question = perg(first_sentence, second_sentence)

	ans = a1/(1-r)

	answer = choiceg(ans)
	q,a = make_qa_pair(question, answer, {})  
	print('question: %s \nanswer: %s'%(q,a))

if __name__ == '__main__':
	example()
