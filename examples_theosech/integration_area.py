from sympy import *
from qagen import *

'''
A point P(x,x**2) lies on the curve y=x**2. 
Calculate the minimum distance from the point A(2,-0.5) to the point P.
'''

def example(seed=None):
	random.seed(seed)
	a = random.randint(-1000,1000)
	x = Symbol('x')

	first_sentence = "A point P(x,x**2) lies on the curve y=x**2."
	second_sentence = "Calculate the minimum distance from the point A({},-0.5) to the point P.".format(a)
	question = seqg(first_sentence, second_sentence)
	distEq = sqrt(((x+a)**2) + ((x**2+0.5)**2))
	toSolve = diff(distEq**2)
	c = solve(toSolve)
	ans = [distEq.subs(x,c[0])]

	answer = choiceg(*ans)
	q,a = make_qa_pair(question, answer, {})  
	print('question: %s \nanswer: %s'%(q,a))

if __name__ == '__main__':
	example()