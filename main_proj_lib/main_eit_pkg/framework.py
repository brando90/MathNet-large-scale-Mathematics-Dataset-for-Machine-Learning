import string
import numpy as np

import maps

import pdb


class Problem(object):

    def __init__(self,names_to_function):
        self.g = self.get_global_name(names_to_function)
        pass

    def get_global_name(self,names_to_function):
        # TODO: returns map obj mapping (name) to its corresponding (function)
        return


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
    def __init__(self):
        self.statements = [] # holds the functions that have the problem statements

    def get_statement(self,g):
        each_statements = self.process_chain(g)
        statement = self.join_statements(each_statements)
        return statement

class PerGen(Gen):
    def __init__(self):
        self.statements = [] # holds the functions that have the problem statements

    def get_statement(self,g):
        each_statements = self.process_chain(g)
        statement = self.join_statements(each_statements)
        return statement

#

def intro_sent(g):
    setence = "%s is a rare disease in which the victim has the delusion that he or she is being subjected to intense examination."%(g.disease_name)
    return setence

def prob_disease_sent(array, random=None):

    return sentence

def prob_shaky_given_disease_sent():
    pass

def prob_shaky_given_no_disease_sent():
    pass

##

if __name__ = '__main__':
    d = maps.NamedDict()
    disease_name = ['Quizphobia','Biophobia','Mathphobia','CSphobia']
    d.f = intro_sentence
