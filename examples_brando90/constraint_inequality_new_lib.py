from sympy import *
import random
import numpy as np
from faker import Factory

fake = Factory.create()

from qagen import *
#import qagen

# Mary had x=10 lambs, y=9 goats, z=8 dogs and each was decreased by d=2 units
# by the wolf named Gary. How many of each are there left?

def get_symbols():
    letters = get_list_sympy_variables()
    x,y,z,d = symbols( random.sample(letters,4) )
    return x,y,z,d

class QA_constraint(QAGen):

    def __init__(self):
        super().__init__()
        self.author = 'Brando Miranda'
        self.description = ''' Mary had x=10, y=9, z=8, goats, lambs, dogs, and each was decreased by d=2 units
        by the wolf named Gary. How many of each are there left?'''
        # keywords about the question that could help to make this more searchable in the future
        self.keywords = ['basic algebra']
        self.use_latex = True

    def seed_all(self,seed):
        random.seed(seed)
        np.random.seed(seed)
        fake.random.seed(seed)

    def init_consistent_qa_variables(self):
        if self.debug:
            x,y,z,d = symbols('x y z d')
            Mary, Gary = 'Mary', 'Gary'
            goats,lambs,dogs = 'goats','lambs','dogs'
        else:
            x,y,z,d = self.get_symbols(4)
            Mary, Gary = self.get_names(2)
            farm_animals = utils.get_farm_animals()
            goats,lambs,dogs = self.get_names(self,3, names=farm_animals)
        return x,y,z,d,Mary,Gary,goats,lambs,dogs

    def init_qa_variables(self):
        if self.debug:
            x_val,y_val,z_val = 2,3,4
            d_val = 1
        else:
            x_val,y_val,z_val = np.random.randint(1,1000,[3])
            d_val = np.random.randint(1,np.min([x_val,y_val,z_val]))
        return x_val,y_val,z_val,d_val

    def Q(s, x_val,y_val,z_val,d_val, x,y,z,d,Mary,Gary,goats,lambs,dogs):
        #define some short cuts
        seqg, perg, choiceg = s.seqg, s.perg, s.choiceg
        #
        permutable_part = s.perg(seqg(Eq(x,x_val),','),Eq(y,y_val),Eq(z,z_val))
        animal_list = s.seqg(goats, lambs, dogs)
        question1 = s.seqg(Mary+' had ',
        permutable_part, animal_list,' respectively. Each was decreased by',Eq(d,d_val),'by the wolf named '+Gary+'.')
        q = s.choiceg(question1)
        return q

    def A(s, x_val,y_val,z_val,d_val, x,y,z,d,Mary,Gary,goats,lambs,dogs):
        #define some short cuts
        seqg, perg, choiceg = s.seqg, s.perg, s.choiceg
        #
        permutable_part = s.perg(Eq(x-d,x_val-d_val),Eq(y-d,y_val-d_val),Eq(z-d,z_val-d_val))
        animal_list = s.seqg( goats, lambs, dogs)
        ans_vnl_vsympy = s.seqg(Mary+' has ',permutable_part, animal_list, 'left and each was decreased by the wolf named '+Gary+'.')
        ans_vnl_vsympy2 = s.seqg('The wolf named '+Gary+' decreased each of '+Mary+'\'s sheep and she now has ',permutable_part,' sheep left.')
        a = s.choiceg(ans_vnl_vsympy,ans_vnl_vsympy2)
        return a

    ##

    def get_qa(self,seed):
        # set seed
        self.seed_all(seed)
        # get variables
        variables_consistent = self.init_consistent_qa_variables()
        print('variables_consistent = ',variables_consistent)
        variables = self.init_qa_variables()
        print('variables = ',variables)
        # get qa
        q_str = self.Q(*variables,*variables_consistent)
        a_str = self.A(*variables,*variables_consistent)
        return q_str, a_str

##

def check_single_question(qagenerator):
    qagenerator.debug = True
    q,a = qagenerator.get_qa(1)
    print('qagenerator.debug = ', qagenerator.debug)
    print('q: ', q)
    print('a: ', a)

def check_mc(qagenerator):
    for seed in range(3):
        q_str, ans_list = qagenerator.generate_MC(nb_answers=3,seed=seed)
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
    #check_mc(qagenerator)
    #check_many_to_one(qagenerator)
    #check_one_to_many(qagenerator)
    #check_many_to_one_consistent_format(qagenerator)
