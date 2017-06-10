from qaflow import *
from qaflow.question_answer import *
from sympy import *

'''
IB Math SL Paper 1 May 2009
Let f(x)=e^x*cosx. Find the gradient of the normal to the curve of f at x=π.
'''

def example(seed=None):
	random.seed(seed)
	value = random.randint(-1000,1000)
	const1 = random.randint(-1000,1000)
	const2 = random.randint(-1000,1000)

	first_sentence = "Let y = 3*x + 5*sin(x)."
	second_sentence = "Find the gradient of the normal to the curve of f at x={}.".format(value)
	question = seqg(first_sentence, second_sentence)

	x = Symbol('x')
	temp = diff(const1*x + const2*sin(x))
	normGradient = -1/temp
	ans = normGradient.subs(x, value)
	numericalAns = ans.evalf(10)

	answer = choiceg(ans, numericalAns)
	q,a = make_qa_pair(question, answer, {})  
	print('question: %s \nanswer: %s'%(q,a))

if __name__ == '__main__':
	example()