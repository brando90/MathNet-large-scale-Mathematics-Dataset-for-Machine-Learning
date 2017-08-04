#completed
# Debbug Status: tRun Time Error

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
        self.author = 'Elaheh Ahmadi' #TODO your full name
        self.description = 'A block sits on a plane that is inclined at an angle theta. Assume that the friction force is ' \
                           'large enough to keep the block at rest. What is the maximum sum of horizontal components ' \
                           'of friction and normal forces?'


        # keywords about the question that could help to make this more searchable in the future
        self.keywords = ['Plane', 'Block', 'Friction', 'Force', 'Normal Force', 'maximum', 'theta', 'horizontal force'] #TODO keywords to search type of question
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
            g, m = symbols('g m')
            theta = symbols(chr(952))
        else:
            g, m = symbols('g m')
            theta = symbols(chr(952))
        return g, theta, m

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
            g_val, m_val = 10, 1
        else:
            g_val = random.choice([10, 9.8, 9.81, 9.807])

            m_val = np.random.randint(1,100000)/10
        return g_val, m_val

    def Q(s, g_val, m_val , g, theta, m): #TODO change the signature of the function according to your question
        '''
        A block sits on a plane that is inclined at an angle theta. Assume that the friction force is large enough to
        keep the block at rest. What is the horizontal components of the friction.

        Important Note: first variables are the not consistent variables followed
        by the consistent ones. See sample QA example if you need too.
        '''
        #define some short cuts
        seqg, perg, choiceg = s.seqg, s.perg, s.choiceg

        question_1 = seqg('A block sits on a plane that is inclined at an angle', theta,'. Assume '
        'that the friction force is large enough to keep the block at rest. What is the maximum '
                          ' sum of horizontal components of friction force and normal force and in what ', theta, ' is it maximum'
                          'The object mass is ', Eq(m, m_val), ' (kg) and the gravitational acceleration is,'
                          , Eq(g, g_val), ' (m/s^2).')
        question_2 = seqg('An object with ', Eq(m, m_val), ' (kg) is sited on a plane that is inclined at an angle', theta,'.'
                          ' We know that the the friction force is large enough to keep the block at rest. '
                          'In what ', theta, ' the sum of horizontal components of friction force and normal force are maximum and what is the maximum value of this sum.'
                                                  ' The gravitational acceleration is ', Eq(g, g_val), ' (m/s^2).')
        question_3 = seqg('There is an object in rest on a plane that is inclined at an angle', theta,'. The mass of the object is'
                          ' ', Eq(m, m_val), ' (kg) What should be the angle of the plane so that the sum of horizontal'
                                             ' components of friction force and normal force maximum and what is the value of the sum of forces. The gravitational '
                                             'acceleration is ,', Eq(g, g_val), ' (m/s^2).')

        q = choiceg(question_1, question_2, question_3)
        return q

    def A(s, g_val, m_val, g, theta, m): #TODO change the signature of the function according to your answer
        '''
        F_total = m*g*cos(theta)*sin(theta) + m*g*sin(theta)*cos(theta) =  m*g*(sin(2*theta))/2
        For theta = pi/2 the horizontal force would reach its maximum value.
        Important Note: first variables are the not consistent variables followed
        by the consistent ones. See sample QA example if you need too.
        '''
        #define some short cuts
        seqg, perg, choiceg = s.seqg, s.perg, s.choiceg
        pi = np.pi
        char_pi = chr(960)
        theta_val_rad = round(pi/2,2)
        theta_val_degree = 45.0
        theta_val_char = char_pi+'/2'
        friction_force = round(m_val*g_val*np.sin(theta_val_rad),2)
        friction_force_horizontal = round(friction_force * np.cos(theta_val_rad), 2)
        normal_force = round(m_val*g_val*np.cos(theta_val_rad),2)
        normal_force_horizontal = round(normal_force * np.sin(theta_val_rad),2)
        total_horizontal_force = normal_force_horizontal + friction_force_horizontal

        #### WORK ON THE ANSWERSSSSSSSSSSSSS ######## 
        answer_1 = seqg('The ', theta ,'in which sum of horizontal component of friction force and normal force is '
                                            'maximum is', char_pi,'/2. And the sum of horizontal forces is ', total_horizontal_force, ' (N)')
        answer_2 = seqg('The ', theta, ' in which sum of horizontal component of friction force and normal force is '
                                            'maximum is 45 degree. And the sum of horizontal forces is ', total_horizontal_force, ' (N)')
        answer_3 = seqg('The horizontal component of the friction force is m*g*cos(',theta,')*sin(',theta,
                        ') and the horizontal component of normal force is also m*g*cos(',theta,')*sin(',theta,
                        '). The sum of these two forces is equal to m*g*(sin(2*',theta,'))/2. Thus, in order to maximize this force the'
                        , theta,' must be 45 degree. Thus the maximum value of the sum of horizontal forces is ', total_horizontal_force, ' (N)')
        answer_4 = seqg('The horizontal component of the friction force is m*g*cos(', theta, ')*sin(', theta,
                        ') and the horizontal component of normal force is also m*g*cos(', theta, ')*sin(',
                        theta, '). The sum of these two forces is equal to m*g*(sin(2*', theta,
                        '))/2. Thus, in order to maximize this force the', theta, ' must be ', char_pi,
                        '/2. Thus the maximum value of the sum of horizontal forces is ', total_horizontal_force, ' (N)')
        answer_5 = seqg('Normal force is equal to the projection of the weight perpendicular to the plane which is m*g*cos('
                        ,theta,') and its horizontal component is m*g*cos(',theta,')*sin(',theta,
                        '). The friction force is equal to the projection of the weight in the direction of the plane which is m*g*sin('
                        ,theta,') and its horizontal component is m*g*cos(',theta,')*sin(',theta,
                        '). The sum of these two forces is equal to m*g*(sin(2*',theta,
                        '))/2. Thus, in order to maximize this force the', theta,' must be 45 degree. And the maximum value of the sum of horizontal forces is ', total_horizontal_force, ' (N)')
        answer_6 = seqg('The friction force is equal to the projection of the weight in the direction of the plane which is m*g*sin('
            , theta, ') and its horizontal component is m*g*cos(', theta, ')*sin(', theta,
            '). Normal force is equal to the projection of the weight perpendicular to the plane which is m*g*cos('
            , theta, ') and its horizontal component is m*g*cos(', theta, ')*sin(', theta,
            '). The sum of these two forces is equal to m*g*(sin(2*', theta,
            '))/2. Thus, in order to maximize this force the', theta, ' must be 45 degree. And the maximum value of the sum of horizontal forces is ', total_horizontal_force, ' (N)')


        # choices, try providing a few
        # these van include variations that are hard to encode with permg or variable substitution
        # example, NL variations or equaiton variations
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