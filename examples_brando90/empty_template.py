from sympy import *
import random
import numpy as np

from qagen import *

class QA_constraint(QAGen):

    def __init__(self):
        super().__init__()
        self.author = 'Your username' #TODO
        self.description = '''''' #TODO
        # keywords about the question that could help to make this more searchable in the future
        self.keywords = [''] #TODO
        self.use_latex = True

    def seed_all(self,seed):
        random.seed(seed)
        np.random.seed(seed)
        fake.random.seed(seed)
        # TODO write more seeding libraries that you are using

    def init_consistent_qa_variables(self):
        if self.debug:
            #TODO
        else:
            #TODO
        return x,y,z,d,Mary,Gary,goats,lambs,dogs

    def init_qa_variables(self):
        if self.debug:
            #TODO
        else:
            #TODO
        return x_val,y_val,z_val,d_val

    def Q(s, x_val,y_val,z_val,d_val, x,y,z,d,Mary,Gary,goats,lambs,dogs):
        #define some short cuts
        seqg, perg, choiceg = s.seqg, s.perg, s.choiceg
        # TODO
        #q_format1
        #q_format2
        #...
        # choices
        q = choiceg()
        return q

    def A(s, x_val,y_val,z_val,d_val, x,y,z,d,Mary,Gary,goats,lambs,dogs):
        #define some short cuts
        seqg, perg, choiceg = s.seqg, s.perg, s.choiceg
        # TODO
        #ans_sympy
        #ans_numerical
        #ans_vnl_vsympy1
        #ans_vnl_vsympy2
        #
        a = choiceg()
        return a

    ##

    def get_qa(self,seed):
        '''
        Samples of how questions are formed in general
        '''
        # set seed
        self.seed_all(seed)
        # get variables
        variables_consistent = self.init_consistent_qa_variables()
        #print('variables_consistent = ',variables_consistent)
        variables = self.init_qa_variables()
        #print('variables = ',variables)
        #check_for_duplicates(variables_consistent,variables)
        # get qa
        q_str = self.Q(*variables,*variables_consistent)
        a_str = self.A(*variables,*variables_consistent)
        return q_str, a_str

## Some helper functions to check the formats are coming out well

def check_single_question(qagenerator):
    #qagenerator.debug = True
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
