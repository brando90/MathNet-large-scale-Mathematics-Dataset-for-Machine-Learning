import string

import maps

import pdb

class AlgebraI(object):

    def __init__(self):
        self.name = 'AlgebraI'


class Make_Var_Subject(object):

    def __init__(self):
        self.name = 'Make_Var_subject'
        self.var_names = list(string.ascii_lowercase) # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    def get_making_the_subject_exercises(self,nb_ex):
        pass

    def get_single_new_exercise_sums(self,random_seed):
        '''
        get new exercise with x_1 + x_2 + ... + x_N =  K and make some x_i the subject.
        '''
        make_var_subj = self.var_names[i]
        problem_msg = 'Problem: make %s the subject'
