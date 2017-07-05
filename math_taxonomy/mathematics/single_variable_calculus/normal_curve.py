from sympy import *
import random
import numpy as np
import pdb

from qagen.qagen import *
from qagen import utils
from qagen import unit_test_for_user as user_test

# TODO: You can also put your quesiton example here

class QA_constraint(QAGen):

    def __init__(self):
        '''
        Initializer for your QA question.
        '''
        super().__init__()
        self.author = 'theosech'
        self.description = '''Let f(x) = 3*x + 5*sin(x). Find the gradient of the normal to the curve of f at x=1.'''
        # keywords about the question that could help to make this more searchable in the future
        self.keywords = ['normal gradient', 'derivative', 
        'normal to curve']
        self.use_latex = True

    def seed_all(self,seed):
        '''
        Write the seeding functions of the libraries that you are using.
        Its important to seed all the libraries you are using because the
        framework will assume it can seed stuff for you. It needs this for
        the library to work.
        '''
        np.random.seed(seed)
        self.fake.random.seed(seed)
        random.seed(seed)

    def init_consistent_qa_variables(self):
        """
        Defines and returns all the variables that need to be consistent
        between a question and an answer. Usually only names and variable/symbol
        names.

        Example: when generating MC questions the non consistent variables will
        be used to generate other options. However, the names, symbols, etc
        should remain consistent otherwise some answers will be obviously fake.

        Note: debug flag can be used to deterministically output a QA that has
        simple numbers to check the correctness of your QA.
        """

        return tuple()

    def init_qa_variables(self):
        '''
        Defines and returns all the variables that can vary between a
        question and an answer. Good examples are numerical values that might
        make the answers not obviously wrong.

        Example: when generating MC questions the non consistent variables will
        be used to generate other options. However, the names, symbols, etc
        should remain consistent otherwise some answers will be obviously fake.
        Numerical values that have been fully evaluated are a good example of
        how multiple choice answers can be generated.

        Note: debug flag can be used to deterministically output a QA that has
        simple numbers to check the correctness of your QA.
        '''
        if self.debug:
            value = 1
            const1 = 3
            const2 = 5
        else:
            value = random.randint(-1000,1000)
            const1 = random.randint(-1000,1000)
            const2 = random.randint(-1000,1000)  
        return value, const1, const2

    def Q(s, value, const1, const2): #TODO change the signature of the function according to your question
        '''
        Small question description.

        Important Note: first variables are the not consistent variables followed
        by the consistent ones. See sample QA example if you need too.
        '''
        #define some short cuts
        seqg, perg, choiceg = s.seqg, s.perg, s.choiceg
        s.use_latex = True
        # TODO
        #q_format1
        #q_format2
        #...
        # choices, try providing a few
        # these van include variations that are hard to encode with permg or variable substitution
        # example, NL variations or equaiton variations

        first_sentence = "Let f(x) = {}*x + {}*sin(x).".format(const1, const2)
        second_sentence = "Find the gradient of the normal to the curve of f at x={}.".format(value)
        question = seqg(first_sentence, second_sentence)

        q = choiceg(question)
        return q

    def A(s, value, const1,const2): #TODO change the signature of the function according to your answer
        '''
        Small answer description.

        Important Note: first variables are the not consistent variables followed
        by the consistent ones. See sample QA example if you need too.
        '''
        #define some short cuts
        seqg, perg, choiceg = s.seqg, s.perg, s.choiceg
        # TODO
        #ans_sympy
        #ans_numerical
        #ans_vnl_vsympy1
        #ans_vnl_vsympy2
        # choices, try providing a few
        # these can include variations that are hard to encode with permg or variable substitution
        # example, NL variations or equaiton variations
        x = Symbol('x')
        temp = diff(const1*x + const2*sin(x))
        normGradient = -1/temp
        ans_sympy = normGradient.subs(x, value)
        ans_numerical = ans_sympy.evalf(10)
        ans_vnl_vsympy1 = "The gradient of the normal to the curve is {}".format(ans_numerical)
        ans_vnl_vsympy2 = "The gradient of the normal to the curve is {}".format(ans_sympy)
        answer = choiceg(ans_sympy, ans_numerical, ans_vnl_vsympy1, ans_vnl_vsympy2)

        return answer

if __name__ == '__main__':
    qagenerator = QA_constraint()
    user_test.run_unit_test_for_user(QA_constraint)
    print(qagenerator.get_single_qa(None))

