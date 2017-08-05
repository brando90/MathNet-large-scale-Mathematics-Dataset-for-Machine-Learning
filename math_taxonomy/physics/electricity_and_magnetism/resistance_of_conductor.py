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
        self.description = 'Consider a cable that is l = 3000000 m long. The conductor in this cable consists of x = 10 copper wires, each of diameter d = 0.001 m, bundled together and surrounded by an insulating sheath. The resistivity of copper is p = 3.0 \\cdot 10^{-8} Ωm. Calculate the resistance of the conductor in terms of l, d, p, and x'

        # keywords about the question that could help to make this more searchable in the future
        self.keywords = ['Physics', 'Electricity and Magnetism', 'E&M', 'resistance']
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
            l, x,d,p = symbols('l x d p')
        else:
            l,x,d,p = self.get_symbols(4)

        return  l,x,d,p

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
            l_val, x_val, d_val, diameter_radius, p_val, diameter = 3000000, 10, .001, 1, 0.00000003, 'diameter'
        else:
            l_val = np.random.randint(1, 1000000)
            x_val = np.random.randint(1,100)
            d_val = np.random.randint(1, 5000)/100000
            diameter_radius = np.random.randint(1,100)
            p_val = np.random.randint(2000,5000)/100000000000
            if diameter_radius > 50:
                d_val = d_val/2
                diameter = 'radius'
            else:
                diameter = 'diameter'


        return l_val, x_val, d_val, diameter_radius, p_val, diameter

    def Q(s, l_val, x_val, d_val, diameter_radius, p_val, diameter, l,x,d,p):
        '''
        Important Note: first variables are the not consistent variables followed
        by the consistent ones. See sample QA example if you need too.
        '''
        seqg, perg, choiceg = s.seqg, s.perg, s.choiceg

        Consider = choiceg('Consider', 'There is', 'Let there be', 'Consider for a moment', 'Consider the existence of')
        length_eq = Eq(l, l_val)
        long = choiceg('in length', 'long')
        thats = choiceg('that is', '''that's''', 'which is')
        whose = choiceg('whose length is', 'with a length of', 'traversing a distance of','that traverses a distance of')


        a0 = seqg(Consider, 'a cable',thats,length_eq,'m long.')
        a1 = seqg('{0} a cable {3} {1} m {2}.'.format(Consider, length_eq, long, thats))
        a2 = seqg('A cable is {0} m {1}.'.format(length_eq, long))
        a3 = seqg('{0} a cable {1} {2} m.'.format(Consider, whose, length_eq))
        a4 = seqg('{0} a long cable {1} {2} m.'.format(Consider, whose, length_eq))
        a5 = seqg('{0} a long cable {2} {1} m.'.format(Consider, length_eq, thats))
        a6 = seqg('A long cable is {0} m.'.format(length_eq))
        a_part = choiceg(a0, a1,a2,a3,a4,a5,a6)

        x_eq = Eq(x, x_val)
        d_eq = Eq(d, d_val)
        conductor = choiceg('there is', 'there lies', 'consider there being', '''there's''','resides')

        each = choiceg('each of','', 'and each has a', 'and each contains a','and each consists of a', 'each one having', 'each having','each containing','each consisting of','each of which having','each of which consisting of', 'each of which contains')

        b0 = seqg('The conductor in this cable consists of',x_eq,'copper wires,',each,diameter,d_eq,'m, bundled together and surrounded by an insulating sheath.')
        b1 = seqg('The conductor in this cable consists of {0} copper wires, {3} {1} {2} m, bundled together and surrounded by an insulating sheath.'.format(x_eq, diameter, d_eq, each))
        b2 = seqg('In the cable {3} a conductor which consists of {0} copper wires, {3} {1} {2} m, bundled together and surrounded by an insulating sheath.'.format(x_eq, diameter, d_eq, conductor, each))
        b3 = seqg('Built into the cable is a conductor which consists of {0} copper wires, {3} {1} {2} m, bundled together and surrounded by an insulating sheath.'.format(x_eq, diameter, d_eq, each))
        b4 = seqg('The conductor in this cable consists of an insulating sheath that surrounds {0} copper wires, {3} {1} {2} m,'.format(x_eq, diameter, d_eq, each))
        b5 = seqg('In the cable {3} a conductor which consists of an insulating sheath that surrounding {0} copper wires, {3} {1} {2} m.'.format(x_eq, diameter, d_eq, conductor, each))
        b6 = seqg('Built into the cable is a conductor which consists of an insulating sheath that surrounds {0} copper wires, {3} {1} {2} m.'.format(x_eq, diameter, d_eq, each))
        b_part = choiceg(b0,b1,b2,b3,b4,b5,b6)

        p_eq = Eq(p, p_val)
        c0 = seqg('The resistivity of copper is',p_eq,'Ωm.')
        c1 = seqg('''The copper's resistivity is''',p_eq,'Ωm.')
        c2 = seqg(p_eq, 'Ωm is the resistivity of copper.')
        c3 = seqg(p_eq, '''Ωm is the copper's resistivity.''')
        c4 = seqg('Take the resistivity of copper as being', p_eq, 'Ωm.')
        c5 = seqg('''Take the copper's resistivity as being''', p_eq, 'Ωm.')
        c6 = seqg('Use',p_eq, 'Ωm as the resistivity of the copper.')
        c7 = seqg('Use',p_eq, '''Ωm as the copper's resistivity.''')
        c_part = choiceg(c0,c1,c2,c3,c4,c5,c6,c7)

        Calculate = choiceg('Calculate', 'Compute', 'Find', 'Find a numerical answer for')
        calculate = choiceg('calculate', 'compute', 'find', 'find a numerical answer for')

        ll = str(l)
        xx = str(x)
        dd = str(d)
        pp = str(p)

        terms1 = seqg(perg(ll + ',', dd + ',', pp + ','), 'and', xx)
        terms2 = seqg(perg(ll + ',', dd + ',', xx + ','), 'and', pp)
        terms3 = seqg(perg(ll + ',', xx + ',', pp + ','), 'and', dd)
        terms4 = seqg(perg(xx + ',', dd + ',', pp + ','), 'and', ll)
        terms = choiceg(terms1, terms2, terms3, terms4)

        d0 = seqg(Calculate,'the resistance of the conductor in terms of', terms)
        d1 = seqg('''{0} the conductor's resistance in terms of {1}.'''.format(Calculate, terms))
        d2 = seqg('{0} the resistance of the conductor in the cable in terms of {1}.'.format(Calculate,terms))
        d3 = seqg('In terms of {0} {1} the resistance of the conductor.'.format(terms, calculate))
        d4 = seqg('''In terms of {0} {1} the conductor's resistance.'''.format(terms, calculate))
        d5 = seqg('In terms of {0} {1} the resistance of the conductor in the cable.'.format(terms,calculate))

        d_part = choiceg(d0,d1,d2,d3,d4,d5)

        q = seqg(a_part, b_part, c_part, d_part)

        return q

    def A(s, l_val, x_val, d_val, diameter_radius, p_val, diameter, l,x,d,p):
        '''
        Important Note: first variables are the not consistent variables followed
        by the consistent ones. See sample QA example if you need too.
        '''
        seqg, perg, choiceg = s.seqg, s.perg, s.choiceg

        R = symbols('R')
        pi = np.pi
        if diameter == 'diameter':
            A = pi*((d/2)**2)
        else:
            A = pi*(d**2)

        Eq(1/R, x*A/(p*l))
        res1 = Eq(R, (p*l)/(x*A))
        res2 = Eq((p*l)/(x*A), R)
        resistance = choiceg(res1,res2)

        iis = choiceg('is', 'is equal to', 'equals')
        eq_resist = choiceg('', 'equivalent resistance', 'resistance')

        ll = str(l)
        xx = str(x)
        dd = str(d)
        pp = str(p)
        
        terms1 = seqg(perg(ll + ',', dd + ',', pp + ','), 'and', xx)
        terms2 = seqg(perg(ll + ',', dd + ',', xx + ','), 'and', pp)
        terms3 = seqg(perg(ll + ',', xx + ',', pp + ','), 'and', dd)
        terms4 = seqg(perg(xx + ',', dd + ',', pp + ','), 'and', ll)
        terms = choiceg(terms1, terms2, terms3, terms4)

        a0 = seqg(resistance, 'is the',eq_resist,'of the conductor in terms of', terms)
        a1 = seqg('''{0} is the conductor's {1} in terms of {2}.'''.format(resistance, eq_resist, terms))
        a2 = seqg(resistance, 'is the',eq_resist,'of the conductor in the cable in terms of',terms)
        a3 = seqg('The',eq_resist,'of the conductor', iis, resistance)
        a4 = seqg('''The conductor's''',eq_resist,iis, resistance)
        a5 = seqg('The', eq_resist,'of the conductor in the cable',iis, resistance)
        a6 = seqg('In terms of',terms,'the',eq_resist,'of the conductor',iis,resistance)
        a7 = seqg('In terms of',terms,resistance,iis,'the',eq_resist,'of the conductor.')


        a = choiceg(a0, a1, a2, a3, a4, a5,a6,a7)
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