import string
import random
import math

import numpy as np
import unittest

import maps

import pdb


class Problem(object):

    def __init__(self,array_generators,key_words_values,solution_creater):
        self.array_generators = array_generators
        self.key_words_values = key_words_values
        self.g = maps.NamedDict() # global variables for this problem
        self.solution_creater = solution_creater

    def generate_and_save_QAs_to_file(self,location,question_name,answer_name,n):
        '''
        generates n new questions and answers and saves them to location with corresponding question and answer names.
        '''
        question_answers = self._generate_new_QAs(n)
        self._save_QAs_to_file(location,question_name,answer_name,question_answers)

    def _save_QAs_to_file(self,location,question_name,answer_name,question_answers):
        '''
        save the array of question and answers [...,(q,a),...] to a location.
        Things will be saved as location/question_name_id and location/answer_name_id.
        '''
        for i in range( len(question_answers) ):
            q,a = question_answers[i]
            #
            loc_q = location+'/'+question_name+str(i)
            loc_a = location+'/'+answer_name+str(i)
            with open(loc_q,mode='w') as question_file, open(loc_a,mode='w') as answer_file:
                question_file.write(q)
                answer_file.write(a)

    def _generate_new_QAs(self,n):
        '''
        generates exactly n number new question and answers.
        '''
        qas = []
        for i in range(n):
            q = self.generate_new_problem_statement() # note this resets the random state
            a = self.generate_solution()
            qas.append((q,a))
        return qas

    def generate_problem_statement(self):
        '''
        Generates a specific problem
        '''
        question = self._generate_statements()
        return question

    def generate_new_problem_statement(self):
        '''
        Generates a specific problem
        '''
        self._sample_random_state()
        #
        question = self._generate_statements()
        return question

    def generate_solution(self):
        '''
        Generates a solution for the current specific problem according to the current
        random state.
        (note: that your solution creator will use the value of global variables for this specific problem to generate the solution)
        '''
        soln = self.solution_creater(self.g)
        return soln

    def _sample_random_state(self):
        '''
        Re-sets the random state for the current problem.
        This function should be called when trying to generate a new problem
        statement so that the names and values related to the problem change.
        '''
        hash_map = {}
        #pdb.set_trace()
        for key_words_in_problem, func_sets_state_for_key_word in self.key_words_values.items():
            #pdb.set_trace()
            hash_map[key_words_in_problem] = func_sets_state_for_key_word()
        self.g = maps.NamedDict(hash_map)

    def _generate_statements(self):
        '''
        According to the generators that been given to the problem, go through them
        and generate new problem statements according to the current random state.
        (note this function will not change the random state, so you have to call the
        change state first and then call this if you want to generate a new problem)
        '''
        problem_statement = ''
        for gen in self.array_generators:
            problem_statement = problem_statement + gen.get_statement(self.g)
        return problem_statement

class Gen(object):

    def process_chain(self,g):
        '''
        processes the chain of statements and generates the array string with the finished statement.
        '''
        each_statements = []
        for i in range(len(self.statements)):
            func_for_statement = self.statements[i]
            current_statement = func_for_statement(g)
            each_statements.append(current_statement)
        return each_statements

    def join_statements(self,statements):
        '''
        given an array of strings, joins them into one big string.
        '''
        statement = ''
        for i in range(len(statements)):
            current_statement = statements[i]
            statement = statement + current_statement
        return statement

class SeqGen(Gen):

    def __init__(self,statements):
        self.statements = statements # holds the functions that have the problem statements

    def get_statement(self,g):
        '''
        returns the string of the statements for this part of the problem.
        Note that they will be in the ordered given in the initialization
        (i.e. its a sequential generator)
        '''
        each_statements = self.process_chain(g)
        statement = self.join_statements(each_statements)
        return statement

class PerGen(Gen):

    def __init__(self,statements):
        self.statements = statements # holds the functions that have the problem statements

    def get_statement(self,g):
        '''
        returns the string of the statements for this part of the problem.
        Note that they will be permutated
        (i.e. its a permutation generator)
        '''
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
    sentence = 'A person selected uniformly at random has %s with probability %f. '%(g.disease_name,g.p_f)
    return sentence

def prob_shaky_given_disease_sent(g):
    sentence = 'A person with %s has %s with probability %f. '%(g.disease_name,g.symptom,g.p_s_f)
    return sentence

def prob_shaky_given_no_disease_sent(g):
    sentence = 'A person without %s has %s with probability %f'%(g.disease_name,g.symptom,g.p_s_nf)
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

def get_p_f_test():
    return 1.0/50 # Return a random floating point number N such that a <= N <= b for a <= b and b <= N <= a for b < a.

def get_p_s_f_test():
    return 9.0/10 # Return a random floating point number N such that a <= N <= b for a <= b and b <= N <= a for b < a.

def get_p_s_nf_test():
    return 1.0/20 # Return a random floating point number N such that a <= N <= b for a <= b and b <= N <= a for b < a.

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
    #key_words_values = {'disease_name':get_disease_names, 'p_f':get_p_f_test, 'p_s_nf':get_p_s_nf_test, 'p_s_f':get_p_s_f_test ,'symptom':get_symptom_names}
    # actual generator nodes
    first_seq_gen = SeqGen([intro_sent])
    permutation_gen = PerGen([prob_disease_sent,prob_shaky_given_disease_sent,prob_shaky_given_no_disease_sent])
    last_seq_gen = SeqGen([question])
    #soln
    soln_creater = solution_creater
    # create
    generators = [first_seq_gen,permutation_gen,last_seq_gen]
    problem = Problem(array_generators=generators,key_words_values=key_words_values,solution_creater=soln_creater)
    # make Q&A
    one_question = problem.generate_problem_statement()
    one_soln = problem.generate_solution()
    return one_question, one_soln

#

class Test_problem(unittest.TestCase):
    #make sure methods start with word test

    def get_problem(self):
        first_seq_gen = [intro_sent]
        permutation_gen = [prob_disease_sent,prob_shaky_given_disease_sent,prob_shaky_given_no_disease_sent]
        last_seq_gen = [question]
        # key words to random values that will be chose
        key_words_values = {'disease_name':get_disease_names, 'p_f':get_p_f_test, 'p_s_nf':get_p_s_nf_test, 'p_s_f':get_p_s_f_test ,'symptom':get_symptom_names}
        # actual generator nodes
        first_seq_gen = SeqGen([intro_sent])
        permutation_gen = PerGen([prob_disease_sent,prob_shaky_given_disease_sent,prob_shaky_given_no_disease_sent])
        last_seq_gen = SeqGen([question])
        #soln
        soln_creater = solution_creater
        # create
        generators = [first_seq_gen,permutation_gen,last_seq_gen]
        problem = Problem(array_generators=generators,key_words_values=key_words_values,solution_creater=soln_creater)
        return problem

    def probability_example_problem_unit_test(self):
        # functions for generator
        first_seq_gen = [intro_sent]
        permutation_gen = [prob_disease_sent,prob_shaky_given_disease_sent,prob_shaky_given_no_disease_sent]
        last_seq_gen = [question]
        # key words to random values that will be chose
        key_words_values = {'disease_name':get_disease_names, 'p_f':get_p_f_test, 'p_s_nf':get_p_s_nf_test, 'p_s_f':get_p_s_f_test ,'symptom':get_symptom_names}
        # actual generator nodes
        first_seq_gen = SeqGen([intro_sent])
        permutation_gen = PerGen([prob_disease_sent,prob_shaky_given_disease_sent,prob_shaky_given_no_disease_sent])
        last_seq_gen = SeqGen([question])
        #soln
        soln_creater = solution_creater
        # create
        generators = [first_seq_gen,permutation_gen,last_seq_gen]
        problem = Problem(array_generators=generators,key_words_values=key_words_values,solution_creater=soln_creater)
        # make Q&A
        one_question = problem.generate_problem_statement()
        one_soln = problem.generate_solution()
        return one_question, one_soln

    def test_check_sample_problem(self):
        one_question, one_soln = self.probability_example_problem_unit_test()
        self.assertEqual(one_soln, 18.0/67 )

    def test_check_sample_problem_save_to_file(self):
        location = '/Users/brandomiranda/Dropbox (MIT)/eit_proj1_data/probability_example'
        question_name = 'probability_disease_question'
        answer_name = 'probability_disease_answer'
        n = 10
        #
        problem = self.get_problem()
        problem.generate_and_save_QAs_to_file(location,question_name,answer_name,n)

if __name__ == '__main__':
    unittest.main()
