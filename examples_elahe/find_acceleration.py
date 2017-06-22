from sympy import *
import random

from qaflow import *
from qaflow.question_answer import *


def acceleration(v1, v0, t1, t0):
    return (x1 - x0) / (t1 - t0)

def example1():
    # We try to find acceleration of an object that moves with constant accelaration and we have its velocity in two different times

    v0, v1, t0, t1 = symbols('v0 v1 t0 t1')
    # addition of matrices'
    question = seqg('Find velocity of an object that moves in one dimensional world given that we have its velocity changes from ', Eq(v0,3), 'to ', Eq(v1 , 4), '(m) in time frame of ', Eq(t0,1), ' to ', Eq(t1 ,2),'.')
    answer = acceleration(v1,v0,t1,t0)
    replacements = {}
    #pdb.set_trace()
    replacements[1] = [random.randint(0,200) for i in range(100)]
    replacements[2] = [random.randint(0,200) for i in range(100)]
    replacements[3] = [random.randint(0,200) for i in range(100)]
    replacements[4] = [random.randint(0,200) for i in range(100)]
    #answer = seqg( 'rubush' )
    #q,a = make_qa_pair(question, answer, seed=1)
    q,a = make_qa_pair(question,answer,replacements, seed = 1)
    print('question: %s \n answer: %s' %(q,a))


def example2():
    # We try to find acceleration of an object that moves with constant accelaration and we have its velocity in two different times

    v0, v1, t0, t1 = symbols('v0 v1 t0 t1')
    # addition of matrices'
    question = seqg(
        'Find velocity of an object that moves in two dimensional world given that we have its velocity changes from ',
        Eq(v0, [0,1]), 'to ', Eq(v1, [2, 3]), '(m) in time frame of ', Eq(t0, 4 ), ' to ', Eq(t1, 5), '.')
    answer = acceleration(v1, v0, t1, t0)
    replacements = {}
    # pdb.set_trace()
    replacements[0] = [random.randint(0, 200) for i in range(100)]
    replacements[1] = [random.randint(0, 200) for i in range(100)]
    replacements[2] = [random.randint(0, 200) for i in range(100)]
    replacements[3] = [random.randint(0, 200) for i in range(100)]
    replacements[4] = [random.randint(0, 200) for i in range(100)]
    replacements[5] = [random.randint(0, 200) for i in range(100)]
    # answer = seqg( 'rubush' )
    # q,a = make_qa_pair(question, answer, seed=1)
    q, a = make_qa_pair(question, answer, replacements, seed = 2)
    print('question: %s \n answer: %s' % (q, a))


def example3():
    # We try to find acceleration of an object that moves with constant accelaration and we have its velocity in two different times

    v0, v1, t0, t1 = symbols('v0 v1 t0 t1')
    # addition of matrices'
    question = seqg(
        'Find velocity of an object that moves in three dimensional world given that we have its velocity changes from ',
        Eq(v0, [0,1,6]), 'to ', Eq(v1, [2, 3,7]), '(m) in time frame of ', Eq(t0, 4 ), ' to ', Eq(t1, 5), '.')
    answer = acceleration(v1, v0, t1, t0)
    replacements = {}
    # pdb.set_trace()
    replacements[0] = [random.randint(0, 200) for i in range(100)]
    replacements[1] = [random.randint(0, 200) for i in range(100)]
    replacements[2] = [random.randint(0, 200) for i in range(100)]
    replacements[3] = [random.randint(0, 200) for i in range(100)]
    replacements[4] = [random.randint(0, 200) for i in range(100)]
    replacements[5] = [random.randint(0, 200) for i in range(100)]
    replacements[6] = [random.randint(0, 200) for i in range(100)]
    replacements[7] = [random.randint(0, 200) for i in range(100)]
    # answer = seqg( 'rubush' )
    # q,a = make_qa_pair(question, answer, seed=1)
    q, a = make_qa_pair(question, answer, replacements, seed = 3)
    print('question: %s \n answer: %s' % (q, a))

def example4():
    # We try to find acceleration of an object that moves with constant accelaration and we have its velocity in two different times

    v0, v1, t0, t1 = symbols('v0 v1 t0 t1')
    # addition of matrices'
    question = seqg(
        'Find velocity of an object that moves in four dimensional world given that we have its velocity changes from ',
        Eq(v0, [0,1,6,8]), 'to ', Eq(v1, [2, 3,7,9]), '(m) in time frame of ', Eq(t0, 4 ), ' to ', Eq(t1, 5), '.')
    answer = acceleration(v1, v0, t1, t0)
    replacements = {}
    # pdb.set_trace()
    replacements[0] = [random.randint(0, 200) for i in range(100)]
    replacements[1] = [random.randint(0, 200) for i in range(100)]
    replacements[2] = [random.randint(0, 200) for i in range(100)]
    replacements[3] = [random.randint(0, 200) for i in range(100)]
    replacements[4] = [random.randint(0, 200) for i in range(100)]
    replacements[5] = [random.randint(0, 200) for i in range(100)]
    replacements[6] = [random.randint(0, 200) for i in range(100)]
    replacements[7] = [random.randint(0, 200) for i in range(100)]
    replacements[8] = [random.randint(0, 200) for i in range(100)]
    replacements[9] = [random.randint(0, 200) for i in range(100)]
    # answer = seqg( 'rubush' )
    # q,a = make_qa_pair(question, answer, seed=1)
    q, a = make_qa_pair(question, answer, replacements, seed = 4)
    print('question: %s \n answer: %s' % (q, a))


def example5():
    # We try to find acceleration of an object that moves with constant accelaration and we have its velocity in two different times

    v0, v1, t0, t1 = symbols('v0 v1 t0 t1')
    # addition of matrices'
    question = seqg(
        'Find velocity of an object that moves in five dimensional world given that we have its velocity changes from ',
        Eq(v0, [0,1,6,8,10]), 'to ', Eq(v1, [2, 3,7,9,11]), '(m) in time frame of ', Eq(t0, 4 ), ' to ', Eq(t1, 5), '.')
    answer = acceleration(v1, v0, t1, t0)
    replacements = {}
    # pdb.set_trace()
    replacements[0] = [random.randint(0, 200) for i in range(100)]
    replacements[1] = [random.randint(0, 200) for i in range(100)]
    replacements[2] = [random.randint(0, 200) for i in range(100)]
    replacements[3] = [random.randint(0, 200) for i in range(100)]
    replacements[4] = [random.randint(0, 200) for i in range(100)]
    replacements[5] = [random.randint(0, 200) for i in range(100)]
    replacements[6] = [random.randint(0, 200) for i in range(100)]
    replacements[7] = [random.randint(0, 200) for i in range(100)]
    replacements[8] = [random.randint(0, 200) for i in range(100)]
    replacements[9] = [random.randint(0, 200) for i in range(100)]
    replacements[10] = [random.randint(0, 200) for i in range(100)]
    replacements[11] = [random.randint(0, 200) for i in range(100)]

    # answer = seqg( 'rubush' )
    # q,a = make_qa_pair(question, answer, seed=1)
    q, a = make_qa_pair(question, answer, replacements , seed = 5)
    print('question: %s \n answer: %s' % (q, a))


if __name__ == '__main__':
    example1()
