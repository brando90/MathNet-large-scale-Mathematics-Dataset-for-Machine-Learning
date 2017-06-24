from sympy import *
import unittest

def run_unit_test_for_user():
    unittest.main()

class Test_user_QA(unittest.TestCase):
    def __init__(self):
        #TODO hairuo
        #unittest.TestCase.__init__(self)
        #self.QAFormat = QAFormat_instance
        pass

    def test_author_and_description_and_keywords(self):
        qagenerator = QA_constraint()
        self.assertTrue(qagenerator.author != None)
        self.assertTrue(qagenerator.description != None)
        self.assertTrue(qagenerator.keywords != None)

    def test_total_number_variables_is_larger_than_user_options(self):
        #TODO
        pass

    def test_total_number_variables_is_not_subset_than_user_options(self):
        #TODO
        pass


if __name__ == '__main__':
    unittest.main()
