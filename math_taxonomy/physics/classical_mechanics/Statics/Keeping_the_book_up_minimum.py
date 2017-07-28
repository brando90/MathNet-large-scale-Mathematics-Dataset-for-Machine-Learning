# Completed
# Debug Status: RunTime error

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
        self.description = 'A book of mass M is positioned against a vertical wall. The coefficient of friction between ' \
                           'the book and the wall is μ. You wish to keep the book from falling by pushing on it with a ' \
                           'force F applied at an angle theta with respect to the horizontal. For a given theta, what is ' \
                           'the minimum F required?'
        # keywords about the question that could help to make this more searchable in the future
        self.keywords = ['Physics', 'Classical Mechanics', 'Mass', 'Wall', 'Friction', 'Force']
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
           mu = symbols(chr(956))
           m, g = symbols('m g')
           theta = symbols(chr(952))
        else:
            mu, m, g, theta = self.get_symbols(4)
        return mu, m, g, theta

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
            mu_val, m_val, g_val, theta_val = 1, 1, 10, 30
        else:
            mu_val = np.random.randint(0,1000)
            m_val = np.random.randint(1,10000)/10
            g_val = random.choice([10, 9.8, 9.81, 9.807])
            theta_val = np.random.randint(0, 89)

        return mu_val, m_val, g_val, theta_val

    def Q(s, mu_val, m_val, g_val, theta_val, mu, m, g, theta): #TODO change the signature of the function according to your question
        '''
        A book of mass M is positioned against a vertical wall. The coefficient of friction between
        the book and the wall is μ. You wish to keep the book from falling by pushing on it with a
        force F applied at an angle theta with respect to the horizontal. For a given theta, what is
        the minimum F required?

        Important Note: first variables are the not consistent variables followed
        by the consistent ones. See sample QA example if you need too.
        '''
        #define some short cuts
        seqg, perg, choiceg = s.seqg, s.perg, s.choiceg
        info_V1 = seqg('A book of mass {0} = {1} (kg) is positioned against a vertical wall. The coefficient of friction between'
        'the book and the wall is {2} = {3}. You wish to keep the book from falling by pushing on it with a'
        'force F applied at an angle {4} = {5} degree with respect to the horizontal.'.format(m, m_val, mu, mu_val, theta, theta_val))
        info_V2 = seqg(
            'There is a box with mass {0} = {1} (kg) that is positioned against a vertical wall. The coefficient of friction between'
            'the book and the wall is {2} = {3}. You insert a force F to the book at an angle {4} = {5} degree with respect '
            'to the horizontal.'.format(m, m_val, mu, mu_val, theta, theta_val))
        wanted_V1 = seqg(' For this given {0}, what is the minimum force required to keep the object from falling? The gravitational acceleration is'
                         ' {1} = {2} (m/s^2).'.format(theta, g, g_val))
        wanted_V2 = seqg(' Calculate the minimum force to keep the book up for this given {0}. '
                         'The gravitational acceleration is {1} = {2} (m/s^2).'.format(theta, g, g_val))
        wanted_V3 = seqg(' Based on given information find the minimum force to keep the object up. The gravitational acceleration is'
                         ' {0} = {1} (m/s^2).'.format(g, g_val))
        wanted_V4 = seqg(' Calculate the minimum force to keep the box up for this given {0}. '
                         'The gravitational acceleration is {1} = {2} (m/s^2).'.format(theta, g, g_val))

        question_1 = seqg(info_V1, wanted_V1)
        question_2 = seqg(info_V1, wanted_V2)
        question_3 = seqg(info_V1, wanted_V3)
        question_4 = seqg(info_V2, wanted_V1)
        question_5 = seqg(info_V2, wanted_V3)
        question_6 = seqg(info_V2, wanted_V4)
        q = choiceg(question_1, question_2, question_3, question_4, question_5, question_6)
        return q

    def A(s, mu_val, m_val, g_val, theta_val, mu, m, g, theta): #TODO change the signature of the function according to your answer
        '''
        forces in y direction: Fs + F*sin(theta) = mg
        forces in x direction: F*cos(theta) = N
        Fs = mu*N = mu*F*cos(theta)
        F = mg/(sin(theta) + mu*cos(theta))

        Important Note: first variables are the not consistent variables followed
        by the consistent ones. See sample QA example if you need too.
        '''

        seqg, perg, choiceg = s.seqg, s.perg, s.choiceg
        pi = np.pi
        theta_radian = (theta_val * pi) / 180
        F_min_val = m_val*g_val/(np.sin(theta_radian) + mu_val*np.cos(theta_radian))
        F_min = seqg('{0}*{1}/(sin({2})+{3}*cos({4}))'.format(m, g, theta, mu, theta))
        F_y = seqg('Fs + F*sin({0}) - m*g = 0'.format(theta))
        F_x = seqg('N - F*cos(0) = 0'.format(theta))
        F_s = seqg('Fs <= {0}*N'.format(mu))
        answer_1 = seqg('{0} (N)'.format(F_min_val))
        answer_2 = seqg('The minimum force can be calculated by this equation: {0}')
        answer_3 = seqg('The minimum force is {0} = {1} (N)'.format(F_min, F_min_val))
        explanation_init = seqg('In order to find the minimum force that keep the object on the wall we need to follow'
                                ' Newton laws. Because the object will is at rest the sum of the forces in each direction must be zero.')
        explanation_force_y = seqg(' The Newton equation in y direction is ', F_y)
        explanation_force_x = seqg(' The Newton equation in x direction is ', F_x)
        explanation_friction_force = seqg(' The general equation for friction force is ', F_s)
        conclusion = seqg(' After solving these three equations we can calculate the minimum force.')
        answer_4 = seqg(explanation_init, perg(explanation_force_x, explanation_force_y, explanation_friction_force),
                        conclusion, 'So the minimum force is ',answer_1)
        answer_5 = seqg(explanation_init, perg(explanation_force_x, explanation_force_y, explanation_friction_force),
                        conclusion, answer_2)
        answer_6 = seqg(explanation_init, perg(explanation_force_x, explanation_force_y, explanation_friction_force),
                        conclusion, answer_3)


        a = choiceg( answer_1, answer_2, answer_3, answer_4, answer_5, answer_6)
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