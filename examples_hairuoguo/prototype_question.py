import numpy as np
import sympy as sympy
from class_prototype import *

class SimpleQuestionExample1(QAFormat):
    
    def __init__(self, variable_seed, correct_seed):
        QAFormat.__init__(self, variable_seed, correct_seed)
         
    def generate_q(self, seed):
        '''output formatted string for question'''
        self.question.set_expression(self.question_expression)
        '''Implement this method below'''
        #anything involve permutations would probably go here
        question = self.question.create_expression(seed)
        return "Solve: %s, %s, find %s" % question
        
    
    def generate_a(self, seed):
        '''output formatted string for answer'''
        self.answer.set_expression(self.answer_expression)
        '''Implement this method below'''
        answer = self.answer.create_expression(seed)
        return str(answer)
 
    def question_expression(self, seed):
        '''generate the mathematical expressions for the question'''
        np.random.seed(seed)
        '''Implement this method below'''
        var1 = self.question.get_symbol()
        var2 = self.question.get_symbol()
        var3 = self.question.get_symbol()

        expr1 = sympy.Eq(var1, var2)
        expr2 = sympy.Eq(var2, var3)
        
        return expr1, expr2, var1

    def answer_expression(self, seed):
        '''generate the mathematical expressions for the answer'''
        np.random.seed(seed)
        '''Implement this method below'''
        var1 = self.answer.get_symbol()
        var2 = self.answer.get_symbol()
        var3 = self.answer.get_symbol()

        expr = sympy.Eq(var1, var3)

        return expr

class SimpleQuestionExample2(SimpleQuestionExample1):
    #We can make this a subclass of the first example because they share the same question formatting
     
    def __init__(self, variable_seed, correct_seed):
        QAFormat.__init__(self, variable_seed, correct_seed)

    
    def question_expression(self, seed):
        '''generate the mathematical expressions for the question'''
        np.random.seed(seed)
        '''Implement this method below'''
        var1 = self.question.get_symbol()
        var2 = self.question.get_symbol()
        var3 = self.question.get_symbol()
        
        const1 = np.random.randint(1, 10)
        const2 = np.random.randint(1, 10)

        expr1 = sympy.Eq(var1, const1*var2)
        expr2 = sympy.Eq(var2, var3/const2)

        return expr1, expr2, var1

    def answer_expression(self, seed):
        '''generate the mathematical expressions for the answer'''
        np.random.seed(seed)
        '''Implement this method below'''
        var1 = self.answer.get_symbol()
        var2 = self.answer.get_symbol()
        var3 = self.answer.get_symbol()

        const1 = np.random.randint(1, 10)
        const2 = np.random.randint(1, 10)

        expr = var3*const1/const2

        return expr
        

class SimpleQuestionExample3(QAFormat):

    def __init__(self, variable_seed, correct_seed):
        QAFormat.__init__(self, variable_seed, correct_seed)
        
    def generate_q(self, seed):
        '''formatting for question'''
        self.question.set_expression(self.question_expression)
        question_expression = self.question.create_expression(seed)
        '''Implement this method below'''
        raise NotImplementedError
    
    def generate_a(self, seed):
        '''formatting for answer'''
        self.answer.set_expression(self.answer_expression)
        answer_expression = self.answer.create_expression(seed)
        '''Implement this method below'''
        raise NotImplementedError
    
    def question_expression(self, seed):
        '''generate the expression for the question'''
        np.random.seed(seed)
        '''Implement this method below'''
        #TODO: maybe something that would make it so that you only had to declare these variables once across the question and answer?
        raise NotImplementedError

    def answer_expression(self, seed):
        '''generate the expression for the answer'''
        np.random.seed(seed)
        '''Implement this method below'''
        raise NotImplementedError

 
if __name__ == "__main__":
    example1_instance = SimpleQuestionExample1(1, 1)
    example2_instance = SimpleQuestionExample2(1, 1)
    print(example1_instance.generate_mc_q(0))
    print(example1_instance.generate_mc_q(0))
    print(example2_instance.generate_mc_q(1))
    print(example2_instance.generate_mc_q(1))
    print(example1_instance.generate_mc_a(4, 0))
    print(example1_instance.generate_mc_a(4, 0))
    print(example2_instance.generate_mc_a(4, 1))
    print(example2_instance.generate_mc_a(3, 1))
 
