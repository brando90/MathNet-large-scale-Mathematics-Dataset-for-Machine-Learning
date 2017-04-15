import unittest
from sympy import *
import numpy as np
import random

from funcflow import *

def make_qa_pair(question,answer,assignments={},seed=None):
    '''
    Given a question, answer (and optional assignments) written with the funcflow
    framework, returns a tuple with two strings with the question and answer.
    '''
    #np.random.seed(arg.rand_x)
    #tf.set_random_seed( arg.rand_x )
    if seed != None:
        random.seed(seed)
    assignments = { key: [random.sample(value,1)[0]] for key,value in assignments.items() }
    #print('new_assignments: ', assignments)
    q = question.execute(assignments)
    a = answer.execute(assignments)
    return (q,a)
