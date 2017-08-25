from sympy import *
import unittest
import random
import numpy as np
import unit_tester_generators as utg
import string
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
        qag._seed_all(seed)
        name1,name2 = qag.get_names(2)
        for i in range(30):
            qag.seed_all(seed)
            qag.reset_variables_states()
            new_name1,new_name2 = qag.get_names(2)
            self.assertEqual(new_name1,name1, msg='Names should be deterministic given seed')
            self.assertEqual(new_name2,name2, msg='Names should be deterministic given seed')

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
        qag._seed_all(seed)
        symbol1,symbol2 = qag.get_symbols(2)
        for i in range(30):
            qag._seed_all(seed)
            qag.reset_variables_states()
            new_symbol1,new_symbol2 = qag.get_symbols(2)
            self.assertEqual(new_symbol1,symbol1, msg='Symbols should be deterministic given seed')
            self.assertEqual(new_symbol2,symbol2, msg='Symbols should be deterministic given seed')

    def test_seqg(self):
        seed = 0
        qag = utg.QA_unit_tester_example()
        qag.generator_unit_test = True
        x, y, z = symbols('x y z')
        expr1 = Eq(x, y)
        args = ['Lorem ipsum', '1', 2, 3, expr1]
        kwargs = {}
        test1 = qag.seqg(*args)
        self.assertEqual(test1(), 'Lorem ipsum 1 2 3 x = y', msg='seqg should return string')
        self.assertEqual(str(test1), str((qag.seqg, tuple(args), kwargs)), msg='seqg DE object should have expected arguments')

    def test_perg(self):
        seed = 0
        qag = utg.QA_unit_tester_example()
        qag._seed_all(seed)
        qag.generator_unit_test = True
        x, y, z = symbols('x y z')
        expr1 = Eq(x, y)
        args = ['Lorem ipsum', '1', 2, 3, expr1]
        kwargs = {}
        test1 = qag.perg(*args)
        self.assertEqual(str(test1), str((qag.perg, tuple(args), kwargs)), msg='Perg DE object should be as expected')
        test1_str = test1()
        qag._seed_all(seed)
        test2_str = test1()
        self.assertEqual(test1_str, test2_str, msg='Perg should be deterministic given seed')
        permuted = False
        for n in range(100):
            qag._seed_all(n)
            test3_str = test1()
            if test3_str != test1_str: permuted = True
        self.assertTrue(permuted, msg='Seed should affect order chosen by perg')


    def test_choiceg(self):
        seed = 0
        qag = utg.QA_unit_tester_example()
        qag._seed_all(seed)
        qag.generator_unit_test = True
        x, y, z = symbols('x y z')
        expr1 = Eq(x, y)
        qag._seed_all(seed)
        args = ['Lorem ipsum', '1', 2, 3, expr1]
        kwargs = {}
        test1 = qag.choiceg(*args)
        self.assertEqual(str(test1), str((qag.choiceg, tuple(args), kwargs)), msg='Choiceg DE object should be as expected')
        test1_str = test1()
        qag._seed_all(seed)
        test2_str = test1()
        self.assertEqual(test1_str, test2_str, msg='Choiceg should be deterministic given seed')
        permuted = False
        for n in range(100):
            qag._seed_all(n)
            test3_str = test1()
            if test3_str != test1_str: permuted = True
        self.assertTrue(permuted, msg='Seed should affect argument chosen by choiceg')


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
        self.assertEqual(qag._preprocess_arg(arg_expr), arg_expr, msg='Expressions should not be changed')
        self.assertEqual(qag._preprocess_arg(arg_de), 'Lorem ipsum 1 2 3 x = y' , msg='DE objects should be executed')
        self.assertEqual(qag._preprocess_arg(arg_str), arg_str, msg='Strings should not be changed')
        self.assertEqual(qag._preprocess_arg(arg_sym), arg_sym, msg='Symbols should not be changed')
        self.assertEqual(qag._preprocess_arg(arg_int), arg_int, msg='Integers should not be changed')


    def test_convert_to_list_of_string(self):
        seed = 0
        qag = utg.QA_unit_tester_example()
        qag.generator_unit_test = True
        x, y, z = symbols('x y z')
        expr1 = Eq(x, y)
        args = ['Lorem ipsum', '1', 2, 3, expr1]
        self.assertEqual(qag.convert_to_list_of_string(args), ['Lorem ipsum', '1', '2', '3', qag.sympy2text(expr1)], msg='Should convert to list of strings')


    def test_sympy2text(self):
        x, y, z = symbols('xray yankee zulu')
        expr1 = Eq(x, y)
        seed = 0
        qag = utg.QA_unit_tester_example()
        qag.use_latex = True
        self.assertEqual(qag.sympy2text(expr1), latex(expr1), msg='Should use latex output if latex flag is true')
        self.assertEqual(qag.sympy2text(x), latex(x), msg='Should use latex output if latex flag is true')
        qag.use_latex = False
        self.assertEqual(qag.sympy2text(expr1), str(expr1), msg='Should use symbolic output if latex flag is false')
        self.assertEqual(qag.sympy2text(x), 'xray', msg='Should use symbolic output if latex flag is false')

    def test_get_symbols(self):
        seed = 0
        qag = utg.QA_unit_tester_example()
        symbols_str = 'x y z X Y Z'
        symbols_list = [symbols(n) for n in ['x', 'y', 'z', 'X', 'Y', 'Z']]
        test1a, test1b = qag.get_symbols(2, symbols_str=symbols_str)
        test2a, test2b = qag.get_symbols(2, symbols_list=symbols_list)
        test3a, test3b = qag.get_symbols(2)
        test4a, test4b = qag.get_symbols(2, uppercase=True)
        self.assertNotEqual(str(test1a), str(test1b), msg='Symbols should not contain duplicates')
        self.assertTrue((test1a in symbols_list and test1b in symbols_list), msg='If symbols_str is used, generated output should be in symbols_str')
        self.assertNotEqual(str(test2a), str(test2b), msg='Symbols should not contain duplicates')
        self.assertTrue((test2a in symbols_list and test2b in symbols_list), msg='If symbols_list is used, generated output should be in symbols_list')
        self.assertNotEqual(str(test3a), str(test3b), msg='Symbols generated from default set should not contain duplicates')
        self.assertTrue((str(test3a) in list(string.ascii_lowercase) and str(test3b) in list(string.ascii_lowercase)), msg='Symbols generated from default lowercase set should be in default lowercase set')
        self.assertNotEqual(str(test4a), str(test4b), msg='Symbols generated from default uppercase set should not contain duplicates')
        self.assertTrue((str(test4a) in list(string.ascii_letters) and str(test4b) in list(string.ascii_letters)), msg='Symbols generated from default uppercase set should be in default uppercase set')
        prev_choices = []
        qag = utg.QA_unit_tester_example()
        for n in range(10):
            sym = qag.get_symbols(1)
            self.assertTrue(sym not in prev_choices, msg='Generated symbols should not contain duplicates')
            prev_choices.append(sym)


    def test_get_names(self):
        seed = 0
        qag = utg.QA_unit_tester_example()
        test1a, test1b = qag.get_names(2)
        test2a, test2b = qag.get_names(2, full_name=False)
        names_list = ['Harry', 'Dick', 'Bob']
        test3 = qag.get_names(1, names_list=names_list)[0]
        self.assertNotEqual(test1a, test1b, msg='Names generated from list should not contain duplicates')
        self.assertTrue((' ' in test1a and ' ' in test1b), msg='If full_name flag is on, names should be full names')
        self.assertNotEqual(test2a, test2b, msg='Names generated from list should not contain duplicates')
        self.assertTrue((' ' not in test2a and ' ' not in test2b), msg='')
        self.assertTrue(test3 in names_list, msg='If full_name flag is off, names should only be first names')
        qag = utg.QA_unit_tester_example()
        prev_names = []
        for n in range(20):
            name = qag.get_names(1)
            self.assertTrue(name not in prev_names, msg='Generated names should not output previously generated names')
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
        self.assertTrue('Harry' in qag.names, msg='Registered names should be in qag.names')
        self.assertTrue(expr1 in qag.sympy_vars, msg='Registered expressions should be in sympy_vars')
        self.assertTrue(x in qag.sympy_vars, msg='Registered symbols should be in sympy_vars')

if __name__ == '__main__':
    unittest.main()
