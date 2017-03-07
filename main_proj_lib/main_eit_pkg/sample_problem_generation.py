import string
import numpy as np

import maps

import pdb

class AlgebraI(object):

    def __init__(self):
        self.name = 'AlgebraI'


class Make_Var_Subject_Pilot(object):

    def __init__(self):
        self.name = 'Make_Var_subject'
        self.var_names = list(string.ascii_lowercase) # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        self.dropbox_proj_loc = '/Users/brandomiranda/Dropbox (MIT)/eit_proj1_data/algebra1/make_var_subj_pilot'

    def get_making_the_subject_exercises(self,nb_ex=100):
        for exercise_index in range(nb_ex):
            problem_loc = self.dropbox_proj_loc+'/make_subject_pilot_problem_'+str(exercise_index)
            soln_loc = self.dropbox_proj_loc+'/make_subject_pilot_soln_'+str(exercise_index)
            with open(problem_loc,mode='w') as problem_file, open(soln_loc,mode='w') as soln_file:
                nb_variables = np.random.randint(low=3,high=10)
                problem_msg, soln_msg = self.get_single_new_exercise_sums(nb_variables,largest_int=100)
                problem_file.write(problem_msg)
                soln_file.write(soln_msg)

    def get_single_new_exercise_sums(self,nb_variables=26,largest_int=10):
        '''
        get new exercise with x_1 + x_2 + ... + x_N =  K and make some x_i the subject.
        '''
        # variables in equation
        variables_in_eq = np.random.choice( self.var_names, size=nb_variables, replace=False )
        # choose target variable
        target_var = np.random.choice( variables_in_eq, size=1 )
        integer = np.random.randint(0,high=largest_int)
        # create equation
        equation = ''
        for i in range(0,len(variables_in_eq)-1):
            var = variables_in_eq[i]
            equation = equation + var + '+'
        equation = equation+variables_in_eq[-1]
        equation = '%s=%d'%(equation,integer)
        # create problem msg
        problem_msg = 'Problem: make %s the subject of equation: %s'%(target_var[0],equation)
        # get solution
        soln_msg = self.get_solution_to_problem(equation,target_var,variables_in_eq,integer)
        return problem_msg, soln_msg

    def get_solution_to_problem(self,equation,target_var,variables_in_eq,integer):
        variables_in_eq = list( variables_in_eq[:] )
        if not (target_var in variables_in_eq):
            raise ValueError('Target Variable %s not in variables_in_eq %s'%(target_var,variables_in_eq))
        else:
            # get solution
            variables_in_eq.remove(target_var)
            print(variables_in_eq)
            lhs_variables = ''
            for i in range(0,len(variables_in_eq)-1):
                var = variables_in_eq[i]
                lhs_variables = lhs_variables + var + '+'
            lhs_variables = lhs_variables + variables_in_eq[-1]
            soln_expression = '%s = %s - (%s)'%(target_var[0],str(integer),lhs_variables)
            return soln_expression



if __name__ == '__main__':
    maker_var_subject = Make_Var_Subject_Pilot()
    # problem_msg,soln_msg = maker_var_subject.get_single_new_exercise_sums(nb_variables=5)
    # print( problem_msg )
    # print( soln_msg )
    maker_var_subject.get_making_the_subject_exercises()
