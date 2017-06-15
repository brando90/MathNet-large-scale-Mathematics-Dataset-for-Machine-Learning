from sympy import *
import random
import collections
import unittest

import pdb

global_seed = 0

def register_random_seeding_funcs(*args):
    #TODO
    pass

def set_global_q_seed(seed):
    # TODO
    global_seed = seed
    pass

def consistent_variable(f,*args,**kwargs):
    '''

    '''
    set_all_seeds(global_seed)
    if callable(f):
        f_val = f(args,kwargs)
        return f_val
    else:
        raise ValueError('The type {} is not supported.'.format(type(f)))


class random_controll_tests(unittest.TestCase):
    #sess = tf.InteractiveSession()

    def consistent_variable(self):
        val = consistent_variable()
        print(val)

if __name__ == '__main__':
    unittest.main()
