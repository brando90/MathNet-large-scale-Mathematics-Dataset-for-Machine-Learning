from sympy import *
import random
import collections
import string
import re
import importlib.util
import inspect
from qagen.qagen import *

import pdb

def get_farm_animals():
    '''
    Returns a list for farm animal.
    '''
    farm_animals = ['goats','lambs','dogs','cats','ducks','chicken','hen','pigs',
    'horses','donkeys','rabbits','guinea pigs','gooses','sheeps','piglets'
    ,'bulls','stallions','rams','cows','calfs','trukeys']
    return farm_animals

def get_colleges():
    '''
    Returns a list of colleges
    '''
    colleges = ["MIT", "Vanderbilt", "Tufts", "Stanford", "Harvard", "Boston College",
    "Northeastern", "Yale", "Dartmouth", "Duke", "Northwestern", "Boston University"]
    return colleges

def get_diseases():
    '''
    Returns a list of diseases of varying severity
    '''
    diseases = ['Cancer','Gingivitis','Scurvy','Alzheimers', 'Carpal Tunnel Syndrome',
    'Type I Diabetes','Type II Diabetes', 'Depression', 'Diarrhea', 'Down Syndrome', 'Dyslexia',
    'Dermatitis']
    return diseases

def get_team_sports():
    '''
    Returns a list of team sports
    '''
    team_sports = ["basketball", "soccer", "volleyball", "baseball", "dodgeball", "football",
    "ice hockey"]
    return team_sports

def get_capital_letters():
    '''
    Returns a list of the capital letters of the english alphabet
    '''
    capital_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    return capital_letters

def duplicates_present(args1,args2):
    '''
    Check for dulplicates between and within lists

    [],[] -> True
    [1,2,3],[] -> False
    [1,1,1,2],[] -> True
    [1,2,3],[1,2,3] -> True
    '''
    # if length of joint list decreases, then there is some duplicate (either btw the lists or within a list)
    print(args1, args2)
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

def get_classes(question):
    file_spec = importlib.util.spec_from_file_location(question, question)
    file_module = importlib.util.module_from_spec(file_spec)
    file_spec.loader.exec_module(file_module)
    classes = [x[1] for x in inspect.getmembers(file_module, inspect.isclass)]
    classes = [x for x in classes if (issubclass(x, QAGen) and x().__class__.__name__ != 'QAGen')]

    return classes
