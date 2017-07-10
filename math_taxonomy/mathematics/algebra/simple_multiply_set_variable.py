from sympy import *
import random
import numpy as np
import pdb

from qagen.qagen import *
from qagen import utils
from qagen import unit_test_for_user as user_test

# Mary had x=10 lambs, y=9 goats, z=8 dogs and each was decreased by d=2 units
# by the wolf named Gary. How many of each are there left?

class QA_constraint(QAGen):

    def __init__(self):
        '''
        Initializer for your QA question.
        '''
        super().__init__()
        self.author = 'Brando Miranda'
        self.description = '''What's x if x = cb, b = a and a = 3, c = 2?'''
        # keywords about the question that could help to make this more searchable in the future
        self.keywords = ['basic algebra']
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
            x,a,b,c = symbols('x a b c')
        else:
            x,a,b,c = self.get_symbols(4)
        return x,a,b,c

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
            a_val,c_val = 3,2
        else:
            a_val,c_val = np.random.randint(-1000,1000,[2])
        return a_val,c_val

    def Q(s, a_val,c_val, x,a,b,c):
        '''
        Small question description.

        Important Note: first variables are the not consistent variables followed
        by the consistent ones. See sample QA example if you need too.
        '''
        #define some short cuts
        seqg, perg, choiceg = s.seqg, s.perg, s.choiceg
        #
        perm1 = perg(Eq(x,c*b), Eq(b,a) )
        perm2 = perg(Eq(a,3), Eq(c,2) )
        q1 = seqg('What\'s',x,'if ',perm1,' when ',perm2,'?')
        q2 = seqg('Find the value of',x,'if ',perm1,'when the variables are',perm2,'?')
        q = choiceg(q1,q2)
        return q

    def A(s, a_val,c_val, x,a,b,c):
        '''
        Small answer description.

        Important Note: first variables are the not consistent variables followed
        by the consistent ones. See sample QA example if you need too.
        '''
        #define some short cuts
        seqg, perg, choiceg = s.seqg, s.perg, s.choiceg
        #
        a1 = seqg( Eq(x,a_val*c_val) )
        a2 = seqg('The value of ',x,' has been computed to be: ',choiceg(Eq(x,a_val*c_val),a_val*c_val) )
        a3 = seqg( Eq( Eq(x,b*c),a_val*c_val) )
        a = choiceg(a1,a2,a3)
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

def check_get_symbol(qagenerator):
    seed = 1
    seed = 2
    qagenerator.seed_all(1)
    symbol1 = qagenerator.get_symbol()
    qagenerator.seed_all(1)
    symbol2 = qagenerator.get_symbol()
    print(symbol1)
    print(symbol2)

#should check if same DE object if seed is same

#TODO: tests that check all nonimplemented in QA that user must implement.

if __name__ == '__main__':
    qagenerator = QA_constraint()
    # uncomment the following to check formats:
    #check_mc(qagenerator)
    #check_many_to_many(qagenerator)
    #check_many_to_one_consistent_format(qagenerator)
    ## run unit test given by framework
    user_test.run_unit_test_for_user(QA_constraint)
    # check_get_symbol(qagenerator)
