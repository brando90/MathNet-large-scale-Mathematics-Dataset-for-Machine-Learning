from sympy import *
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
        self.description = "Sally just graduated from high school. Sally was accepted to three reputable "
        self.description += "colleges. With probability 0.2 Sally attends Yale . With probability 0.3 Sally attends MIT . "
        self.description += "With probability 0.5 Sally attends Duke . Sally is either happy or sad. If Sally attends Yale "
        self.description += "Sally is happy with probability 0.4 . If Sally attends MIT Sally is happy with probability "
        self.description += "0.5 . If Sally attends Duke Sally is happy with probability 0.6 . What is the probability "
        self.description += "that Sally is happy in college?"
        # keywords about the question that could help to make this more searchable in the future
        self.keywords = ['conditional probability', 'probability', 
        'colleges','happiness']
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
            Yale = "Yale"
            MIT = "MIT"
            Duke = "Duke"
            Sally = "Sally"
        else:
            colleges = utils.get_colleges()
            Yale, MIT, Duke = self.get_names(3, names_list=colleges)
            Sally = self.get_names(1)[0]
        return Yale, MIT, Duke, Sally

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
            prob_col_1 = 0.2
            prob_col_2 = 0.3
            prob_col_3 = 1 - prob_col_1 - prob_col_2
            prob_happy_1, prob_happy_2, prob_happy_3 = 0.4, 0.5, 0.6
       
        else:
            lb, ub = 0, 1
            prob_col_1 = random.uniform(lb, ub)
            prob_col_2 = random.uniform(lb, 1-prob_col_1)
            prob_col_3 = 1 - prob_col_1 - prob_col_2
            prob_happy_1 = random.uniform(lb,ub)
            prob_happy_2 = random.uniform(lb,ub)    
            prob_happy_3 = random.uniform(lb,ub)    
        return prob_col_1, prob_col_2, prob_col_3, prob_happy_1, prob_happy_2, prob_happy_3

    def Q(s,prob_col_1, prob_col_2, prob_col_3, prob_happy_1, prob_happy_2, prob_happy_3,Yale, MIT, Duke, Sally): #TODO change the signature of the function according to your question
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
        beggining_q = seqg(Sally, "just graduated from high school. Sally was accepted to three reputable colleges.")
        perm1 = seqg("With probability", prob_col_1, "Sally attends", Yale, ".")
        perm2 = seqg("With probability", prob_col_2, "Sally attends", MIT, ".")
        perm3 = seqg("With probability", prob_col_3, "Sally attends", Duke, ".")
        perm7 = seqg(Sally ,"is either happy or sad.")
        perm4 = seqg("If Sally attends", Yale, "Sally is happy with probability", prob_happy_1, ".")
        perm5 = seqg("If Sally attends", MIT, "Sally is happy with probability", prob_happy_2, ".")
        perm6 = seqg("If Sally attends", Duke, "Sally is happy with probability", prob_happy_3, ".")
        perm8 = seqg("What is the probability that", Sally ,"is happy in college?")

        permutable_part_1 = perg(perm1, perm2, perm3)
        permutable_part_2 = perg(perm4, perm5, perm6)

        question1 = seqg(beggining_q, permutable_part_1, perm7, permutable_part_2, perm8)
        q = choiceg(question1)
        return q

    def A(s,prob_col_1, prob_col_2, prob_col_3, prob_happy_1, prob_happy_2, prob_happy_3,Yale, MIT, Duke, Sally): #TODO change the signature of the function according to your answer
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
        ans_numerical = seqg(prob_col_1*prob_happy_1 + prob_col_2*prob_happy_2 + prob_col_3*prob_happy_3)
        ans_vnl = Sally + " is happy with probability {0}.".format(str(ans_numerical))
        a = choiceg(ans_numerical, ans_vnl)
        return a

if __name__ == '__main__':
    qagenerator = QA_constraint()
    user_test.run_unit_test_for_user(QA_constraint)
    print(qagenerator.get_single_qa(None))

