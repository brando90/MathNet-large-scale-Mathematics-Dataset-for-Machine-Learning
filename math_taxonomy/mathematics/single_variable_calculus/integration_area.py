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
        self.description = '''A point P(x,x**2) lies on the curve y=x**2. Calculate the minimum distance from the point A(2,-0.5) to the point P.'''
        # keywords about the question that could help to make this more searchable in the future
        self.keywords = ['area of integration', 'area','integration']
        self.use_latex = True

    def seed_all(self,seed):
        '''
        Write the seeding functions of the libraries that you are using.
        Its important to seed all the libraries you are using because the
        framework will assume it can seed stuff for you. It needs this for
        the library to work.
        '''
        random.seed(seed)
        np.random.seed(seed)
        self.fake.random.seed(seed)

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
        if self.debug:
            A = "A"
            P = "P"
        else:
            letters = utils.get_capital_letters()
            A, P = self.get_names(2, names_list=letters)

        return A,P

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
            x_coord = 2
       
        else:
            x_coord = random.randint(-1000,1000)

        return (x_coord,)

    def Q(s, x_coord, A, P): #TODO change the signature of the function according to your question
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
        first_sentence = "A point {}(x,x**2) lies on the curve y=x**2.".format(P)
        second_sentence = "Calculate the minimum distance from the point {}({},-0.5) to the point {}.".format(A, x_coord, P)
        question = seqg(first_sentence, second_sentence)
        q = choiceg(question)
        return q

    def A(s, x_coord, A, P): #TODO change the signature of the function according to your answer
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
        distEq = sqrt(((x+x_coord)**2) + ((x**2+0.5)**2))
        toSolve = diff(distEq**2)
        c = solve(toSolve)
        numerical_ans = distEq.subs(x,c[0])
        ans_vnl_vsympy1 = "The minimum distance is {}".format(numerical_ans)
        ans_vnl_vsympy2 = "The minimum distance from point {} to point {} is {}".format(A, P, numerical_ans)
        answer = choiceg(str(numerical_ans), ans_vnl_vsympy1, ans_vnl_vsympy2)
        return answer

if __name__ == '__main__':
    qagenerator = QA_constraint()
    user_test.run_unit_test_for_user(QA_constraint)
    print(qagenerator.get_single_qa(None))

