from sympy import *
import random

from qaflow import *
from qaflow.question_answer import *

def dot_product(V, U):
    length = V.len
    product = 0

    for i in length:
        product += V[i]*U[i]

    return product


def example_2_1():

    # In this question we try to define dot product of two vector
    V, U  = symbols('V U')
    question = seqg('Find the dot product of the two vectors V and U when', perg(Eq(V, [0, 1 ])),' and ', perg(Eq(U, [2, 3 ])), '.')
    answer = dot_product(V, U)
    replacement = {}
    replacement[0] = [round(random.uniform(-100,100),1) for i in range(100)]
    replacement[1] = [round(random.uniform(-100,100),1) for i in range(100)]
    replacement[2] = [round(random.uniform(-100,100),1) for i in range(100)]
    replacement[3] = [round(random.uniform(-100,100),1) for i in range(100)]

    q, a = make_qa_pair(question,answer, replacement,seed = 1)
    print('question: %s \n answer: %s' % (q, a)))


def example_2_2():

    # In this question we try to define dot product of two vector
    V, U  = symbols('V U')
    question = seqg('Find the dot product of the two vectors V and U when', perg(Eq(V, [0, 1, 2])),' and ', perg(Eq(U, [3, 4, 5])), '.')
    answer = dot_product(V, U)
    replacement = {}
    replacement[0] = [round(random.uniform(-100,100),1) for i in range(100)]
    replacement[1] = [round(random.uniform(-100,100),1) for i in range(100)]
    replacement[2] = [round(random.uniform(-100,100),1) for i in range(100)]
    replacement[3] = [round(random.uniform(-100,100),1) for i in range(100)]
    replacement[4] = [round(random.uniform(-100,100),1) for i in range(100)]
    replacement[5] = [round(random.uniform(-100,100),1) for i in range(100)]
    q, a = make_qa_pair(question,answer, replacement,seed = 2)
    print('question: %s \n answer: %s' % (q, a)))



def example_2_3():
    # In this question we try to define dot product of two vector
    V, U = symbols('V U')
    question = seqg('Find the dot product of the two vectors V and U when', perg(Eq(V, [0, 1, 2,3])), ' and ',
                    perg(Eq(U, [4, 5, 6 ,7])), '.')
    answer = dot_product(V, U)
    replacement = {}
    replacement[0] = [round(random.uniform(-100,100),1) for i in range(100)]
    replacement[1] = [round(random.uniform(-100,100),1) for i in range(100)]
    replacement[2] = [round(random.uniform(-100,100),1) for i in range(100)]
    replacement[3] = [round(random.uniform(-100,100),1) for i in range(100)]
    replacement[4] = [round(random.uniform(-100,100),1) for i in range(100)]
    replacement[5] = [round(random.uniform(-100,100),1) for i in range(100)]
    replacement[6] = [round(random.uniform(-100,100),1) for i in range(100)]
    replacement[7] = [round(random.uniform(-100,100),1) for i in range(100)]
    q, a = make_qa_pair(question, answer, replacement,seed=3)
    print('question: %s \n answer: %s' % (q, a)))


def example_2_4():
    # In this question we try to define dot product of two vector
    V, U = symbols('V U')
    question = seqg('Find the dot product of the two vectors V and U when', perg(Eq(V, [0, 1, 2, 3, 4])), ' and ',
                    perg(Eq(U, [5, 6, 7, 8, 9])), '.')
    answer = dot_product(V, U)
    replacement = {}
    replacement[0] = [round(random.uniform(-100,100),1) for i in range(100)]
    replacement[1] = [round(random.uniform(-100,100),1) for i in range(100)]
    replacement[2] = [round(random.uniform(-100,100),1) for i in range(100)]
    replacement[3] = [round(random.uniform(-100,100),1) for i in range(100)]
    replacement[4] = [round(random.uniform(-100,100),1) for i in range(100)]
    replacement[5] = [round(random.uniform(-100,100),1) for i in range(100)]
    replacement[6] = [round(random.uniform(-100,100),1) for i in range(100)]
    replacement[7] = [round(random.uniform(-100,100),1) for i in range(100)]
    replacement[8] = [round(random.uniform(-100,100),1) for i in range(100)]
    replacement[9] = [round(random.uniform(-100,100),1) for i in range(100)]
    q, a = make_qa_pair(question, answer,replacement, seed=4)
    print('question: %s \n answer: %s' % (q, a)))




def example_2_5():
    # In this question we try to define dot product of two vector
    V, U = symbols('V U')
    question = seqg('Find the dot product of the two vectors V and U when', perg(Eq(V, [0, 1, 2, 3, 4, 5])), ' and ',
                    perg(Eq(U, [6, 7, 8, 9, 10, 11])), '.')
    answer = dot_product(V, U)
    replacement = {}
    replacement[0] = [round(random.uniform(-100,100),1) for i in range(100)]
    replacement[1] = [round(random.uniform(-100,100),1) for i in range(100)]
    replacement[2] = [round(random.uniform(-100,100),1) for i in range(100)]
    replacement[3] = [round(random.uniform(-100,100),1) for i in range(100)]
    replacement[4] = [round(random.uniform(-100,100),1) for i in range(100)]
    replacement[5] = [round(random.uniform(-100,100),1) for i in range(100)]
    replacement[6] = [round(random.uniform(-100,100),1) for i in range(100)]
    replacement[7] = [round(random.uniform(-100,100),1) for i in range(100)]
    replacement[8] = [round(random.uniform(-100,100),1) for i in range(100)]
    replacement[9] = [round(random.uniform(-100,100),1) for i in range(100)]
    replacement[10] = [round(random.uniform(-100, 100), 1) for i in range(100)]
    replacement[11] = [round(random.uniform(-100, 100), 1) for i in range(100)]
    q, a = make_qa_pair(question, answer,replacement, seed=5)
    print('question: %s \n answer: %s' % (q, a)))




if __name__ == '__main__':

    example_2_1()
