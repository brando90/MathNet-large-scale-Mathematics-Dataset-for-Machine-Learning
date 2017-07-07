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
        self.description = 'A pair of concentric spheres consists of a solid sphere and a spherical shell. The solid '
        self.description += 'sphere has a radius r_1 = a and carries a charge density ρ(r)= b(1−(r/a)). b is a '
        self.description += 'positive constant. r is the radial distance from the center of the sphere. The spherical '
        self.description += 'shell has a radius r_2 = 2a and carries a uniform area charge density σ such that the electric '
        self.description += 'field is zero for r > r_2. Find the magnitudes of the electric fields in the regions where r < r_1 '
        self.description += 'and where r_1 < r < r_2. Use values of a = 1 and b = 2.'


        # keywords about the question that could help to make this more searchable in the future
        self.keywords = ['physics', 'electricity and magnetism', 'electric field', "gauss's law"]
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
            r_1, r_2, r = symbols('r_1 r_2 r')
            a, b, c = symbols('a b c')
        else:
            r_1, r_2, r = symbols('r_1 r_2 r')
            a, b, c = self.get_symbols(3)
        return  r_1, r_2, r, a, b, c

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
            a_val, b_val, c_val = 1, 2, 2
        else:
            a_val = np.random.uniform(.1, 10)
            b_val = np.random.uniform(1,50)
            c_val = np.random.randint(2, 10)

        return a_val, b_val, c_val

    def Q(s, a_val, b_val, c_val, r_1, r_2, r, a, b, c):
        '''
        Find the electric field in different regions of two concentric spheres of non-uniform charge density.
        Important Note: first variables are the not consistent variables followed
        by the consistent ones. See sample QA example if you need too.
        '''
        #define some short cuts
        seqg, perg, choiceg = s.seqg, s.perg, s.choiceg

        part1 = seqg('A pair of concentric spheres consists of a solid sphere and a spherical shell.')
        part2 = seqg('The solid sphere has a radius r_1 =', a,'and carries a charge density ρ(r)=' , str(b) +'(1−(r/' + str(a) +')).')
        part3 = seqg(b, 'is a positive constant.')
        part4 = seqg('r is the radial distance from the center of the sphere.')
        part5 = seqg('The spherical shell has a radius r_2 =', str(c_val) + str(a), 'and carries a uniform area charge density σ such that the electric field is zero for r > r_2.')
        part6 = seqg('Find the magnitudes of the electric fields in the regions where r < r_1 and where r_1 < r < r_2.')
        part7 = seqg('Use values of', a,'=',a_val, 'and', b, '=', str(b_val) + '.')

        question1 = seqg(part1, part2, perg(part3, part4), part5, part6, part7)
        question2 = seqg(part1, part2, perg(part3, part4), part7, part5, part6)

        q = choiceg(question1, question2)
        return q

    def A(s, a_val, b_val, c_val, r_1, r_2, r, a, b, c):
        '''
        Find the electric field in different regions of two concentric spheres of non-uniform charge density.
        Important Note: first variables are the not consistent variables followed
        by the consistent ones. See sample QA example if you need too.
        '''
        seqg, perg, choiceg = s.seqg, s.perg, s.choiceg

        q_enc = integrate(r**2 - r**3, r)
        efield_1 = b_val/a_val * q_enc/(r**2)
        efield_2 = b_val * (a_val**3)/12/r**2

        answer1 = seqg('The electric field for r < r_1 is', str(efield_1)+ '/ϵ_0', 'and the electric field for r_1 < r < r_2 is', str(efield_2) + '/ϵ_0.')
        a = choiceg(answer1)
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