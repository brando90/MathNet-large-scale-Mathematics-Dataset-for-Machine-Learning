from sympy import *
import random
import collections
import string

import pdb

# def get_list_sympy_variables():
#     '''
#
#     '''
#     #TODO maybe extend this to provide greek letters too? latex?
#     letters = list(string.ascii_letters)
#     " ".join(letters)
#     return letters

def get_farm_animals():
    '''
    Returns a lisk for farm animal.

    '''
    farm_animals = ['goats','lambs','dogs','cats','ducks','chicken','hen','pigs',
    'horses','donkeys','rabbits','guinea pigs','gooses','sheeps','piglets'
    ,'bulls','stallions','rams','cows','calfs','trukey']
    return farm_animals
