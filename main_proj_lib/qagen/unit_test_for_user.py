from sympy import *
import unittest

from qagen.delayed_execution import *

def run_unit_test_for_user(qa_constructor,*args,user_defined_unit_test=None,**kwargs):
    '''
    Runs some tests to help the user have a reliable question answer class.

    qa_constructor = the users class name
    '''
    #TODO add feature user defined unit tests
    runner = unittest.TextTestRunner()
    #
    test_suite = unittest.TestSuite()
    # add tests
    # TODO: change this horrible code, we dont need to add tests like this
    test_suite.addTest( Test_author_and_description_and_keywords(qa_constructor,arg,kwargs) )
    test_suite.addTest( Test_basic_user_test(qa_constructor,arg,kwargs) )
    test_suite.addTest( Test_basic_uses_generators(qa_constructor,arg,kwargs) )
    runner.run(test_suite)

class Test_author_and_description_and_keywords(unittest.TestCase):

    def __init__(self,qa_constructor,args,kwargs):
        super().__init__()
        self.qa_constructor = qa_constructor
        self.args = args
        self.kwargs = kwargs

    def runTest (self):
        # TODO how do I stop hardcoding the tests here, just go over your
        # test cases and run them
        self.test_author_and_description_and_keywords()

    def test_author_and_description_and_keywords(self):
        #print('---')
        qagenerator = self.qa_constructor()
        self.assertNotEqual(qagenerator.author, None)
        self.assertNotEqual(qagenerator.description, None)
        self.assertNotEqual(qagenerator.keywords, None)

class Test_basic_user_test(unittest.TestCase):

    def __init__(self,qa_constructor,args,kwargs):
        super().__init__()
        self.qa_constructor = qa_constructor
        self.args = args
        self.kwargs = kwargs

    def runTest (self):
        # TODO how do I stop hardcoding the tests here, just go over your
        qagenerator = self.qa_constructor()
        qagenerator.debug = True
        q,a = qagenerator.get_single_qa(seed=1)
        #print(q)
        #print('>>qagenerator.generator_unit_test: ',qagenerator.generator_unit_test)
        self.assertEqual(qagenerator.description,q)

class Test_basic_uses_generators(unittest.TestCase):

    def __init__(self,qa_constructor,args,kwargs):
        super().__init__()
        self.qa_constructor = qa_constructor
        self.args = args
        self.kwargs = kwargs

    def runTest (self):
        # TODO how do I stop hardcoding the tests here, just go over your
        qagenerator = self.qa_constructor()
        qagenerator.debug = False
        qagenerator.generator_unit_test = True
        q,a = qagenerator.get_single_qa(seed=1)
        #
        q_is_de = isinstance(q, DelayedExecution)
        a_is_de = isinstance(a, DelayedExecution)
        if q_is_de or a_is_de:
            gen_ops = 'seqg, perg, choiceg '
            warning_string = 'Your {} is not returning a {} generator. Make sure you do for the framework to work correctly.'
            if not q_is_de:
                #print(warning_string.join('question',gen_ops))
                raise ValueError(warning_string.format('question',gen_ops))
            if not a_is_de:
                #print(warning_string.join('answer',gen_ops))
                raise ValueError(warning_string.format('answer',gen_ops))
        self.assertEqual( type(q()),str )
        self.assertEqual( type(a()),str )
        #
        qagenerator.debug = True
        q,a = qagenerator.get_single_qa(seed=1)
        qs = q()
        self.assertEqual(qs,qagenerator.description)

###

class Test_MC(unittest.TestCase):

    def __init__(self,qa_constructor,args,kwargs):
        super().__init__()
        self.qa_constructor = qa_constructor
        self.args = args
        self.kwargs = kwargs

    def runTest (self):
        # TODO
        pass

class Test_one_to_many_constant_format(unittest.TestCase):

    def __init__(self,qa_constructor,args,kwargs):
        super().__init__()
        self.qa_constructor = qa_constructor
        self.args = args
        self.kwargs = kwargs

    def runTest (self):
        # TODO
        pass

class Test_many_to_many(unittest.TestCase):

    def __init__(self,qa_constructor,args,kwargs):
        super().__init__()
        self.qa_constructor = qa_constructor
        self.args = args
        self.kwargs = kwargs

    def runTest (self):
        # TODO
        pass

    # it would be nice to add some tests where we create a lot of questions
    # and see if the users code breaks
    #
    #
    # def test_total_number_variables_is_larger_than_user_options(self):
    #     #TODO
    #     pass
    #
    # def test_total_number_variables_is_not_subset_than_user_options(self):
    #     #TODO
    #     pass

if __name__ == '__main__':
    unittest.main()
