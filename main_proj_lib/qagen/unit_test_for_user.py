from sympy import *
import unittest

def run_unit_test_for_user(qa_constructor,*args,**kwargs):
    runner = unittest.TextTestRunner()
    #
    test_suite = unittest.TestSuite()
    # add tests
    # TODO: change this horrible code, we dont need to add tests like this
    test_suite.addTest(Test_author_and_description_and_keywords(qa_constructor,arg,kwargs))
    test_suite.addTest(Test_basic_user_test(qa_constructor,arg,kwargs))
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
        print('---')
        qagenerator = self.qa_constructor()
        self.assertTrue(qagenerator.author != None)
        self.assertTrue(qagenerator.description != None)
        self.assertTrue(qagenerator.keywords != None)

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
        print(q)
        self.assertTrue(qagenerator.description == q)
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
