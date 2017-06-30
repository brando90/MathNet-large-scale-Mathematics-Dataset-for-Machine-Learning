from sympy import *
from sympy.functions.combinatorial.numbers import nC, nP, nT
import random
import numpy as np
import pdb

from qagen.qagen import *
from qagen import utils
from qagen import unit_test_for_user as user_test

# TODO: You can also put your quesiton example here

class QA_constraint(QAGen):

    def __init__(self):
        '''
        Initializer for your QA question.
        '''
        super().__init__()
        self.author = 'theosech'
        self.description = "The first three terms of a geometric sequence are 27, -9, and 3." 
        "Find the sum to infinity of the sequence." 
        # keywords about the question that could help to make this more searchable in the future
        self.keywords = ['geometric series sum', 'geometric series', 'sum to infinity']
        self.use_latex = True

    def seed_all(self,seed):
        '''
        Write the seeding functions of the libraries that you are using.
        Its important to seed all the libraries you are using because the
        framework will assume it can seed stuff for you. It needs this for
        the library to work.
        '''
        random.seed(seed)

    def init_consistent_qa_variables(self):
        """
        Defines and returns all the variables that need to be consistent
        between a question and an answer. Usually only names and variable/symbol
        names.

        Example: when generating MC questions the non consistent variables will
        be used to generate other options. However, the names, symbols, etc
        should remain consistent otherwise some answers will be obviously fake.

        Note: debug flag can be used to deterministically output a QA that has
        simple numbers to check the correctness of your QA.
        """
        return tuple()

    def init_qa_variables(self):
        '''
        Defines and returns all the variables that can vary between a
        question and an answer. Good examples are numerical values that might
        make the answers not obviously wrong.

        Example: when generating MC questions the non consistent variables will
        be used to generate other options. However, the names, symbols, etc
        should remain consistent otherwise some answers will be obviously fake.
        Numerical values that have been fully evaluated are a good example of
        how multiple choice answers can be generated.

        Note: debug flag can be used to deterministically output a QA that has
        simple numbers to check the correctness of your QA.
        '''
        if self.debug:
            a1 = 27
            r = -1/3
        else:
            a1 = random.randint(-1000,1000)
            r = random.randint(-999,999)/1000
        a2 = a1*r
        a3 = a2*r

        return a1,a2,a3,r

    def Q(s, a1,a2,a3,r): #TODO change the signature of the function according to your question
        '''
        Small question description.

        Important Note: first variables are the not consistent variables followed
        by the consistent ones. See sample QA example if you need too.
        '''
        #define some short cuts
        seqg, perg, choiceg = s.seqg, s.perg, s.choiceg
        s.use_latex = True
        # TODO
        #q_format1
        #q_format2
        #...
        # choices, try providing a few
        # these van include variations that are hard to encode with permg or variable substitution
        # example, NL variations or equaiton variations

        first_sentence = "The first three terms of a geometric sequence are {0}, {1}, and {2}.".format(a1,a2,a3)
        second_sentence = "Find the sum to infinity of the sequence."
        question = perg(first_sentence, second_sentence)

        q = choiceg(question)
        return q

    def A(s, a1,a2,a3,r): #TODO change the signature of the function according to your answer
        '''
        Small answer description.

        Important Note: first variables are the not consistent variables followed
        by the consistent ones. See sample QA example if you need too.
        '''
        #define some short cuts
        seqg, perg, choiceg = s.seqg, s.perg, s.choiceg
        # TODO
        #ans_sympy
        #ans_numerical
        #ans_vnl_vsympy1
        #ans_vnl_vsympy2
        # choices, try providing a few
        # these can include variations that are hard to encode with permg or variable substitution
        # example, NL variations or equaiton variations
        ans = a1/(1-r)
        ans_vnl = "The sum to infinity is {}.".format(ans)
        a = choiceg(ans, ans_vnl)
        return a

if __name__ == '__main__':
    qagenerator = QA_constraint()
    print(qagenerator.get_single_qa(None))

