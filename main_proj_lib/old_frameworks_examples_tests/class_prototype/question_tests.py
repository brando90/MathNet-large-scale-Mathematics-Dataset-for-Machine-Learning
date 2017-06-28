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

    def __init__(self, QAFormat_instance):
        unittest.TestCase.__init__(self)
        self.QAFormat = QAFormat_instance

    def test_generate_q(self):
        self.QAFormat.generate_q(0)
          
    def test_generate_a(self):
        self.QAFormat.generate_a(0)

    def test_question_expression(self):
        self.QAFormat.question.create_expression()

    def test_answer_expression(self):
        self.QAFormat.answer.create_expression()
