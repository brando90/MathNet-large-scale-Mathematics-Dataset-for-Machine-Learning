from sympy import *
import random
import collections
import string
import unittest

import pdb

from qagen.qaops import *
from qagen import utils

class QA:
    '''
    QA indicates the "format" a question should have.
    '''

    def seed_all(self, seed):
        raise NotImplementedError

    def init_consistent_qa_variables(self, debug):
        raise NotImplementedError

    def init_qa_variables(self,*args,**kwargs):
        raise NotImplementedError

    def Q(self,*args,**kwargs):
        raise NotImplementedError

    def A(self,*args,**kwargs):
        raise NotImplementedError

class QAGen(QA,QAOps):

    def _create_all_variables(self):
        '''
        Create distinct variables for qa and register them for the current QA
        '''
        # TODO:
        # is the best way to implement this is to try as many times to decrease prob of duplicates?
        # while there are duplicats keep trying to generate different
        tries = 0
        while tries < 30:
            variables_consistent = self.init_consistent_qa_variables()
            self.register_qa_variables(variables_consistent)
            variables = self.init_qa_variables()
            self.register_qa_variables(variables)
            # if no duplicates variable generation was successful
            if not utils.duplicates_present(variables_consistent,variables):
                break
            tries +=1
        return variables, variables_consistent

    def generate_single_MC(self,nb_answers_choices,seed):
        '''
        Generates single MC (Multiple Choice) question with nb_answers_choices
        number of choice answers.

        '''
        self.seed_all(seed)
        # get variables for qa and register them for the current q,a
        variables, variables_consistent = self._create_all_variables()
        # set q and correct a
        q_str = self.Q(*variables,*variables_consistent)
        correct_a_str = self.A(*variables,*variables_consistent)
        # collect alternative answers
        ans_list = [correct_a_str]
        for i in range(nb_answers_choices-1):
            #self.seed_all(seed)
            variables = self.init_qa_variables()
            a_str = self.A(*variables,*variables_consistent)
            ans_list.append(a_str)
        # randomize where the answer is
        ans_list = random.sample( ans_list, len(ans_list) )
        mc = q_str, ans_list
        return mc

    def generate_many_to_one(self,nb_questions,seed):
        self.seed_all(seed)
        # get variables for qq
        variables_consistent = self.init_consistent_qa_variables()
        variables = self.init_qa_variables()
        # set q and correct a
        q_list = []
        for i in range(nb_questions):
            q_str = self.Q(*variables,*variables_consistent)
            q_list.append(q_str)
        # get answer
        a_str = self.A(*variables,*variables_consistent)
        return q_list, a_str

    def generate_one_to_many(self,nb_answers,seed):
        self.seed_all(seed)
        # get variables for qq
        variables_consistent = self.init_consistent_qa_variables()
        variables = self.init_qa_variables()
        # set q and correct a
        q_str = self.Q(*variables,*variables_consistent)
        correct_a_str = self.A(*variables,*variables_consistent)
        # collect alternative answers
        ans_list = [correct_a_str]
        for i in range(nb_answers-1):
            a_str = self.A(*variables,*variables_consistent)
            ans_list.append(a_str)
        return q_str, ans_list

    def generate_many_to_one_consistent_format(self,nb_different_qa,seed_output_format,nb_different_q=2):
        '''

        We want consistent output. So the seed for the answers accross all variety of
        questions must be the same

        '''
        #TODO: doesn't actually work. Why?
        qa_pair_list = []
        for seed_qa in range(nb_different_qa):
            q_list = []
            self.seed_all(seed_qa)
            # get variables for qa
            variables_consistent = self.init_consistent_qa_variables()
            variables = self.init_qa_variables()
            # now give NL variety to the qustions
            for seed_q in range(nb_different_q):
                q_str = self.Q(*variables,*variables_consistent)
                q_list.append(q_str)
            self.seed_all(seed_output_format)
            correct_a_str = self.A(*variables,*variables_consistent)
            qa_pair_list.append( (q_list,correct_a_str) )
        return qa_pair_list

    def get_single_qa(self,seed):
        '''
        Example of how Q,A are formed in general.
        '''
        # set seed
        self.seed_all(seed)
        # get variables for qa and register them for the current q,a
        variables, variables_consistent = self._create_all_variables()
        # get concrete qa strings
        q_str = self.Q(*variables,*variables_consistent)
        a_str = self.A(*variables,*variables_consistent)
        return q_str, a_str
##

class TestStringMethods(unittest.TestCase):

    def test_MC(self):
        pass

if __name__ == '__main__':
    unittest.main()
