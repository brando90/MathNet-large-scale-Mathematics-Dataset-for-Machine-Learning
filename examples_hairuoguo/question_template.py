import numpy as np

class TemplateMC(QAFormat):
    
    def __init__(variable_seed, correct_seed):
        QAFormat.__init__(variable_seed, correct_seed)
         
    def generate_q(self, seed):
    '''created formatted string for question'''
        self.question.set_expression(question_expression)
        question_expression = self.question.create_expression(seed)
    '''Implement this method below'''
        except NotImplementedError
    
    def generate_a(self, seed):
    '''create formatted string for answer'''
        self.answer.set_expression(answer_expression)
        answer_expression = self.answer.create_expression(seed)
    '''Implement this method below'''
        except NotImplementedError
    
    def question_expression(self, seed):
    '''generate the mathematical expressions for the question'''
        np.random.seed(seed)
    '''Implement this method below'''
        #TODO: maybe something that would make it so that you only had to declare these variables once across the question and answer?
        except NotImplementedError

    def answer_expression(self, seed):
    '''generate the mathematical expressions for the answer'''
        np.random.seed(seed)
    '''Implement this method below'''
        except NotImplementedError
        

        

 


