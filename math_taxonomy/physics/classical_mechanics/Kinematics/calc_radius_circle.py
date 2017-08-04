from sympy import *
import random
import numpy as np

from qagen.qagen import *
from qagen import utils
from qagen import unit_test_for_user as user_test

# TODO: You can also put your quesiton example here

class QA_constraint(QAGen):

    def __init__(self):
        '''
        Initializer for your QA question.
        '''
        super().__init__()
        self.author = 'Elaheh Ahmadi'
        self.description = ' A drum of radius R rolls down a slope without slipping. Its axis has acceleration a ' \
                           'parallel to the slope. What is the drum’s angular acceleration α?'
        # keywords about the question that could help to make this more searchable in the future
        self.keywords = ['Physics', 'Kinematics', 'Classical mechanics', 'Gravitational Acceleration', 'Time', 'Object',
                         'Plane', 'Block', 'Drum', 'Roll', 'Slope']
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
            R, a, alpha = symbols('R a alpha')
        else:
            R = symbols(random.choice(['R', 'r']))
            a = symbols('a')
            alpha = symbols(chr(954))
        return R, a, alpha

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
            a_val, alpha_val = 2, 1
        else:
            a_val, alpha_val = np.random.randint(1, 100000, 2)/10
        return a_val, alpha_val

    def Q(s, a_val, alpha_val, R, a, alpha): #TODO change the signature of the function according to your question
        '''
        A drum of radius R rolls down a slope without slipping. Its angular acceleration is  α.
        What is the acceleration of its axis?

        Important Note: first variables are the not consistent variables followed
        by the consistent ones. See sample QA example if you need too.
        '''
        #define some short cuts
        seqg, perg, choiceg = s.seqg, s.perg, s.choiceg
        angular_acc_sentence = seqg('its angular acceleration is {0} = {1} (1/s^2)'.format(alpha, alpha_val))
        linear_acc_sentence_V1 = seqg('its linear acceleration is {0} = {1} (m/s^2)'.format(a, a_val))
        linear_acc_sentence_V2 = seqg('its axis has acceleration {0}  = {1} (m/s^2)'.format(a, a_val))
        info_V1 = seqg(' A drum of radius {0} rolls down a slope without slipping', angular_acc_sentence, '. And,'
                       , linear_acc_sentence_V1)
        info_V2 = seqg('A circle is rolling without slipping with ', angular_acc_sentence, '. And,'
                       , linear_acc_sentence_V1)
        info_V3 = seqg('A wheel is rolling without slipping with ', angular_acc_sentence, '. And,'
                       , linear_acc_sentence_V1)
        info_V4 = seqg('A wheel is rolling without slipping with  ', angular_acc_sentence, '. And,'
                       , linear_acc_sentence_V1)
        info_V5 = seqg(' A drum of radius {0} rolls down a slope without slipping', linear_acc_sentence_V1, '. And,'
                       , angular_acc_sentence)
        info_V6 = seqg('A circle is rolling without slipping with ', linear_acc_sentence_V1, '. And,'
                       , angular_acc_sentence)
        info_V7 = seqg('A wheel is rolling without slipping with ', linear_acc_sentence_V1, '. And,'
                       , angular_acc_sentence)
        info_V8 = seqg('A wheel is rolling without slipping with  ', linear_acc_sentence_V1, '. And,'
                       , angular_acc_sentence)
        info_V9 = seqg(' A drum of radius {0} rolls down a slope without slipping', angular_acc_sentence, '. And,'
                       , linear_acc_sentence_V2)
        info_V10 = seqg('A circle is rolling without slipping with ', angular_acc_sentence, '. And,'
                       , linear_acc_sentence_V2)
        info_V11 = seqg('A wheel is rolling without slipping with ', angular_acc_sentence, '. And,'
                       , linear_acc_sentence_V2)
        info_V12 = seqg('A wheel is rolling without slipping with  ', angular_acc_sentence, '. And,'
                       , linear_acc_sentence_V2)
        info_V13 = seqg(' A drum of radius {0} rolls down a slope without slipping', linear_acc_sentence_V2, '. And,'
                       , angular_acc_sentence)
        info_V1 = seqg('A circle is rolling without slipping with ', linear_acc_sentence_V2, '. And,'
                       , angular_acc_sentence)
        info_V7 = seqg('A wheel is rolling without slipping with ', linear_acc_sentence_V2, '. And,'
                       , angular_acc_sentence)
        info_V8 = seqg('A wheel is rolling without slipping with  ', linear_acc_sentence_V2, '. And,'
                       , angular_acc_sentence)
        wanted_V1 = seqg('Find the radius {0} of the object.'.format(R))
        wanted_V2 = seqg('Calculate the radius {0} of the object .'.format(R))
        wanted_V3 = seqg('What is the object radius {0}.'.format(R))
        question_V1 = seqg(info_V1, wanted_V1)
        question_V2 = seqg(info_V1, wanted_V2)
        question_V3 = seqg(info_V1, wanted_V3)
        question_V4 = seqg(info_V2, wanted_V1)
        question_V5 = seqg(info_V2, wanted_V2)
        question_V6 = seqg(info_V2, wanted_V3)
        question_V7 = seqg(info_V3, wanted_V1)
        question_V8 = seqg(info_V3, wanted_V2)
        question_V9 = seqg(info_V3, wanted_V3)
        question_V10 = seqg(info_V4, wanted_V1)
        question_V11 = seqg(info_V4, wanted_V2)
        question_V12 = seqg(info_V4, wanted_V3)
        question_V13 = seqg(info_V5, wanted_V1)
        question_V14 = seqg(info_V5, wanted_V2)
        question_V15 = seqg(info_V5, wanted_V3)
        question_V16 = seqg(info_V6, wanted_V1)
        question_V17 = seqg(info_V6, wanted_V2)
        question_V18 = seqg(info_V6, wanted_V3)
        question_V19 = seqg(info_V7, wanted_V1)
        question_V20 = seqg(info_V7, wanted_V2)
        question_V21 = seqg(info_V7, wanted_V3)
        question_V22 = seqg(info_V8, wanted_V1)
        question_V23 = seqg(info_V8, wanted_V2)
        question_V24 = seqg(info_V8, wanted_V3)
        q = choiceg(question_V1, question_V2,question_V3, question_V4, question_V5, question_V6, question_V7,
                    question_V8, question_V9, question_V10, question_V11, question_V12, question_V13, question_V14,
                    question_V15, question_V16, question_V17, question_V18, question_V19, question_V20, question_V21,
                    question_V22, question_V23, question_V24)
        return q

    def A(s,a_val, alpha_val, R, a, alpha): #TODO change the signature of the function according to your answer
        '''
        a = R*alpha

        Important Note: first variables are the not consistent variables followed
        by the consistent ones. See sample QA example if you need too.
        '''
        #define some short cuts
        seqg, perg, choiceg = s.seqg, s.perg, s.choiceg
        R_val =  a_val/ alpha_val
        R_val_eq = seqg('{0}/{1}'.format(a, alpha))
        answer_V1 = R_val
        answer_V2 = seqg('{0} = {1} = {2} (m/s^2)'.format(R, R_val_eq, R_val))
        answer_V3 = seqg('We can find the linear acceleration via {0} = {1} na after using the given values {0} = {2} '
                         '(m/s^2)'.format(R, R_val_eq, R_val))
        a = choiceg(answer_V1, answer_V2, answer_V3)
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
    ## uncomment the following to check formats:
    #check_mc(qagenerator)
    #check_many_to_one(qagenerator)
    #check_one_to_many(qagenerator)
    #check_many_to_one_consistent_format(qagenerator)
    ## run unit test given by framework
    user_test.run_unit_test_for_user(QA_constraint)