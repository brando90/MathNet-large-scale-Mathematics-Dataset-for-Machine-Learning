from qaflow import *
from qaflow.question_answer import *
import sympy

'''
The angle A of the triangle is 30 degrees. The angle B of the triangle is 60 degrees. What is the third angle C?
'''

def example(seed=None):
	random.seed(seed)
	A = random.randint(1,178)
	B = random.randint(1,179-A)

	first_sentence = "The angle A of the triangle is {} degrees.".format(A)
	second_sentence = "The angle B of the triangle is {} degrees.".format(B)
	third_sentence = "What is the third angle C?"

	part1 = perg(first_sentence, second_sentence)
	question = seqg(part1, third_sentence)

	ans = 180-A-B
	answer = choiceg(ans)
	q,a = make_qa_pair(question, answer, {})  
	print('question: %s \nanswer: %s'%(q,a))

if __name__ == '__main__':
	example()