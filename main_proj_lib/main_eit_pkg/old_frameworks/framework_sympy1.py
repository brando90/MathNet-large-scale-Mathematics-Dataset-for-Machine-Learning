import string
import random
import math

import numpy as np
import unittest

import maps

from sympy import *

import pdb

class QA(object):

    def __init__(self,Q,A):
        self.Q = Q
        self.A = A
        self.math_variables = maps.NamedDict()
        self.tree_rep = node()


class seqg(object):
    def __init__(self,*generator):
        self.adj = []
        #self.math_variables = maps.NamedDict()
        self.DFS_compile(generator)

    def DFS_compile(self,*generator):
        self.DFS_compile_visit(generator)

    def DFS_compile_visit(self,*generator):
        for g in generator:
            if self.is_leaf(g): # if sympy or string or numerical_val
                self.adj.append(g)
            else:
                self.adj.append(g)




def seqg(*generator):
    '''
    Sequential Generator
    '''
    math_objs = []
    for gen in generator:
        if callable(gen) && gen != Symbol: ## checks if gen is a function (pointer/handle)
            sentence.append( gen() )
        else:
            sentence.append( gen )
    sentence = [ evaluate(obj) for obj in math_objs ]
    return sentence

def perg(*generator):
    '''
    Permutation Generator
    '''
    sentence = ''
    generator = random.sample( generator, len(generator) )
    for gen in generator:
        if callable(gen): ## checks if gen is a function (pointer/handle)
            sentence = sentence + gen()
        else:
            sentence = sentence + gen
    return sentence

'''
Example:
    Q = 'solve x,  a = b,  x = 2*b, a = 8, can you do it?'
    A = 'x = 2*b' or A = 'x = 2*b' or 'x = 2*8' or x = '16'
'''

def demo():
    '''
    Example:
        Q = 'solve x,  a = b,  x = 2*b, a = 8, can you do it?'
        A = 'x = 2*b' or A = 'x = 2*b' or 'x = 2*8' or x = '16'
    '''
    x a b = symbols('x a b')
    question = seqg('solve ', x, seqg( a = b , ' ,', seqg( x = 2* , b, ',' ), a=8, ',' ), ' can you do it?')
    pass


##

class Test_problem(unittest.TestCase):
    #make sure methods start with word test

    def test_get_problem(self):
        question = seqg('solve x, ', seqg( ' a = b, ', seqg( ' x = 2*', 'b,' ), ' a = 8,' ), ' can you do it?')
        self.assertEqual(question, 'solve x,  a = b,  x = 2*b, a = 8, can you do it?')



if __name__ == '__main__':
    demo()
    unittest.main()
