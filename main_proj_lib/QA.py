import inspect
import numpy as np
from qagen import utils
import sympy
from question_answer import DuplicateAssignmentError

       
#TODO: when question creators start to use more libraries, we can create functions that create generators from the libraries so that question creators can select which generators to use/keep track of generators by themselves


class QAFormat():

    def __init__(self, variable_seed, correct_seed):
        self.correct_seed = correct_seed
        self.question = Question(variable_seed)
        self.answer = Answer(variable_seed)

    '''
    Right now there is implicit consistency enforced across all names/sympy variables. 

    Should we make explicit consistency an option? It would probably involve the functions below (i.e., explicitly defining which variables are consistent acrosquestion and answer. Are there any cases where there will need to be variables that are inconsistent?)
    
    def init_consistent(self):
        #runs initialization function as both question, answer
        self.question =   
        self.answer =  

    def init(self):

    def create_variables(self):
        except NotImplementedError
    '''
    
    def generate_mc_q(self, q_format_seed=None):
        #TODO
        #q_format_seed would probably involve changing NL around questions
        #do formatting with seed here? Unclear what formatting would be rn
        #maybe change it to NL format seed (consistent w/ answer) instead?
        correct_q = self.generate_q(self.correct_seed)
        return "Select the best answer to the following question: " + correct_q
        

    def generate_mc_a(self, num_answers, a_format_seed=None):
        answers = []
        correct_answer = generate_a(self.correct_seed)
        answers.append(correct_answer)
        incorrect_gen = np.random.RandomState()
        for n in xrange(num_answers-1):
            seed = incorrect_gen.random()
            answers.append(self.generate_a(seed)
            #generate incorrect answers
        #permute answer order based on a_format_seed
        format_gen = np.random.RandomState(a_format_seed)
        return format_gen.shuffle(answers)
        
            

    def generate_q(self, seed):
        '''Take the question expression and turn it into an answer'''
        except NotImplementedError
    
    def generate_a(self, seed):
        '''Take the answer expression and turn it into an answer'''
        except NotImplementedError

    def perm(self, elements_list):
        except NotImplementedError




class QA():

    def __init__(self, variable_seed):
        
        self.variable_seed = variable_seed #this is used to generate sympy variables and faker. It is consistent across both question and answer
        self.sympy_vars = set()
        self.names = set()
        self.faker = faker.Faker()
        self.random_gen = np.random.RandomState(variable_seed)
    
    
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
    #TODO: Take advantage of Faker's uniqueness option for generating names
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

    def set_expression(self, func):
        self.create_expression = func
    
    def create_expression(self, seed):
        except NotImplementedError

class Question():
    
    def __init__(self, variable_seed):
        QA.__init__(self,  variable_seed):

class Answer():
    
    def __init__(self, variable_seed):
        QA.__init__(self, variable_seed):

class NL():

    def __init__(self, seed):


#TODO: how to substitute in NL


def main():
    pass

if __name__ == "__main__":
    main()
