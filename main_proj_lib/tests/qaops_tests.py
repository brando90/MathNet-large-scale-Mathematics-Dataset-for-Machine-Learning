from sympy import *
import unittest
import random
import numpy as np
import unit_tester_generators as utg

from qagen import utils
from qagen import *

#

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
        qag = utg.QA_unit_tester_example()
        qag.seed_all(seed)
        symbol1,symbol2 = qag.get_symbols(2)
        for i in range(30):
            qag.seed_all(seed)
            qag.reset_variables_states()
            new_symbol1,new_symbol2 = qag.get_symbols(2)
            self.assertEqual(new_symbol1,symbol1)
            self.assertEqual(new_symbol2,symbol2)

    def test_seqg(self):
        seed = 0
        qag = utg.QA_unit_tester_example()
        qag.generator_unit_test = True
        x, y, z = symbols('x y z')
        expr1 = Eq(x, y)
        args = ['Lorem ipsum', '1', 2, 3, expr1]
        kwargs = {}
        test1 = qag.seqg(*args)
        self.assertEqual(test1(), 'Lorem ipsum 1 2 3 Eq(x, y)') 
        self.assertEqual(str(test1), str((qag.seqg, args, kwargs)))

    def test_perg(self):
        seed = 0
        qag = utg.QA_unit_tester_example()
        qag.seed_all(seed)
        qag.generator_unit_test = True
        x, y, z = symbols('x y z')
        expr1 = Eq(x, y)
        args = ['Lorem ipsum', '1', 2, 3, expr1]
        kwargs = {}
        test1 = qag.perg(*args)
        self.assertEqual(str(test1), str((qag.perg, args, kwargs)))
        test1_str = test1()
        qag.seed_all(seed)
        test2_str = test1()
        self.assertEqual(test1_str, test2_str)
        permuted = False
        for n in range(100):
            qag.seed_all(n)
            test3_str = test1()
            if test3_str != test1_str: permuted = True
        self.assertTrue(permuted)
    
    
    def test_choiceg(self):
        seed = 0
        qag = utg.QA_unit_tester_example()
        qag.seed_all(seed)
        qag.generator_unit_test = True
        x, y, z = symbols('x y z')
        expr1 = Eq(x, y)
        args = ['Lorem ipsum', '1', 2, 3, expr1]
        kwargs = {}
        test1 = qag.choiceg(*args)
        self.assertEqual(str(test1), str((qag.choiceg, args, kwargs)))
        test1_str = test1()
        qag.seed_all(seed)
        test2_str = test1()
        self.assertEqual(test1_str, test2_str)
        permuted = False
        for n in range(100):
            qag.seed_all(n)
            test3_str = test1()
            if test3_str != test1_str: permuted = True
        self.assertTrue(permuted)
    

    def test_preprocess_arg(self):
        qag = utg.QA_unit_tester_example()
        x, y, z = symbols('x y z')
        arg_expr = Eq(x, y)
        qag.generator_unit_test = True
        args = ['Lorem ipsum', '1', 2, 3, expr1]
        arg_de = qag.seqg(*args)
        arg_str = 'Lorem ipsum'
        arg_sym = x
        arg_int = 1
        unittest.assertEquals(qag._preprocess_arg(arg_expr), arg_expr)
        unittest.assertEquals(qag._preprocess_arg(arg_de), 'Lorem ipsum 1 2 3 Eq(x, y)' )
        unittest.assertEquals(qag._preprocess_arg(arg_str), arg_str)
        unittest.assertEquals(qag._preprocess_arg(arg_sym), arg_sym)
        unittest.assertEquals(qag._preprocess_arg(arg_int), arg_int)
        
    
    def test_convert_to_list_of_string(self):
        seed = 0
        qag = utg.QA_unit_tester_example()
        qag.generator_unit_test = True
        x, y, z = symbols('x y z')
        expr1 = Eq(x, y)
        args = ['Lorem ipsum', '1', 2, 3, expr1]
        self.assertEqual(self.args, ['Lorem ipsum', '1', '2', '3', qag.sympy2text(expr1)]) 
        

    def test_sympy2text(self):
        x, y, z = symbols('xray yankee zulu')
        expr1 = Eq(x, y)
        seed = 0
        qag = utg.QA_unit_tester_example()
        qag.use_latex = True
        self.assertEqual(expr1, latex(expr1))
        self.assertEqual(x, latex(x))
        qag.use_latex = False   
        self.assertEqual(expr1, str(expr1))
        self.assertEqual(x, 'xray')

    def test_get_symbols(self):
        seed = 0
        qag = utg.QA_unit_tester_example()
        symbols_str = 'x y z X Y Z'
        symbols_list = [symbols(n) for n in ['x', 'y', 'z', 'X', 'Y', 'Z']]
         

    def test_get_names(self):
        seed = 0
        qag = utg.QA_unit_tester_example()

    def test_register_qa_variables(self):
        seed = 0
        qag = utg.QA_unit_tester_example()

if __name__ == '__main__':
    unittest.main()
