from sympy import *
import unittest

import utils

class Test_user_QA(unittest.TestCase):
    def __init__(self):
        #TODO hairuo
        #unittest.TestCase.__init__(self)
        #self.QAFormat = QAFormat_instance
        pass

    def test_author(self):
        #TODO hairuo
        #self.assertTrue(self.QAFormat.author != None)
        pass

    def test_description(self):
        #TODO hairuo
        #self.assertTrue(self.QAFormat.description != None)
        pass

    def test_keywords(self):
        #TODO
        #self.assertTrue(len(self.QAFormat.keywords) > 0)
        pass

    def test_total_number_variables_is_larger_than_user_options(self):
        #TODO
        pass

    def test_total_number_variables_is_not_subset_than_user_options(self):
        #TODO
        pass


if __name__ == '__main__':
    unittest.main()
