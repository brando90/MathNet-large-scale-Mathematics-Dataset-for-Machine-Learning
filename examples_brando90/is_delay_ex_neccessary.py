from sympy import *
import random

from qaflow import *
from qaflow.question_answer import *

'''
6.042 Problem Set 8, Problem 1
Sally Smart just graduated from high school. She was accepted to three reputable colleges.
With probability 4/12, she attends Yale. With probability 5/12, she attends MIT.
With probability 3/12, she attends Little Hoop Community College. Sally is either happy or sad.
If she attends Yale, she is happy with probability 4/12. If she attends MIT, she is happy
with probability 7/12. If she attends Little Hoop, she is happy with probability 11/12.
What is the probability that Sally is happy in college?
'''
def get_colleges(ind):
    colleges = ["MIT", "Vanderbilt", "Tufts", "Stanford", "Harvard", "Boston College", "Northeastern", "Yale", "Dartmouth"]
    return colleges[3*(ind-1):3*ind]

def example(seed=None):
    random.seed(seed)
    first_college = "Yale"
    second_college = "MIT"
    third_college = "Little Hoop Community College"
    person = "Sally Smart"

    lb, ub = 0, 1
    prob_col_1 = random.uniform(lb, ub)
    prob_col_2 = random.uniform(lb, 1-prob_col_1)
    prob_col_3 = 1 - prob_col_1 - prob_col_2
    prob_happy_1 = random.uniform(lb,ub)
    prob_happy_2 = random.uniform(lb, ub)
    prob_happy_3 = random.uniform(lb, ub)

    beggining_q = seqg(person, "just graduated from high school. She was accepted to three reputable colleges.")

    perm1 = seqg("With probability", prob_col_1, "she attends ", first_college)
    perm2 = seqg("With probability", prob_col_2, "she attends ", second_college)
    perm3 = seqg("With probability", prob_col_3, "she attends ", third_college)
    perm4 = seqg("If she attends", first_college, "she is happy with probability", prob_happy_1)
    perm5 = seqg("If she attends", second_college, "she is happy with probability", prob_happy_2)
    perm6 = seqg("If she attends", third_college, "she is happy with probability", prob_happy_3)

    permutable_part_1 = perg(perm1, perm2, perm3)
    permutable_part_2 = perg(perm4, perm5, perm6)

    question = seqg(beggining_q, permutable_part_1, permutable_part_2)

    replacemements = {}
    replacemements[first_college] = get_colleges(1)
    replacemements[second_college] = get_colleges(2)
    replacemements[third_college] = get_colleges(3)

    ans = [prob_col_1*prob_happy_1 + prob_col_2*prob_happy_2 + prob_col_3*prob_happy_3]
    answer = choiceg(*ans)
    q,a = make_qa_pair(question, answer, replacemements)
    print('question: %s \nanswer: %s'%(q,a))

def example1(seed=None):
    random.seed(seed)
    # first_college = "Yale"
    # second_college = "MIT"
    # third_college = "Little Hoop Community College"
    first_college = get_college_rand()
    second_college = get_college_rand()
    third_college = get_college_rand()
    person = get_person_rand()

    lb, ub = 0, 1
    prob_col_1 = random.uniform(lb, ub)
    prob_col_2 = random.uniform(lb, 1-prob_col_1)
    prob_col_3 = 1 - prob_col_1 - prob_col_2
    prob_happy_1 = random.uniform(lb,ub)
    prob_happy_2 = random.uniform(lb, ub)
    prob_happy_3 = random.uniform(lb, ub)

    beggining_q = seqg(person, "just graduated from high school. She was accepted to three reputable colleges.")

    perm1 = seqg("With probability", prob_col_1, "she attends ", first_college)
    perm2 = seqg("With probability", prob_col_2, "she attends ", second_college)
    perm3 = seqg("With probability", prob_col_3, "she attends ", third_college)
    perm4 = seqg("If she attends", first_college, "she is happy with probability", prob_happy_1)
    perm5 = seqg("If she attends", second_college, "she is happy with probability", prob_happy_2)
    perm6 = seqg("If she attends", third_college, "she is happy with probability", prob_happy_3)

    permutable_part_1 = perg(perm1, perm2, perm3)
    permutable_part_2 = perg(perm4, perm5, perm6)

    question = seqg(beggining_q, permutable_part_1, permutable_part_2)

    ans = [prob_col_1*prob_happy_1 + prob_col_2*prob_happy_2 + prob_col_3*prob_happy_3]
    answer = choiceg(*ans)
    q,a = make_qa_pair(question, answer, replacemements)
    print('question: %s \nanswer: %s'%(q,a))

def example(seed=None):
    random.seed(seed)
    i,j,k = rand(1)
    first_college = get_colleges2(i)
    second_college = get_colleges2(j)
    third_college = get_colleges2(k)
    person = "Sally Smart"

    lb, ub = 0, 1
    prob_col_1 = random.uniform(lb, ub)
    prob_col_2 = random.uniform(lb, 1-prob_col_1)
    prob_col_3 = 1 - prob_col_1 - prob_col_2
    prob_happy_1 = random.uniform(lb,ub)
    prob_happy_2 = random.uniform(lb, ub)
    prob_happy_3 = random.uniform(lb, ub)

    beggining_q = seqg(person, "just graduated from high school. She was accepted to three reputable colleges.")

    perm1 = seqg("With probability", prob_col_1, "she attends ", first_college)
    perm2 = seqg("With probability", prob_col_2, "she attends ", second_college)
    perm3 = seqg("With probability", prob_col_3, "she attends ", third_college)
    perm4 = seqg("If she attends", first_college, "she is happy with probability", prob_happy_1)
    perm5 = seqg("If she attends", second_college, "she is happy with probability", prob_happy_2)
    perm6 = seqg("If she attends", third_college, "she is happy with probability", prob_happy_3)

    permutable_part_1 = perg(perm1, perm2, perm3)
    permutable_part_2 = perg(perm4, perm5, perm6)

    question = seqg(beggining_q, permutable_part_1, permutable_part_2)

    ans = [prob_col_1*prob_happy_1 + prob_col_2*prob_happy_2 + prob_col_3*prob_happy_3]
    answer = choiceg(*ans)
    q,a = make_qa_pair(question, answer, replacemements)
    print('question: %s \nanswer: %s'%(q,a))

if __name__ == '__main__':
    example()
