import unittest

class TestQAFormatFields(unittest.TestCase):

    def __init__(self, QAFormat_instance):
        unittest.TestCase.__init__(self) 
        self.QAFormat = QAFormat_instance
    
    def test_author(self):
        self.assertTrue(self.QAFormat.author != None)
    
    def test_description(self):
        self.assertTrue(self.QAFormat.description != None)

    def test_keywords(self):
        self.assertTrue(len(self.QAFormat.keywords) > 0)


class TestQAFormatMethods(unittest.TestCase):

    def test_generate_q(self):

    def test_generate_a(self):

    def test_question_expression(self):

    def test_answer_expression(self): 
