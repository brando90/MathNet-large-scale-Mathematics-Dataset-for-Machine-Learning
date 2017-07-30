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
        self.description = 'An oceanographer studies how the ion concentration in seawater depends on depth. The oceanographer does this by lowering into the water (until completely submerged) a pair of concentric metallic cylinders at the end of a cable and taking data to determine the resistance between these electrodes as a function of depth. The water between the two cylinders forms a cylindrical shell of inner radius a = 1, outer radius b = 2, and length l much larger than 2. The oceanographer applies a potential difference Δv between the inner and outer surfaces of the cylinders, producing an outward radial current i. Let p represent the resistivity of the water. Calculate the resistance of the water between the cylinders in terms of l, a = 1, b = 2, and p'

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
            a, b, l,v,i,p = symbols('a b l v i p')
        else:
            a,b,l, v, i, p = self.get_symbols(6)

        return  a,b,l,v,i,p

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
            d_val, a_val, b_val = 9, 1, 2
        else:
            d_val = np.random.randint(1, 10)
            a_val = np.random.randint(1,100)
            b_val = np.random.randint(150, 500)

        return d_val, a_val, b_val

    def Q(s, d_val,a_val, b_val,a,b,l,v,i,p):
        '''
        Find the magnitude of the electric field caused by a charged particle at a certain distance away from the source charge.
        Important Note: first variables are the not consistent variables followed
        by the consistent ones. See sample QA example if you need too.
        '''
        #define some short cuts

        seqg, perg, choiceg = s.seqg, s.perg, s.choiceg
        if d_val > 5:
            sci = 'oceanographer'
            an = 'An'
        else:
            sci = 'scientist'
            an = 'A'


        thats = choiceg('which is', 'that is', '')
        cylinders = choiceg('cylinders', 'concentric cylinders', 'coaxial cylinders', 'two cylinders')
        study = choiceg('studies', 'is studying')
        related = choiceg('related', 'correlated','correlated with one another', 'related to one another')
        ions = choiceg('ion concentration', 'concentration of ions')
        depth = choiceg('depth and the {0} in seawater'.format(ions), 'the {0} in seawater and depth'.format(ions))

        a0 = seqg(an,sci,study,'how the',ions,'in seawater depends on depth.'.format(an, sci, study, ions))
        a1 = seqg('{0} {1} {2} how the {3} in seawater depends on depth.'.format(an, sci, study, ions))
        a2 = seqg('{0} {1} {2} how the {3} in seawater is dependent on depth.'.format(an, sci, study, ions))
        a3 = seqg('{0} {1} {2} how the {3} in seawater depends on depth.'.format(an, sci, study, ions))
        a4 = seqg('{0} {1} {2} how the {3} are {4}.'.format(an, sci, study, depth, related))
        a5 = seqg('{0} {1} conducts an experiment to determine how the {2} are {3}.'.format(an, sci, depth, related))
        a_part = choiceg(a0, a1, a2, a3, a4, a5)

        concentric = choiceg('concentric', 'coaxial')

        b0 = seqg('The',sci,'does this by lowering into the water (until completely submerged) a pair of',concentric,'metallic cylinders at the end of a cable and taking data to determine the resistance between these electrodes as a function of depth.')
        b1 = seqg('The {0} does this by lowering into the water (until completely submerged) a pair of {1} metallic cylinders at the end of a cable and taking data to determine the resistance between these electrodes as a function of depth.'.format(sci, concentric))
        b2 = seqg('The {0} does this by lowering a pair of {1} metallic cylinders into the water (until completely submerged) at the end of a cable and taking data to determine the resistance between these electrodes as a function of depth.'.format(sci, concentric))
        b3 = seqg('To carry out their experiment, the {0} lowers into the water (until completely submerged) a pair of {1} metallic cylinders at the end of a cable and records data to determine the resistance between these electrodes as a function of depth.'.format(sci, concentric))
        b4 = seqg('The {0} does this by lowering into the water a pair of {1} metallic cylinders at the end of a cable until they are completely submerged. The {0} then records data to determine the resistance between these electrodes as a function of depth.'.format(sci, concentric))
        b5 = seqg('The {0} does this by lowering into the water a pair of {1} metallic cylinders at the end of a cable until they are completely submerged, and then the {0} records data to determine the resistance between these electrodes as a function of depth.'.format(sci, concentric))
        b6 = seqg('The {0} does this by lowering a pair of {1} metallic cylinders into the water at the end of a cable until they are completely submerged. The {0} then records data to determine the resistance between these electrodes as a function of depth.'.format(sci, concentric))
        b7 = seqg('To carry out their experiment, the {0} lowers into the water a pair of {1} metallic cylinders at the end of a cable until they are completely submerged. The {0} records data to determine the resistance between these electrodes as a function of depth.'.format(sci, concentric))
        b8 = seqg('The {0} does this by lowering a pair of {1} metallic cylinders into the water at the end of a cable until they are completely submerged, and then records data to determine the resistance between these electrodes as a function of depth.'.format(sci, concentric))
        b9 = seqg('To carry out their experiment, the {0} lowers into the water a pair of {1} metallic cylinders at the end of a cable until they are completely submerged, and then records data to determine the resistance between these electrodes as a function of depth.'.format(sci, concentric))
        b10 = seqg('To carry out their experiment, the {0} lowers a pair of {1} metallic cylinders at the end of a cable into the water until they are completely submerged, and then records data to determine the resistance between these electrodes as a function of depth.'.format(sci, concentric))
        b11 = seqg('To carry out their experiment, the {0} lowers a pair of {1} metallic cylinders at the end of a cable into the water until they are completely submerged. The {0} records data to determine the resistance between these electrodes as a function of depth.'.format(sci, concentric))
        b_part = choiceg(b0, b1, b2,b3,b4,b5,b6,b7,b8,b9,b10,b11)

        aa = Eq(a, a_val)
        bb = Eq(b, b_val)

        c0 = seqg('The water between the two cylinders forms a cylindrical shell of inner radius',a, '=',str(a_val)+', outer radius',b,'=',str(b_val)+', and length',l,'much larger than',str(b_val)+'.')
        c1 = seqg('The water between the two cylinders forms a cylindrical shell of inner radius {0}, outer radius {1}, and length {2} much larger than {3}.'.format(aa, bb, l,b_val))
        c2 = seqg('The water between the two cylinders forms a cylindrical shell of outer radius {1}, inner radius {0}, and length {2} much larger than {3}.'.format(aa, bb, l, b_val))
        c3 = seqg('The water between the two cylinders forms a cylindrical shell of length {2}, inner radius {0}, and outer radius {1}. {2} >> {3}.'.format(aa, bb, l, b_val))
        c4 = seqg('The water between the two cylinders forms a cylindrical shell of length {2}, inner radius {0}, and outer radius {1}. Length {2} is much larger than {3}.'.format(aa, bb, l,b_val))
        c5 = seqg('The water between the two cylinders forms a cylindrical shell of length {2}, outer radius {1}, and inner radius {0}. {2} >> {3}.'.format(aa, bb, l, b_val))
        c6 = seqg('The water between the two cylinders forms a cylindrical shell of length {2}, outer radius {1}, and inner radius {0}. Length {2} is much larger than {3}.'.format(aa, bb, l, b_val))
        c_part = choiceg(c0, c1, c2, c3, c4, c5, c6)


        in_out = choiceg('inner and outer', 'outer and inner')

        d0 = seqg('The',sci,'applies a potential difference Δ'+str(v),'between the',in_out,'surfaces of the cylinders, producing an outward radial current',str(i)+'.')
        d1 = seqg('The {3} applies a potential difference Δ{0} between the {2} surfaces of the {4}, producing an outward radial current {1}.'.format(v, i, in_out,sci, cylinders))
        d2 = seqg('The {3} applies a potential difference of Δ{0} between the {2} surfaces of the {4}, producing an outward radial current {1}.'.format(v, i, in_out,sci, cylinders))
        d3 = seqg('The {3} applies a potential difference Δ{0} between the {2} surfaces of the {4}, producing an outward radial current {1}.'.format(v, i, in_out, sci, cylinders))
        d4 = seqg('A potential difference Δ{0} is applied between the {2} surfaces of the {3}, producing an outward radial current {1}.'.format(v, i, in_out, cylinders))
        d5 = seqg('A potential difference Δ{0} {3} applied between the {2} surfaces of the {4} produces an outward radial current {1}.'.format(v, i, in_out, thats, cylinders))
        d6 = seqg('A potential difference Δ{0} {3} applied between the {2} surfaces of the {4} produces a current {1} {3} directed radially outward.'.format(v, i, in_out, thats, cylinders))
        d7 = seqg('A current {1} directed radially outward is produced by a potential difference Δ{0} {3} applied between the {2} surfaces of the {4}.'.format(v, i, in_out, thats, cylinders))
        d8 = seqg('A current {1} directed radially outward is produced by a potential difference Δ{0} {3} that is applied between the {2} surfaces of the {4} by the {5}.'.format(v, i, in_out, thats, cylinders, sci))
        d9 = seqg('A current {1} directed radially outward is produced by a potential difference Δ{0} {3} that is applied by the {5} between the {2} surfaces of the {4}.'.format(v, i, in_out, thats, cylinders, sci))
        d10 = seqg('A current {1} is produced by a potential difference Δ{0} {3} applied between the {2} surfaces of the {4} and is directed radially outward.'.format(v, i, in_out, thats, cylinders))
        d11 = seqg('A current {1} is produced by a potential difference Δ{0} {3} applied between the {2} surfaces of the {4}. The current {1} is directed radially outward.'.format(v, i, in_out, thats, cylinders))
        d_part = choiceg(d0, d1, d2, d3, d4, d5, d6,d7,d8, d9,d10, d11)

        e0 = seqg('Let',p,'represent the resistivity of the water.')
        e1 = seqg('Let {0} represent the resistivity of the water.'.format(p))
        e2 = seqg('{0} represents the resistivity of the water.'.format(p))
        e3 = seqg('The resistivity of the water is represented by {0}.'.format(p))
        e4 = seqg('The variable {0} represents the resistivity of the water.'.format(p))
        e_part = choiceg(e0, e1, e2, e3, e4)


        ord1 = seqg(perg(seqg(str(l) + ','), seqg(a,'= ' +str(a_val)+','),seqg(b,'= '+str(b_val)+',')), seqg('and', p))
        ord2 = seqg(perg(seqg(str(l) + ','), seqg(str(p) + ','), seqg(b, '= ' + str(b_val) + ',')),seqg('and', a, '= ' + str(a_val)+'.'))
        ord3 = seqg(perg(seqg(str(l) + ','), seqg(str(p) + ','), seqg(a, '= ' + str(a_val) + ',')),seqg('and', b, '= ' + str(b_val) + '.'))
        ord4 = seqg(perg(seqg(str(p) + ','), seqg(a, '= ' + str(a_val) + ','), seqg(b, '= ' + str(b_val) + ',')),seqg('and', l))
        order = choiceg(ord1, ord2, ord3, ord4)

        calc = choiceg('Calculate', 'Find', 'Compute', 'Derive an equation for', 'Derive an expression for')
        calc1 = choiceg('calculate', 'find', 'compute', 'derive an equation for', 'derive an expression for')
        terms = choiceg('in terms of', 'in terms of the following variables:', 'using', 'using the following variables', 'with respect to', 'with respect to the following variables')

        f0 = seqg(calc,'the resistance of the water between the',cylinders,terms,order)
        f1 = seqg('{0} the resistance of the water between the {1} {2} {3}.'.format(calc, cylinders, terms, order))
        f2 = seqg('For the area between the {0} {1} the resistance of the water {2} {3}.'.format(cylinders, calc1,terms, order))
        f3 = seqg('For the area between the {0} {1} the resistance of the water {2} {3}.'.format(cylinders, calc1,terms, order))
        f4 = seqg('{0} the resistance of the water between the {1} {2} {3}.'.format(calc, cylinders,terms, order))
        f5 = seqg('What is the resistance of the water between the {0}? Express your answer {1} {2}'.format(cylinders, terms, order))
        f6 = seqg('In terms of {0}, {1} the resistance of the water between the {2}.'.format(order, calc1, cylinders))
        f7 = seqg('Using the variables {0}, {1} the resistance of the water between the {2}.'.format(order, calc1, cylinders))
        f_part = choiceg(f0, f1, f2, f3, f4, f5, f6, f7)

        q = seqg(a_part, b_part, c_part, d_part, e_part, f_part)

        return q

    def A(s, d_val, a_val, b_val, a,b,l,v,i,p):
        '''
        We use the electric force equation for point charges to solve for the electric field.
        Important Note: first variables are the not consistent variables followed
        by the consistent ones. See sample QA example if you need too.
        '''
        seqg, perg, choiceg = s.seqg, s.perg, s.choiceg

        dR = symbols('dR')
        r = symbols('r')
        pi = np.pi
        dr = symbols('dr')
        Eq = (dR, p/(2*pi*l)*dr/r)
        dl = p/(2*pi*l)
        resist = symbols('R')
        resistance = dl*ln(b_val/a_val)

        answer1 = seqg('The resistance is', resistance)

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