from sympy import *
import random
import numpy as np
import pdb

from qagen.qagen import *
from qagen import utils
from qagen import unit_test_for_user as user_test


class QA_constraint(QAGen):

    def __init__(self):
        """
        Initializer for your QA question.
        """

        super().__init__()
        self.author = 'Ivan Jutamulia'
        self.description = '''Let S be the surface parametrized by (x, y, 10 - 5x - 5y) in the region x, y >= 0 and x + y > 2. Find the integral of the function x z over the surface S.'''
        # keywords about the question that could help to make this more searchable in the future
        self.keywords = ['multivariable calculus']
        self.use_latex = True

    def seed_all(self, seed):
        """
        Write the seeding functions of the libraries that you are using.
        Its important to seed all the libraries you are using because the
        framework will assume it can seed stuff for you. It needs this for
        the library to work.
        """
        random.seed(seed)
        np.random.seed(seed)
        self.fake.random.seed(seed)

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
            x, y, z = symbols('x y z')
        else:
            x, y, z = self.get_symbols(3)
        return x, y, z

    def init_qa_variables(self):
        """
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
        """
        if self.debug:
            a, b = 0, 2
        else:
            a = np.random.randint(-100, 0)
            b = np.random.randint(1, 100)
        return a, b

    def Q(s, a, b, x, y, z):
        """
        Small question description.
        Important Note: first variables are the not consistent variables followed
        by the consistent ones. See sample QA example if you need too.
        """
        seqg, perg, choiceg = s.seqg, s.perg, s.choiceg
        given = seqg('Let S be the surface parametrized by ({0}, {1}, 10 - 5{0} - 5{1}) in the region {0}, {1} >= {2} and {0} + {1} > {3}.'.format(x, y, a, b))
        calc = seqg('Find the integral of the function {0} {1} over the surface S.'.format(x, z))
        ask = seqg('What is the value of the integral of the function {0} {1} over the surface S?'.format(x, z))
        question1 = seqg(given, calc)
        question2 = seqg(given, ask)
        q = choiceg(question1, question2)
        return q

    def A(s, a, b, x, y, z):
        """
        Small answer description.
        Important Note: first variables are the not consistent variables followed
        by the consistent ones. See sample QA example if you need too.
        """
        # define some short cuts
        seqg, perg, choiceg = s.seqg, s.perg, s.choiceg
        param = (x, y, 10 - 5*x - 5*y)
        r_x = (diff(param[0], x), diff(param[1], x), diff(param[2], x))
        r_y = (diff(param[0], y), diff(param[1], y), diff(param[2], y))
        cross = (r_x[1] * r_y[2] - r_x[2] * r_y[1], r_x[2] * r_y[0] - r_x[0] * r_y[2], r_x[0] * r_y[1] - r_x[1] * r_y[0])
        mag = sqrt(cross[0]**2 + cross[1]**2 + cross[2]**2)
        expression = param[0] * param[2]
        value = integrate(expression * mag, (y, a, b-x), (x, a, b))

        answer1 = seqg('The value of the surface integral is {0}'.format(value))
        answer2 = seqg('{0} is the value of the surface integral.'.format(value))
        a = choiceg(answer1, answer2)
        return a

    ##

    def get_qa(self,seed):
        """
        Example of how Q,A are formed in general.
        """
        # set seed
        self.seed_all(seed)
        # get variables for qa and register them for the current q,a
        variables, variables_consistent = self._create_all_variables()
        # get concrete qa strings
        q_str = self.Q(*variables,*variables_consistent)
        a_str = self.A(*variables,*variables_consistent)
        return q_str, a_str


# Some helper functions to check the formats are coming out correctly


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
    check_single_question_debug(qagenerator)
    # user_test.run_unit_test_for_user(QA_constraint)


