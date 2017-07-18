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
        self.description = 'Consider a toroid with n square windings of side length 0.005 m. The radius of the toroid is 0.01 m, and the wrapped wire carries a current of 5 Å. Calculate the magnetic field at a distance d from the central axis of the toroid, considering points both inside of and outside of the coils.'

        # keywords about the question that could help to make this more searchable in the future
        self.keywords = ['physics', 'electricity and magnetism', 'magnetic field', 'toroid']
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
            n, d = symbols('n d')
        else:
            n, d = self.get_symbols(2)
        return n, d

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
            r, a, I = 0.01, 0.005, 5
        else:
            r = round(np.random.uniform(.0001,1), 4)
            a = round(np.random.uniform(.00005, r), 5)
            I = np.random.randint(1,1000)


        return r, a, I

    def Q(s,r, a, I, n, d):
        '''
        Important Note: first variables are the not consistent variables followed
        by the consistent ones. See sample QA example if you need too.
        '''
        #define some short cuts
        seqg, perg, choiceg = s.seqg, s.perg, s.choiceg

        pre1 = ('Consider a toroid with')
        pre2 = ('A toroid has')

        n1 = seqg(n,'square windings of side length', a,'m. The radius of the toroid is',r,'m, and the wrapped wire carries a current of',I,'Å.')
        n2 = seqg(n, 'square windings of side length', a,'m. The radius of the toroid is', r,'m, and the wire carries a current of', I, 'Å.')
        n3 = seqg(n, 'square windings of side length', a,'m, and a radius of', r,'m. The wrapped wire carries a current of', I, 'Å.')
        n4 = seqg(n, 'square windings of side length', a,'m. The radius of the toroid is', r,'m. The wrapped wire carries a current of', I, 'Å.')
        n5 = seqg(n, 'square windings of side length', a,'m. The radius of the toroid is', r,'m, and the wrapped wire carries a current of', I, 'Å.')
        n6 = seqg(n, 'square windings of side length', a,'m. The radius of the toroid is', r,'m, and the wrapped wire carries a current of', I, 'Å.')
        n7 = seqg(n, 'square windings of side length', a,'m. The wrapped wire carries a current of', I, 'Å. The radius of the toroid is', r,'m.')

        end1 = seqg('Calculate the magnetic field at a distance', d,'from the central axis of the toroid, considering points both inside of and outside of the coils.')
        end2 = seqg('Find the magnetic field at a distance', d,'from the central axis of the toroid, considering points both inside of and outside of the coils.')
        end3 = seqg('Compute the magnetic field at a distance', d,'from the central axis of the toroid, considering points both inside of and outside of the coils.')

        q1 = seqg(pre1, n1, end1)
        q2 = seqg(pre1, n2, end1)
        q3 = seqg(pre1, n3, end1)
        q4 = seqg(pre1, n4, end1)
        q5 = seqg(pre1, n5, end1)
        q6 = seqg(pre1, n6, end1)
        q7 = seqg(pre1, n7, end1)
        q8 = seqg(pre2, n1, end1)
        q9 = seqg(pre2, n2, end1)
        q10= seqg(pre2, n3, end1)
        q11= seqg(pre2, n4, end1)
        q12= seqg(pre2, n5, end1)
        q13= seqg(pre2, n6, end1)
        q14= seqg(pre2, n7, end1)

        q15 = seqg(pre1, n1, end2)
        q16 = seqg(pre1, n2, end2)
        q17 = seqg(pre1, n3, end2)
        q18= seqg(pre1, n4, end2)
        q19= seqg(pre1, n5, end2)
        q20= seqg(pre1, n6, end2)
        q21= seqg(pre1, n7, end2)
        q22= seqg(pre2, n1, end2)
        q23= seqg(pre2, n2, end2)
        q24 = seqg(pre2, n3, end2)
        q25 = seqg(pre2, n4, end2)
        q26 = seqg(pre2, n5, end2)
        q27 = seqg(pre2, n6, end2)
        q28 = seqg(pre2, n7, end2)

        q29 = seqg(pre1, n1, end3)
        q30 = seqg(pre1, n2, end3)
        q31 = seqg(pre1, n3, end3)
        q32 = seqg(pre1, n4, end3)
        q33 = seqg(pre1, n5, end3)
        q34 = seqg(pre1, n6, end3)
        q35 = seqg(pre1, n7, end3)
        q36 = seqg(pre2, n1, end3)
        q37 = seqg(pre2, n2, end3)
        q38 = seqg(pre2, n3, end3)
        q39 = seqg(pre2, n4, end3)
        q40 = seqg(pre2, n5, end3)
        q41 = seqg(pre2, n6, end3)
        q42 = seqg(pre2, n7, end3)

        q = choiceg(q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20, q21, q22, q23, q24, q25, q26, q27, q28, q29, q30, q31, q32, q33, q34, q35, q36, q37, q38, q39, q40, q41, q42)
        return q

    def A(s,r, a, I, n, d):
        '''
        Important Note: first variables are the not consistent variables followed
        by the consistent ones. See sample QA example if you need too.
        '''
        seqg, perg, choiceg = s.seqg, s.perg, s.choiceg
        B_dL = 'B*2*pi*' + str(d)
        I_inside = str(n) + str(I)
        B_in = '(µ_0*'+ str(n) + '*'+str(I) + ')/(2π*' +str(d) + ')'

        in1 = seqg('The magnetic field inside of the toroid is', str(B_in) +'.')
        in2 = seqg('The magnetic field inside the toroid is', str(B_in) +'.')
        in3 = seqg('Inside of the toroid the magnetic field is', str(B_in) + '.')
        in4 = seqg('Inside of the toroid the magnetic field equals', str(B_in) + '.')
        out1 = seqg('There is no magnetic field outside of the toroid.')
        out2 = seqg('Outside of the toroid there is no magnetic field.')
        out3 = seqg('Outside of the toroid the magnetic field is zero.')
        out4 = seqg('The magnetic field is zero outside of the toroid.')

        a1 = perg(in1, out1)
        a2 = perg(in1, out2)
        a3 = perg(in1, out3)
        a4 = perg(in1, out4)
        a5 = perg(in2, out1)
        a6 = perg(in2, out2)
        a7 = perg(in2, out3)
        a8 = perg(in2, out4)
        a9 = perg(in3, out1)
        a10 = perg(in3, out2)
        a11 = perg(in3, out3)
        a12 = perg(in3, out4)
        a13 = perg(in4, out1)
        a14 = perg(in4, out2)
        a15 = perg(in4, out3)
        a16 = perg(in4, out4)

        a = choiceg(a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16)
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