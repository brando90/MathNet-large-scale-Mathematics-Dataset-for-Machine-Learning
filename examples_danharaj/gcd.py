import sympy as sym
from sympy.core.numbers import igcd, igcdex
import random
import numpy as np
import pdb

from qagen.qagen import *
from qagen import utils
from qagen import unit_test_for_user as user_test

class QA_constraint(QAGen):
    def __init__(self):
        super().__init__()
        self.author = 'Dan Haraj'
        self.description = (
            "Given integers a = 15 , b = 20 , find their greatest common divisor"
            " which is the smallest positive"
            " integer d for which there exist integers x , y such that"
            " a x + b y = d .")
        self.keywords = ['algebra', 'number theory']

    def seed_all (self, seed):
        random.seed(seed)
        np.random.seed(seed)
        self.fake.random.seed(seed)

    def init_consistent_qa_variables (self):
        if self.debug:
            a, b, d, x, y = symbols('a b d x y')
        else:
            a, b, d, x, y = self.get_symbols(5)
        return a, b, d, x, y

    def init_qa_variables(self):
        if self.debug:
            a_val = 15
            b_val = 20
        else:
            a_val, b_val = tuple(np.random.randint(2,100, [2]))
        return a_val, b_val

    def Q(s, a_val, b_val, a, b, d, x, y):
        seqg, perg, choiceg = s.seqg, s.perg, s.choiceg
        permutable_part = perg(seqg(sym.Eq(a, a_val), ','), seqg(sym.Eq(b, b_val), ','))
        q1 = seqg("Given integers"
               , permutable_part
               , "find their greatest common divisor which is the smallest"
               , "positive integer"
               , d
               , "for which there exist integers"
               , x, ",", y
               , "such that", sym.Eq(a*x + b*y, d), ".")
        q2 = seqg ("If", a, ",", b
               , "are integers then there exist"
               , d, ",", x, ",", y
               , "such that", d, "is the smallest positive integer such that"
               , sym.Eq(a*x + b*y, d), "."
               , "if", permutable_part, "solve for", d, ",", x, ",", y, ".")
        return choiceg(q1, q2)

    def A(s, a_val, b_val, a, b, d, x, y):
        seqg, choiceg = s.seqg, s.choiceg
        x_val, y_val, d_val = igcdex(a_val, b_val)
        a1 = seqg(sym.Eq(d, d_val), sym.Eq(x, x_val), sym.Eq(y, y_val))
        a2 = seqg("The greatest common divisor of"
               , a, "and", b, "is", sym.Eq(d,d_val)
               , "with coefficients", sym.Eq(x, x_val), sym.Eq(y, y_val))
        return choiceg(a1, a2)

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

if __name__ == '__main__':
    qg = QA_constraint()
    q, a = qg.get_qa(421)
    print(q)
    print(a)
    user_test.run_unit_test_for_user(QA_constraint)
