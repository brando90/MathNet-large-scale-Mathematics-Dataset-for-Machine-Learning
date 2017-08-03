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
        self.description = '''A cylindrical glass rod is heated with a torch until it conducts enough current to cause a light bulb to glow. The rod has a length l = 0.02 m, a diameter d = 0.005 m, and its ends, plated with material of infinite conductivity, are connected to the rest of the circuit. When red hot, the rod's conductivity varies with position x measured from the center of the rod as y(x) = z*L^2/x^2, with z = 0.04 (Ωm)^-1. What is the steady-state magnitude of the electric field e? Express your answer in terms of l, Δv, and x'''

        # keywords about the question that could help to make this more searchable in the future
        self.keywords = ['Physics', 'Electricity and Magnetism', 'E&M', 'resistance', 'conductivity']
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
            l, x, d, z, y, v, j, e = symbols('l x d z y v j e')
        else:
            l,x,d,z, y, v, j, e = self.get_symbols(8)

        return  l, x, d, z, y, v, j, e

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
            l_val, d_val, diameter_radius, z_val, diameter = 0.02, 0.005, 1, 0.04, 'diameter'
        else:
            l_val = np.random.randint(1, 1000000)
            d_val = np.random.randint(1, 5000)/100000
            diameter_radius = np.random.randint(1,100)
            z_val = np.random.randint(2000,5000)/100000000000
            if diameter_radius > 50:
                d_val = d_val/2
                diameter = 'radius'
            else:
                diameter = 'diameter'


        return l_val, d_val, z_val, diameter

    def Q(s, l_val, d_val, z_val, diameter, l,x,d,z,y, v, j,e):
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
        calculate = choiceg('Calculate', 'Compute', 'Find', 'Find a numerical answer for')
        conducts = choiceg('conducts','is conducting')
        torch = choiceg('torch','fire','heating agent','blow torch', 'Bunsen burner', 'stove','hot plate', 'heating mantle', 'heating apparatus','heater')
        heat1 = choiceg('heats', 'is used to heat','heats up','is used to heat up')
        heat2 = choiceg('heated with','heated using','heated up with','heated up using','heated up through the application of a {0} to the rod'.format(torch),'heated by applying a {0} to the rod'.format(torch))


        a0 = seqg('A cylindrical glass rod is',heat2,'a',torch,'until it',conducts,'enough current to cause a light bulb to glow.')
        a1 = seqg('A {0} {1} a cylindrical glass rod until it {2} enough current to cause a light bulb to glow.'.format(torch, heat1, conducts))
        a2 = seqg('A {0} {1} a cylindrical glass rod until it {2} a large enough current to cause a light bulb to glow.'.format(torch, heat1, conducts))
        a3 = seqg('A glass rod {0} cylindrical in shape is {1} a {2} until it {3} enough current to cause a light bulb to glow.'.format(thats,heat2, torch, conducts))
        a4 = seqg('A glass rod {0} a cylinder is {1} a {2} until it {3} enough current to cause a light bulb to glow.'.format(thats, heat2, torch, conducts))
        a_part = choiceg(a0,a1,a2,a3,a4)

        l_eq = Eq(l, l_val)
        d_eq = Eq(d,d_val)

        b0 = seqg('The rod has a length',l_eq,'m, a',diameter,d_eq,'m, and its ends, plated with material of infinite conductivity, are connected to the rest of the circuit.')
        b1 = seqg('The length of the rod is {0} m and its {1} is {2} m, and its ends, plated with material of infinite conductivity, are connected to the rest of the circuit.'.format(l_eq, diameter, d_eq))
        b2 = seqg('The rod has a {1} {2} m and length {0} m. Its ends are plated with material of infinite conductivity, and are connected to the rest of the circuit.'.format(l_eq, diameter, d_eq))
        b3 = seqg('The rod has a {1} {2} m, a length {0} m, and its ends, plated with material of infinite conductivity, are connected to the rest of the circuit.'.format(l_eq, diameter, d_eq))
        b4 = seqg('The rod is of length {0} m, {1} {2} m, and its ends, plated with material of infinite conductivity, are connected to the rest of the circuit.'.format(l_eq, diameter, d_eq))
        b5 = seqg('The {0} of the rod is {1} m and the length of the rod is {2} m. The rod is plated at its ends with a material of infinite conductivity. The rod is connected to the circuit.'. format(diameter, d_eq, l_eq))
        b6 = seqg('The length of the rod is {0} m and its {1} is {2} m, and its ends, which are plated with material of infinite conductivity, are connected to the rest of the circuit.'.format(l_eq, diameter, d_eq))
        b7 = seqg('The rod has a {1} {2} m and length {0} m. The rod is plated at its ends with a material of infinite conductivity. The rod is connected to the circuit.'.format(l_eq, diameter, d_eq))
        b8 = seqg('The rod has a {1} {2} m, a length {0} m, and its ends, which are plated with material of infinite conductivity, are connected to the rest of the circuit.'.format(l_eq, diameter, d_eq))
        b9 = seqg('The rod is of length {0} m, {1} {2} m, and its ends, which are plated with material of infinite conductivity, are then connected to the rest of the circuit.'.format(l_eq, diameter, d_eq))
        b_part = choiceg(b0,b1,b2,b3,b4,b5,b6,b7,b8,b9)

        z_eq = Eq(z, z_val)
        z_str = str(z)
        x_str = str(x)
        l_str = str(l)
        d_str = str(d)
        y_str = str(y)
        v_str = str(v)
        j_str = str(j)
        e_str = str(e)
        red = choiceg('red', 'white','extremely','really','very', '')
        hot = choiceg('the rod becomes {0}'.format(red), 'the rod is {0}'.format(red))
        conductive = choiceg('''rod's conductivity''', 'conductivity of the rod')
        varies = choiceg('varies with','changes with','is dependent on','is related to')
        centre = choiceg('center of the rod', '''the rod's center''', '''the rod's centre''')

        c0 = seqg('When red hot, the',conductive,varies,'position', x,'measured from the',centre,'as',y_str+'('+x_str+') =',z_str+'*L^2/'+x_str+'^2, with',z_eq,'(Ωm)^-1.')
        c1 = seqg('When {3} hot, the {4} {5} position {0} measured from the {6} as {7}({0}) = {1}*L^2/{0}^2, with {2} (Ωm)^-1.'.format(x, z,z_eq,red, conductive, varies, centre,y))
        c2 = seqg('When {3} hot, the {4} {5} position {0} measured from the {6} as {7}({0}) = {1}*L^2/{0}^2, with {2} (Ωm)^-1.'.format(x, z, z_eq,hot, conductive, varies,centre,y))
        c3 = seqg('The {4} {5} position {0} when the rod is {3} hot. The conductivity when measured from the {6} is {7}({0}) = {1}*L^2/{0}^2, with {2} (Ωm)^-1 when.'.format(x, z,z_eq,red, conductive, varies, centre,y))
        c4 = seqg('The {4} {5} position {0} when the rod is {3} hot. The conductivity when measured from the {6} is {7}({0}) = {1}*L^2/{0}^2, with {2} (Ωm)^-1 when.'.format(x, z, z_eq, hot, conductive, varies, centre,y))
        c_part = choiceg(c0,c1,c2,c3,c4)

        whats = choiceg('what is', '''what's''')
        calculate = choiceg('calculate','find','compute','find a numerical value')
        Whats = choiceg('What is', '''What's''')
        Calculate = choiceg('Calculate', 'Find', 'Compute', 'Find a numerical value for')

        terms1 = seqg(perg(l_str + ',', 'Δ'+v_str + ','), 'and ' + x_str)
        terms2 = seqg(perg(x_str + ',', 'Δ'+v_str + ','), 'and', l_str)
        terms3 = seqg(perg(l_str + ',', x_str + ','), 'and Δ' + v_str)
        terms = choiceg(terms1, terms2, terms3)

        d0 = seqg('What is the steady-state magnitude of the electric field',e_str + '? Express your answer in terms of',terms)
        d1 = seqg('What is the steady-state magnitude of the electric field {0}? Express your answer in terms of {1}.'.format(e, terms))
        d2 = seqg('{3} the magnitude of the electric field {1} surrounding the rod when a voltage Δ{0} is applied? Express your answer in terms of {2}.'.format(v, e, terms, Whats))
        d3 = seqg('{3} the magnitude of the electric field {1} surrounding the rod when a voltage Δ{0} is applied? Express your answer in terms of {2}.'.format(v, e, terms, Calculate))
        d4 = seqg('Expressing your answer in terms of {2}, {3} the magnitude of the steady-state magnetic field {1} surrounding the rod when a voltage Δ{0} is applied to the rod.'.format(v, e, terms, calculate))
        d5 = seqg('Expressing your answer in terms of {2}, {3} the magnitude of the steady-state magnetic field {1} surrounding the rod when a voltage Δ{0} is applied to the rod?'.format(v, e, terms, whats))

        d_part = choiceg(d0,d1,d2,d3,d4,d5)

        q = seqg(a_part, b_part, c_part, d_part)

        return q

    def A(s, l_val, d_val, z_val, diameter, l,x,d,z,y, v, j,e):
        '''
        Important Note: first variables are the not consistent variables followed
        by the consistent ones. See sample QA example if you need too.
        '''
        seqg, perg, choiceg = s.seqg, s.perg, s.choiceg

        R = symbols('R')
        pi = np.pi
        dx = symbols('dx')

        if diameter == 'radius':
            A = pi*((d_val*2)**2)
        else:
            A = pi*(d_val**2)

        dR = 4 * (x ** 2) * dx / (z * (l ** 2) * A)
        resistance1 = Eq(R, l_val/(3*A*z_val))
        resistance2 = Eq(l_val/(3 * A * z_val), R)
        resistance = choiceg(resistance1, resistance2)

        iis = choiceg('is', 'is equal to', 'equals')
        rod = choiceg('glass rod', 'rod')

        v_str = str(v)
        l_str = str(l)
        x_str = str(x)

        ends = choiceg('two ends of the rod', '''rod's two ends''', 'ends of the rod', 'two ends')
        terms1 = seqg(perg(l_str + ',', 'Δ' + v_str + ','), 'and ' + x_str)
        terms2 = seqg(perg(x_str + ',', 'Δ' + v_str + ','), 'and', l_str)
        terms3 = seqg(perg(l_str + ',', x_str + ','), 'and Δ' + v_str)
        terms = choiceg(terms1, terms2, terms3)

        I = 12*v/l
        current_density1 = Eq(j, I/A)
        current_density2 = Eq(I / A, j)
        current_density = choiceg(current_density1,current_density2)

        sigma = (l**2)/(x**2)
        e_field1 = Eq(e, I/sigma)
        e_field2 = Eq(I/sigma, e)
        e_field = choiceg(e_field1, e_field2)
        steady = choiceg('steady-state magnitude of the electric field','magnitude of the electric field','''electric field's magnitude''')

        a0 = seqg('{0} is the {2} of the {1}.'.format(e_field, rod, steady))
        a1 = seqg('In terms of {0}, the {4} of the {1} {2} {3}.'.format(terms, rod, iis, e_field, steady))
        a1 = seqg('''{0} {2} the {1}.'''.format(e_field, steady,iis))
        a2 = seqg('The',steady, iis, e_field)
        a3 = seqg('''The {0}'s electric field {1} {2}.'''.format(rod, iis, e_field))
        a4 = seqg('{0} is the electric field surrounding the {1} in terms of {2}.'.format(e_field, rod, terms))
        a5 = seqg('''{0} is the {1}'s electric field using {2}.'''.format(e_field, rod, terms))
        a6 = seqg('The magnitude of the electric field of the',rod, iis, e_field,'in terms of',terms)
        a7 = seqg('''The {0}'s electric field using {3} {1} {2}'''.format(rod, iis, e_field, terms))
        a8 = seqg('When using {2}, {0} is the electric field surrounding the {1}.'.format(e_field, rod, terms))
        a9 = seqg('''When using {2}, {0} is the {1}'s electric field.'''.format(e_field, rod, terms))



        a = choiceg(a0, a1, a2, a3, a4, a5, a6, a7, a8,a9)
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