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
        self.description = 'A rope with length L and mass density Ω per unit length is suspended vertically from one' \
                           ' end. Find the tension in height y.'

        self.keywords = ['Physics', 'Classical Mechanics', 'Mass', 'Rope', 'Tension', 'Density']
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
        # TODO write more seeding libraries that you are using

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
            L, y, g = symbols('L y g')
            ru = symbols(chr(956))
        else:
            L, y, g = symbols('L y g')
            ru = symbols(chr(956))
        return L, y, ru, g

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
            L_val, ru_val, g_val = 1, 1, 10
        else:
            L_val, ru_val = np.random.randint(.01,1000,2)
            g_val = random.choice([10, 9.8, 9.81, 9.807])
            y_val = np.random.randint(0,L_val)
        return L_val, ru_val, g_val, y_val

    def Q(s, L_val, ru_val, g_val, y_val, L, y, ru, g): #TODO change the signature of the function according to your question
        '''
        A rope with length L and mass density Ω per unit length is suspended vertically from one end.
        Find the tension in given height.

        Important Note: first variables are the not consistent variables followed
        by the consistent ones. See sample QA example if you need too.
        '''
        #define some short cuts
        seqg, perg, choiceg = s.seqg, s.perg, s.choiceg
        # TODO
        info_V1 = seqg('A rope with length {0} = {1} (m) and mass density {2} = {3] (kg/m) per unit length is suspended'
                       ' vertically from one end.'.format(L, L_val, ru, ru_val))
        wanted_V1 = seqg(' Find the tension of the rope in height {0} = {1} (m) .'.format(y, y_val))
        wanted_V2 = seqg(' Find the equation for the tension of the rope in height {0} = {1} (m).'.format(y, y_val))
        g_sentence_V1 = seqg(' Assume the gravitational acceleration is {0} = {1} (m/s^2).'.format(g, g_val))
        g_sentence_V2 = seqg(' Gravitational Acceleration is {0} = {1} (m/s^2).')
        question_1 = seqg(info_V1, wanted_V1, g_sentence_V1)
        question_2 = seqg(info_V1, wanted_V1, g_sentence_V2)
        question_3 = seqg(info_V1, wanted_V2, g_sentence_V1)
        question_4 = seqg(info_V1, wanted_V2, g_sentence_V2)
        q = choiceg(question_1, question_2, question_3, question_4)
        return q

    def A(s, L_val, ru_val, g_val, y_val, L, y, ru, g): #TODO change the signature of the function according to your answer
        '''
        T(y) = ru*g*y

        Important Note: first variables are the not consistent variables followed
        by the consistent ones. See sample QA example if you need too.
        '''
        #define some short cuts
        seqg, perg, choiceg = s.seqg, s.perg, s.choiceg
        ans = ru_val*g_val*y_val
        answer_value = seqg('{0} (N)'.format(ans))
        answer_symbol = seqg('{0}*{1}*{2}'.format(ru, g, y))
        info_V1 = seqg('The tension as a function of height can be calculate by this function. ')
        info_V2 = seqg('The tension as a function of height is: ')
        conclusion_V1 = seqg('Given the values in question the tension in height {0} is '.format(y, ans))
        conclusion_V2 = seqg('After including the given values for {0}, {1}, and {2} the tension is '.format(ru, g, y))
        answer_1 = seqg(info_V1, answer_symbol, conclusion_V1, answer_value)
        answer_2 = seqg(info_V1, answer_symbol, conclusion_V2, answer_value)
        answer_3 = seqg(info_V2, answer_symbol, conclusion_V1, answer_value)
        answer_4 = seqg(info_V2, answer_symbol, conclusion_V2, answer_value)
        answer_5 = seqg(answer_value)
        answer_6 = seqg(answer_symbol, ' = ', answer_value)
        a = choiceg(answer_1, answer_2, answer_3, answer_4, answer_5, answer_6)
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