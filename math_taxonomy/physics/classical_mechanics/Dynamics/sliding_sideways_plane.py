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
        self.description = 'A block is placed on a plane inclined at angle μ. The coefficient of friction between the' \
                           ' block and the plane is μ = tanμ. The block is given a kick so that it initially moves with ' \
                           'speed V horizontally along the plane (that is, in the direction perpendicular to the ' \
                           'direction pointing straight down the plane). What is the speed of the block after a very' \
                           ' long time?'
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
        if   self.debug:
            theta, mu, V, g, Vf = symbols('theta mu V g Vf')
        else:
            mu = symbols(chr(956))
            theta = symbols(chr(952))
            V, g, Vf = symbols('V g Vf')
        return theta, mu, V, g, Vf

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
            V_val, g_val, theta_val = 10, 10, 30
        else:
            g_val = random.choice([10, 9.8, 9.81, 9.807])
            V_val = np.random.randint(1, 10000, 2)/10
            theta_val = np.random.randint(0,90)

        return V_val, g_val, theta_val

    def Q(s, V_val, g_val, theta_val, theta, mu, V, g, Vf):
        '''
        A block is placed on a plane inclined at angle μ. The coefficient of friction between the' \
         block and the plane is μ = tanμ. The block is given a kick so that it initially moves with ' \
        speed V horizontally along the plane (that is, in the direction perpendicular to the ' \
        direction pointing straight down the plane). What is the speed of the block after a very' \
        long time?

        Important Note: first variables are the not consistent variables followed
        by the consistent ones. See sample QA example if you need too.
        '''
        #define some short cuts
        seqg, perg, choiceg = s.seqg, s.perg, s.choiceg
        info_V1 = seqg('A block is placed on a plane inclined at angle {0} = {1} degree. The coefficient of friction between the' \
         'block and the plane is {2} = tan({0}). The block is given a kick so that it initially moves with ' \
        'speed {3} = {4} (m/s) horizontally along the plane (that is, in the direction perpendicular to the ' \
        'direction pointing straight down the plane). '.format(theta, theta_val, mu, V, V_val))
        wanted_V1 = seqg(' What is the speed of the block {0} after a very' \
        'long time?'.format(Vf))
        g_sentence_V1 = seqg('Assume that gravitational acceleration is {0} = {1} (m/s^2)'.format(g, g_val))
        g_sentence_V2 = seqg('We know that gravitational acceleration is {0} = {1} (m/s^2)'.format(g, g_val))
        question_V1 = seqg(info_V1, wanted_V1, g_sentence_V1)
        question_V2 = seqg(info_V1, wanted_V1, g_sentence_V2)

        q = choiceg(question_V1, question_V2)
        return q

    def A(s, V_val, g_val, theta_val, theta, mu, V, g, Vf):
        '''
        Vf = V/2
        Important Note: first variables are the not consistent variables followed
        by the consistent ones. See sample QA example if you need too.
        '''
        #define some short cuts
        seqg, perg, choiceg = s.seqg, s.perg, s.choiceg
        Vf_val = V_val/2
        Vf_symbol = seqg('{0} = {1}/2'.format(Vf, V))
        answer_V1 = seqg('{0} (m/s)'.format(Vf_val))
        answer_V2 = seqg('{0} = {1} = {2} (m/s)'.format(Vf, Vf_symbol, Vf_val))
        a = choiceg(answer_V1, answer_V2)
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