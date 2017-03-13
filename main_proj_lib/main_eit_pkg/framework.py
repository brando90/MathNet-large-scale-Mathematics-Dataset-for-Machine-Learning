import string
import numpy as np

import maps

import pdb


class Problem(object):

    def __init__(self,):
        #self.g = self.get_global_name(names_to_function)
        #


    def get_global_name(self,names_to_function):
        # TODO: returns map obj mapping (name) to its corresponding (function)
        return

    def generate_problem_statement(self):



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
        each_statements = shuffle(each_statements) # TODO
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
    sentence = 'A person with %s has %ss with probability %f'(g.disease_name,g.symptom,g.p_s_f)
    return sentence

def prob_shaky_given_no_disease_sent(g):
    sentence = 'A person without %s has %s with probability %f'(g.disease_name,g.symptom,g.p_s_f)
    return sentence

#

def get_disease_names():
    diseases = ['CSphobia','Biophobia','Mathphobia'] #TODO: re-think
    #
    
    return

##

def probability_example_problem():
    first_seq_gen = [intro_sent]
    permutation_gen = [prob_disease_sent,prob_shaky_given_disease_sent,prob_shaky_given_no_disease_sent]
    #
    key_words_values = {'disease_name':}
    return

if __name__ = '__main__':
