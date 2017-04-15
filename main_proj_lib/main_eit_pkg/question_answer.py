import unittest
from sympy import *
import numpy as np
import random

from funcflow import *

def make_qa_pair(question,answer,assigments={},seed=None):
    '''
    Given a question, answer (and optional assigments) written with the funcflow
    framework, returns a tuple with two strings with the question and answer.
    '''
    #np.random.seed(arg.rand_x)
    #tf.set_random_seed( arg.rand_x )
    if seed != None:
        random.seed(seed)
    assigments = { key: [random.sample(value,1)[0]] for key,value in assigments.items() }
    #print('new_assigments: ', assigments)
    q = question.execute(assigments)
    a = answer.execute(assigments)
    return (q,a)
