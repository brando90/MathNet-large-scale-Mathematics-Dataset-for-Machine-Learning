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
        self.description = 'A coaxial cable consists of two concentric long hollow cylinders of zero resistance. The inner cylinder has radius a, the outer cylinder has radius b, and the length of both cylinders is l, with l >> b. The cable transmits DC power from a battery to the circuit. The battery provides an emf e between the two conductors at one end of both cylinders. A resistor of resistance R is connected between the two conductors at the other end of both cylinders. A current I flows down the inner conductor and back up the outer conductor. The battery charges the inner conductor to a charge −Q and the outer conductor to a charge +Q. Calculate the magnitude of the magnetic field B when r < a, r > b, and a < r < b, in terms of a, b, l, r, I, and R.'

        # keywords about the question that could help to make this more searchable in the future
        self.keywords = ['Physics', 'Electricity and Magnetism', 'E&M', 'Poynting vector', 'energy flow']
        self.use_latex = True

    def seed_all(self, seed):
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
            a, b, l, e, R, I, Q, B, r = symbols('a b l e R I Q B r')
        else:
            a, b, l, e, R, I, Q, B, r = self.get_symbols(9, uppercase = True)

        return a, b, l, e, R, I, Q, B, r

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
            diameter_radius, diameter = 90, 'radius'
        else:
            diameter_radius = np.random.randint(1, 100)
            if diameter_radius > 50:
                diameter = 'radius'
            else:
                diameter = 'diameter'

        return diameter_radius, diameter

    def Q(s, diameter_radius, diameter, a, b, l, e, R, I, Q, B, r):
        '''
        Important Note: first variables are the not consistent variables followed
        by the consistent ones. See sample QA example if you need too.
        '''
        seqg, perg, choiceg = s.seqg, s.perg, s.choiceg

        if diameter_radius < 51:
            aa = '2'+str(a)
            bb = '2'+str(b)
        else:
            aa = str(a)
            bb = str(b)

        Consider = choiceg('Consider', 'There is', 'Let there be', 'Consider for a moment', 'Consider the existence of')

        resist = choiceg('zero resistance','a resistance of zero','no resistance','a resistance equal to zero')
        zero1 = choiceg('of {0}'.format(resist),'having {0}'.format(resist),'and have {0}'.format(resist),'that have {0}'.format(resist))
        zero2 = choiceg('has {0}'.format(resist), 'contains {0}'.format(resist), 'consists of {0}'.format(resist))
        zero3 = choiceg('that has {0}'.format(resist),'of {0}'.format(resist),'having {0}'.format(resist),'that have {0}'.format(resist),'has {0}'.format(resist), 'contains {0}'.format(resist), 'consists of {0}'.format(resist))

        AA = seqg('A coaxial cable consists of two', perg('concentric', 'long', 'hollow'),'cylinders of zero resistance.')
        a0 = seqg('A coaxial cable consists of two', perg('concentric', 'long', 'hollow'),'cylinders {0}.'.format(zero1))
        a1 = seqg('A coaxial cable consisting of two', perg('concentric', 'long', 'hollow'),'cylinders {0}.'.format(zero2))
        a2 = seqg('Two', perg('concentric', 'long', 'hollow'), 'cylinders {0} comprise a coaxial cable.'.format(zero3))
        a3 = seqg('Two', perg('concentric', 'long', 'hollow'), 'cylinders comprise a coaxial cable {0}.'.format(zero3))
        a_part = choiceg(AA, a0,a1,a2,a3)

        compare = choiceg('{0} >> {1}'.format(l,b),'{1} << {0}'.format(l,b))
        wit = choiceg('with','and')
        cable = choiceg('both cylinders','the two cylinders','the 2 cylinders','the cable','the coaxial cable')

        b0 = seqg('The inner cylinder has',diameter,aa+', the outer cylinder has',diameter,bb+', and the length of both cylinders is',str(l)+', with',l,'>>',str(b)+'.')
        b1 = seqg('The inner cylinder has {0} {1}, the outer cylinder has {0} {2}, and the length of {6} is {3}, {5} {4}.'.format(diameter,aa, bb, l, compare,wit,cable))
        b2 = seqg('The outer cylinder has {0} {2}, the inner cylinder has {0} {1}, and the length of {6} is {3}, {5} {4}.'.format(diameter, aa, bb, l, compare,wit,cable))
        b3 = seqg('The length of {6} is {3}, the outer cylinder has {0} {2}, and the inner cylinder has {0} {1}, {5} {4}.'.format(diameter, aa, bb, l, compare,wit,cable))
        b4 = seqg('The length of {6} is {3}, the inner cylinder has {0} {1}, and the outer cylinder has {0} {2}, {5} {4}.'.format(diameter, aa, bb, l, compare, wit,cable))
        b5 = seqg('The inner cylinder has {0} {1}, the length of {6} is {3}, and the outer cylinder has {0} {2}, {5} {4}.'.format(diameter,aa, bb, l, compare,wit,cable))
        b6 = seqg('The outer cylinder has {0} {2}, the length of {6} is {3}, and the inner cylinder has {0} {1}, {5} {4}.'.format(diameter, aa, bb, l, compare, wit, cable))
        b_part = choiceg(b0,b1,b2,b3,b4,b5,b6)

        transmits = choiceg('transmits', 'supplies', 'carries')
        transmitted = choiceg('transmitted','supplied','carried')

        c0 = seqg('The cable', transmits,'DC power from a battery to the circuit.')
        c1 = seqg('The battery', transmits,'DC power through the cable to the circuit.')
        c2 = seqg('The battery',transmits,'DC power to the circuit.')
        c3 = seqg('The battery',transmits,'DC power to the cable.')
        c4 = seqg('DC power is',transmitted,'through the cable to the circuit by the battery.')
        c5 = seqg('DC power is',transmitted,'through circuit by the battery.')
        c6 = seqg('DC power is',transmitted,'to the cable by the battery.')
        c_part = choiceg(c0,c1,c2,c3,c4,c5,c6)

        comma1 = choiceg('. A', ', and a')
        comma2 = choiceg('. The', ', and the')

        DD = seqg('The battery provides an emf',e,'between the two conductors at one end of both cylinders. A resistor of resistance',R,'is connected between the two conductors at the other end of both cylinders.'.format(cable, R, e, comma1))
        d0 = seqg('The battery provides an emf {2} between the two conductors at one end of the {0}{3} resistor of resistance {1} is connected between the two conductors at the other end of the {0}.'.format(cable, R, e, comma1))
        d1 = seqg('A resistor of resistance {2} is connected between the two conductors at one end of {0}{3} battery provides an emf {1} between the two conductors at the other end of the {0}.'.format(cable,e,R, comma2))
        d2 = seqg('Connected between the two conductors at one end of {0} is a resistor of resistance {2}{3} battery provides an emf {1} between the two conductors at the other end of the {0}.'.format(cable,e,R, comma2))
        d3 = seqg('Connected between the two conductors at one end of {0} is a battery of emf {1}{3} resistor of resistance {2} is connected between the two conductors at the other end of the {0}.'.format(cable, e, R, comma1))
        d4 = seqg('At one end of the {0} there is a battery of emf {1} connected between the {0}{3} resistor of resistance {2} is connected between the two conductors at the other end of the {0}.'.format(cable,e,R, comma1))
        d5 = seqg('At one end of the {0} there is a resistor of resistance {2} connected between the {0}{3} battery of emf {1} is connected between the two conductors at the other end of the {0}.'.format(cable, e, R, comma2))
        d6 = seqg('At one end of the {0} there is a resistor of resistance {2} connected between the {0}{3} battery provides an emf {1} between the two conductors at the other end of the {0}.'.format(cable, e, R, comma2))
        d_part = choiceg(DD, d0,d1,d2,d3,d4,d5,d6)

        e0 = seqg('A current',I,'flows down the inner conductor and back up the outer conductor.')
        e1 = seqg('A current {0} flows throughout the {1}.'.format(I, cable))
        e2 = seqg('A current {0} flows through the {1}.'.format(I, cable))
        e3 = seqg('Through the {1} flows a current {0}.'.format(I, cable))
        e_part = choiceg(e0,e1,e2,e3)

        c_d_e = perg(c_part,d_part,e_part)

        f0 = seqg('The battery charges the inner conductor to a charge −' + str(Q),'and the outer conductor to a charge +'+str(Q)+'.')
        f1 = seqg('The battery charges the inner conductor to a charge −{0} and the outer conductor to a charge +{0}.'.format(Q))
        f2 = seqg('The battery charges the outer conductor to a charge +{0} and the inner conductor to a charge -{0}.'.format(Q))
        f3 = seqg('The inner conductor is charged to a charge −{0} and the outer conductor to a charge +{0} by the battery.'.format(Q))
        f4 = seqg('The outer conductor is charged to a charge +{0} and the inner conductor to a charge -{0} by the battery.'.format(Q))
        f_part = choiceg(f0,f1,f2,f3,f4)

        Calculate = choiceg('Calculate', 'Compute', 'Find', 'Derive an expression for')
        calculate = choiceg('calculate', 'compute', 'find', 'derive an expression for')

        r_a = choiceg(seqg(r,'<',str(a)+','), seqg(a,'>',str(r)+','))
        r_b = choiceg(seqg(b,'<',str(r)+','), seqg(r,'>',str(b)+','))
        r_a_b = choiceg(seqg(a, '<',r, '<', str(b) + ','), seqg(b, '>',r, '>', str(a) + ','))

        less_than1 = seqg(perg(r_a, r_b), 'and',r,'>',b)
        less_than2 = seqg(perg(r_b, r_a_b), 'and', r, '<', a)
        less_than3 = seqg(perg(r_a, r_a_b), 'and', a, '<',r, '<', b)
        less_than4 = seqg(perg(r_a, r_b), 'and', b, '<', r)
        less_than5 = seqg(perg(r_b, r_a_b), 'and', a, '>', r)
        less_than6 = seqg(perg(r_a, r_a_b), 'and', b, '>',r, '>', a)
        less_than = choiceg(less_than1,less_than2,less_than3, less_than4, less_than5, less_than6)

        terms1 = seqg(perg(str(a) + ',', str(b) + ',', str(l) + ',', str(r) + ',', str(I) + ','), 'and', str(R))
        terms2 = seqg(perg(str(R) + ',', str(b) + ',', str(l) + ',', str(r) + ',', str(I) + ','), 'and', str(a))
        terms3 = seqg(perg(str(a) + ',', str(R) + ',', str(l) + ',', str(r) + ',', str(I) + ','), 'and', str(b))
        terms4 = seqg(perg(str(a) + ',', str(b) + ',', str(R) + ',', str(r) + ',', str(I) + ','), 'and', str(l))
        terms5 = seqg(perg(str(a) + ',', str(b) + ',', str(l) + ',', str(R) + ',', str(I) + ','), 'and', str(r))
        terms6 = seqg(perg(str(a) + ',', str(b) + ',', str(l) + ',', str(r) + ',', str(R) + ','), 'and', str(I))
        terms = choiceg(terms1,terms2,terms3,terms4,terms5,terms6)

        GG = seqg(Calculate, 'the magnitude of the magnetic field',B,'when r < a, r > b, and a < r < b, in terms of',str(a) + ',', str(b) + ',', str(l) + ',', str(r) + ',', str(I) + ', and', str(R)+'.')
        g0 = seqg('{0} the magnitude of the magnetic field {1} when {2}, in terms of {3}.'.format(Calculate, B,less_than, terms))
        g1 = seqg('When {0}, {1} the magnitude of the magnetic field {2} in terms of {3}.'.format(less_than, calculate, B, terms))
        g2 = seqg('In terms of {3}, {0} the magnitude of the magnetic field {1} when {2}.'.format(Calculate, B,less_than, terms))
        g3 = seqg('When {0}, {1} the magnitude of the magnetic field {2}. Express your answer in terms of {3}.'.format(less_than, calculate, B, terms))
        g4 = seqg('{0} the magnitude of the magnetic field {1} when {2}.'.format(Calculate, B,less_than))
        g5 = seqg('When {0}, {1} the magnitude of the magnetic field {2}.'.format(less_than, calculate, B))
        g_part = choiceg(GG, g0,g1, g2, g3, g4, g5)

        q = seqg(a_part, b_part, c_d_e, f_part, g_part)

        return q

    def A(s, diameter_radius, diameter, a, b, l, e, R, I, Q, B, r):
        '''
        Important Note: first variables are the not consistent variables followed
        by the consistent ones. See sample QA example if you need too.
        '''
        seqg, perg, choiceg = s.seqg, s.perg, s.choiceg

        pi = np.pi
        mu_0 = 4 * pi * 10**-7
        zero = choiceg('0', 'zero')

        Eq(B*2*pi*r, I*mu_0)
        bfield1 = Eq(B, I*mu_0/(2*pi*r))
        bfield2 = Eq(I*mu_0/(2*pi*r), B)
        bfield = choiceg(bfield1, bfield2)

        r_a = choiceg(seqg(r,'<',a), seqg(a,'>',r))
        r_b = choiceg(seqg(b,'<',r), seqg(r,'>',b))
        r_a_b = choiceg(seqg(a, '<',r, '<', b), seqg(b, '>',r, '>', a))


        a0 = seqg('When {0}, the magnetic field is {1}.'.format(r_a, zero))
        a1 = seqg('The magnetic field is {1} when {0}.'.format(r_a, zero))
        b0 = seqg('When {0}, the magnetic field is {1}.'.format(r_b, zero))
        b1 = seqg('The magnetic field is {1} when {0}.'.format(r_b, zero))
        c0 = seqg('When {0}, the magnetic field is {1}.'.format(r_a_b, bfield))
        c1 = seqg('The magnetic field is {1} when {0}.'.format(r_a_b, bfield))

        a_b_c = perg(choiceg(a0,a1), choiceg(b0,b1), choiceg(c0,c1))

        a = choiceg(a_b_c)
        return a

    def get_qa(self, seed):
        '''
        Example of how Q,A are formed in general.
        '''
        # set seed
        self.seed_all(seed)
        # get variables for qa and register them for the current q,a
        variables, variables_consistent = self._create_all_variables()
        # get concrete qa strings
        q_str = self.Q(*variables, *variables_consistent)
        a_str = self.A(*variables, *variables_consistent)
        return q_str, a_str


## Some helper functions to check the formats are coming out correctly

##

def check_single_question_debug(qagenerator):
    '''
    Checks by printing a single quesiton on debug mode
    '''
    qagenerator.debug = True
    q, a = qagenerator.get_qa(seed=1)
    print('qagenerator.debug = ', qagenerator.debug)
    print('q: ', q)
    print('a: ', a)


def check_single_question(qagenerator):
    '''
    Checks by printing a single quesiton on debug mode
    '''
    q, a = qagenerator.get_qa(seed=random.randint(0, 1000))
    print('qagenerator.debug = ', qagenerator.debug)
    print('q: ', q)
    print('a: ', a)


def check_mc(qagenerator):
    '''
    Checks by printing the MC(Multiple Choice) option
    '''
    nb_answers_choices = 10
    for seed in range(3):
        # seed = random.randint(0,100)
        q_str, ans_list = qagenerator.generate_single_qa_MC(nb_answers_choices=nb_answers_choices, seed=seed)
        print('\n-------seed-------: ', seed)
        print('q_str:\n', q_str)
        print('-answers:')
        print("\n".join(ans_list))


def check_many_to_many(qagenerator):
    for seed in range(3):
        q, a = qagenerator.generate_many_to_many(nb_questions=4, nb_answers=3, seed=seed)
        print('-questions:')
        print("\n".join(q))
        print('-answers:')
        print("\n".join(a))


def check_many_to_one_consis(qagenerator):
    for seed in range(3):
        print()
        q, a = qagenerator.generate_many_to_one(nb_questions=5, seed=seed)
        print("\n".join(q))
        print('a: ', a)
        # print("\n".join(a))


def check_many_to_one_consistent_format(qagenerator):
    nb_qa_pairs, nb_questions = 10, 3
    qa_pair_list = qagenerator.generate_many_to_one_consistent_format(nb_qa_pairs, nb_questions)
    for q_list, a_consistent_format in qa_pair_list:
        print()
        print("\n".join(q_list))
        print('a: ', a_consistent_format)


if __name__ == '__main__':
    qagenerator = QA_constraint()
    check_single_question(qagenerator)
    #user_test.run_unit_test_for_user(QA_constraint)