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
        # if callable(gen): ## checks if gen is a function (pointer/handle)
        #     print('callable ', gen)
        #     sentence = sentence + gen()
        # else:
        #     print('string ', gen)
        #     sentence = sentence + gen
        print('string ', gen)
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
            print('callable ', gen)
            sentence = sentence + gen()
        else:
            print('string ', gen)
            sentence = sentence + gen
    return sentence

# def demo():
#     sentence1 = seqg('solve x, ', perg( ' a = b, ', seqg( ' x = 2*', 'b,' ), ' a = 8,' ), ' can you do it?')
#     def func1():
#         return perg( ' a = b, ', seqg( ' x = 2*', 'b,' ), ' a = 8,' )
#     sentence2 = seqg('solve x, ', func1() , ' can you do it?')
#     print(sentence1)
#     print(sentence2)

##

class Test_problem(unittest.TestCase):
    #make sure methods start with word test

    def test_get_problem(self):
        #seqg( ' a = b, ', seqg( ' x = 2*', 'b,' ), ' a = 8,' )
        question = seqg('solve x, ', seqg( ' a = b, ', seqg( ' x = 2*', 'b,' ), ' a = 8,' ), ' can you do it?')
        self.assertEqual(question, 'solve x,  a = b,  x = 2*b, a = 8, can you do it?')



if __name__ == '__main__':
    #demo()
    unittest.main()
