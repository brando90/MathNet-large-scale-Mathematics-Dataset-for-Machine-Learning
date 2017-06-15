from sympy import *
import random
import collections
import unittest

import pdb

def register_random_seeding_funcs(*args):
    #TODO
    pass

def consistent_variable(*args,f=None,seed=1,**kwargs):
    '''

    '''
    if f != None:
        if callable(f):
            return f(args,kwargs)
        else:
            raise ValueError('The type {} is not supported.'.format(type(f)))
    else:
        raise ValueError('The type {} is not supported.'.format(type(f)))


class random_controll_tests(unittest.TestCase):
    #sess = tf.InteractiveSession()

    def consistent_variable(self):
        val = consistent_variable()
        print(val)

if __name__ == '__main__':
    unittest.main()
