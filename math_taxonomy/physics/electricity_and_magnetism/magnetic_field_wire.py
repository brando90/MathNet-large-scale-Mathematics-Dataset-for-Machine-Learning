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
        self.description = 'A straight wire of radius 0.01 m and infinite length is carrying a uniformly distributed current of magnitude 10 Å that is flowing in the +k direction. Find the magnitude of the magnetic field at a distance d > 0.01 m and a distance d < 0.01 m from the axis of the wire.'

        # keywords about the question that could help to make this more searchable in the future
        self.keywords = ['physics', 'electricity and magnetism', 'magnetic field']
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
            d, x = symbols('d x')
        else:
            d, x = self.get_symbols(2)
        return d, x

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
            r, I, dir_val = .01, 10, 2
        else:
            r = round(np.random.uniform(.0001,1), 4)
            I = np.random.randint(1,1000)
            dir_val = np.random.randint(0,5)


        return r, I, dir_val

    def Q(s,r, I, dir_val, d, x):
        '''
        Important Note: first variables are the not consistent variables followed
        by the consistent ones. See sample QA example if you need too.
        '''
        #define some short cuts
        seqg, perg, choiceg = s.seqg, s.perg, s.choiceg
        direction = ['+i', '+j', '+k', '-i', '-j', '-k']
        given = seqg('A straight wire of radius', r, 'm and infinite length is carrying a uniformly distributed current of magnitude', I, 'Å that is flowing in the',direction[dir_val],'direction.')
        form1 = seqg('Find the magnitude of the magnetic field at a distance',d,'>',r, 'm and a distance', d, '<',r,'m from the axis of the wire.')
        form2 = seqg('Find the magnitude of the magnetic field at a distance',d,'<',r,'m and a distance',d,'>',r,'m from the axis of the wire.')
        form3 = seqg('Calculate the magnetic field at a distance',d,'>', r, 'm and a distance',d,'<', r,'m from the axis of the wire.')
        form4 = seqg('Calculate the magnetic field at a distance',d,'<', r, 'm and a distance',d,'>', r,'m from the axis of the wire.')
        question1 = seqg(given, form1)
        question2 = seqg(given, form2)
        question3 = seqg(given, form3)
        question4 = seqg(given, form4)

        q = choiceg(question1, question2, question3, question4)
        return q

    def A(s,r, I, dir_val, d, x):
        '''
        Important Note: first variables are the not consistent variables followed
        by the consistent ones. See sample QA example if you need too.
        '''
        seqg, perg, choiceg = s.seqg, s.perg, s.choiceg
        B_out = '(µ_0*'+ str(I)+')/(2*π*'+ str(d) + ')'
        B_in = '(µ_0*' + str(I)+'*' + str(d) + ')/(2*π*' + str(r**2) + ')'

        answer1 = seqg('The magnetic field at a distance', d,'>',r,'m from the axis of the wire is', B_out + '.')
        answer2 = seqg('The magnetic field at a distance', d,'<',r,'m from the axis of the wire is', B_in + '.')

        answer = perg(answer1, answer2)
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
    #user_test.run_unit_test_for_user(QA_constraint)