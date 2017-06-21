from sympy import *
import random
import collections
import string

import pdb
import unittest

class QAFormat:

    def seed_all(self, seed):
        raise NotImplementedError

    def init_consistent_qa_variables(self, seed):
        raise NotImplementedError

    def init_qa_variables(self,*args,**kwargs):
        raise NotImplementedError

    def Q(self,*args,**kwargs):
        raise NotImplementedError

    def A(self,*args,**kwargs):
        raise NotImplementedError

class QAGen(QAFormat):

    def generate_MC(self,nb_answers,seed):
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

class TestStringMethods(unittest.TestCase):

    def test_MC(self):
        pass

if __name__ == '__main__':
    unittest.main()
