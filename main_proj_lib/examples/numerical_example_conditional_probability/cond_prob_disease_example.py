import string
import random
import math

import numpy as np
import unittest

from main_eit_pkg import *

import maps

import pdb


# functions that

def intro_sent(g):
    sentence = '%s is a rare disease in which the victim has the delusion that he or she is being subjected to intense examination. '%(g.disease_name)
    return sentence

def prob_disease_sent(g):
    sentence = 'A person selected uniformly at random has %s with probability %f. '%(g.disease_name,g.p_f)
    return sentence

def prob_shaky_given_disease_sent(g):
    sentence = 'A person with %s has %s with probability %f. '%(g.disease_name,g.symptom,g.p_s_f)
    return sentence

def prob_shaky_given_no_disease_sent(g):
    sentence = 'A person without %s has %s with probability %f. '%(g.disease_name,g.symptom,g.p_s_nf)
    return sentence

def question(g):
    sentence = 'What is the probability that a person selected uniformly at random has has %s, given that he or she has %s? '%(g.disease_name,g.symptom)
    return sentence
#

def get_disease_names():
    diseases = ['CSphobia','Biophobia','Mathphobia'] #TODO: re-think
    #
    rand_i = random.randint(a=0,b=len(diseases)-1) # Return a random integer N such that a <= N <= b.
    disease_name = diseases[rand_i]
    return disease_name

def get_symptom_names():
    diseases = ['shaky arm','soft teeth','strident attitude'] #TODO: re-think
    #
    rand_i = random.randint(a=0,b=len(diseases)-1) # Return a random integer N such that a <= N <= b.
    disease_name = diseases[rand_i]
    return disease_name

def get_p_f():
    return random.uniform(a=0, b=1) # Return a random floating point number N such that a <= N <= b for a <= b and b <= N <= a for b < a.

def get_p_s_f():
    return random.uniform(a=0, b=1) # Return a random floating point number N such that a <= N <= b for a <= b and b <= N <= a for b < a.

def get_p_s_nf():
    return random.uniform(a=0, b=1) # Return a random floating point number N such that a <= N <= b for a <= b and b <= N <= a for b < a.

#

def solution_creater(g):
    p_f = g.p_f
    p_s_f = g.p_s_f
    p_s_nf = g.p_s_nf
    p_nf = 1 - p_f
    # total probability rule p(s) = p(s|f)p(f) + p(s|~f)p(~f)
    p_s = p_s_f*p_f + p_s_nf*p_nf
    # bayes theorem p(f|s) = p(s|f)p(f) / p(s)
    p_f_s = (p_s_f * p_f)/p_s
    return p_f_s

#

def probability_example_problem():
    '''
    Probability example to generate varied problems
    '''
    # functions for generator
    first_seq_gen = [intro_sent]
    permutation_gen = [prob_disease_sent,prob_shaky_given_disease_sent,prob_shaky_given_no_disease_sent]
    last_seq_gen = [question]
    # key words to random values that will be chose
    key_words_values = {'disease_name':get_disease_names, 'p_f':get_p_f, 'p_s_nf':get_p_s_nf, 'p_s_f':get_p_s_f ,'symptom':get_symptom_names}
    # actual generator nodes
    first_seq_gen = SeqGen([intro_sent])
    permutation_gen = PerGen([prob_disease_sent,prob_shaky_given_disease_sent,prob_shaky_given_no_disease_sent])
    last_seq_gen = SeqGen([question])
    #soln
    soln_creater = solution_creater
    # create problem class to automatically generate varied questions/problems and answers/solution
    generators = [first_seq_gen,permutation_gen,last_seq_gen]
    problem = Problem(array_generators=generators,key_words_values=key_words_values,solution_creater=soln_creater)
    # make Q&A
    one_question = problem.generate_problem_statement()
    one_soln = problem.generate_solution()
    return one_question, one_soln

def print_example():
    print('one_question ', one_question)
    print('one_soln ', one_soln)

if __name__ == '__main__':
    print_example()
