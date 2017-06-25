from sympy import *
import random
import collections
import string
import re

import pdb

def get_farm_animals():
    '''
    Returns a lisk for farm animal.

    '''
    farm_animals = ['goats','lambs','dogs','cats','ducks','chicken','hen','pigs',
    'horses','donkeys','rabbits','guinea pigs','gooses','sheeps','piglets'
    ,'bulls','stallions','rams','cows','calfs','trukeys']
    return farm_animals

def duplicates_present(args1,args2):
    '''
    Check for dulplicates between and within lists

    [],[] -> True
    [1,2,3],[] -> False
    [1,1,1,2],[] -> True
    [1,2,3],[1,2,3] -> True
    '''
    # if length of joint list decreases, then there is some duplicate (either btw the lists or within a list)
    if len(args1+args2) == 0:
        # TODO check hairuo, what do we do when both are empty?
        # said true cuz if there are duplicates other code will keep trying to
        # generate variables until they aren't empty...could lead to infinite loop?
        return True
    length_all_elements_list = len(args1+args2)
    length_all_elements_set = len(set(args1+args2))
    return length_all_elements_set < length_all_elements_list

def make_strings_to_single_spaced(inp_string):
    '''
    Given a string with potentially double or more spaced, removes them and puts
    single spaces.
    '''
    list_words = inp_string.split() # Return a list of the words in the string, using sep as the delimiter string.
    string_single_spaces = ' '.join(list_words)
    return string_single_spaces
