import string
import random
import math

import numpy as np

import maps

import pdb


class Problem(object):

    def __init__(self,array_generators,key_words_values,solution_creater):
        self.array_generators = array_generators
        self.key_words_values = key_words_values
        self.g = maps.NamedDict()
        self.solution_creater = solution_creater

    def generate_problem_statement(self):
        '''
        Generates a specific problem
        '''
        self.sample_random_state()
        #
        question = self.generate_statements()
        return question

    def sample_random_state(self):
        hash_map = {}
        #pdb.set_trace()
        for k,v in self.key_words_values.items():
            #pdb.set_trace()
            hash_map[k] = v()
        self.g = maps.NamedDict(hash_map)

    def generate_statements(self):
        problem_statement = ''
        for gen in self.array_generators:
            problem_statement = problem_statement + gen.get_statement(self.g)
        return problem_statement

    def generate_solution(self,g):
        soln = self.solution_creater(g)
        return soln

class Gen(object):

    def process_chain(self,g):
        '''
        processes the chain of statements and generates the string with the finished statement.
        '''
        each_statements = []
        for i in range(len(self.statements)):
            func_for_statement = self.statements[i]
            current_statement = func_for_statement(g)
            each_statements.append(current_statement)
        return each_statements

    def join_statements(self,statements):
        statement = ''
        for i in range(len(statements)):
            current_statement = statements[i]
            statement = statement + current_statement
        return statement

class SeqGen(Gen):

    def __init__(self,statements):
        self.statements = statements # holds the functions that have the problem statements

    def get_statement(self,g):
        each_statements = self.process_chain(g)
        statement = self.join_statements(each_statements)
        return statement

class PerGen(Gen):

    def __init__(self,statements):
        self.statements = statements # holds the functions that have the problem statements

    def get_statement(self,g):
        each_statements = self.process_chain(g)
        #pdb.set_trace()
        random.shuffle(each_statements)
        statement = self.join_statements(each_statements)
        return statement

#

def intro_sent(g):
    sentence = '%s is a rare disease in which the victim has the delusion that he or she is being subjected to intense examination.'%(g.disease_name)
    return sentence

def prob_disease_sent(g):
    sentence = 'A person selected uniformly at random has %s with probability %f'%(g.disease_name,g.p_f)
    return sentence

def prob_shaky_given_disease_sent(g):
    sentence = 'A person with %s has %s with probability %f'%(g.disease_name,g.symptom,g.p_s_f)
    return sentence

def prob_shaky_given_no_disease_sent(g):
    sentence = 'A person without %s has %s with probability %f'%(g.disease_name,g.symptom,g.p_s_nf)
    return sentence

def question(g):
    sentence = 'What is the probability that a person selected uniformly at random has has %s, given that he or she has %s?'%(g.disease_name,g.symptom)
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

def solution_creater(g):
    p_f = g.p_f
    p_s_f = g.p_s_f
    p_s_nf = g.p_s_nf
    p_nf = 1 - p_f
    #
    p_s = p_s_f*p_f + p_s_nf*p_nf
    # bayes theorem
    p_f_s = (p_s_f * p_f)/p_s
    return p_f_s
##

def probability_example_problem():
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
    # create
    generators = [first_seq_gen,permutation_gen,last_seq_gen]
    problem = Problem(array_generators=generators,key_words_values=key_words_values,solution_creater=soln_creater)
    #
    one_question = problem.generate_problem_statement()
    return one_question

if __name__ == '__main__':
    one_question = probability_example_problem()
    print('one_question: ', one_question)
