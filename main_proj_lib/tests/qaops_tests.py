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
        # check that seed_all(self,seed) works
        seed = 0 # random.randint(0,500)
        qag = utg.QA_unit_tester_example()
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
        self.assertEqual(test1(), 'Lorem ipsum 1 2 3 x = y') 
        self.assertEqual(str(test1), str((qag.seqg, tuple(args), kwargs)))

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
        self.assertEqual(str(test1), str((qag.perg, tuple(args), kwargs)))
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
        qag.seed_all(seed)
        args = ['Lorem ipsum', '1', 2, 3, expr1]
        kwargs = {}
        test1 = qag.choiceg(*args)
        self.assertEqual(str(test1), str((qag.choiceg, tuple(args), kwargs)))
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
        args = ['Lorem ipsum', '1', 2, 3, arg_expr]
        arg_de = qag.seqg(*args)
        arg_str = 'Lorem ipsum'
        arg_sym = x
        arg_int = 1
        self.assertEqual(qag._preprocess_arg(arg_expr), arg_expr)
        self.assertEqual(qag._preprocess_arg(arg_de), 'Lorem ipsum 1 2 3 x = y' )
        self.assertEqual(qag._preprocess_arg(arg_str), arg_str)
        self.assertEqual(qag._preprocess_arg(arg_sym), arg_sym)
        self.assertEqual(qag._preprocess_arg(arg_int), arg_int)
        
    
    def test_convert_to_list_of_string(self):
        seed = 0
        qag = utg.QA_unit_tester_example()
        qag.generator_unit_test = True
        x, y, z = symbols('x y z')
        expr1 = Eq(x, y)
        args = ['Lorem ipsum', '1', 2, 3, expr1]
        self.assertEqual(qag.convert_to_list_of_string(args), ['Lorem ipsum', '1', '2', '3', qag.sympy2text(expr1)]) 
        

    def test_sympy2text(self):
        x, y, z = symbols('xray yankee zulu')
        expr1 = Eq(x, y)
        seed = 0
        qag = utg.QA_unit_tester_example()
        qag.use_latex = True
        self.assertEqual(qag.sympy2text(expr1), latex(expr1))
        self.assertEqual(qag.sympy2text(x), latex(x))
        qag.use_latex = False   
        self.assertEqual(qag.sympy2text(expr1), str(expr1))
        self.assertEqual(qag.sympy2text(x), 'xray')

    def test_get_symbols(self):
        seed = 0
        qag = utg.QA_unit_tester_example()
        symbols_str = 'x y z X Y Z'
        symbols_list = [symbols(n) for n in ['x', 'y', 'z', 'X', 'Y', 'Z']]
        test1a, test1b = qag.get_symbols(2, symbols_str=symbols_str)
        test2a, test2b = qag.get_symbols(2, symbols_list=symbols_list)
        test3a, test3b = qag.get_symbols(2)
        test4a, test4b = qag.get_symbols(2, uppercase=True)
        self.assertNotEqual(str(test1a), str(test1b))
        self.assertTrue((test1a in symbols_list and test1b in symbols_list))
        self.assertNotEqual(str(test2a), str(test2b))
        self.assertTrue((test2a in symbols_list and test2b in symbols_list))
        self.assertNotEqual(str(test3a), str(test3b))
        self.assertTrue((str(test3a) in list(string.ascii_lowercase) and str(test3b) in list(string.ascii_lowercase)))
        self.assertNotEqual(str(test4a), str(test4b))
        self.assertTrue((str(test4a) in list(string.ascii_letters) and str(test4b) in list(string.ascii_letters)))
        prev_choices = [] 
        qag = utg.QA_unit_tester_example()
        for n in range(10):
            sym = qag.get_symbols(1)
            self.assertTrue(sym not in prev_choices) 
            prev_choices.append(sym)
         

    def test_get_names(self):
        seed = 0
        qag = utg.QA_unit_tester_example()
        test1a, test1b = qag.get_names(2)
        test2a, test2b = qag.get_names(2, full_name=False)
        names_list = ['Harry', 'Dick', 'Bob']
        test3 = qag.get_names(1, names_list=names_list)[0]
        self.assertNotEqual(test1a, test1b)
        self.assertTrue((' ' in test1a and ' ' in test1b))
        self.assertNotEqual(test2a, test2b)
        self.assertTrue((' ' not in test2a and ' ' not in test2b))
        self.assertTrue(test3 in names_list) 
        qag = utg.QA_unit_tester_example()
        prev_names = []
        for n in range(20):
            name = qag.get_names(1)
            self.assertTrue(name not in prev_names)
            prev_names.append(name)

    def test_register_qa_variables(self):
        seed = 0
        qag = utg.QA_unit_tester_example()
        x, y, z = symbols('xray yankee zulu')
        expr1 = Eq(x, y)
        variables = []
        variables.append(expr1)
        variables.append(x)
        variables.append('Harry')
        qag.register_qa_variables(variables)
        self.assertTrue('Harry' in qag.names)
        self.assertTrue(expr1 in qag.sympy_vars)
        self.assertTrue(x in qag.sympy_vars)

if __name__ == '__main__':
    unittest.main()
