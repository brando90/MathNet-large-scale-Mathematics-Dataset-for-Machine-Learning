import unittest
from sympy import *
import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib import rcParams

import pdb

from qaflow.funcflow import *


class Q(DelayedExecution):
    '''
    Question subclass of DelayedExecution
    Acts as recursive base case for overloaded adding operations of all DelayedExecution subclasses. Base case is a list containing null string.

    E.g., Q() + 'solve' + x + perg( Eq(a,b),Eq(x,2*b),Eq(a,8)) + 'can you do it?'
    '''
    def __init__(self):
        func = lambda *args: []
        DelayedExecution.__init__(self, func)

class A(DelayedExecution):
    '''
    Answer subclass of DelayedExecution. Same as Q subclass above, but meant as syntactic sugar for composing answers instead of questions.
    '''

    def __init__(self):
        func = lambda *args: []
        DelayedExecution.__init__(self, func)

def make_qa_pair(question,answer,assignments={},seed=None, use_latex=False):
    '''
    @question, @answer: DelayedExecution that returns sequential list of elements
    Given a question, answer (and optional assignments) written with the funcflow
    framework, returns a tuple with two strings with the question and answer.

    If node seed is used, it doesn't explicitly set a seed. If you want a seed
    from the os do:
    One suggestion for seeding a random seed: seed = int.from_bytes(os.urandom(4), sys.byteorder)
    '''
    #np.random.seed(arg.rand_x)
    #tf.set_random_seed( arg.rand_x )
    # seed = int.from_bytes(os.urandom(4), sys.byteorder)
    if seed == None:
        seed = random.random() #if no seed given, choose random seed
    random.seed(seed) #set random with seed to generate deterministic values
    mapped_seed = random.random() #get deterministic value of seed mapped to [0, 1)
    assignments = { key: [value[int(mapped_seed*len(value))]] for key,value in assignments.items() } #choose value from assignments based on 
    #print('new_assignments: ', assignments)
    
    #execute question and answer, conver to lists of strings, join
    q = ' '.join(convert_to_list_of_string(question.execute(assignments), use_latex=use_latex))
    a = ' '.join(convert_to_list_of_string(answer.execute(assignments), use_latex=use_latex))

    '''Start code for latex visualization'''
    rcParams['text.usetex'] = True #use local latex compiler
    rcParams['text.latex.preamble'] = r'\usepackage{amsmath}' #use amsmath package
    
    fig = plt.figure() #plot question and answer using matplotlib
    renderer = fig.canvas.get_renderer()
    t = plt.text(0.001, 0.001, "Question: %s \n Answer: %s" % (q, a), fontsize = 12)
    wext = t.get_window_extent(renderer=renderer)

    fig.set_size_inches(wext.width / 65, wext.height / 40, forward=True)
    fig.patch.set_facecolor('white')
    plt.axis('off')
    plt.tight_layout()
    plt.show()
    '''End code for latex visualization'''
    
    
    return (q,a)
