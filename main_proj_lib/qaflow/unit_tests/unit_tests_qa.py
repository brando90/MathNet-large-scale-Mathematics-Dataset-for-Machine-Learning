#from require import require
import unittest
from sympy import *
import numpy as np
import random

from qaflow import *
from qaflow.question_answer import *

class Test_problem(unittest.TestCase):

    def ans_with_sympy(self,x,two,eight):
        return seqg(x, ' = ', two*eight )

    def ans_with_delayed_multiplication(self,x):
        ##
        @func_flow
        def my_mult(a,b):
            return a*b
        return seqg(x, ' = ', seqg( my_mult(2,8) ) )

    def ans_with_string(self,x):
        return seqg(x,' = ',2,'*',8)

    def explicit_delay_executor(self,x,a,b):
        return seqg( DelayedExecution(lambda a,b: a*b, a, b) )

    def just_pass_lambda_func(self,x,a,b):
        # Doesn't quite work!
        return seqg( lambda a,b: a*b, a, b )

    def ans_with_delayed_and_straight_mult(self,x):
        explicit_mul = self.ans_with_string(x)
        @func_flow
        def my_mult(a,b):
            return a*b
        evaluated_mul = seqg( my_mult(2,8) )
        return seqg( explicit_mul,' = ', evaluated_mul )

    ##

    def test_ans_with_sympy(self):
        x,y,a,b, X = symbols('x y a b X')
        e,f,g,h = symbols('e f g h')
        two, eight = symbols('2 8')
        ## solve x,  a = b,  x = 2*b, a = 8, can you do it?
        question = seqg(seqg('solve ',x,', '), seqg( seqg(Eq(a,b),', ') , seqg(Eq(x,two*b),', ') , seqg(Eq(a,eight),', ') ), 'can you do it?')
        ## pssible alternative assignments for symbols
        assignments = {}
        assignments[a] = [a,e,f,g,h]
        assignments[x] = [x,X]
        assignments[eight] = [1,2,3,4,5,6,7,8]
        ## possible answer(s)
        ans1 = self.ans_with_sympy(two,eight)
        ## generator for a choice of answer
        answer = choiceg( ans1 )
        q,a = make_qa_pair(question,answer,assignments)
        print('question: %s \n answer %s \n'%(q,a))

    def test_example_subs_seq_mutliple_choices(self):
        x,y,a,b, X = symbols('x y a b X')
        e,f,g,h = symbols('e f g h')
        #check numpy matrices work
        ## solve x,  a = b,  x = 2*b, a = 8, can you do it?
        question = seqg(seqg('solve ',x,', '), seqg( seqg(Eq(a,b),', ') , seqg(Eq(x,2*b),', ') , seqg(Eq(a,8),', ') ), 'can you do it?')
        ## pssible alternative assignments for symbols
        assignments = {}
        assignments[a] = [a,e,f,g,h]
        assignments[x] = [x,X]
        assignments[8] = [random.randint(0,200) for i in range(100)]
        ## possible answer(s)
        ans1 = self.ans_with_string(x)
        ans2 = self.ans_with_delayed_multiplication(x)
        ans3 = self.ans_with_delayed_and_straight_mult(x)
        ans4 = self.explicit_delay_executor(x,2,8)
        #ans5 = self.just_pass_lambda_func(x,2,8)
        ## generator for a choice of answer
        answer = choiceg( ans1,ans2,ans3,ans4 )
        #answer = choiceg(ans5)
        q,a = make_qa_pair(question,answer,assignments)
        print('question: %s \nanswer %s'%(q,a))

    def test_matrices_handling(self):
        A, B, C = symbols('A B C')
        assignments = {}
        assignments[A] = [B, C]
        np_matrix_B = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
        np_matrix_C = np.array([[0, 1, 0], [0, 1, 0], [0, 0, 0]])
        B = ImmutableMatrix(Matrix(np_matrix_B))
        C = ImmutableMatrix(Matrix(np_matrix_C))
        question = Question() + 'Test this: ' + A
        answer = Answer() + 'Test this: ' + A
        q, a = make_qa_pair(question, answer, assignments, use_latex=True)
        self.assertEqual(q, a)
        assignments[A] = [B]
        q, a = make_qa_pair(question, answer, assignments, use_latex=True)
        B_string = 'Test this:  $%s$' % latex(B)
        self.assertEqual(q, B_string)
        self.assertEqual(a, B_string)
        assignments[A] = [C]
        q, a = make_qa_pair(question, answer, assignments, use_latex=True)
        C_string = 'Test this:  $%s$' % latex(C)
        self.assertEqual(q, C_string)
        self.assertEqual(a, C_string)    
    
    def test_random_seeding(self):
        a, b, c, d, e, f = symbols('a b c d e f')
        assignments = {}
        question = Question() + a
        answer = Answer() + a
        assignments[a] = [a, b, c, d, e, f]
        seed = 0.1
        q1, a1 = make_qa_pair(question, answer, assignments, seed=seed, use_latex=True)
        q2, a2 = make_qa_pair(question, answer, assignments, seed=seed, use_latex=True)
        #check that deterministic
        self.assertEqual(q1, q2)
        self.assertEqual(a1, a2)
        #check for randomness if no entry
        q3, a3 = make_qa_pair(question, answer, assignments, use_latex=True)
        self.assertEqual(q3, a3)
        #check works wtih all seeds
        q3, a3 = make_qa_pair(question, answer, assignments, seed=1, use_latex=True)
        self.assertEqual(q3, a3)
        q3, a3 = make_qa_pair(question, answer, assignments, seed=0.5, use_latex=True)
        self.assertEqual(q3, a3)
        q3, a3 = make_qa_pair(question, answer, assignments, seed=-1.5, use_latex=True)
        self.assertEqual(q3, a3)

class Test_duplicate_checking(unittest.TestCase):
        
        def test_empty_assignments(self):
            #check empty
            assignments = {}
            try:
                check_for_duplicate_assignments(assignments)
            except:
                self.assertTrue(False)

        def test_no_duplicates(self):
            #check no duplicates
            a, b, c, d, e, f = symbols('a b c d e f')
            assignments = {}
            assignments[a] = [c, d]
            assignments[b] = [e, f]
            try:
                check_for_duplicate_assignments(assignments)
            except:
                self.assertTrue(False)
    
        def test_duplicate_symbols(self):
            #check symbols
            a, b, c, d, e, f = symbols('a b c d e f')
            assignments = {}
            assignments[a] = [d, e]
            assignments[b] = [e, f]
            assignments[c] = [d, f]
            with self.assertRaises(DuplicateAssignmentError):
                check_for_duplicate_assignments(assignments)

        def test_assignment_is_not_variable(self):
            #tests to make sure that assignment is also not a variable
            a, b, c, d, e, f = symbols('a b c d e f')
            assignments = {}
            assignments[a] = [d, e]
            assignments[b] = [a]
            with self.assertRaises(DuplicateAssignmentError):
                check_for_duplicate_assignments(assignments)
            assignments[b] = [a]
            assignments[a] = [d, e]
            with self.assertRaises(DuplicateAssignmentError):
                check_for_duplicate_assignments(assignments)

'''
class Test_latex_flag(unittest.TestCase)

        def test_latex_expressions(self):
        #check that latex works for expressions
        def test_latex_strings(self):
        #check that latex works for just strings
        def test_latex_matrices(self):
        #check that latex works for matrices
'''


if __name__ == '__main__':
    '''
    unit_test = Test_problem()
    #unittest.main()
    unit_test.test_example_subs_seq_mutliple_choices()
    unit_test.test_matrices_handling()
    unit_test.test_random_seeding()
    '''
    unit_test = Test_duplicate_checking()
    unit_test.test_empty_assignments()
    unit_test.test_no_duplicates()
    unit_test.test_duplicate_symbols()
    unit_test.test_assignment_is_not_variable()
