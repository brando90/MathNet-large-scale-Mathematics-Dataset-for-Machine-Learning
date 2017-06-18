from qaflow import *
from qaflow.question_answer import *
from sympy.functions.combinatorial.numbers import nC, nP, nT

''' 
Out of 30 people we want to form a team of 5 to play basketball. 
How many such distinct teams can be formed? 
'''

def get_activity():
	activities = ["basketball" , "soccer", "volleyball", "dodgeball"]
	return activities[random.randint(0,3)]

def example(seed=None):
	random.seed(seed)
	activity = get_activity()
	number_people = random.randint(0,1000)
	team_size = random.randint(0, number_people)

	first_sentence = "Out of " + str(number_people) + " we want to form a team of " + str(team_size) + " to play " + str(activity) + "."
	second_sentence = "How many such distinct teams can be formed?"
	question = seqg(first_sentence, second_sentence)

	ans = nC(number_people, team_size)
	answer = choiceg(ans)
	q,a = make_qa_pair(question, answer, {})  
	print('question: %s \nanswer: %s'%(q,a))

if __name__ == '__main__':
	example()