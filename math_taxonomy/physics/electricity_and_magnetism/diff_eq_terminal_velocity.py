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
        self.description = 'There are two conducting rails separated by a distance w. At one end there is a battery which can maintain an emf e. A bar of mass m is connected to the rails. The bar conducts current between the two rails and has resistance r. It moves along the rails in the ⟨+i⟩ direction. There is a uniform magnetic field b everywhere between the rails and is directed in the ⟨+j⟩ direction. One can find a differential equation involving v(t) and dv(t)/dt if they set v(0)=0, and look for a solution of the form x+ye^(−zt), where x, y, and z are constants. From this differential equation, find the terminal speed u that the bar will approach.'

        # keywords about the question that could help to make this more searchable in the future
        self.keywords = ['physics', 'electricity and magnetism', 'differential equation']
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
            w, e, m, r, b,v, x, y, z, u = symbols('w e m r b v x y z u')
        else:
            w, e, m, r, b, v, x, y, z, u = self.get_symbols(10)
        return w, e, m, r, b, v, x,y,z, u

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
            dir_val, dir_val2 = 0, 0
        else:

            dir_val = np.random.randint(0,5)
            dir_val2 = np.random.randint(0,3)

        return dir_val, dir_val2

    def Q(s, dir_val, dir_val2, w, e, m, r, b, v,x,y,z, u):
        '''
        Important Note: first variables are the not consistent variables followed
        by the consistent ones. See sample QA example if you need too.
        '''
        #define some short cuts
        seqg, perg, choiceg = s.seqg, s.perg, s.choiceg

        dir1 = ['⟨+i⟩', '⟨+j⟩', '⟨+k⟩', '⟨-i⟩', '⟨-j⟩', '⟨-k⟩']
        direction_mag = [['⟨+j⟩','⟨+k⟩','⟨-j⟩','⟨-k⟩'],['⟨+i⟩','⟨+k⟩','⟨-i⟩','⟨-k⟩'],['⟨+i⟩','⟨+j⟩','⟨-i⟩','⟨-j⟩']]

        if dir_val > 2:
            dir_val_alt = dir_val - 3
        else:
            dir_val_alt = dir_val

        dir2 = direction_mag[dir_val_alt]

        wit = choiceg('which can maintain', 'with', 'which has', 'that has')

        pre1 = seqg('There are two conducting rails separated by a distance',str(w) + '. At one end there is a battery',wit,'an emf',str(e) + '.')
        pre2 = seqg('There are two conducting rails separated by a distance',str(w)+'; at one end there is a battery',wit,'an emf',str(e) + '.')
        pre3 = seqg('Consider two conducting rails separated by a distance',str(w)+'. At one end there is a battery',wit,'an emf',str(e) + '.')
        pre4 = seqg('Consider two conducting rails separated by a distance',str(w)+', and at one end there is a battery',wit,'an emf',str(e) + '.')
        pre5 = seqg('There are two conducting rails separated by a distance',str(w)+', and at one end there is a battery',wit,'an emf',str(e) + '.')

        a1 = seqg('A bar of mass',m,'is connected to the rails.')
        a2 = seqg('A bar is connected to the rails and is of mass', str(m) + '.')
        a3 = seqg('A bar is connected to the rails and has mass', str(m) + '.')
        a4 = seqg('A bar connected to the rails has mass', str(m) + '.')

        b1_a = seqg('The bar conducts current between the two rails and has resistance',str(r)+'. It moves along the rails in the',dir1[dir_val],'direction.')
        b1_b = seqg('The bar moves along the rails in the', dir1[dir_val], 'direction and conducts current between the two rails. It has resistance', str(r) + '.')
        b1_c = seqg('There is a uniform magnetic field',b,'everywhere between the rails and is directed in the',dir2[dir_val2],'direction.')
        b1_1 = choiceg(b1_a, b1_b)
        b1 = perg(b1_1, b1_c)

        cap = choiceg('find', 'compute', 'solve for', 'derive')

        c1 = seqg('One can',cap, 'a differential equation involving', str(v) +'(t) and d' +str(v) + '(t)/dt if they set',str(v) + '(0)=0, and look for a solution of the form', str(x)+'+'+str(y)+'e^(−'+str(z)+'t), where '+str(x)+', '+str(y)+', and ' + str(z),'are constants. From this differential equation,',cap,'the terminal speed',u,'that the bar will approach.')
        c2 = seqg('One can {4} a differential equation involving {0}(t) and d{0}(t)/dt if they set {0}(0)=0, and look for a solution of the form {1}+{2}e^(−{3}t), where {1}, {3}, and {2} are constants. From this differential equation {4} the terminal speed {5} that the bar will approach.'.format(v, x, y, z,cap,u))
        c3 = seqg('One can {4} a differential equation involving {0}(t) and d{0}(t)/dt if they set {0}(0)=0, and look for a solution of the form {1}+{2}e^(−{3}t), where {3}, {2}, and {1} are constants. From this differential equation {4} the terminal speed {5} that the bar will approach.'.format(v, x, y, z,cap,u))
        c4 = seqg('One can {4} a differential equation involving {0}(t) and d{0}(t)/dt if they set {0}(0)=0, and look for a solution of the form {1}+{2}e^(−{3}t), where {3}, {1}, and {2} are constants. From this differential equation {4} the terminal speed {5} that the bar will approach.'.format(v, x, y, z,cap,u))
        c5 = seqg('One can {4} a differential equation involving {0}(t) and d{0}(t)/dt if they set {0}(0)=0, and look for a solution of the form {1}+{2}e^(−{3}t), where {2}, {1}, and {3} are constants. From this differential equation {4} the terminal speed {5} that the bar will approach.'.format(v, x, y, z,cap,u))
        c6 = seqg('One can {4} a differential equation involving {0}(t) and d{0}(t)/dt if they set {0}(0)=0, and look for a solution of the form {1}+{2}e^(−{3}t), where {2}, {3}, and {1} are constants. From this differential equation {4} the terminal speed {5} that the bar will approach.'.format(v, x, y, z,cap,u))

        q1 = seqg(pre1, a1, b1, c1)
        q2 = seqg(pre1, a1, b1, c2)
        q3 = seqg(pre1, a1, b1, c3)
        q4 = seqg(pre1, a1, b1, c4)
        q5 = seqg(pre1, a1, b1, c5)
        q6 = seqg(pre1, a1, b1, c6)
        q7 = seqg(pre2, a1, b1, c1)
        q8 = seqg(pre2, a1, b1, c2)
        q9 = seqg(pre2, a1, b1, c3)
        q10= seqg(pre2, a1, b1, c4)
        q11= seqg(pre2, a1, b1, c5)
        q12= seqg(pre2, a1, b1, c6)
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
        q61= seqg(pre1, a3, b1, c1)
        q62= seqg(pre1, a3, b1, c2)
        q63= seqg(pre1, a3, b1, c3)
        q64= seqg(pre1, a3, b1, c4)
        q65= seqg(pre1, a3, b1, c5)
        q66= seqg(pre1, a3, b1, c6)
        q67= seqg(pre2, a3, b1, c1)
        q68= seqg(pre2, a3, b1, c2)
        q69= seqg(pre2, a3, b1, c3)
        q70= seqg(pre2, a3, b1, c4)
        q71= seqg(pre2, a3, b1, c5)
        q72= seqg(pre2, a3, b1, c6)
        q73= seqg(pre3, a3, b1, c1)
        q74= seqg(pre3, a3, b1, c2)
        q75= seqg(pre3, a3, b1, c3)
        q76= seqg(pre3, a3, b1, c4)
        q77= seqg(pre3, a3, b1, c5)
        q78= seqg(pre3, a3, b1, c6)
        q79= seqg(pre4, a3, b1, c1)
        q80= seqg(pre4, a3, b1, c2)
        q81= seqg(pre4, a3, b1, c3)
        q82= seqg(pre4, a3, b1, c4)
        q83= seqg(pre4, a3, b1, c5)
        q84= seqg(pre4, a3, b1, c6)
        q85= seqg(pre5, a3, b1, c1)
        q86= seqg(pre5, a3, b1, c2)
        q87= seqg(pre5, a3, b1, c3)
        q88= seqg(pre5, a3, b1, c4)
        q89= seqg(pre5, a3, b1, c5)
        q90= seqg(pre5, a3, b1, c6)
        q91= seqg(pre1, a4, b1, c1)
        q92= seqg(pre1, a4, b1, c2)
        q93= seqg(pre1, a4, b1, c3)
        q94= seqg(pre1, a4, b1, c4)
        q95= seqg(pre1, a4, b1, c5)
        q96= seqg(pre1, a4, b1, c6)
        q97= seqg(pre2, a4, b1, c1)
        q98= seqg(pre2, a4, b1, c2)
        q99= seqg(pre2, a4, b1, c3)
        q100=seqg(pre2, a4, b1, c4)
        q101=seqg(pre2, a4, b1, c5)
        q102=seqg(pre2, a4, b1, c6)
        q103=seqg(pre3, a4, b1, c1)
        q104=seqg(pre3, a4, b1, c2)
        q105=seqg(pre3, a4, b1, c3)
        q106=seqg(pre3, a4, b1, c4)
        q107=seqg(pre3, a4, b1, c5)
        q108=seqg(pre3, a4, b1, c6)
        q109=seqg(pre4, a4, b1, c1)
        q110=seqg(pre4, a4, b1, c2)
        q111=seqg(pre4, a4, b1, c3)
        q112=seqg(pre4, a4, b1, c4)
        q113=seqg(pre4, a4, b1, c5)
        q114=seqg(pre4, a4, b1, c6)
        q115=seqg(pre5, a4, b1, c1)
        q116=seqg(pre5, a4, b1, c2)
        q117=seqg(pre5, a4, b1, c3)
        q118=seqg(pre5, a4, b1, c4)
        q119=seqg(pre5, a4, b1, c5)
        q120=seqg(pre5, a4, b1, c6)

        q = choiceg(q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20, q21, q22, q23, q24, q25, q26, q27, q28, q29, q30, q31, q32, q33, q34, q35, q36, q37, q38, q39, q40, q41, q42, q43, q44, q45, q46, q47, q48, q49, q50, q51, q52, q53, q54, q55, q56, q57, q58, q59, q60, q61, q62, q63, q64, q65, q66, q67, q68, q69, q70, q71, q72, q73, q74, q75, q76, q77, q78, q79, q80, q81, q82, q83, q84, q85, q86, q87, q88, q89, q90, q91, q92, q93, q94, q95, q96, q97, q98, q99, q100, q101, q102, q103, q104, q105, q106, q107, q108, q109, q110, q111, q112, q113, q114, q115, q116, q117, q118, q119, q120)
        return q

    def A(s,dir_val,dir_val2, w, e, m, r, b, v,x,y,z, u):
        '''
        Important Note: first variables are the not consistent variables followed
        by the consistent ones. See sample QA example if you need too.
        '''
        seqg, perg, choiceg = s.seqg, s.perg, s.choiceg


        pi = np.pi
        mu_0 = 4*pi*(10**-7)
        d_flux = b*v*w
        emf1 = Eq(e, -d_flux)
        emf2 = Eq(-d_flux, e)
        emf = choiceg(emf1, emf2)

        I = symbols('I')
        I_1 = e/r
        I_induced = -d_flux/r
        currentI = I_1 + I_induced
        current1 = Eq(I, currentI)
        current2 = Eq(currentI, I)
        current = choiceg(current1, current2)

        F = symbols('F')
        force = currentI*w*b

        t = symbols('t')
        e_val = 2.718281828459045
        Eq(force, -z*m*b*(e_val**(-z*t)))
        Eq(e, x*w*b)
        x_val = solve(e - x*w*b, x)
        y_val = solve(-e - y*w*b,y)
        eq_1 = z*m
        eq_2 = -(w**2)*(b**2)/r
        z_val = solve(eq_1 + eq_2, z)

        v_term1 = Eq(u, e/(w*b))
        v_term2 = Eq(e/(w*b), u)
        v_term = choiceg(v_term1,v_term2)


        in1 = seqg('The terminal velocity is',v_term)
        in2 = seqg('The equation for the terminal velocity of the bar is',v_term)
        in3 = seqg('The terminal velocity',u,'of the bar will approach',v_term)
        in4 = seqg('The terminal velocity of the bar approaches',v_term)
        in5 = seqg(v_term,'is the terminal velocity of the bar.')
        in6 = seqg(v_term,'is the terminal velocity that the bar approaches.')


        a = choiceg(in1, in2, in3, in4, in5, in6)
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