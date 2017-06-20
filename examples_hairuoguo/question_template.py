import numpy as np

class Template(QAFormat):
    
    def __init__(self):
        QAFormat.__init__(self)
         
    def generate_q(self, seed):
        '''output formatted string for question'''
        self.question.set_expression(self.question_expression)
        question = self.question.create_expression(*self.const_vars, *self.vars)
        '''Implement this method below'''
        #anything involve permutations would probably go here
        raise NotImplementedError 
    
    def generate_a(self, seed):
        '''output formatted string for answer'''
        self.answer.set_expression(self.answer_expression)
        answer = self.answer.create_expression(*self.const_vars, *self.vars)
        '''Implement this method below'''
        raise NotImplementedError

    def create_const_variables(self):
        '''function that returns variables constant across question and answer'''
        '''Implement this method below'''
        raise NotImplementedError

    def create_variables(self):
        '''function that returns variables that are not constant across question and answer'''
        '''Implement this method below'''
        raise NotImplementedError

    def question_expression(self):
        '''generate the mathematical expressions for the question'''
        '''Implement this method below'''
        raise NotImplementedError

    def answer_expression(self):
        '''generate the mathematical expressions for the answer'''
        '''Implement this method below'''
        raise NotImplementedError

