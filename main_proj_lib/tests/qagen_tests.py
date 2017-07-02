from sympy import *
import unittest
import random
import numpy as np
from qagen import *
from qagen import utils
import numpy as np
import unit_tester_generators as utg
import inspect

class TestQAGen(unittest.TestCase):

    
    def test_create_all_variables(self):
        qag = utg.QA_unit_tester_example()
        variables, variables_consistent = qag._create_all_variables()
        self.assertEqual(len(qag.sympy_vars), len(set(qag.sympy_vars)), msg='qag.sympy_vars should not contain duplicates')
        self.assertEqual(len(qag.names), len(set(qag.names)), msg='qag.names should not contain duplicates') 

    def test_generate_single_qa_MC(self):
        qag = utg.QA_unit_tester_example()
        qag.debug = False
        permute = False
        for n in range(1, 100):
            q1, a1 = qag.generate_single_qa_MC(4, n)
            q2, a2 = qag.generate_single_qa_MC(4, n)
            if (q1, a1) != qag.generate_single_qa_MC(4, n-1):
                permute = True
            self.assertEqual(str(q1), str(q2), msg='Question generation should be deterministic given seed')
            self.assertEqual(str(a1), str(a2), msg='Answer generation should be deterministic given seed')
            self.assertEqual(len(a1), len(set(a1)), msg='Answers generated should not contain duplicates')
        self.assertTrue(permute, msg='Seeding should result in different questions and answers generated')

    def test_generate_single_qa_many_to_one(self):
        qag = utg.QA_unit_tester_example()
        permute = False
        for n in range(1, 100):
            q_list1, a_str1 = qag.generate_single_qa_many_to_one(3, n)
            q_list2, a_str2 = qag.generate_single_qa_many_to_one(3, n)
            if a_str1 != qag.generate_single_qa_many_to_one(3, n-1):
                permute = True
            self.assertEqual(str(q_list1), str(q_list2), msg='Questions generated should be deterministic given seed')
            self.assertEqual(str(a_str1), str(a_str2), msg='Answers generated should be deterministic given seed')
            self.assertEqual(len(q_list1), 3, msg='Number of questions generated should be consistent with input argument')
            self.assertEqual(len(q_list2), 3, msg='Number of questions generated should be consistent with input argument')
            #self.assertEqual(qag.Q.args, qag.A.args) # check to make sure that values passed into Q,A are same.
        self.assertTrue(permute, msg='Seeding should result in different questions and answers generated')
        
         

    def test_generate_one_to_many(self):
        qag = utg.QA_unit_tester_example()
        permute = False
        qag.debug = True
        for n in range(1, 100):
            q_1, a_list1 = qag.generate_one_to_many(3, n)
            q_2, a_list2 = qag.generate_one_to_many(3, n)
            if q_1 != qag.generate_one_to_many(3, n-1)[0]:
                permute = True
            self.assertEqual(str(q_1), str(q_2), msg='Question generation should be deterministic given seed')
            self.assertEqual(str(a_list1), str(a_list2), msg='Answer generation should be deterministic given seed')
            self.assertEqual(len(a_list1), 3, msg='Number of answers generated should be consistent with inputted argument')
            self.assertEqual(len(a_list2), 3, msg='Number of answers generated should be consistent with inputted argument')
            #self.assertEqual(qag.Q.args, qag.A.args)# check to make sure that values passed into Q,A are same.
        self.assertTrue(permute, msg='Seeding should result in different questions and answers generated')
        #check variables are same  

    def test_generate_many_to_many(self):
        qag = utg.QA_unit_tester_example()
        permute = False
        for n in range(1, 100):
            q_list1, a_str1 = qag.generate_many_to_many(3, 3, n)
            q_list2, a_str2 = qag.generate_many_to_many(3, 3, n)
            if a_str1 != qag.generate_many_to_many(3, 3, n-1):
                permute = True
            self.assertEqual(str(q_list1), str(q_list2), msg='Question generation should be deterministic given seed.')
            self.assertEqual(str(a_str1), str(a_str2), msg='Answer generation should be deterministic given seed')
            self.assertEqual(len(q_list1), 3, msg='Number of questions generated should be consistent with inputted argument')
            self.assertEqual(len(q_list2), 3, msg='Number of questions generated should be consistent with inputted argument')
            #self.assertEqual(qag.Q.args, qag.A.args)# check to make sure that values passed into Q,A are same.
        self.assertTrue(permute, msg='Seeding should result in different questions and answers generated')
        #check variables are same 
    '''
    Probably deprecated because we can't enforce consistency across multiple generated q,a pairs; we can only guarantee that the format will be deterministic w.r.t seed
    def test_generate_many_to_one_consistent_format(self):
        qag = utg.QA_unit_tester_example()
    '''


    def test_reset_variables_states(self):
        qag = utg.QA_unit_tester_example()
        qag._create_all_variables()
        self.assertEqual(len(qag.names), 0, msg='qag.names should be empty')
        self.assertEqual(len(qag.sympy_vars), 0, msg='qag.sympy_vars should be empty')

    def test_get_single_qa(self):
        qag = utg.QA_unit_tester_example()
        permute = False
        for n in range(1, 100):
            q_list1, a_str1 = qag.get_single_qa(n)
            q_list2, a_str2 = qag.get_single_qa(n)
            if a_str1 != qag.get_single_qa(n-1):
                permute = True
            self.assertEqual(str(q_list1), str(q_list2), msg='Questions generated should be deterministic given seed')
            self.assertEqual(str(a_str1), str(a_str2), msg='Answers generated should be deterministic given seed')
            #self.assertEqual(qag.Q.args, qag.A.args)# check to make sure that values passed into Q,A are same.
        self.assertTrue(permute, msg='Seeding should result in different questions and answers generated.')

if __name__ == "__main__":
    unittest.main()
