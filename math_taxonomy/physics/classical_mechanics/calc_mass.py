from sympy import *
import random
import numpy as np

from qagen import *
from qagen import utils
from qagen import unit_test_for_user as user_test

# TODO: You can also put your quesiton example here

class QA_constraint(QAGen):

    def __init__(self):
        '''
        Initializer for your QA question.
        '''
        super().__init__()
        self.author = 'Elaheh Ahmadi' #TODO your full name
        self.description = "Calculating a mass of an object given the total force applied to it and its acceleration"  #TODO example string of your question
        # keywords about the question that could help to make this more searchable in the future
        self.keywords = ['physics' ,'classical mechanics','force', 'mass', 'acceleration'] #TODO keywords to search type of question
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
        fake.random.seed(seed)
        # TODO write more seeding libraries that you are using

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
            force, a = symbols('m a')
        else:
            force, a = self.get_symbols(2)
        return force, a

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
            force_val, a_val = 1, 2
        else:
            dim = np.random.randint(1,100)
            force_val, a_val = round(np.random.randint(-1000000,1000000, dim)/100,1), round(np.random.randint(-1000000, 1000000, dim)/100,1)
        return force_val, a_val

    def Q(s, force_val, a_val, force, a): #TODO change the signature of the function according to your question
        '''
        Finding the mass of an object given the total force applied to it and acceleration.

        Important Note: first variables are the not consistent variables followed
        by the consistent ones. See sample QA example if you need too.
        '''
        #define some short cuts
        seqg, perg, choiceg = s.seqg, s.perg, s.choiceg

        question_1 =  ('Find the mass of an object given the force applied to ', Eq(force, force_val), " (N) and its acceleration ",
                       Eq(a, a_val), " (m/s^2).")
        question_2 = ('There is a mass floating in a multi dimensional world. We know that the total force applied to it is ',
                      Eq(force, force_val), "(N). Also, we observed that its acceleration is, ", Eq(a, a_val),
                      " (m/s^2). Find the mass of this object given these information.")
        question_3 = ('What is the total mass of an object with acceleration ', Eq(a, a_val),
                      " (m/s^2) if the total force applied to it is ", Eq(force, force_val), " (N).")
        question_4 = ('Given the fact that total force applied to a mass is its acceleration times its mass,'
                      ' find the mass of an object when we know the total forced applied to it is ', Eq(force, force_val), "(N), and its acceleration is ",
                      Eq(a, a_val), " (m/s^2).")
        question_5 = ('A spaceship is wondering around in a multi dimensional world. The captain wants to know the'
                      ' mass of the spaceship be able to control it. There are a three physicists '
                      'and mathematicians on the spaceship. They calculated that the total force on the ship is ',
                      Eq(force, force_val), "(N), and its acceleration in the world is, ", Eq(a, a_val),
                      "(m/s^2). Help the captain to control the ship by finding the total mass of the ship.")

        q = choiceg(question_1, question_2, question_3, question_4, question_5)

        return q

    def A(s, force_val, a_val, force, a): #TODO change the signature of the function according to your answer
        '''
        The answer is m = |F|/|a|

        Important Note: first variables are the not consistent variables followed
        by the consistent ones. See sample QA example if you need too.
        '''
        #define some short cuts
        seqg, perg, choiceg = s.seqg, s.perg, s.choiceg
        force_magnitude = np.sqrt(np.dot(force_val, force_val))
        a_magnitude = np.sqrt(np.dot(a_val, a_val))
        ans_val = force_magnitude / a_magnitude
        answer_1 = seqg("The mass of the object is ", ans_val," (kg).")
        answer_2 = seqg("After dividing the magnitude of the total force over the magnitude of the acceleration, "
                        "the mass of the object is equal to ", ans_val,"(kg).")

        # choices, try providing a few
        # these van include variations that are hard to encode with permg or variable substitution
        # example, NL variations or equaiton variations
        a = choiceg(answer_1, answer_2)
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