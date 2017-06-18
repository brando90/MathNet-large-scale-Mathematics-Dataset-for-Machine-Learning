import numpy as np
import sympy as sympy

class SimpleQuestionExample1(QAFormat):
    
    def __init__(variable_seed, correct_seed):
        QAFormat.__init__(variable_seed, correct_seed)
         
    def generate_q(self, seed):
    '''formatting for question'''
        self.question.set_expression(question_expression)
        np.random.seed(seed)
    '''Implement this method below'''
    #anything involve permutations would probably go here
        question = self.question_expression()
        print("Solve: %s, %s, find %s" % answer)
        
    
    def generate_a(self, seed):
    '''formatting for answer'''
        self.answer.set_expression(answer_expression)
        np.random.seed(seed)
    '''Implement this method below'''
        answer = self.answer_expression()
        print(answer)
 
    def question_expression(self):
    '''generate the expression for the question'''
        np.random.seed(seed)
    '''Implement this method below'''
        var1 = self.question.get_symbol()
        var2 = self.question.get_symbol()
        var3 = self.question.get_symbol()

        expr1 = sympy.Eq(var_1, var_2)
        expr2 = sympy.Eq(var_2, var_3)
        
        return expr1, expr2, var1

    def answer_expression(self):
    '''generate the expression for the answer'''
    '''Implement this method below'''
        var1 = self.answer.get_symbol()
        var2 = self.answer.get_symbol()
        var3 = self.answer.get_symbol()

        expr = sympy.Eq(var1, var3)

        return expr

class SimpleQuestionExample2(QAFormat)
     
    def __init__(variable_seed, correct_seed):
        QAFormat.__init__(variable_seed, correct_seed)

    def generate_q(self, seed):
    '''formatting for question'''
        self.question.set_expression(question_expression)
        question_expression = self.question.create_expression(seed)
    '''Implement this method below'''
        
    
    def generate_a(self, seed):
    '''formatting for answer'''
        self.answer.set_expression(answer_expression)
        answer_expression = self.answer.create_expression(seed)
    '''Implement this method below'''
    
    def question_expression(self, seed):
    '''generate the expression for the question'''
        np.random.seed(seed)
    '''Implement this method below'''
        var1 = self.question.get_symbol()
        var2 = self.question.get_symbol()
        var3 = self.question.get_symbol()
        
        const1 = np.random.randint(1, 10)
        const2 = np.random.randint(1, 10)
        const3 = np.random.randint(1, 10)

        expr1 = 
        expr2 = 
        expr3 = 

    def answer_expression(self, seed):
    '''generate the expression for the answer'''
        np.random.seed(seed)
    '''Implement this method below'''
        var1 = self.answer.get_symbol()
        var2 = self.answer.get_symbol()
        var3 = self.answer.get_symbol()

        

class MatrixQuestionExample(QAFormat)

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
        np.random.seed(seed)
    '''Implement this method below'''
        #TODO: maybe something that would make it so that you only had to declare these variables once across the question and answer?
        except NotImplementedError

    def answer_expression(self, seed):
    '''generate the expression for the answer'''
        np.random.seed(seed)
    '''Implement this method below'''
        except NotImplementedError

 


