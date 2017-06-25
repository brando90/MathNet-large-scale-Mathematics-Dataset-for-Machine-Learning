from sympy import *
import random
import numpy as np

from qagen import *

class QA_constraint(QAGen):

    def __init__(self):
        super().__init__()
        self.author = 'Hairuo Guo' 
        self.description = 'Algebra word problem about dividing a sum of money' 
        # keywords about the question that could help to make this more searchable in the future
        self.keywords = ['algebra', 'word problem'] 
        self.use_latex = True

    def seed_all(self,seed):
        random.seed(seed)
        np.random.seed(seed)
        self.fake.random.seed(seed)
        # TODO write more seeding libraries that you are using

    def init_consistent_qa_variables(self):
        if self.debug:
            name1 = 'Bob'
            name2 = 'Alice'
            name3 = 'Tim'
        else:
            name1 = self.get_name()
            name2 = self.get_name()
            name3 = self.get_name()

        return name1, name2, name3

    def init_qa_variables(self):
        if self.debug:
            const1 = 1000 
            const2 = 3
            const3 = 2
        else:
            const1 = np.random.randint(500, 1000)
            const2 = np.random.randint(10)
            const3 = np.random.randint(10)

        return const1, const2, const3

    def Q(s, const1, const2, const3, name1, name2, name3):
        #define some short cuts
        seqg, perg, choiceg = s.seqg, s.perg, s.choiceg
        str1 = 'There are %s dollars split among three people: %s, %s, and %s. '
        str2 = '%s has %s times as many dollars as %s. '
        str3 = '%s has %s times as many dollars as %s. '
        str4 = 'How many dollars does each of them have? '

        str1 = str1 % (const1, name1, name2, name3)
        str2 = str2 % (name2, const2, name1)
        str3 = str3 % (name3, const3, name2)
        
        q_str = seqg(str1, perg(str2, str3), str4) 
        q = choiceg(q_str)
        return q

    def A(s, const1, const2, const3, name1, name2, name3):
        #define some short cuts
        seqg, perg, choiceg = s.seqg, s.perg, s.choiceg
        
        has_str = "%s has %.2f dollars"
        name1_quant = float(const1)/(const2 + const3*const2 + 1)
        name1_has = has_str % (name1, name1_quant)  
        name2_has = has_str % (name2, name1_quant*const2)
        name3_has = has_str % (name3, name1_quant*const2*const3)
        
        a_str = perg(name1_has, name2_has, name3_has) 
         
        a = choiceg(a_str)
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
