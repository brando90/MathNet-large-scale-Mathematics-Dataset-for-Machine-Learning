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
        self.description = '''Let the triangle T have vertices p = (1, 0), q = (0, 1), and r = (2, 3). Find the area of the triangle T using a matrix.'''
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
            p, q, r = symbols('p q r')
        else:
            p, q, r = self.get_symbols(3)
        return p, q, r

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
            a, b, c, d, e, f = 1, 0, 0, 1, 2, 3
        else:
            a, b, c, d, e, f = np.random.randint(-100, 100, [6])
        return a, b, c, d, e, f

    def Q(s, a, b, c, d, e, f, p, q, r):
        """
        Small question description.
        Important Note: first variables are the not consistent variables followed
        by the consistent ones. See sample QA example if you need too.
        """
        seqg, perg, choiceg = s.seqg, s.perg, s.choiceg
        given = seqg('Let the triangle T have vertices {0} = ({1}, {2}), {3} = ({4}, {5}), and {6} = ({7}, {8}).'.format(p, a, b, q, c, d, r, e, f))
        calc = seqg('Find the area of the triangle T using a matrix.')
        ask = seqg('Using a matrix, what is the area of the triangle T?')
        q3 = seqg('Using a matrix, calculate the area of the triangle T.')
        q4 = seqg('Using a matrix, find the area of the triangle T.')
        q5 = seqg('Calculate the area of the triangle T using a matrix.')
        question1 = seqg(given, calc)
        question2 = seqg(given, ask)
        question3 = seqg(given, q3)
        question4 = seqg(given, q4)
        question5 = seqg(given, q5)
        q = choiceg(question1, question2, question3, question4, question5)
        return q

    def A(s, a, b, c, d, e, f, p, q, r):
        """
        Small answer description.
        Important Note: first variables are the not consistent variables followed
        by the consistent ones. See sample QA example if you need too.
        """
        # define some short cuts
        seqg, perg, choiceg = s.seqg, s.perg, s.choiceg
        vector_qp = (a - c, b - d)
        vector_qr = (e - c, f - d)
        area_matrix = np.matrix([[vector_qp[0], vector_qr[0]], [vector_qp[1], vector_qr[1]]])
        # area is equal to half the absolute value of the determinant of this matrix
        determinant = np.linalg.det(area_matrix)
        area = 1/2 * abs(determinant)
        answer1 = seqg('The area of the triangle T is {0}.'.format(area))
        answer2 = seqg('{0} is the area of the triangle T.'.format(area))
        answer = choiceg(answer1, answer2)
        return answer

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


