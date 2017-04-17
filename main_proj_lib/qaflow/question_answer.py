import unittest
from sympy import *
import numpy as np
import random

from qaflow.funcflow import *

def make_qa_pair(question,answer,assignments={},seed=None):
    '''
    Given a question, answer (and optional assignments) written with the funcflow
    framework, returns a tuple with two strings with the question and answer.

    If node seed is used, it doesn't explicitly set a seed. If you want a seed
    from the os do:
    One suggestion for seeding a random seed: seed = int.from_bytes(os.urandom(4), sys.byteorder)
    '''
    #np.random.seed(arg.rand_x)
    #tf.set_random_seed( arg.rand_x )
    # seed = int.from_bytes(os.urandom(4), sys.byteorder)
    if seed != None:
        random.seed(seed)
    assignments = { key: [random.sample(value,1)[0]] for key,value in assignments.items() }
    #print('new_assignments: ', assignments)
    q = question.execute(assignments)
    a = answer.execute(assignments)
    return (q,a)
