from sympy import *
import random
import numpy as np
from faker import Factory

from qagen import *

register_random_seeding_funcs(random.seed,np.seed,)

# Mary had x=10 lambs, y=9 goats, z=8 dogs and each was decreased by a=2 units
# by the wolf named Gary. How many of each are there left?

def qa_example_replacements(seed=1):
    #pre-code for question
    x,y,z = consistent_variable(Symbols('x,y,z'))
    x_val, y_val, z_val = numpy.randint(1,100,[3])
    Mary = consistent_variable(fake.name)
    Gary = consistent_variable(fake.name)
    # define question
    permutable_part = permg()
    question = seqg(Mary+'had',
    permutable_part,'and each was decreased by',decreased_amount,
    'by the wolf named '+Gary+'.')
    #pre-code for answer

    #answer
    permutable_part =
    ans_vnl_vsympy = seqg(Mary+'has',
    permutable_part,'and each was decreased by the wolf named '+Gary+'.')
    question = choiceg()



if __name__ == '__main__':
    seed = random.randint(1,10)
    print('seed = ', seed)
    example_replacements(seed)
