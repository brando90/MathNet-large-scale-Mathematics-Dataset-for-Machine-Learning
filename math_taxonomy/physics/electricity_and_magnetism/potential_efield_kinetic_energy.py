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
        self.description = '''A particle with a charge of 2 nC is in a uniform electric field directed to the left. It is released from rest and moves to the left. After it has moved 5 cm, its kinetic energy is found to be 4*10^-6 J. What is the magnitude and direction of the electric field?'''

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
        q, k, d = symbols('q k d') # charge, distance
        return  q, k, d

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
            q_val, k_val, d_val = 2, 4, 5
            direction = 'to the left'
        else:
            q_val = np.random.randint(1,1000)
            k_val = np.random.randint(1,9999)
            d_val = np.random.randint(1,1000)

            dir_val = np.random.uniform(1, 100)
            if dir_val > 25 and dir_val < 51:
                direction = 'right'
            elif dir_val <= 25:
                direction = 'left'
            elif dir_val >= 51 and dir_val <= 75:
                direction = 'up'
            else:
                direction = 'down'

        return q_val,k_val, d_val, direction

    def Q(s,q_val,k_val, d_val, direction, q,k, d):
        '''
        Important Note: first variables are the not consistent variables followed
        by the consistent ones. See sample QA example if you need too.
        '''
        #define some short cuts
        seqg, perg, choiceg = s.seqg, s.perg, s.choiceg

        if direction == 'left' or direction == 'right':
            phrase = 'to the '
        else:
            phrase = ''

        k_sort = k_val
        if k_sort < 10:
            power = '6'
        elif k_sort >= 10 and k_val < 100:
            power = '5'
            k_val = k_sort/10.0
        elif k_sort >= 100 and k_sort < 1000:
            power = '4'
            k_val = k_sort/100.00
        else:
            power = '3'
            k_val = k_sort/1000.000
        given = seqg('A particle with a charge of', q_val,'nC is in a uniform electric field directed', phrase + direction + '.', 'It is released from rest and moves', phrase + direction + '.', 'After it has moved',d_val, 'cm, its kinetic energy is found to be', str(k_val) + '*10^-' + power,'J.')
        form1 = seqg('''What is the magnitude and direction of the electric field?''')
        form2 = seqg('''What is the magnitude of the electric field equal to? In what direction is it directed?''')
        form3 = seqg('What is the direction and magnitude of the electric field?')
        question1 = seqg(given, form1)
        question2 = seqg(given, form2)
        question3 = seqg(given, form3)
        q = choiceg(question1, question2, question3)
        return q

    def A(s,q_val,k_val, d_val, direction, q,k, d):
        '''
        Important Note: first variables are the not consistent variables followed
        by the consistent ones. See sample QA example if you need too.
        '''
        if direction == 'left' or direction == 'right':
            phrase = 'to the '
        else:
            phrase = ''
        seqg, perg, choiceg = s.seqg, s.perg, s.choiceg
        potential = (k_val * 10**-6)/(q_val* 10**-9)
        efield = potential/(d_val/100)
        answer1 = seqg('The electric field is equal to', efield, 'N/C.')
        answer2 = seqg('The electric field has a magnitude of', efield, 'N/C and is directed', phrase + direction + '.')
        answer3 = seqg('''The electric field is directed''', phrase + direction, 'and has a magnitude of', str(efield) + '.')
        a = choiceg(answer1, answer2, answer3)
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

    #user_test.run_unit_test_for_user(QA_constraint)