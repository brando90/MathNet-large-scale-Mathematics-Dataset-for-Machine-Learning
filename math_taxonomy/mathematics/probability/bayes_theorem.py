from sympy import *
import random
import numpy as np
import pdb

from qagen.qagen import *
from qagen import *
from qagen import utils
from qagen import unit_test_for_user as user_test

class QA_constraint(QAGen):

    def __init__(self):
        '''
        Initializer for your QA question.
        '''
        super().__init__()
        self.author = 'Erick Rodriguez'
        self.description = 'A patient takes a test to see if they have Cancer .'
        self.description+= 'A person has Cancer with probability p = 0.05 , and does not have Cancer with probability n = 0.95 .'
        self.description+= 'The test reads a true positive with probability t = 0.85 .'
        self.description+= 'The test incorrectly reads positive with probability f = 0.15 .'
        self.description+= 'What is the probability of the patient having Cancer if the test reads positive?'
        self.keywords = ['Bayes Theorem', 'probability', 'mathematics', 'Bayes Rule']
        self.use_latex = True
        self.debug = False

    def seed_all(self,seed):
        '''
        Write the seeding functions of the libraries that you are using.
        Its important tdo seed all the libraries you are using because the
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
            Cancer = 'Cancer'
            t,f,p,n = symbols('t f p n')
        else:
            t,f,p,n = self.get_symbols(4)
            diseases = utils.get_diseases()
            Cancer = self.get_names(1, names_list=diseases)[0]
        return t,f,p,n,Cancer

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
            t_value = 0.85
            f_value = 0.15
            p_value = 0.05
            n_value = 1-p_value
        else:
            t_value = np.random.randint(60,95)*0.01
            f_value = np.random.randint(1,20)*0.01
            p_value = np.random.randint(1,20)*0.01
            n_value = 1-p_value
        return t_value,f_value,p_value,n_value

    def Q(s,t_value,f_value,p_value,n_value,t,f,p,n,Cancer):
        '''
        Small question description.
        Important Note: first variables are the not consistent variables followed
        by the consistent ones. See sample QA example if you need too.
        '''
        #define some short cuts
        seqg, perg, choiceg = s.seqg, s.perg, s.choiceg
        # TODO
        q_start = seqg('A patient takes a test to see if they have',Cancer,'. ')
        perm1 = seqg('A person has',Cancer,'with probability', Eq(p,p_value), ', and does not have',Cancer,'with probability',Eq(n,n_value), '. ')
        perm2 = seqg('The test reads a true positive with probability', seqg(Eq(t,t_value), '. '))
        perm3 = seqg('The test incorrectly reads positive with probability', seqg(Eq(f,f_value), '. '))
        perm4 = seqg('The test reads a false positive with probabiliy', seqg(Eq(f,f_value), '. '))
        q_end = seqg('What is the probability of the patient having',Cancer,'if the test reads positive?')
        q_end2 = seqg(' If the test comes back positive, What is the likelihood the patient actually has',Cancer,'? ')
        false_pos_perm = choiceg(perm3,perm4)
        end_perm = choiceg(q_end,q_end2)
        permutable_part = perg(perm1,perm2,false_pos_perm)
        q_format1 = seqg(q_start,permutable_part,end_perm)
        #q_format2
        #...
        # choices, try providing a few
        # these van include variations that are hard to encode with permg or variable substitution
        # example, NL variations or equaiton variations
        q = choiceg(q_format1)
        return q

    def A(s,t_value,f_value,p_value,n_value,t,f,p,n,Cancer):
        '''
        Small answer description.
        Important Note: first variables are the not consistent variables followed
        by the consistent ones. See sample QA example if you need too.
        '''
        #define some short cuts
        seqg, perg, choiceg = s.seqg, s.perg, s.choiceg
        # TODO
        #ans_sympy
        ans_numerical = (t_value*p_value)/(t_value*p_value+f_value*n_value)
        ans_vnl_vsympy1 = seqg("If the test reads positive, the probability of the patient having",Cancer,"is {0}.".format(str(ans_numerical)))
        ans_vnl_vsympy2 = seqg("The probability of",Cancer,"is {0}.".format(str(ans_numerical)))
        # choices, try providing a few
        # these van include variations that are hard to encode with permg or variable substitution
        # example, NL variations or equaiton variations
        a = choiceg(ans_vnl_vsympy1,ans_vnl_vsympy2)
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
    Checks by printing a single question on debug mode
    '''
    qagenerator.debug = True
    q,a = qagenerator.get_qa(seed=1)
    print('qagenerator.debug = ', qagenerator.debug)
    print('q: ', q)
    print('a: ', a)

def check_single_question(qagenerator):
    '''
    Checks by printing a single question on debug mode
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

if __name__ == '__main__':
    qagenerator = QA_constraint()
    # uncomment the following to check formats:
    #check_mc(qagenerator)
    check_many_to_many(qagenerator)
    #check_many_to_one_consistent_format(qagenerator)
    #check_get_symbol(qagenerator)
    # Latex diplay
    #q,a = qagenerator.get_single_qa(seed=0)
    #utils.display_latex(q,a)
    ## run unit test given by framework
    user_test.run_unit_test_for_user(QA_constraint)
