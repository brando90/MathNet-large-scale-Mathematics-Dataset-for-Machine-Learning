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
        self.description = '''Suppose that the temperature in Celsius at the point (x, y) near an airport is given by f(x, y) = 1/180 * (7400 - 4x - 9y - (0.03)xy) with distances x and y measured in kilometers. Suppose that your aircraft takes off from this airport at the location p(200, 200) and heads northeast in the direction specified by the vector v = (3, 4). What initial rate of change of temperature will you observe?'''
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
            x, y, p, v = symbols('x y p v')
        else:
            x, y, p, v = self.get_symbols(4)
        return x, y, p, v

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
            a, b, c, d = 200, 200, 3, 4
        else:
            a, b = np.random.randint(-1000, 1000, [2])
            c, d = np.random.randint(-100, 100, [2])
        return a, b, c, d

    def Q(s, a, b, c, d, x, y, p, v):
        """
        Small question description.
        Important Note: first variables are the not consistent variables followed
        by the consistent ones. See sample QA example if you need too.
        """
        seqg, perg, choiceg = s.seqg, s.perg, s.choiceg
        function = seqg('Suppose that the temperature in Celsius at the point ({0}, {1}) near an airport is given by '
                        'f({0}, {1}) = 1/180 * (7400 - 4{0} - 9{1} - (0.03){0}{1}) with distances {0} and {1} '
                        'measured in kilometers.'.format(x, y))
        point_vector = seqg('Suppose that your aircraft takes off from this airport at the location {0}({1}, {2}) '
                            'and heads northeast in the direction specified '
                            'by the vector {3} = ({4}, {5}).'.format(p, a, b, v, c, d))
        ask = seqg('What initial rate of change of temperature will you observe?')
        question1 = seqg(function, point_vector, ask)
        q = choiceg(question1)
        return q

    def A(s, a, b, c, d, x, y, p, v):
        """
        Small answer description.
        Important Note: first variables are the not consistent variables followed
        by the consistent ones. See sample QA example if you need too.
        """
        # define some short cuts
        seqg, perg, choiceg = s.seqg, s.perg, s.choiceg
        function = 1/180 * (7400 - 4 * x - 9 * y - (0.03) * x * y)
        dx = diff(function, x)
        dy = diff(function, y)

        # find the unit vector
        mag = sqrt(c**2 + d**2)
        unit = (c/mag, d/mag)

        # find directional derivative
        directional = unit[0] * dx + unit[1] * dy

        # use the point
        ans = directional.evalf(subs={x: a, y: b})

        answer1 = seqg('You will observe initially a change of {0} degrees Celsius in temperature per '
                       'kilometer traveled.'.format(ans))
        answer = choiceg(answer1)
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


