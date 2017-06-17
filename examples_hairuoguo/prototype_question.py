import numpy as np

class TemplateMC(QAFormat):
    
    def __init__(variable_seed, correct_seed):
        QAFormat.__init__(variable_seed, correct_seed)
         
    def generate_q(self, seed):
    '''formatting for question'''
        self.question.set_expression(question_expression)
        question_expression = self.question.create_expression(seed)
    '''Implement this method below'''
        except NotImplementedError
    
    def generate_a(self, seed):
    '''formatting for answer'''
        self.answer.set_expression(answer_expression)
        answer_expression = self.answer.create_expression(seed)
    '''Implement this method below'''
        except NotImplementedError
    
    def question_expression(self, seed):
    '''generate the expression for the question'''
    '''Implement this method below'''
        except NotImplementedError

    def answer_expression(self, seed):
    '''generate the expression for the answer'''
    '''Implement this method below'''
        except NotImplementedError
        

        

 


