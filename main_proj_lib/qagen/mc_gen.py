from sympy import *
import random
import collections
import unittest

import pdb

# def get_question_generator(user_qa_func,seed):
#     '''
#     returns the function that creates questions.
#
#     note: this is equivalent to:
#     q = lambda seed: user_qa_func(seed)[0]
#     '''
#     def q(seed):
#         q_val,_ = user_qa_func(seed)[0]
#         return q_val
#     return q
#
# def get_answer_generator(user_qa_func,seed):
#     '''
#     returns the function that creates questions.
#
#     note: this is equivalent to:
#     a = lambda seed: user_qa_func(seed)[1]
#     '''
#     def a(seed):
#         _,a_val = user_qa_func(seed)[0]
#         return a_val
#     return a

def gen_mc(user_qa_func):
    # TODO is there a better way to do an alias?
    return genenerate_multiple_choice(user_qa_func)

def genenerate_multiple_choice_pair(user_qa_func,nb_choices):
    '''

    TODO: an only numeric version of this code
    '''
    # get function pointers/handles for q & a generators
    q = lambda seed: user_qa_func(seed)[0]
    a = lambda seed: user_qa_func(seed)[1]
    #
    q_seed = random.randint()
    question = q(q_seed)
    correct_ans = a(q_seed)
    ans = []
    for mc_i in range(nb_choices-1):
        a_choice = a(q_seed)
        # TODO: it would be nice to guarnatee that no other answer will be the same as another answer
        ans.append()
    return
