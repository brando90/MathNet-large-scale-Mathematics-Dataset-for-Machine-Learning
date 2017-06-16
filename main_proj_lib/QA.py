import inspect
import numpy as np
from qagen import utils
import sympy
from question_answer import DuplicateAssignmentError

class NL():

    def __init__(self, seed):


#TODO: Perg
#TODO: how to substitute in NL

       
#TODO: when question creators start to use more libraries, we can create functions that create generators from the libraries so that question creators can select which generators to use/keep track of generators by themselves


class QAFormat():

    def __init__(self, variable_seed, const_seed):
        self.variable_seed = variable_seed
        self.const_seed = const_seed
        
        self.sympy_vars = Set() #to check for repeats
        self.names = Set() #to check for repeats
        self.faker = faker.Faker()
        self.random_gen = np.random.RandomState(variable_seed)

    #maybe we can wrap around these to automatically set global randomState so that question creator doesn't have to remember to? Same applies to generate_mc methods 
    def create_question(self, const_seed):
        except NotImplementedError

    def create_answer(self, const_seed):
        except NotImplementedError
    
    def generate_mc_q(self, q_format_seed):
        except NotImplementedError

    def generate_mc_a(self, a_format_seed):
        except NotImplementedError

    def get_symbols(num, symbols_str=None):
        '''
        Gets random symbol from string of sympy symbols
        '''

        if symbols_str == None:
            letters = list(string.ascii_letters)
            symbols = sympy.Symbols(" ".join(letters))
        else:
            symbols = sympy.Symbols(symbols_str)
            duplicates = self.sympy_vars.intersection(set(symbols))
            if len(duplicates) > 0:
                except DuplicateAssignmentError(duplicates)
        symbols = self.random_gen.sample(list(symbols), num)
        self.sympy_vars.add(symbols)
            return tuple(symbols)
            
             

    def get_symbol():
        return self.get_symbol(1)[0]

    def get_names(num, names=None):
        if names == None:
            names = Set()
            while len(names) < num:
                name = self.faker.name()
                if name in self.names:
                    continue
                names.add(name)
            return tuple(names)
        else:
            duplicates = self.names.intersection(Set(names))
            if len(duplicates) > 0
                except DuplicateAssignmentError(duplicates) 
            names = self.random_gen.sample(names, num)
            self.names.add(names)
            return tuple(names)
            
    def get_name():
        return self.get_name(1)[0]


class QA():

    def __init__(self, seed):
        np.random.seed(seed)
    
    def create_expression(self):
        except NotImplementedError

class Question():
    
    def __init__(self, seed):
        QA.__init__(self, seed):

class Answer():
    
    def __init__(self, seed):
        QA.__init__(self, seed):


def main():
    pass

if __name__ == "__main__":
    main()
