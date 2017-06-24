from sympy import *
import unittest

import utils

class Test_Utils(unittest.TestCase):

    def test_duplicates(self):
        # TODO utils.check_for_duplicates([],[])
        self.assertFalse( utils.duplicates_present([1,2,3],[]) )
        self.assertTrue( utils.duplicates_present([1,1,1,2],[]) )
        self.assertTrue( utils.duplicates_present([1,2,3],[1,2,3]) )
        #
        self.assertFalse( utils.duplicates_present(['1','2','3'],[]) )
        self.assertTrue( utils.duplicates_present(['1','1','1','2'],[]) )
        self.assertTrue( utils.duplicates_present(['1','2','3'],['1','2','3']) )
        #
        a,b,c,d,e,f = symbols('a b c d e f')
        self.assertFalse( utils.duplicates_present([a,b,c],[]) )
        self.assertTrue( utils.duplicates_present([a,a,a,b],[]) )
        self.assertTrue( utils.duplicates_present([a,b,c],[a,b,c]) )

    def test_make_strings_to_single_spaced(self):
        self.assertTrue(utils.make_strings_to_single_spaced('I  love   coding')=='I love coding')

    # def __init__(self, QAFormat_instance):
    # TODO hairuo
    #     unittest.TestCase.__init__(self)
    #     self.QAFormat = QAFormat_instance

    # def test_author(self):
    # TODO hairuo
    #     self.assertTrue(self.QAFormat.author != None)
    #
    # def test_description(self):
    # TODO hairuo
    #     self.assertTrue(self.QAFormat.description != None)
    #
    # def test_keywords(self):
    # TODO
    #     self.assertTrue(len(self.QAFormat.keywords) > 0)

if __name__ == '__main__':
    unittest.main()
