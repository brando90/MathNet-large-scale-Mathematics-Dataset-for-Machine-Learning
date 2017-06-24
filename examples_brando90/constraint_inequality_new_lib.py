from sympy import *
import random
import numpy as np

from qagen import *
from qagen import utils

# Mary had x=10 lambs, y=9 goats, z=8 dogs and each was decreased by d=2 units
# by the wolf named Gary. How many of each are there left?

class QA_constraint(QAGen):

    def __init__(self):
        '''
        Initializer for your QA question.
        '''
        super().__init__()
        self.author = 'Brando Miranda'
        self.description = ''' Mary had x=10, y=9, z=8, goats, lambs, dogs, and each was decreased by d=2 units
        by the wolf named Gary. How many of each are there left?'''
        # keywords about the question that could help to make this more searchable in the future
        self.keywords = ['basic algebra']
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
            x,y,z,d = symbols('x y z d')
            Mary, Gary = 'Mary', 'Gary'
            goats,lambs,dogs = 'goats','lambs','dogs'
        else:
            x,y,z,d = self.get_symbols(4)
            Mary, Gary = self.get_names(2)
            farm_animals = utils.get_farm_animals()
            goats,lambs,dogs = self.get_names(3,names_list=farm_animals)
        return x,y,z,d,Mary,Gary,goats,lambs,dogs

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
            x_val,y_val,z_val = 2,3,4
            d_val = 1
        else:
            x_val,y_val,z_val = np.random.randint(1,1000,[3])
            d_val = np.random.randint(1,np.min([x_val,y_val,z_val]))
        return x_val,y_val,z_val,d_val

    def Q(s, x_val,y_val,z_val,d_val, x,y,z,d,Mary,Gary,goats,lambs,dogs):
        '''
        Small question description.

        Important Note: first variables are the not consistent variables followed
        by the consistent ones. See sample QA example if you need too.
        '''
        #define some short cuts
        seqg, perg, choiceg = s.seqg, s.perg, s.choiceg
        #
        permutable_part = perg(seqg(Eq(x,x_val),','),seqg(Eq(y,y_val),','),seqg(Eq(z,z_val),','))
        animal_list = seqg( goats+',', lambs+',', dogs)
        question1 = seqg(Mary+' had ',
        permutable_part, animal_list,' respectively. Each was decreased by',Eq(d,d_val),'by the wolf named '+Gary+'.')
        q = s.choiceg(question1)
        return q

    def A(s, x_val,y_val,z_val,d_val, x,y,z,d,Mary,Gary,goats,lambs,dogs):
        '''
        Small answer description.

        Important Note: first variables are the not consistent variables followed
        by the consistent ones. See sample QA example if you need too.
        '''
        #define some short cuts
        seqg, perg, choiceg = s.seqg, s.perg, s.choiceg
        #
        permutable_part = perg(seqg(Eq(x-d,x_val-d_val),','),seqg(Eq(y-d,y_val-d_val),','),seqg(Eq(z-d,z_val-d_val),','))
        animal_list = seqg( goats+',', lambs+',', dogs)
        ans_vnl_vsympy = seqg(Mary+' has ',permutable_part, animal_list, 'left and each was decreased by the wolf named '+Gary+'.')
        ans_vnl_vsympy2 = seqg('The wolf named '+Gary+' decreased each of '+Mary+'\'s sheep and she now has ',permutable_part,' ',animal_list,' left.')
        a = s.choiceg(ans_vnl_vsympy,ans_vnl_vsympy2)
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

##

def check_single_question(qagenerator):
    #qagenerator.debug = True
    q,a = qagenerator.get_qa(1)
    print('qagenerator.debug = ', qagenerator.debug)
    print('q: ', q)
    print('a: ', a)

def check_mc(qagenerator):
    for seed in range(3):
        q_str, ans_list = qagenerator.generate_single_MC(nb_answers_choices=3,seed=seed)
        print('seed: ',seed)
        print('q_str: ',q_str)
        print('ans_list: ',ans_list)
        print(len(ans_list))

def check_one_to_many(qagenerator):
    for seed in range(3):
        q,a = qagenerator.generate_one_to_many(nb_answers=3,seed=seed)
        print('q: ', q)
        print("\n".join(a))

def check_many_to_one_consis(qagenerator):
    for seed in range(3):
        print()
        q,a = qagenerator.generate_many_to_one(nb_questions=5,seed=seed)
        print("\n".join(q))
        print('a: ', a)
        #print("\n".join(a))

def check_many_to_one_consistent_format(qagenerator):
    nb_different_qa = 3
    seed_output_format = 0
    nb_different_q = 2
    qa_pair_list = qagenerator.generate_many_to_one_consistent_format(nb_different_qa,seed_output_format,nb_different_q=nb_different_q)
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
