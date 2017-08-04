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
        self.description = 'We project an object upward and measure the time that it ' \
                           'takes to pass two given points in both direction. Based on having gravitational acceleration' \
                           ' we aim to find one of the times. '
        # keywords about the question that could help to make this more searchable in the future
        self.keywords = ['Physics', 'Kinematics', 'Classical mechanics', 'Gravitational Acceleration', 'Time', 'Object']
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
            A, B, T_A, T_B, h, g = symbols('A B T_A T_B h g')
        else:
            A, B, T_A, T_B, h, g = self.get_symbols(6)
        return A, B, T_A, T_B, h, g

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
            T_A_val, h_val, g_val = 1, 2, 10
        else:
            T_A_val = np.random.randint(0, 1000)
            h_val = np.random.randint(0, 10000)
            g_val = random.choice([10, 9.8, 9.81, 9.807])
        return T_A_val, h_val, g_val

    def Q(s, A, B, T_A, T_B, h, g, T_A_val, h_val, g_val): #TODO change the signature of the function according to your question
        '''
        'We are trying to find g. So we project an object upward and measure the time that it takes to pass two given
        points in both direction.'

        Important Note: first variables are the not consistent variables followed
        by the consistent ones. See sample QA example if you need too.
        '''
        #define some short cuts
        seqg, perg, choiceg = s.seqg, s.perg, s.choiceg
        info_V1 = seqg('We project an object upward and measure the time it takes to pass two points {0} and {1} in both'
                       ' directions. ')
        info_V2 = seqg('We throw an object upward and measure the time it takes to pass two points {0} and {1} in both'
                       ' directions. ')
        given_V1 = seqg('It takes {0} = {1} (s) to pass point {2} and we know that'
                        ' gravitational acceleration is {3} = {4} (m/s^2) and that point {5} is positioned {6} = {7} (m)'
                        ' above point {8}.'.format(T_A, T_A_val, A, g, g_val, h, h_val, B))
        given_V2 = seqg('It takes {0} = {1} (s) to pass point {2} and we know that'
                        'point {2} is positioned {3} = {4} (m) above point {5}. Also, gravitational acceleration is {6}'
                        ' = {7} (m/s^2).'.format(T_A, T_A_val, B, h, h_val, A, g, g_val))
        wanted_V1 = seqg('Based on these information calculate the {0}, the time that it takes to pass point {1} in '
                         'both directions '.format(T_B, B))
        wanted_V2 = seqg('Calculate the time it takes for the object to pass point {0} in both direction, {1}.'.format(B, T_B))
        question_V1 = seqg(info_V1, given_V1, wanted_V1)
        question_V2 = seqg(info_V1, given_V1, wanted_V2)
        question_V3 = seqg(info_V1, given_V2, wanted_V1)
        question_V4 = seqg(info_V1, given_V2, wanted_V2)
        question_V5 = seqg(info_V2, given_V1, wanted_V1)
        question_V6 = seqg(info_V2, given_V1, wanted_V2)
        question_V7 = seqg(info_V2, given_V2, wanted_V1)
        question_V8 = seqg(info_V2, given_V2, wanted_V2)
        q = choiceg(question_V1, question_V2, question_V3, question_V4, question_V5, question_V6, question_V7,
                    question_V8)
        return q

    def A(s,  A, B, T_A, T_B, h, g, T_A_val, h_val, g_val):
        '''
        T_B= sqrt(-8*h/g + T_A^2)

        Important Note: first variables are the not consistent variables followed
        by the consistent ones. See sample QA example if you need too.
        '''

        seqg, perg, choiceg = s.seqg, s.perg, s.choiceg
        T_B_val = np.sqrt(-(8 * h_val / g_val )+ T_A_val ^ 2)
        T_B_eq = seqg('({0}^2  - (8*{1}/{2}) )^1/2'.format(T_A, h, g))
        info_V1 = seqg('The {0} can be found via this equation, ', T_B_eq, '. Given the values {0} = {1} (m/s^2).'
                       .format(T_B, T_B_val))
        info_V2 = seqg('{0} = ', T_B_eq, ' = {1} (m/s^2).'.format(T_B, T_B_val))
        answer_V1 = T_B_val
        answer_V2 = seqg(info_V1)
        answer_V3 = seqg(info_V2)
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