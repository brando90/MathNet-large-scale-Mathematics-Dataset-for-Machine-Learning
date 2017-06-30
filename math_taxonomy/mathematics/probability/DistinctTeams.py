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
        self.description = "Out of 30 people we want to form a team of 5 to play" 
        " basketball. How many such distinct teams can be formed?"
        # keywords about the question that could help to make this more searchable in the future
        self.keywords = ['combinatorics', 'distinct groups', 'combinations']
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
        if self.debug:
            basketball = "basketball"
        else:
            team_sports = utils.get_team_sports()
            basketball = self.get_names(1,names_list=team_sports)
            basketball = basketball
        return basketball

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
            total_num_people = 30
            group_size = 5
        else:
            total_num_people = random.randint(1,100) 
            group_size = random.randint(1,total_num_people)

        return total_num_people, group_size

    def Q(s, total_num_people, group_size, basketball): #TODO change the signature of the function according to your question
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

        first_sentence = "Out of {} people we want to form a team of {} to play.".format(total_num_people, group_size)
        second_sentence = "How many such distinct teams can be formed?"

        question1 = seqg(first_sentence, second_sentence)
        q = choiceg(question1)
        return q

    def A(s, total_num_people, group_size, basketball): #TODO change the signature of the function according to your answer
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
        ans = seqg(nC(total_num_people, group_size))
        ans_vnl = "{} distinct teams can be formed.".format(ans)
        a = choiceg(ans, ans_vnl)
        return a

if __name__ == '__main__':
    qagenerator = QA_constraint()
    print(qagenerator.get_single_qa(None))

