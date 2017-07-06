from qaflow import *
from qaflow.question_answer import *
import sympy

'''
The length of side A of a triangle is 8. The length of side B is 6. What is the length of hypotenuse C?
'''

def example(seed=None):
	random.seed(seed)
	A = random.randint(0,1000)
	B = random.randint(0,1000)

	first_sentence = "The length of side A of a triangle is {}".format(A)
	second_sentence = "The length of side B of a triangle is {}".format(B)
	third_sentence = "What is the length of hypotenuse C?"

	part1 = perg(first_sentence, second_sentence)
	question = seqg(part1, third_sentence)

	ans = sqrt(A**2 + B**2)
	answer = choiceg(ans, float(ans))
	q,a = make_qa_pair(question, answer, {})  
	print('question: %s \nanswer: %s'%(q,a))

if __name__ == '__main__':
	example()
