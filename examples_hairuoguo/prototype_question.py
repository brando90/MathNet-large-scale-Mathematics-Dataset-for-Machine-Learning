import numpy as np
import sympy as sympy
from class_prototype import *

class SimpleQuestionExample1(QAFormat):

    def __init__(self):
        QAFormat.__init__(self)

    def generate_q(self, seed):
        '''output formatted string for question'''
        self.question.set_expression(self.question_expression)
        '''Implement this method below'''
        #anything involve permutations would probably go here
        question = self.question.create_expression(*self.const_vars, *self.vars)
        return "Solve: %s, %s, find %s" % question

    def generate_a(self, seed):
        '''output formatted string for answer'''
        self.answer.set_expression(self.answer_expression)
        '''Implement this method below'''
        answer = self.answer.create_expression(*self.const_vars, *self.vars)
        return str(answer)

    def create_const_variables(self):
        var1 = self.get_symbol()
        var2 = self.get_symbol()
        var3 = self.get_symbol()

        return var1, var2, var3

    def create_variables(self):

        const1 = np.random.randint(1, 10)
        const2 = np.random.randint(1, 10)

        return const1, const2

    def question_expression(self, var1, var2, var3, const1, const2):
        '''generate the mathematical expressions for the question'''
        '''Implement this method below'''
        expr1 = sympy.Eq(var1, const1*var2)
        expr2 = sympy.Eq(var2, var3/const2)

        return expr1, expr2, var1

    def answer_expression(self, var1, var2, var3, const1, const2):
        '''generate the mathematical expressions for the answer'''
        '''Implement this method below'''

        expr = var3*const1/const2

        return expr



class SimpleQuestionExample2(QAFormat):

    def __init__(self):
        QAFormat.__init__(self)

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
    example1 = SimpleQuestionExample1()
    example1.set_correct_seed(1)
    example1.init_consistent(1)
    print(example1.generate_mc_q(0))
    print(example1.generate_mc_q(0))
    print(example1.generate_mc_a(4, 0))
    print(example1.generate_mc_a(4, 0))
