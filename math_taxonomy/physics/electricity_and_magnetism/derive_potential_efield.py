from sympy import *
import random
import numpy as np

from qagen.qagen import *
from qagen import utils
from qagen import unit_test_for_user as user_test

class QA_constraint(QAGen):

    def __init__(self):
        '''
        Initializer for your QA question.
        '''
        super().__init__()
        self.author = 'Max Augustine'
        self.description = 'In a certain region of space, the electric potential is V(x,y,z) = axy + bx^5 + cz, where a = 2 b = 3 c = 4 . Calculate the x-, y-, and z-components of the electric field.'

        # keywords about the question that could help to make this more searchable in the future
        self.keywords = ['physics', 'electricity and magnetism', 'electric field', 'potential']
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
            x, y, z, a, b, c = symbols('x y z a b c')
        else:
            x, y, z, a, b, c = self.get_symbols(6)
        return  x, y, z, a, b, c

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
            a_val, b_val, c_val, exp, order_val = 2, 3, 4, 5, 0
        else:
            a_val = np.random.randint(1,100)
            b_val = np.random.randint(1,100)
            c_val = np.random.randint(1,100)
            exp = np.random.randint(1,10)
            order_val = np.random.randint(1,6)

        return a_val,b_val, c_val, exp, order_val

    def Q(s,a_val,b_val, c_val, exp, order_val, x, y, z, a, b, c):
        '''
        Important Note: first variables are the not consistent variables followed
        by the consistent ones. See sample QA example if you need too.
        '''
        #define some short cuts
        seqg, perg, choiceg = s.seqg, s.perg, s.choiceg
        order = [str(a)+str(x)+str(y)+' + ' + str(b)+str(x) + '^' + str(exp) + ' + ' + str(c) + str(z), str(a)+str(x)+str(y)+' + ' + str(c) + str(z)+ ' + '+ str(b)+str(x) + '^' + str(exp), str(c) + str(z)+ ' + '+ str(b)+str(x) + '^' + str(exp)+ ' + ' + str(a)+str(x)+str(y), str(c) + str(z)+ ' + '+ str(a)+str(x)+str(y)+ ' + '+ str(b)+str(x) + '^' + str(exp), str(b)+str(x) + '^' + str(exp) + ' + ' + str(a)+str(x)+str(y)+' + ' + str(c) + str(z), str(b)+str(x) + '^' + str(exp) + ' + ' + str(c) + str(z)+ ' + '+str(a)+str(x)+str(y)]

        question = seqg('In a certain region of space, the electric potential is', 'V(' + str(x) + ',' + str(y) + ',' + str(z) + ')', '=', str(order[order_val]) + ',', 'where', perg(Eq(a, a_val), Eq(b, b_val), Eq(c, c_val)), '. Calculate the', str(x) + '-, ' + str(y)+ '-, and ' + str(z) + '-components', 'of the electric field.')

        q = choiceg(question)
        return q

    def A(s,a_val,b_val, c_val, exp, order_val, x, y, z, a, b, c):
        '''
        Important Note: first variables are the not consistent variables followed
        by the consistent ones. See sample QA example if you need too.
        '''
        seqg, perg, choiceg = s.seqg, s.perg, s.choiceg
        expression = a_val*x*y + b_val*(x**exp) + c_val*z
        e_x = str(-expression.diff(x)).replace('**', '^')
        e_y = -expression.diff(y)
        e_z = -expression.diff(z)

        answer1 = seqg('The', str(x)+'-component', 'of the electric field is', str(e_x)+'.')
        answer2 = seqg('The', str(y)+'-component', 'of the electric field is', str(e_y)+'.')
        answer3 = seqg('The', str(z)+'-component', 'of the electric field is', str(e_z)+'.')
        answer = perg(answer1, answer2, answer3)
        a = choiceg(answer)
        return a

    ##

    def get_qa(self,seed):
        '''
        Example of how Q,A are formed in general.
        '''
        # set seed
        self.seed_all(seed)
        # get variables for qa and register them for the current q,a
        variables, variables_consistent = self._create_all_variables()
        # get concrete qa strings
        q_str = self.Q(*variables,*variables_consistent)
        a_str = self.A(*variables,*variables_consistent)
        return q_str, a_str

## Some helper functions to check the formats are coming out correctly

##

def check_single_question_debug(qagenerator):
    '''
    Checks by printing a single quesiton on debug mode
    '''
    qagenerator.debug = True
    q,a = qagenerator.get_qa(seed=1)
    print('qagenerator.debug = ', qagenerator.debug)
    print('q: ', q)
    print('a: ', a)

def check_single_question(qagenerator):
    '''
    Checks by printing a single quesiton on debug mode
    '''
    q,a = qagenerator.get_qa(seed=random.randint(0,1000))
    print('qagenerator.debug = ', qagenerator.debug)
    print('q: ', q)
    print('a: ', a)

def check_mc(qagenerator):
    '''
    Checks by printing the MC(Multiple Choice) option
    '''
    nb_answers_choices = 10
    for seed in range(3):
        #seed = random.randint(0,100)
        q_str, ans_list = qagenerator.generate_single_qa_MC(nb_answers_choices=nb_answers_choices,seed=seed)
        print('\n-------seed-------: ',seed)
        print('q_str:\n',q_str)
        print('-answers:')
        print("\n".join(ans_list))

def check_many_to_many(qagenerator):
    for seed in range(3):
        q,a = qagenerator.generate_many_to_many(nb_questions=4,nb_answers=3,seed=seed)
        print('-questions:')
        print("\n".join(q))
        print('-answers:')
        print("\n".join(a))

def check_many_to_one_consis(qagenerator):
    for seed in range(3):
        print()
        q,a = qagenerator.generate_many_to_one(nb_questions=5,seed=seed)
        print("\n".join(q))
        print('a: ', a)
        #print("\n".join(a))

def check_many_to_one_consistent_format(qagenerator):
    nb_qa_pairs,nb_questions = 10,3
    qa_pair_list = qagenerator.generate_many_to_one_consistent_format(nb_qa_pairs,nb_questions)
    for q_list,a_consistent_format in qa_pair_list:
        print()
        print("\n".join(q_list))
        print('a: ', a_consistent_format)

if __name__ == '__main__':
    qagenerator = QA_constraint()
    check_single_question(qagenerator)
    user_test.run_unit_test_for_user(QA_constraint)