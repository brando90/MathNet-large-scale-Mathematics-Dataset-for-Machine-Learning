import inspect
import numpy as np
from qagen import utils
import sympy

class NL():

    def __init__(self, seed):


#TODO: Perg
#TODO: how to substitute in NL

       
    

class QAFormat():

    def __init__(self, variable_seed, const_seed, q_format_seed, a_format_seed):
        self.variable_seed = variable_seed
        self.const_seed = const_seed
        self.q_format_seed = q_format_seed
        self.a_format_seed = a_format_seed
        self.question = Question()
        self.answer = Answer()
        
        self.sympy_vars = Set() #to check for repeats
        self.names = Set() #to check for repeats
        self.faker = faker.Faker()
        self.random_gen = np.random.RandomState(variable_seed)
        self.q_gen = np.random.RandomState(q_format_seed)
        self.a_gen = np.random.RandomState(a_format_seed)

    
    def generate_mc_q(self):
        except NotImplementedError

    def generate_mc_a(self):
        except NotImplementedError

    def get_symbols(num, symbols_str=None):
        '''
        Gets random symbol from string of sympy symbols
        '''
        if symbols_str == None:
            symbols = sympy.Symbols(utils.get_list_sympy_variables())
        else:
            symbols = sympy.Symbols(symbols_str)
            return symbols
            
             

    def get_symbol():
        return self.get_symbol(1)

    def get_names(num, names=None):
        if names == None:
            names = Set()
            while len(names) < num:
                names.add(self.faker.name())
        else:
            names = list(Set(names))
            return self.random_gen.sample(names, num)
            
    def get_name():
        return self.get_name(1)    


class QA():

    def __init__(self, seed):
        self.seed = seed
        np.random.seed(seed) 

class Question():
    
    def __init__(self, seed):
        self.seed = seed
        QA.__init__(self, seed):
        

class Answer():
    
    def __init__(self, seed):
        self.seed = seed
        QA.__init__(self, seed):

def main():
    pass

if __name__ == "__main__":
    main()
