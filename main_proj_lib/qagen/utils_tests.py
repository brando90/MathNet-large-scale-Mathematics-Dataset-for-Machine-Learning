import unittest

import utils

class Test_Utils(unittest.TestCase):

    def test_duplicates(self):
        # TODO utils.check_for_duplicates([],[])
        self.assertFalse( utils.check_for_duplicates([1,2,3],[]) )
        self.assertTrue( utils.check_for_duplicates([1,1,1,2],[]) )
        self.assertTrue( utils.check_for_duplicates([1,2,3],[1,2,3]) )

    # def __init__(self, QAFormat_instance):
    #     unittest.TestCase.__init__(self)
    #     self.QAFormat = QAFormat_instance

    # def test_author(self):
    #     self.assertTrue(self.QAFormat.author != None)
    #
    # def test_description(self):
    #     self.assertTrue(self.QAFormat.description != None)
    #
    # def test_keywords(self):
    #     self.assertTrue(len(self.QAFormat.keywords) > 0)

if __name__ == '__main__':
    unittest.main()
