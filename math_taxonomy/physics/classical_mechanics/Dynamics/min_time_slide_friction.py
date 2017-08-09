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
        self.description = 'A block starts at rest and slides down plane with coefficient of kinetic friction, μ inclined ' \
                           'at angle theta. What should theta be so that the block travels a given horizontal distance' \
                           ' in the minimum amount of time?'
        # keywords about the question that could help to make this more searchable in the future
        self.keywords = ['physics' ,'classical mechanics' ,'block', 'mass', 'Slide', 'Friction', 'Plane',
                         'Minimum Time']
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
            m, theta, l, g, mu = symbols('m theta l g mu')
        else:
            m = symbols(random.choice(['m', 'M']))
            theta = symbols(chr(952))
            l = symbols(random.choice(['l', 'L']))
            g = symbols('g')
            mu =  symbols(chr(956))
        return m, theta, l, g, mu

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
            m_val = 1
            g_val = 10
            l_val = 1
            mu_val = 0.5
        else:
            m_val = np.random.randint(1, 10000)/10
            g_val = random.choice([10, 9.8, 9.81, 9.807])
            l_val = np.random.randint(1, 1000000)
            mu_val = np.random.randint((1, 10000)/100

        return m_val, g_val, l_val, mu_val

    def Q(s,m_val, g_val, l_val, mu_val, m, theta, l, g, mu):
        '''
        A block starts at rest and slides down a frictionless plane inclined at angle μ.
        What should μ be so that the block travels a given horizontal distance in the minimum amount of time?

        Important Note: first variables are the not consistent variables followed
        by the consistent ones. See sample QA example if you need too.
        '''
        #define some short cuts
        seqg, perg, choiceg = s.seqg, s.perg, s.choiceg
        info_V1 = seqg('A block with mass {0} = {1} (kg) starts at rest and slides down a plane with coefficient of '
                       'kinetic friction, {2} = {3} inclined at angle {4}.'.format(m, m_val, mu, mu_val, theta))
        info_V2 = seqg('An object with mass {0} = {1} (kg) starts sliding down a plane with coefficient of '
                       'kinetic friction, {2} = {3} inclined at angle {4}.'.format(m, m_val, mu, mu_val, theta))
        wanted_V1 = seqg('What should {0} be so that the block travels a given horizontal distance {1} = {2} (m) in the minimum '
                         'amount of time?'.format(theta, l, l_val))
        wanted_V2 = seqg('Find the {0} in which the object travels a given horizontal distance {1} = {2} (m) in the minimum amout'
                         ' of time?'.format(theta, l, l_val))
        wanted_V3 = seqg('Calculate a {0} that the object travels a given horizontal distance {1} = {2} (m) in the minimum amount '
                         'of time.'.format(theta, l, l_val))
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

        q = choiceg(question_V1, question_V2, question_V3, question_V4, question_V5, question_V6, question_V7,
                    question_V8, question_V9, question_V10, question_V11, question_V12, question_V13, question_V14,
                    question_V15, question_V16, question_V17, question_V18, question_V19, question_V20, question_V21,
                    question_V22, question_V23, question_V24)
        return q

    def A(s,m_val, g_val, l_val, mu_val, m, theta, l, g, mu):
        '''
        tan(2*theta) = -1/mu

        Important Note: first variables are the not consistent variables followed
        by the consistent ones. See sample QA example if you need too.
        '''
        #define some short cuts
        seqg, perg, choiceg = s.seqg, s.perg, s.choiceg
        theta_val_rad = (1/2)*np.arctan(-1/mu_val)
        ans_val_degree = theta_val_rad * 180 / np.pi
        ans_symbol = seqg('{0} = {1} degree'.format(theta, ans_val_degree))
        ans_symbol_rad = seqg('{0} = {1} radian'.format(theta, theta_val_rad))
        a_x = symbols('a_x')
        a_x_val = seqg('{0}*(sin({1})-{2}*cos({1}))'.format(g, theta, mu))
        description_V1 = seqg('We want to maximize the acceleration in the x direction which is {0} = {1}. So,'.format(a_x, a_x_val))
        description_V2 = seqg('In order to minimize the time in takes to pass a given horizontal distance we should '
                              'maximize the acceleration in that direction which is {0} = {1}. So,'.format(a_x, a_x_val))
        conclusion_sentence_V1 = seqg('The {0} in which the object will passes {1} = {2} (m) in the minimum time is '
                                      .format(theta, l, l_val))
        answer_V1 = seqg(description_V1, conclusion_sentence_V1, theta_val_rad, ' radian')
        answer_V2 = seqg(description_V1, conclusion_sentence_V1, ans_val_degree, ' degree')
        answer_V3 = seqg(description_V1, conclusion_sentence_V1, ans_symbol)
        answer_V4 = seqg(description_V1, conclusion_sentence_V1, ans_symbol_rad)
        answer_V5 = seqg(description_V2, conclusion_sentence_V1, theta_val_rad, ' radian')
        answer_V6 = seqg(description_V2, conclusion_sentence_V1, ans_val_degree, ' degree')
        answer_V7 = seqg(description_V2, conclusion_sentence_V1, ans_symbol)
        answer_V8 = seqg(description_V2, conclusion_sentence_V1, ans_symbol_rad)
        a = choiceg(answer_V1, answer_V2, answer_V3, answer_V4, answer_V5, answer_V6, answer_V7, answer_V8)
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