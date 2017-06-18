from sympy import *
import random
import numpy as np
from faker import Factory

from qagen import *

register_random_seeding_funcs(random.seed,np.seed,)

# Mary had x=10 lambs, y=9 goats, z=8 dogs and each was decreased by d=2 units
# by the wolf named Gary. How many of each are there left?

def get_symbols():
    letters = get_list_sympy_variables()
    x,y,z,d = random.sample(letters,len(letters))
    return x,y,z,d

def qa_example_replacements():
    #pre-code for question
    x,y,z,d = consistent_variable(get_symbols)
    x_val,y_val,z_val,d_val = numpy.randint(1,100,[4])
    Mary = consistent_variable(fake.name)
    Gary = consistent_variable(fake.name)
    # define question
    permutable_part = permg(Eq(x,x_val),Eq(y,y_val),Eq(z,z_val))
    question = seqg(Mary+'had',
    permutable_part,'and each was decreased by',d,'by the wolf named '+Gary+'.')
    #pre-code for answer

    #answer
    permutable_part = permg(Eq(x-d,x_val-d_val),Eq(y-d,y_val-d_val),Eq(z-d,z_val-d_val))
    ans_vnl_vsympy = seqg(Mary+'has',permutable_part,
    'and each was decreased by the wolf named '+Gary+'.')
    question = choiceg(ans_vnl_vsympy)


if __name__ == '__main__':
    seed = random.randint(1,10)
    print('seed = ', seed)
    example_replacements(seed)
