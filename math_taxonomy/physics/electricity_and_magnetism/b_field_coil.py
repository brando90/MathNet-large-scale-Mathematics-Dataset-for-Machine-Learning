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
        self.description = 'Consider a coil that is created by winding 4000 turns of wire around a cylindrical wooden object that is 1 m long. A resistor is added to bring the resistance of the circuit to 1000 Ω. A battery of 12 V is connected to the coil. What is the strength of the magnetic field inside of the coil?'

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
            t, m, r, v = 4000, 1, 1000, 12
        else:
            t = np.random.uniform(100, 100000000)
            m = round(np.random.uniform(.01,1000), 4)
            r = np.random.randint(1, 100000)
            v = np.random.randint(1, 100)


        return t, m, r, v

    def Q(s, t, m, r, v, w, d):
        '''
        Important Note: first variables are the not consistent variables followed
        by the consistent ones. See sample QA example if you need too.
        '''
        #define some short cuts
        seqg, perg, choiceg = s.seqg, s.perg, s.choiceg


        pre1 = ('Consider a coil')
        pre2 = ('A coil is')
        pre3 = ('A coil of wire is')
        pre4 = ('Consider a wire coil')
        pre5 = ('Consider a coil of wire')

        a1 = seqg('that is created by winding',t,'turns of wire around a cylindrical wooden object that is', m,'m long.')
        a2 = seqg('created by winding',t,'turns of wire around a cylindrical wooden object that is', m,'m in length.')
        a3 = seqg('created by winding', t, 'turns of wire around a wooden object that is', m,'m in length and has a cylindrical shape.')


        b1_a = seqg('A resistor is added to bring the resistance of the circuit to',r,'Ω.')
        b1_b = seqg('A battery of',v,'V is connected to the coil.')
        b1 = perg(b1_a, b1_b)

        c1 = seqg('What is the strength of the magnetic field inside of the coil?')
        c2 = seqg('Find the magnetic field inside of the coil.')
        c3 = seqg('Calculate the magnitude of the magnetic field inside of the coil.')
        c4 = seqg('Compute the magnitude of the magnetic field inside of the coil.')
        c5 = seqg('What is the magnetic field inside of the coil?')
        c6 = seqg('Compute the magnitude of the magnetic field inside of the coil.')



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
        q61 = seqg(pre1, a3, b1, c1)
        q62 = seqg(pre1, a3, b1, c2)
        q63 = seqg(pre1, a3, b1, c3)
        q64 = seqg(pre1, a3, b1, c4)
        q65 = seqg(pre1, a3, b1, c5)
        q66 = seqg(pre1, a3, b1, c6)
        q67 = seqg(pre2, a3, b1, c1)
        q68 = seqg(pre2, a3, b1, c2)
        q69 = seqg(pre2, a3, b1, c3)
        q70 = seqg(pre2, a3, b1, c4)
        q71 = seqg(pre2, a3, b1, c5)
        q72 = seqg(pre2, a3, b1, c6)
        q73 = seqg(pre3, a3, b1, c1)
        q74 = seqg(pre3, a3, b1, c2)
        q75 = seqg(pre3, a3, b1, c3)
        q76 = seqg(pre3, a3, b1, c4)
        q77 = seqg(pre3, a3, b1, c5)
        q78 = seqg(pre3, a3, b1, c6)
        q79 = seqg(pre4, a3, b1, c1)
        q80 = seqg(pre4, a3, b1, c2)
        q81 = seqg(pre4, a3, b1, c3)
        q82 = seqg(pre4, a3, b1, c4)
        q83 = seqg(pre4, a3, b1, c5)
        q84 = seqg(pre4, a3, b1, c6)
        q85 = seqg(pre5, a3, b1, c1)
        q86 = seqg(pre5, a3, b1, c2)
        q87 = seqg(pre5, a3, b1, c3)
        q88 = seqg(pre5, a3, b1, c4)
        q89 = seqg(pre5, a3, b1, c5)
        q90 = seqg(pre5, a3, b1, c6)

        q = choiceg(q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20, q21, q22, q23, q24, q25, q26, q27, q28, q29, q30, q31, q32, q33, q34, q35, q36, q37, q38, q39, q40, q41, q42, q43, q44, q45, q46, q47, q48, q49, q50, q51, q52, q53, q54, q55, q56, q57, q58, q59, q60, q61, q62, q63, q64, q65, q66, q67, q68, q69, q70, q71, q72, q73, q74, q75, q76, q77, q78, q79, q80, q81, q82, q83, q84, q85, q86, q87, q88, q89, q90)
        return q

    def A(s,t, m, r, v, w, d):
        '''
        Important Note: first variables are the not consistent variables followed
        by the consistent ones. See sample QA example if you need too.
        '''
        seqg, perg, choiceg = s.seqg, s.perg, s.choiceg

        B = (4*3.141592)*(10**-7)*t*v/r/m

        in1 = seqg('The magnetic field inside of the coil is', B,'T.')
        in2 = seqg('The magnetic field in the middle of the coil is',B,'T.')
        in3 = seqg('The magnitude of the magnetic field inside the coil is',B,'T.')
        in4 = seqg('The strength of the magnetic field inside the coil is',B,'T.')
        in5 = seqg('The magnetic field inside of the coil is equal to', B, 'T.')
        in6 = seqg(B, 'T is the magnitude of the magnetic field inside of the coil.')
        in7 = seqg(B, 'T is the strength of the magnetic field inside of the coil.')
        in8 = seqg('The strength of the magnetic field in the middle of the coil is', B, 'T.')


        a = choiceg(in1, in2, in3, in4, in5, in6, in7, in8)
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