# Completed
# Debugg status: only works in 1 dim gets sympy.core.sympify.SympifyError: SympifyError in multi dim

from sympy import *
import random
import numpy as np

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
        self.author = 'Elaheh Ahmadi' #TODO your full name
        self.description = 'Find acceleration of an object that moves in dim = one dimensional world given that we know its velocity changes from  v0 = 0 (m/s) to v1 = 1(m/s) in time frame of t0 = 2 (s) to t1 = 3 (s).'

        # keywords about the question that could help to make this more searchable in the future
        self.keywords = ['Physics', 'Finding Acceleration'] #TODO keywords to search type of question
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
             v0, v1, t0, t1, dim = symbols('v0 v1 t0 t1 dim')
        else:
             v0, v1, t0, t1, dim = self.get_symbols(5)
        return  v0, v1, t0, t1, dim

    def _to_hashable_(self, variables):
        v0, v1, t0, t1, dim = variables
        flattener = lambda x: x if isinstance(x, Symbol) else tuple(x);
        return list(map(flattener, (v0,v1))) + [t0, t1, dim]

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
            v0_val, v1_val, t0_val, t1_val, dim_val = 1, 2, 3, 4, 1
        else:
            dim_val = np.random.randint(1,100)
            v0_val = np.random.randint(-1000,1000,dim_val)
            v1_val = np.random.randint(-1000, 1000, dim_val)
            t0_val = np.random.randint(0, 1000)
            t1_val = np.random.randint(1000, 2000)

        return v0_val, v1_val, t0_val, t1_val, dim_val

    def Q(s,v0, v1, t0, t1, dim, v0_val, v1_val, t0_val, t1_val, dim_val):
        '''
        Finding the acceleration of an object bassed on having its velocity at two different times

        Important Note: first variables are the not consistent variables followed
        by the consistent ones. See sample QA example if you need too.
        '''
        #define some short cuts
        seqg, perg, choiceg = s.seqg, s.perg, s.choiceg
        question1 = seqg('Find acceleration of an object that moves in', Eq(dim, dim_val),
                         ' dimensional world given that we know its velocity changes from '
                         , Eq(v0, v0_val), '(m/s) to ', Eq(v1, v1_val), '(m/s) in time frame of ',
                         Eq(t0, t0_val), '(s) to ', Eq(t1, t1_val), '(s).')
        q = choiceg(question1)
        return q

    def A(s,v0_val, v1_val, t0_val, t1_val, dim_val, v0, v1, t0, t1, dim):  
        '''
        We use this equationto find the acceleration a = (v1_val - v0_val)/(t1_val - t0_val).

        Important Note: first variables are the not consistent variables followed
        by the consistent ones. See sample QA example if you need too.
        '''
        #define some short cuts
        seqg, perg, choiceg = s.seqg, s.perg, s.choiceg
        acceleration = (v1_val - v0_val)/(t1_val - t0_val)
        answer = seqg('The acceleration in ', Eq(dim, dim_val), 'dimension is equal to ', acceleration, '(m/s^2).')
        # choices, try providing a few
        # these van include variations that are hard to encode with permg or variable substitution
        # example, NL variations or equaiton variations
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
    ## uncomment the following to check formats:
    #check_mc(qagenerator)
    #check_many_to_one(qagenerator)
    #check_one_to_many(qagenerator)
    #check_many_to_one_consistent_format(qagenerator)
    ## run unit test given by framework
    user_test.run_unit_test_for_user(QA_constraint)