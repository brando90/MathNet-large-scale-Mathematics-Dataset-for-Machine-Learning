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
        pass

    def seed_all(self,seed):
        random.seed(seed)
        np.random.seed(seed)

    def init_consistent_qa_variables(self):
        x,y,z,d = get_symbols()
        Mary = fake.name()
        Gary = fake.name()
        return x,y,z,d,Mary,Gary

    def init_qa_variables(self):
        x_val,y_val,z_val,d_val = np.random.randint(1,1000,[4])
        return x_val,y_val,z_val,d_val

    def Q(self, x_val,y_val,z_val,d_val, x,y,z,d,Mary,Gary):

        permutable_part = perg(Eq(x,x_val),Eq(y,y_val),Eq(z,z_val))
        question1 = seqg(Mary+'had',
        permutable_part,'and each was decreased by',d,'by the wolf named '+Gary+'.')
        q = choiceg(question1)
        return q

    def A(self, x_val,y_val,z_val,d_val, x,y,z,d,Mary,Gary):
        permutable_part = perg(Eq(x-d,x_val-d_val),Eq(y-d,y_val-d_val),Eq(z-d,z_val-d_val))
        ans_vnl_vsympy = seqg(Mary+'has',permutable_part, 'and each was decreased by the wolf named '+Gary+'.')
        a = choiceg(ans_vnl_vsympy)
        return a

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

if __name__ == '__main__':
    qagenerator = QA_constraint()
    q,a = qagenerator.get_qa(1)
    print('q: ', q)
    print('a: ', a)
    # for seed in range(3):
    #     q_str, ans_list = qagenerator.generate_MC(seed)
    #     print('seed: ',seed)
    #     print('q_str: ',q_str)
    #     print('a_str: ',a_str)
