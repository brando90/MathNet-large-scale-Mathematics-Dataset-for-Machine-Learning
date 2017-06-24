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


def check_for_duplicates(args1,arg2):
    '''
    Check for dulplicates between and within lists

    [1,2,3],[] -> False
    [1,1,1,2],[] -> True
    [1,2,3],[1,2,3] -> True
    '''
    # if length of joint list decreases, then there is some duplicate (either btw the lists or within a list)
    # TODO check hairuo, what do we do when both are empty?
    length_all_elements_list = len(set(args1+args2))
    length_all_elements_set = len(args1+args2)
    return length_all_elements_set < length_all_elements_list

def make_strings_to_single_spaced(inp_string):
    # TODO
    list_words = inp_string.split(sep=' ') # Return a list of the words in the string, using sep as the delimiter string.
    string_single_spaces = ' '.join(list_words)
    return string_single_spaces
