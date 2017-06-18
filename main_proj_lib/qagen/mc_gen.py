from sympy import *
import random
import collections
import unittest

import pdb

def get_question_generator(user_qa_func,seed):
    '''
    returns the function that creates answers and sets the seed before returning
    the answer.
    '''
    def q(seed):
        set_all_seeds(seed)
        q_val,_ = user_qa_func(seed)[0]
        return q_val
    return q

def get_answer_generator(user_qa_func,seed):
    '''
    returns the function that creates answers and sets the seed before returning
    the answer.
    '''
    def a(seed):
        set_all_seeds(seed)
        _,a_val = user_qa_func(seed)[0]
        return a_val
    return a

def gen_mc(user_qa_func):
    # TODO is there a better way to do an alias?
    return genenerate_multiple_choice(user_qa_func)

def genenerate_multiple_choice_pair(user_qa_func,nb_choices):
    '''

    '''
    #TODO: code only numeric version of this code
    # get function pointers/handles for q & a generators
    ans = []
    #
    q_seed = random.randint()
    set_global_q_seed(q_seed)
    question = q_gen(q_seed)
    correct_ans = a_gen(q_seed)
    for mc_i in range(nb_choices-1):
        wrong_seed = int.from_bytes(os.urandom(4), sys.byteorder) # TODO do we need this?
        a_choice = a(wrong_seed)
        # TODO: it would be nice to guarnatee that no other answer will be the same as another answer or as the correct
        ans.append()
    return
