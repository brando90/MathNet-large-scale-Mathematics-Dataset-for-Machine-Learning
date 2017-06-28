from sympy import *
import unittest
import random
import numpy as np

from qagen import utils
from qagen import *

#

class QA_unit_tester_example(QAGen):

    def __init__(self):
        '''
        Initializer for your QA question.
        '''
        super().__init__()
        self.author = 'unit_test'
        self.description = ''' '''
        # keywords about the question that could help to make this more searchable in the future
        self.keywords = ['unit_test']
        self.use_latex = True

    def seed_all(self,seed):
        random.seed(seed)
        np.random.seed(seed)
        self.fake.random.seed(seed)

    def init_consistent_qa_variables(self):
        if self.debug:
            x,y,z,d = symbols('x y z d')
            Mary, Gary = 'Mary', 'Gary'
            goats,lambs,dogs = 'goats','lambs','dogs'
        else:
            x,y,z,d = self.get_symbols(4)
            Mary, Gary = self.get_names(2)
            farm_animals = utils.get_farm_animals()
            goats,lambs,dogs = self.get_names(3,names_list=farm_animals)
        return x,y,z,d,Mary,Gary,goats,lambs,dogs

    def init_qa_variables(self):
        if self.debug:
            x_val,y_val,z_val = 2,3,4
            d_val = 1
        else:
            x_val,y_val,z_val = np.random.randint(1,1000,[3])
            d_val = np.random.randint(1,np.min([x_val,y_val,z_val]))
        return x_val,y_val,z_val,d_val

    def Q(s, x_val,y_val,z_val,d_val, x,y,z,d,Mary,Gary,goats,lambs,dogs):
        #define some short cuts
        seqg, perg, choiceg = s.seqg, s.perg, s.choiceg
        #
        return

    def A(s, x_val,y_val,z_val,d_val, x,y,z,d,Mary,Gary,goats,lambs,dogs):
        #define some short cuts
        seqg, perg, choiceg = s.seqg, s.perg, s.choiceg
        #
        return


class Test_QAOps(unittest.TestCase):

    # def __ini__(self):
    #     super().__init__()

    def test_names_are_deterministic_with_seed(self):
        # TODO
        # check that seed_all(self,seed) works
        seed = 0 # random.randint(0,500)
        qag = QA_unit_tester_example()
        qag.seed_all(seed)
        name1,name2 = qag.get_names(2)
        for i in range(30):
            qag.seed_all(seed)
            qag.reset_variables_states()
            new_name1,new_name2 = qag.get_names(2)
            self.assertEqual(new_name1,name1)
            self.assertEqual(new_name2,name2)

    def test_symbols_are_deterministic_with_seed(self):
        '''

        Note: that in the test we need to create a new instance because the
        an instance is created, it will not allow to select the same symbol
        or name twice in a row.
        '''
        # TODO
        # check that seed_all(self,seed) works
        seed = 0 # random.randint(0,500)
        qag = QA_unit_tester_example()
        qag.seed_all(seed)
        symbol1,symbol2 = qag.get_symbols(2)
        for i in range(30):
            qag.seed_all(seed)
            qag.reset_variables_states()
            new_symbol1,new_symbol2 = qag.get_symbols(2)
            self.assertEqual(new_symbol1,symbol1)
            self.assertEqual(new_symbol2,symbol2)

if __name__ == '__main__':
    unittest.main()
