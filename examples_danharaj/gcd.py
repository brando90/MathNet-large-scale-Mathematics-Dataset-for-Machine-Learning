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
            "Given integers a = 15 , b = 20 , find the smallest positive"
            " integer d for which there exist integers x , y such that"
            " a x + b y = d")
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
        question = seqg("Given integers"
                     , permutable_part
                     , "find the smallest positive integer"
                     , d
                     , "for which there exist integers"
                     , x, ",", y
                     , "such that", sym.Eq(a*x + b*y, d))
        return question
    def A(s, a_val, b_val, a, b, d, x, y):
        seqg, perg = s.seqg, s.perg
        x_val, y_val, d_val = igcdex(a_val, b_val)
        a = seqg(sym.Eq(d, d_val), sym.Eq(x, x_val), sym.Eq(y, y_val))
        return a

if __name__ == '__main__':
    user_test.run_unit_test_for_user(QA_constraint)
