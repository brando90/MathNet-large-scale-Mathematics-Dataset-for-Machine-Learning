from sympy import *
import random
import numpy as np

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
        self.author = 'Elaheh Ahmadi'
        self.description = 'A massless pulley hangs from a fixed support. A massless string connecting two masses,' \
                           ' m1 and m2, hangs over the pulley. Find the acceleration of the mass m1?'

        # keywords about the question that could help to make this more searchable in the future
        self.keywords = ['Physics' ,'Classical Mechanics' ,'Block', 'Mass', 'Slide', 'Friction', 'Plane',
                         'Moving Plane', 'Acceleration']
        self.use_latex = True

    def seed_all(self,seed):
        '''
        Write the seeding functions of the libraries that you are using.
        Its important to seed all the libraries you are using because the
        framework will assume it can seed stuff for you. It needs this for
        the library to work.
        '''
        random.seed(seed)
        np.random.seed(seed)

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
            m1, m2, g, a1 = symbols('m1 m2 g a1')
        else:
            m1, m2, g, a1 = symbols('m1 m2 g a1')
        return m1, m2, g, a1

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
            m1_val, m2_val, g_val = 1, 2, 10
        else:
            m1_val, m2_val = np.random.randint(1, 100000, 2)/10
            g_val = random.choice([10, 9.8, 9.81, 9.807])
        return m1_val, m2_val, g_val

    def Q(s, m1_val, m2_val, g_val, m1, m2, g, a1):
        '''
        A massless pulley hangs from a fixed support. A massless string connecting two masses,
        m1 and m2, hangs over the pulley. Find the acceleration of the mass m1?

        Important Note: first variables are the not consistent variables followed
        by the consistent ones. See sample QA example if you need too.
        '''
        #define some short cuts
        seqg, perg, choiceg = s.seqg, s.perg, s.choiceg
        info_V1 = seqg('A massless pulley hangs from a fixed support. A massless string connecting two masses,'
                        '{0} = {1} (kg) and {2} = {3} (kg), hangs over the pulley.'.format(m1, m1_val, m2, m2_val))
        info_V2 = seqg('A massless pulley hangs from a fixed support. A massless string connecting two masses,'
                       '0} = {1} (kg) and {2} = {3} (kg), hangs over the pulley.'.format(m1, m1_val, m2, m2_val))
        wanted_V1 = seqg('Find the acceleration {0} of the mass {1}.'.format(a1, m1))
        wanted_V2 = seqg('Calculate the acceleration {0} of the mass {1}.'.format(a1, m1))
        wanted_V3 = seqg('What is the acceleration {0} of the mass {1}'.format(a1, m1))
        wanted_V4 = seqg('Based on given informations what is the acceleration {0} of the mass {1}.'.format(a1, m1))
        g_sentence_V1 = seqg('Assume that gravitational acceleration is {0} = {1} (m/s^2)'.format(g, g_val))
        g_sentence_V2 = seqg('We know that gravitational acceleration is {0} = {1} (m/s^2)'.format(g, g_val))
        question_V1 = seqg(info_V1, g_sentence_V1, wanted_V1)
        question_V2 = seqg(info_V1, g_sentence_V1, wanted_V2)
        question_V3 = seqg(info_V1, g_sentence_V1, wanted_V3)
        question_V4 = seqg(info_V1, wanted_V1, g_sentence_V1)
        question_V5 = seqg(info_V1, wanted_V2, g_sentence_V1)
        question_V6 = seqg(info_V1, wanted_V3, g_sentence_V1)
        question_V7 = seqg(info_V1, g_sentence_V2, wanted_V1)
        question_V8 = seqg(info_V1, g_sentence_V2, wanted_V2)
        question_V9 = seqg(info_V1, g_sentence_V2, wanted_V3)
        question_V10 = seqg(info_V1, wanted_V1, g_sentence_V2)
        question_V11 = seqg(info_V1, wanted_V2, g_sentence_V2)
        question_V13 = seqg(info_V1, wanted_V3, g_sentence_V2)
        question_V14 = seqg(info_V2, g_sentence_V1, wanted_V1)
        question_V15 = seqg(info_V2, g_sentence_V1, wanted_V2)
        question_V16 = seqg(info_V2, g_sentence_V1, wanted_V3)
        question_V17 = seqg(info_V2, wanted_V1, g_sentence_V1)
        question_V18 = seqg(info_V2, wanted_V2, g_sentence_V1)
        question_V19 = seqg(info_V2, wanted_V3, g_sentence_V1)
        question_V20 = seqg(info_V2, g_sentence_V2, wanted_V1)
        question_V21 = seqg(info_V2, g_sentence_V2, wanted_V2)
        question_V22 = seqg(info_V2, g_sentence_V2, wanted_V3)
        question_V23 = seqg(info_V2, wanted_V1, g_sentence_V2)
        question_V24 = seqg(info_V2, wanted_V2, g_sentence_V2)
        question_V12 = seqg(info_V2, wanted_V3, g_sentence_V2)
        question_V25 = seqg(info_V1, g_sentence_V1, wanted_V4)
        question_V26 = seqg(info_V1, wanted_V4, g_sentence_V1)
        question_V27 = seqg(info_V1, g_sentence_V2, wanted_V4)
        question_V28 = seqg(info_V1, wanted_V4, g_sentence_V2)
        question_V29 = seqg(info_V2, g_sentence_V1, wanted_V4)
        question_V30 = seqg(info_V2, wanted_V4, g_sentence_V1)
        question_V31 = seqg(info_V2, g_sentence_V2, wanted_V4)
        question_V32 = seqg(info_V2, wanted_V4, g_sentence_V2)

        q = choiceg(question_V1, question_V2, question_V3, question_V4, question_V5, question_V6, question_V7,
                    question_V8, question_V9, question_V10, question_V11, question_V12, question_V13, question_V14,
                    question_V15, question_V16, question_V17, question_V18, question_V19, question_V20, question_V21,
                    question_V22, question_V23, question_V24, question_V25, question_V26, question_V27, question_V28,
                    question_V29, question_V30, question_V31, question_V32)
        return q

    def A(s, m1_val, m2_val, g_val, m1, m2, g, a1):
        '''
        a1 = (m1 - m2)g/(m1+m2)

        Important Note: first variables are the not consistent variables followed
        by the consistent ones. See sample QA example if you need too.
        '''
        #define some short cuts
        seqg, perg, choiceg = s.seqg, s.perg, s.choiceg
        a1_val = g_val*(m1_val - m2_val)/m1_val
        a1_symbol = seqg('{0}*({1}-{2})/({1}+{2})'.format(g, m1, m2))
        answer_V1 = seqg('{0} (m/s^2)'.format(a1_val))
        answer_V2 = seqg('{0} = {1} = {2} (m/s^2)'.format(a1, a1_symbol, a1_val))
        answer_V3 = seqg('The acceleration of the mass {0} can be found via the equation {1}. Given the values, '
                         '{2} = {3} (m/s^2).'.format(m1, a1_symbol, a1, a1_val))
        a = choiceg(answer_V1, answer_V2, answer_V3)
        return a

    ##

    def get_qa(self,seed):
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

## Some helper functions to check the formats are coming out correctly

##

def check_single_question_debug(qagenerator):
    '''
    Checks by printing a single quesiton on debug mode
    '''
    qagenerator.debug = True
    q,a = qagenerator.get_qa(seed=1)
    print('qagenerator.debug = ', qagenerator.debug)
    print('q: ', q)
    print('a: ', a)

def check_single_question(qagenerator):
    '''
    Checks by printing a single quesiton on debug mode
    '''
    q,a = qagenerator.get_qa(seed=random.randint(0,1000))
    print('qagenerator.debug = ', qagenerator.debug)
    print('q: ', q)
    print('a: ', a)

def check_mc(qagenerator):
    '''
    Checks by printing the MC(Multiple Choice) option
    '''
    nb_answers_choices = 10
    for seed in range(3):
        #seed = random.randint(0,100)
        q_str, ans_list = qagenerator.generate_single_qa_MC(nb_answers_choices=nb_answers_choices,seed=seed)
        print('\n-------seed-------: ',seed)
        print('q_str:\n',q_str)
        print('-answers:')
        print("\n".join(ans_list))

def check_many_to_many(qagenerator):
    for seed in range(3):
        q,a = qagenerator.generate_many_to_many(nb_questions=4,nb_answers=3,seed=seed)
        print('-questions:')
        print("\n".join(q))
        print('-answers:')
        print("\n".join(a))

def check_many_to_one_consis(qagenerator):
    for seed in range(3):
        print()
        q,a = qagenerator.generate_many_to_one(nb_questions=5,seed=seed)
        print("\n".join(q))
        print('a: ', a)
        #print("\n".join(a))

def check_many_to_one_consistent_format(qagenerator):
    nb_qa_pairs,nb_questions = 10,3
    qa_pair_list = qagenerator.generate_many_to_one_consistent_format(nb_qa_pairs,nb_questions)
    for q_list,a_consistent_format in qa_pair_list:
        print()
        print("\n".join(q_list))
        print('a: ', a_consistent_format)

if __name__ == '__main__':
    qagenerator = QA_constraint()
    check_single_question(qagenerator)
    ## uncomment the following to check formats:
    #check_mc(qagenerator)
    #check_many_to_one(qagenerator)
    #check_one_to_many(qagenerator)
    #check_many_to_one_consistent_format(qagenerator)
    ## run unit test given by framework
    user_test.run_unit_test_for_user(QA_constraint)