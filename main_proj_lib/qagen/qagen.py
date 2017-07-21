from sympy import *
import random
import collections
import string
import unittest

import pdb

from qagen.delayed_execution import *
from qagen.qaops import *
from qagen import utils

class QA:
    '''
    QA indicates the "format" a question should have.
    '''

    def seed_all(self, seed):
        raise NotImplementedError

    def init_consistent_qa_variables(self, debug=False):
        ''' returns consistent variables as list'''
        raise NotImplementedError

    def init_qa_variables(self,*args,**kwargs):
        '''returns consistent variables as list'''
        raise NotImplementedError

    def Q(self,*args,**kwargs):
        raise NotImplementedError

    def A(self,*args,**kwargs):
        raise NotImplementedError

class QAGen(QA,QAOps):

    def _to_hashable_(self, variables):
        '''
        Convert a set of variables to a format that can be hashed to check for duplicates
        '''
        return variables

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
            if not utils.duplicates_present(self._to_hashable_(variables_consistent),self._to_hashable_(variables)):
                break
            tries +=1
        self.reset_variables_states()
        return variables, variables_consistent

    def generate_single_qa_MC(self,nb_answers_choices,seed):
        '''
        Generates single MC (Multiple Choice) question with nb_answers_choices
        number of choice answers.
        Note that "single" means that the variables for the question and answer
        are the same, just maybe the formats might be different.
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
            # note: its not neccessary to seed because the random number generators move their random states as their functions are used
            #self.seed_all(seed)
            variables = self.init_qa_variables()
            a_str = self.A(*variables,*variables_consistent)
            ans_list.append(a_str)
        # randomize where the answer is
        ans_list = random.sample( ans_list, len(ans_list) )
        for i in range(len(ans_list)):
            if ans_list[i] == correct_a_str:
                index_ans = i
                break
        mc = q_str, ans_list, index_ans
        return mc

    def generate_single_qa_many_to_one(self,nb_questions,seed):
        '''
        Generates single question with nb_questions number of choice questions.
        Note that "single" means that the variables for the question and answer
        are the same, just maybe the formats might be different.
        '''
        self.seed_all(seed)
        # get variables for qa and register them for the current q,a
        variables, variables_consistent = self._create_all_variables()
        # set q and correct a
        q_list = []
        for i in range(nb_questions):
            q_str = self.Q(*variables,*variables_consistent)
            q_list.append(q_str)
        # get answer
        a_str = self.A(*variables,*variables_consistent)
        return q_list, a_str

    def generate_one_to_many(self,nb_answers,seed):
        '''
        Generates single question with nb_answers number of choice answers.
        Note that "single" means that the variables for the question and answer
        are the same, just maybe the formats might be different.
        '''
        self.seed_all(seed)
        # get variables for qa and register them for the current q,a
        variables, variables_consistent = self._create_all_variables()
        # set q and correct a
        q_str = self.Q(*variables,*variables_consistent)
        # collect alternative correct answers
        ans_list = []
        for i in range(nb_answers):
            a_str = self.A(*variables,*variables_consistent)
            ans_list.append(a_str)
        return q_str, ans_list

    def generate_many_to_many(self,nb_questions,nb_answers,seed):
        '''
        Generates single question with nb_answers number of choice question.
        Note that "single" means that the variables for the question and answer
        are the same, just maybe the formats might be different.
        '''
        self.seed_all(seed)
        # get variables for qa and register them for the current q,a
        variables, variables_consistent = self._create_all_variables()
        # set q and correct a
        q_list = []
        for i in range(nb_questions):
            q_str = self.Q(*variables,*variables_consistent)
            q_list.append(q_str)
        # collect alternative correct answers
        ans_list = []
        for i in range(nb_answers):
            a_str = self.A(*variables,*variables_consistent)
            ans_list.append(a_str)
        return q_list, ans_list

    def generate_many_to_one_consistent_format(self,nb_qa_pairs,nb_questions,seed_output_format=1):
        '''
        Generates many q,a pairs as many nb_qa_pairs and each will
        have nb_q total number of ways to phrase the question.
        Note that each q,a pair is as follows (Q_i,A_i)_i=(Q_i[q_i1,...,q_inb_q],a_i)
        in other words many different ways to phrase the question map to the same
        one answer.
        The answer is expressed consistently accross different versions of the q,a
        pair.
        '''
        qa_pair_list = []
        for seed_qa in range(nb_qa_pairs):
            self.debug = False # Note this is a temporary hack to turn of randomness of choiceg,permg
            self.reset_variables_states()
            q_list = []
            self.seed_all(seed_qa)
            # get variables for qa and register them for the current q,a
            variables, variables_consistent = self._create_all_variables()
            # now give NL variety to the qustions
            for seed_q in range(nb_questions):
                q_str = self.Q(*variables,*variables_consistent)
                q_list.append(q_str)
            self.seed_all(seed_output_format) # TODO why doesn't it work with this?
            #self.debug = True # Note this is a temporary hack to turn of randomness of choiceg,permg
            correct_a_str = self.A(*variables,*variables_consistent)
            qa_pair_list.append( (q_list,correct_a_str) )
        return qa_pair_list


    def reset_variables_states(self):
        '''
        Resets to empty list the lists keeping track of variables.
        '''
        self.names = []
        self.sympy_vars = []

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
