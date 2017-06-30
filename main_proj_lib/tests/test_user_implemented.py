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
    
    test_seed_all(qag)
    test_init_consistent_qa_variables(qag)
    test_init_qa_variables(qag)
    test_Q(qag)
    test_A(qag)

def test_seed_all(qag):
    #test seeding changes how variables are generated
    for n in range(10):
        seed = random.randint(0, 1000)
        qag.seed_all(seed)
        name1 = qag.get_names(1)
        symbol1 = qag.get_symbols(1)
        variables1, const_variables1 = qag._create_all_variables()
        qag.reset_variables_states()
        qag.seed_all(seed)
        name2 = qag.get_names(1)
        symbol2 = qag.get_symbols(1)
        variables2, const_variables2 = qag._create_all_variables()
        
        assert name1 == name2
        assert str(symbol1) == str(symbol2)
        assert variables1 == variables2
        assert const_variables1 == const_variables2
    

def test_init_consistent_qa_variables(qag):
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
    
    assert vars2 == vars1
    assert vars3 == vars4 #test that debug flag removes randomness
    assert len(vars1) == len(set(vars1))
    assert len(vars1) > 0
    assert ((len(qag.sympy_vars)) > 0 or (len(qag.names) > 0))
    

def test_init_qa_variables(qag):
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
    
    assert vars2 == vars1
    assert vars3 == vars4 #test that debug flag removes randomness
    assert len(vars1) == len(set(vars1))

def test_Q(qag):
    variables, const_variables = qag._create_all_variables() 
    qag.generator_unit_test = True
    question_ob = qag.Q(*variables, *const_variables)
    assert isinstance(question_ob, de.DelayedExecution)
    

def test_A(qag):
    variables, const_variables = qag._create_all_variables() 
    qag.generator_unit_test = True
    answer_ob = qag.A(*variables, *const_variables)
    assert isinstance(answer_ob, de.DelayedExecution)
    
    


if __name__ == "__main__":
    if len(sys.argv) > 1:
        run_tests(sys.argv[1])
