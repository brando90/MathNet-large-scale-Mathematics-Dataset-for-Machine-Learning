import sympy as sym
from sympy.core.numbers import igcd, igcdex
import random
import numpy as np
import pdb

from qagen.qagen import *
from qagen import utils
from qagen import unit_test_for_user as user_test

# The name of the class can be arbitrary but should be suggestive
class QA_gcd(QAGen):
    def __init__(self):
        super().__init__()
        # Set some descriptive information about the QA problem
        # The author should be you
        # The description should be an instance of a question your code can
        # generate
        # The keywords should suggest what sort of domain this problem
        # belongs to
        self.author = 'Dan Haraj'
        # This example problem is for finding the greatest common divisor
        # of two numbers and also the coefficients that make bezout's identity
        # hold.
        self.description = (
            "Given integers a = 15 and b = 20, find their greatest common divisor"
            " d and integers x and y such that a x + b y = d.")
        # This problem falls under both algebra and number theory
        self.keywords = ['algebra', 'number theory']

    def seed_all (self, seed):
        # In this function you should initialize all the random number
        # generators your code uses. random is the standard random number
        # package. np.random is the random number generator that numpy uses
        # and fake.random is used by the faker package.
        #
        # You might not need all of these and you might need more of them
        # if you use further other packages.
        random.seed(seed)
        np.random.seed(seed)
        self.fake.random.seed(seed)

    def init_consistent_qa_variables (self):
        # Some variables are shared between the question and the answer.
        # This function should initialize these.
        #
        # In this example our questions mention 5 variables.
        if self.debug:
            # These variables should be set to the ones that are used in your
            # problem instance as given in the description.
            #
            # For this code example our example question uses the variable
            # names 'a', 'b', 'd', 'x' and 'y'.
            a, b, d, x, y = symbols('a b d x y')
        else:
            # otherwise you should initialize the symbols to random names.
            # the framework will make sure that generated pairs of questions
            # and answers share these variables.
            #
            # In this example we use 5 distinct variables.
            a, b, d, x, y = self.get_symbols(5)
        return a, b, d, x, y

    def init_qa_variables(self):
        # Define parameters of the question answer pair here. In this example
        # the questions are parameterized by the values of the integers whose
        # GCD we are asking for.
        #
        # The parameters will be different for your questions.
        if self.debug:
            # These values should correspond to the parameters of the question
            # given in the description.
            a_val = 15
            b_val = 20
        else:
            # Otherwise generate parameters that are reasonable for your
            # question.
            a_val, b_val = tuple(np.random.randint(2,100, [2]))
        return a_val, b_val

    def Q(self, a_val, b_val, a, b, d, x, y):
        splices = { 'a_var': a
                  , 'a_eq': sym.latex(sym.Eq(a, a_val))
                  , 'b_var': b
                  , 'b_eq': sym.latex(sym.Eq(b, b_val))
                  , 'd_var': d
                  , 'x_var': x
                  , 'y_var': y
                  , 'bezout': sym.latex(sym.Eq(a*x + b*y, d))}

        qa1 = ("Given integers %(a_eq)s and %(b_eq)s, find their greatest common "
             "divisor %(d_var)s and integers %(x_var)s and %(y_var)s such that "
             "%(bezout)s.")

        qa2 = ("If %(a_var)s and %(b_var)s are integers then there exist "
             "%(d_var)s, %(x_var)s, %(y_var)s such that %(d_var)s is the smallest "
             "positive integer such that %(bezout)s. "
             "If %(a_eq)s and %(b_eq)s solve for %(d_var)s, %(x_var)s, and "
             "%(y_var)s.")

        permutable_parts = [ ['a_var', 'b_var']
            , ['a_eq', 'b_eq']
            , ['x_var', 'y_var']]

        questionTemplate = self.choiceg(qa1, qa2)

        return self.interpolate(questionTemplate, splices, permutable_parts)

    def A(s, a_val, b_val, a, b, d, x, y):
        # In this method you should generate an answer based on the particular
        # parameters and variable names generated for this QA instance.
        # It is ideal to rely on sympy and other libraries to do the solving
        # for you.
        seqg, choiceg = s.seqg, s.choiceg
        x_val, y_val, d_val = igcdex(a_val, b_val)
        a1 = seqg(sym.Eq(d, d_val), sym.Eq(x, x_val), sym.Eq(y, y_val))
        a2 = seqg("The greatest common divisor of"
               , a, "and", b, "is", sym.Eq(d,d_val)
               , "with coefficients", sym.Eq(x, x_val), sym.Eq(y, y_val))
        # try to generate at least 2 or 3 different wordings of the answer.
        return choiceg(a1, a2)

    def get_qa(self,seed):
        # This function illustrates how the framework can be used to generate
        # a question/answer pair from your instance. This sort of function
        # is useful to define for debugging purposes.
        self.seed_all(seed)
        # get variables for qa and register them for the current q,a
        variables, variables_consistent = self._create_all_variables()
        # get concrete qa strings
        q_str = self.Q(*variables,*variables_consistent)
        a_str = self.A(*variables,*variables_consistent)
        return q_str, a_str

# your module should include a code block like this so that when it is run
# as a script it automatically runs some standard unit tests that will check
# that your implementation is sufficiently coherent and robust.
if __name__ == '__main__':
    user_test.run_unit_test_for_user(QA_gcd)
