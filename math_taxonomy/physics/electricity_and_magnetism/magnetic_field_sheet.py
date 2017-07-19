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
        self.description = 'Consider a sheet of infinite area carrying a total current of 10 Å in the +i direction. The current is distributed uniformly across the very large width w of the sheet. Calculate the magnetic field at a distance d both above and below the sheet.'

        # keywords about the question that could help to make this more searchable in the future
        self.keywords = ['physics', 'electricity and magnetism', 'magnetic field', 'infinite sheet']
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
            w, d = symbols('w d')
        else:
            w, d = self.get_symbols(2)
        return w, d

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
            I, dir_val = 10, 0
        else:
            I = round(np.random.uniform(.01,1000), 4)
            dir_val = np.random.randint(0,5)


        return I, dir_val

    def Q(s, I, dir_val, w, d):
        '''
        Important Note: first variables are the not consistent variables followed
        by the consistent ones. See sample QA example if you need too.
        '''
        #define some short cuts
        seqg, perg, choiceg = s.seqg, s.perg, s.choiceg

        direction = ['+i', '+j', '+k', '-i', '-j', '-k']

        pre1 = ('Consider a sheet of infinite area carrying')
        pre2 = ('An infinite sheet carries')
        pre3 = ('Consider an infinite sheet carrying')
        pre4 = ('Consider an infinite sheet that carries')
        pre5 = ('A sheet of infinite area carries')

        a1 = seqg('a total current of',I,'Å in the',direction[dir_val],'direction.')
        a2 = seqg('a total current of magnitude', I, 'Å in the', direction[dir_val], 'direction.')


        b1 = seqg('The current is', perg('distributed', 'uniformly'), 'across the very large width',w,'of the sheet.')

        c1 = seqg('Calculate the magnetic field at a distance',d,'both above and below the sheet.')
        c2 = seqg('Find the magnetic field at a distance', d, 'both above and below the sheet.')
        c3 = seqg('Compute the magnetic field at a distance', d, 'both above and below the sheet.')
        c4 = seqg('Calculate the magnetic field at a distance', d, 'both below and above the sheet.')
        c5 = seqg('Find the magnetic field at a distance', d, 'both below and above the sheet.')
        c6 = seqg('Compute the magnetic field at a distance', d, 'both below and above the sheet.')



        q1 = seqg(pre1, a1, b1, c1)
        q2 = seqg(pre1, a1, b1, c2)
        q3 = seqg(pre1, a1, b1, c3)
        q4 = seqg(pre1, a1, b1, c4)
        q5 = seqg(pre1, a1, b1, c5)
        q6 = seqg(pre1, a1, b1, c6)
        q7 = seqg(pre2, a1, b1, c1)
        q8 = seqg(pre2, a1, b1, c2)
        q9 = seqg(pre2, a1, b1, c3)
        q10 = seqg(pre2, a1, b1, c4)
        q11 = seqg(pre2, a1, b1, c5)
        q12 = seqg(pre2, a1, b1, c6)
        q13= seqg(pre3, a1, b1, c1)
        q14= seqg(pre3, a1, b1, c2)
        q15= seqg(pre3, a1, b1, c3)
        q16= seqg(pre3, a1, b1, c4)
        q17= seqg(pre3, a1, b1, c5)
        q18= seqg(pre3, a1, b1, c6)
        q19= seqg(pre4, a1, b1, c1)
        q20= seqg(pre4, a1, b1, c2)
        q21= seqg(pre4, a1, b1, c3)
        q22= seqg(pre4, a1, b1, c4)
        q23= seqg(pre4, a1, b1, c5)
        q24= seqg(pre4, a1, b1, c6)
        q25= seqg(pre5, a1, b1, c1)
        q26= seqg(pre5, a1, b1, c2)
        q27= seqg(pre5, a1, b1, c3)
        q28= seqg(pre5, a1, b1, c4)
        q29= seqg(pre5, a1, b1, c5)
        q30= seqg(pre5, a1, b1, c6)
        q31= seqg(pre1, a2, b1, c1)
        q32= seqg(pre1, a2, b1, c2)
        q33= seqg(pre1, a2, b1, c3)
        q34= seqg(pre1, a2, b1, c4)
        q35= seqg(pre1, a2, b1, c5)
        q36= seqg(pre1, a2, b1, c6)
        q37= seqg(pre2, a2, b1, c1)
        q38= seqg(pre2, a2, b1, c2)
        q39= seqg(pre2, a2, b1, c3)
        q40= seqg(pre2, a2, b1, c4)
        q41= seqg(pre2, a2, b1, c5)
        q42= seqg(pre2, a2, b1, c6)
        q43= seqg(pre3, a2, b1, c1)
        q44= seqg(pre3, a2, b1, c2)
        q45= seqg(pre3, a2, b1, c3)
        q46= seqg(pre3, a2, b1, c4)
        q47= seqg(pre3, a2, b1, c5)
        q48= seqg(pre3, a2, b1, c6)
        q49= seqg(pre4, a2, b1, c1)
        q50= seqg(pre4, a2, b1, c2)
        q51= seqg(pre4, a2, b1, c3)
        q52= seqg(pre4, a2, b1, c4)
        q53= seqg(pre4, a2, b1, c5)
        q54= seqg(pre4, a2, b1, c6)
        q55= seqg(pre5, a2, b1, c1)
        q56= seqg(pre5, a2, b1, c2)
        q57= seqg(pre5, a2, b1, c3)
        q58= seqg(pre5, a2, b1, c4)
        q59= seqg(pre5, a2, b1, c5)
        q60= seqg(pre5, a2, b1, c6)

        q = choiceg(q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20, q21, q22, q23, q24, q25, q26, q27, q28, q29, q30, q31, q32, q33, q34, q35, q36, q37, q38, q39, q40, q41, q42, q43, q44, q45, q46, q47, q48, q49, q50, q51, q52, q53, q54, q55, q56, q57, q58, q59, q60)
        return q

    def A(s,I, dir_val, w, d):
        '''
        Important Note: first variables are the not consistent variables followed
        by the consistent ones. See sample QA example if you need too.
        '''
        seqg, perg, choiceg = s.seqg, s.perg, s.choiceg
        B_2L = 'µ_0*I_inside'
        I_inside = 'I*L/w'
        B_in = '(µ_0*'+ str(I) + ')/(2*' +str(w) + ')'

        dir_above = ['+k', '+k', '-i', '-k', '-k', '+i' ]
        dir_below = ['-k', '-k', '+i', '+k', '+k', '-i' ]

        in1 = seqg('The magnetic field above the sheet is', B_in,'and acts in the', dir_above[dir_val],'direction.')
        in2 = seqg('The magnetic field above the sheet is equal to', B_in, 'and acts in the', dir_above[dir_val],'direction.')
        in3 = seqg('The magnitude of the magnetic field above the sheet is', B_in, 'and acts in the', dir_above[dir_val],'direction.')
        in4 = seqg('The magnetic field above the sheet acts in the', dir_above[dir_val],'direction and is equal to', str(B_in) + '.')

        out1 = seqg('The magnetic field below the sheet is', B_in, 'and acts in the', dir_below[dir_val], 'direction.')
        out2 = seqg('The magnetic field below the sheet is equal to', B_in, 'and acts in the', dir_below[dir_val], 'direction.')
        out3 = seqg('The magnitude of the magnetic field below the sheet is', B_in, 'and acts in the', dir_below[dir_val],'direction.')
        out4 = seqg('The magnetic field below the sheet acts in the',dir_below[dir_val],'direction and is equal to', str(B_in) + '.')


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