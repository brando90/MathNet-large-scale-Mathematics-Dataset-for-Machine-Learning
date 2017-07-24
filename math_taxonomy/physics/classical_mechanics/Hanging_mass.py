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
        self.description = 'A mass m, held up by two strings, hangs from a ceiling. The strings ' \
                           'form a right angle. If the right String makes an angle theta with the ceiling, what is the tension in right string? '
        # keywords about the question that could help to make this more searchable in the future
        self.keywords = ['Physics', 'Classical Mechanics', 'Mass', 'Strings', 'Tension'] #TODO keywords to search type of question
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
            g, m, T_wanted = symbols('g m T_wanted')
            theta = symbols(chr(952))
        else:
            g, theta, m, T_wanted = self.get_symbols(4)
        return g, theta, m, T_wanted

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
            g_val, m_val, theta_val = 10, 1, 30
        else:
            g_val = random.choice([10, 9.8, 9.81, 9.807])
            theta_val = np.random.randint(0,89)
            m_val = np.random.randint(1,100000,1)/10

        return g_val, m_val, theta_val

    def Q(s, g_val, m_val, theta_val, g, theta, m, T_wanted): #TODO change the signature of the function according to your question
        '''
        A mass m, held up by two strings, hangs from a ceiling. The strings form a right angle.
        If the right/left string makes an angle theta with the ceiling what is the tension of this String.

        Important Note: first variables are the not consistent variables followed
        by the consistent ones. See sample QA example if you need too.
        '''
        #define some short cuts
        seqg, perg, choiceg = s.seqg, s.perg, s.choiceg
        # TODO
        question_1 = seqg('A mass ', Eq(m, m_val), ' held up by two strings, hangs from a ceiling. The two strings form' \
                                                    ' a right angle. If the right string makes an angle ', Eq(theta, theta_val), ' with the' \
                                                    ' ceiling what is the tension in this string. The gravitational acceleration is,', Eq(g, g_val), ' (m/s^2).')
        question_2 = seqg('A mass ', Eq(m, m_val), ' held up by two strings, hangs from a ceiling. The two strings form' \
                                                    ' a right angle. If the left string makes an angle theta with the' \
                                                    ' ceiling what is the tension in this string. The gravitational acceleration is,', Eq(g, g_val), ' (m/s^2).')
        question_3 = seqg('A mass ', Eq(m, m_val), ' held up by two strings, hangs from a ceiling. The two strings form' \
                                                    ' a right angle. If the left string makes an angle theta with the' \
                                                    ' ceiling what is the tension in this string if the gravitational acceleration is,', Eq(g, g_val), ' (m/s^2).')
        question_4 = seqg('A mass ', Eq(m, m_val), ' held up by two strings, hangs from a ceiling. The two strings form' \
                                                   ' a right angle. If the right string makes an angle theta with the' \
                                                   ' ceiling what is the tension in this string if the gravitational acceleration is,',
                          Eq(g, g_val), ' (m/s^2).')

        # choices, try providing a few
        # these van include variations that are hard to encode with permg or variable substitution
        # example, NL variations or equaiton variations
        q = choiceg(question_1, question_2, question_3, question_4)
        return q

    def A(s, g_val, m_val, theta_val, g, theta, m, T_wanted):
        '''
        T_wanted = m*g*cos(theta)

        Important Note: first variables are the not consistent variables followed
        by the consistent ones. See sample QA example if you need too.
        '''
        #define some short cuts
        seqg, perg, choiceg = s.seqg, s.perg, s.choiceg
        pi = np.pi
        theta_radian = (theta_val * pi) / 180
        ans_val = m_val*g_val*np.cos(theta_radian)
        ans_String = m + '*' + g + '*' + 'cos(' + theta + ')'
        answer_1 = seqg('The tension in the string is ', Eq(ans_String, ans_val), ' (N).')
        answer_2 = seqg(ans_val)
        answer_3 = seqg(Eq(ans_String, ans_val))
        answer_4 = seqg('In order to find the tension in the string we need to follow newton law. Because the mass is at'
                        ' rest then the net of forces in y and x direction must be equal to zero. After doing the '
                        'calculation the tension in the string could be calculated by this formula ', ans_String,
                        ' which with the given would be equal to ', ans_val, ' (N).')
        # choices, try providing a few
        # these van include variations that are hard to encode with permg or variable substitution
        # example, NL variations or equaiton variations
        a = choiceg(answer_1, answer_2, answer_3, answer_4)
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