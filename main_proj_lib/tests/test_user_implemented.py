import unittest
from sympy import *
import numpy as np
import random
from qagen import delayed_execution as de
from qagen import utils
import os
import sys

def run_tests(qag_file):
   
    taxonomy_base = os.path.abspath('../../math_taxonomy/') 
    classes = utils.get_classes(os.path.join(taxonomy_base, qag_file))
    qa = classes[0]
    qag = qa()
   
    runner = unittest.TextTestRunner()
    test_suite = unittest.TestSuite()
 
    test_suite.addTest(Test_seed_all(qag, arg, kwargs))
    test_suite.addTest(test_init_consistent_qa_variables(qag, arg, kwargs))
    test_suite.addTest(test_init_qa_variables(qag, arg, kwargs))
    test_suite.addTest(test_Q(qag, arg, kwargs))
    test_suite.addTest(test_A(qag, arg, kwargs))
    runner.run(test_suite)

class Test_seed_all(unittest.TestCase):
    
    def __init__(self, qa_constructor, args, kwargs):
        super().__init__()
        self.qa_constructor = qa_constructor
        self.args = args
        self.kwargs = kwargs

    def runTest(self):
        #test seeding changes how variables are generated
        permute = False
        qag = self.qa_constructor
        for n in range(1, 100):
            seed = n
            qag.seed_all(seed)
            name1 = qag.get_names(1)
            symbol1 = qag.get_symbols(1)
            variables1, const_variables1 = qag._create_all_variables()
            qag.reset_variables_states()
            qag.seed_all(seed)
            name2 = qag.get_names(1)
            symbol2 = qag.get_symbols(1)
            variables2, const_variables2 = qag._create_all_variables()
            qag.seed_all(seed-1)
            if name1 != qag.get_names(1):
                permute = True
            self.assertTrue(name1 == name2, msg='Name generation by seed should be deterministic')
            self.assertTrue(str(symbol1) == str(symbol2), msg='Symbol generation by seed should be deterministic')
            self.assertTrue(variables1 == variables2, msg='Variable generation by seed should be deterministic')
            self.assertTrue(const_variables1 == const_variables2, msg='Consistent variable generation by seed should be deterministic')
        self.assertTrue(permute, msg='Seeding should cause generation of different variable values'
        
class Test_init_consistent_qa_variables(unittest.TestCase):
   
    def __init__(self, qa_constructor, args, kwargs):
        super().__init__()
        self.qa_constructor = qa_constructor
        self.args = args
        self.kwargs = kwargs

    def runTest(self):
        qag = self.qa_constructor
    
        seed = random.randint(0, 1000)
        qag.seed_all(seed)
        vars1 = qag.init_consistent_qa_variables()
        qag.reset_variables_states()
        qag.seed_all(seed)
        vars2 = qag.init_consistent_qa_variables()
        
        seed2 = random.randint(0, 1000)
        seed3 = random.randint(0, 1000)
        qag.debug = True
        qag.seed_all(seed2)
        vars3 = qag.init_consistent_qa_variables()
        qag.seed_all(seed3)
        vars4 = qag.init_consistent_qa_variables()
        
        self.assertTrue(vars2 == vars1, msg='Generation by seed should be deterministic')
        self.assertTrue(vars3 == vars4, msg='Debug flag should remove random generation of variables') #test that debug flag removes randomness
        self.assertTrue(len(vars1) == len(set(vars1)), msg='Variables should not contain duplicates')
        self.assertTrue(len(vars1) > 0, msg='Number of variables generated should be at least 1')
        self.assertTrue(((len(qag.sympy_vars)) > 0 or (len(qag.names) > 0)), msg='Either names or symbols should be generated.')
        
class Test_init_qa_variables(unittest.TestCase):
    
    def __init__(self, qa_constructor, args, kwargs):
        super().__init__()
        self.qa_constructor = qa_constructor
        self.args = args
        self.kwargs = kwargs
    
    def runTest(self):
        qag = self.qa_constructor
        seed = random.randint(0, 1000)
        qag.seed_all(seed)
        vars1 = qag.init_qa_variables()
        qag.reset_variables_states()
        qag.seed_all(seed)
        vars2 = qag.init_qa_variables()
        
        seed2 = random.randint(0, 1000)
        seed3 = random.randint(0, 1000)
        qag.debug = True
        qag.seed_all(seed2)
        vars3 = qag.init_qa_variables()
        qag.seed_all(seed3)
        vars4 = qag.init_qa_variables()
        
        self.assertTrue(vars2 == vars1, msg='Generation by seed should be deterministic')
        self.assertTrue(vars3 == vars4, msg='Debug flag should remove random generation of variables') #test that debug flag removes randomness
        self.assertTrue(len(vars1) == len(set(vars1)), msg='Generated variables should not contain duplicates')

class Test_Q(unittest.TestCase):

    def __init__(self, qa_constructor, args, kwargs):
        super().__init__()
        self.qa_constructor = qa_constructor
        self.args = args
        self.kwargs = kwargs

    def runTest(self):
        qag = self.qa_constructor
        variables, const_variables = qag._create_all_variables() 
        qag.generator_unit_test = True
        question_ob = qag.Q(*variables, *const_variables)
        self.assertTrue(isinstance(question_ob, de.DelayedExecution), msg='Question implemention must use perg, seqg, choiceg.')
    

class Test_A(unittest.TestCase):

    def __init__(self, qa_constructor, args, kwargs):
        super().__init__()
        self.qa_constructor = qa_constructor
        self.args = args
        self.kwargs = kwargs

    def runTest(self):
        qag = self.qa_constructor
        variables, const_variables = qag._create_all_variables() 
        qag.generator_unit_test = True
        answer_ob = qag.A(*variables, *const_variables)
        self.assertTrue(isinstance(answer_ob, de.DelayedExecution), msg='Answer implemention must use perg, seqg, choiceg.')
    
    


if __name__ == "__main__":
    if len(sys.argv) > 1:
        run_tests(sys.argv[1])
