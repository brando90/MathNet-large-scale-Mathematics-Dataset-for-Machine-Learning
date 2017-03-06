import string
import numpy as np

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

    def get_single_new_exercise_sums(self,nb_variables=26,largest_int=10):
        '''
        get new exercise with x_1 + x_2 + ... + x_N =  K and make some x_i the subject.
        '''
        # variables in equation
        variables_in_eq = np.random.choice( self.var_names, size=nb_variables, replace=False )
        # choose target variable
        target_var = np.random.choice( variables_in_eq, size=1 )
        # create equation
        equation = ''
        for i in range(0,len(variables_in_eq)-1):
            var = variables_in_eq[i]
            equation = equation + var + '+'
        equation = equation+variables_in_eq[-1]
        equation = '%s=%d'%(equation,np.random.randint(0,high=largest_int))
        # create problem msg
        problem_msg = 'Problem: make %s the subject of equation: %s'%(target_var[0],equation)
        return problem_msg


if __name__ == '__main__':
    maker_var_subject = Make_Var_Subject()
    problem_msg = maker_var_subject.get_single_new_exercise_sums(nb_variables=5)
    print( problem_msg )
