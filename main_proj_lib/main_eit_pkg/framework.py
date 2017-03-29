import string
import random
import math

import numpy as np
import unittest

import maps

import pdb

def seqg(*generator):
    '''
    Sequential Generator
    '''
    sentence = ''
    for gen in generator:
        if callable(gen): ## checks if gen is a function (pointer/handle)
            sentence = sentence + gen()
        else:
            sentence = sentence + gen
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

##

class Test_problem(unittest.TestCase):
    #make sure methods start with word test

    def test_get_problem(self):
        question = seqg('solve x, ', seqg( ' a = b, ', seqg( ' x = 2*', 'b,' ), ' a = 8,' ), ' can you do it?')
        self.assertEqual(question, 'solve x,  a = b,  x = 2*b, a = 8, can you do it?')



if __name__ == '__main__':
    unittest.main()
