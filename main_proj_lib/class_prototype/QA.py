import inspect
import string
import numpy as np
import sympy
from qaflow.question_answer import DuplicateAssignmentError
from faker import Faker

       
#TODO: when question creators start to use more libraries, we can create functions that create generators from the libraries so that question creators can select which generators to use/keep track of generators by themselves


class QAFormat():
    '''
    Class for entire question, answer generating object. 
   '''

    def __init__(self):
        self.question = Question()#seed question with seed for variables/names
        self.answer = Answer()#seed answer with seed for variable/names
        self.faker = Faker()
        self.random_gen = np.random.RandomState()
        self.author = None
        self.description = None
        self.keywords = []

        self.sympy_vars = []

        self.names = []
        self.const_vars = None
        self.vars = None

        self.correct_seed = None

    #TODO: turn into wrapper that accepts as arguments generators to seed
    def _seeding_wrapper(func):
    '''Wrapper for automatically seeding generators when function is called'''
        def seeding_func(self, seed, *args, **kwargs):
            self.faker.seed(seed)
            self.random_gen.seed(seed)
            np.random.seed(seed)
            return func(self, seed, *args, **kwargs)
        return seeding_func

    #TODO: test cases for get_symbols 
    def get_symbols(self, num, symbols_str=None):
        '''
        Gets n=num random symbols, either from given string of symbols separated by spaces (sympy format) or generates them randomly.

        Supports maximum of 26 symbols in question overall
        '''
        if symbols_str != None: #if drawing from all 26 lowercase (no list given)
            symbols = sympy.symbols(symbols_str)
            duplicates = [x for x in symbols if x in self.sympy_vars] #check if symbols already used in question
            if len(duplicates) > 0:
                raise DuplicateAssignmentError(duplicates)
        elif (len(self.sympy_vars) + num) > 26: #check to make sure less than 26 symbols
            raise Exception('You have exceeded the maximum number of variables allowed')
        else: #if given list of possible symbol choices
            letters = list(string.ascii_letters)
            symbols = sympy.symbols(" ".join(letters))
            symbols = symbols[0:26] #enforcing lowercase
        symbols = [x for x in symbols if x not in self.sympy_vars]#constrain possible symbols to those not yet assigned
        sample_index = self.random_gen.randint(0, len(symbols), num)
        symbols = [symbols[i] for i in sample_index]
        self.sympy_vars += symbols
        return tuple(symbols)
            
             

    def get_symbol(self):
        '''Used for getting single symbol'''
        return self.get_symbols(1)[0]

    #TODO: Test cases for get_names
    def get_names(self, num, names=None):
        '''
        Get n=num names from list of given names, or draw them randomly using Faker
        '''
        if names == None: #if no given list, generate using faker
            names = []
            while len(names) < num:
                name = self.faker.name()
                name = name.split(" ")[0]
                if name in self.names:
                    continue
                names.append(name)
            return tuple(names)
        else:
            duplicates = [x for x in names if x in self.names]
            if len(duplicates) > 0: #if assigned duplicates, throw error
                raise DuplicateAssignmentError(duplicates)
            names_indices = self.random_gen.randint(0, len(names), num) 
            names = [names[i] for i in names_indices]
            self.names += (names)
            return tuple(names)
            
    def get_name(self):
        '''used for getting single name'''
        return self.get_names(1)[0]

    def set_correct_seed(self, seed):
        self.correct_seed = seed


    @_seeding_wrapper
    def init_consistent(self, seed):
        '''Initializes variables consistent across question, answer'''
        self.const_vars = self.create_const_variables()
    @_seeding_wrapper
    def init(self, seed):
        '''Initializes variables that change between question, answer'''
        self.vars = self.create_variables()

    def create_const_variables(self):
        '''
        Function for generating consistent variables, to be implemented
        Returns the variables as tuple (separated by commas)
        '''
        raise NotImplementedError

    def create_variables(self):
        '''
        Function for generating inconsistent variables, to be implemented
        Returns the variables as tuple (separated by commas)
        '''
        raise NotImplementedError
    
    def set_const_variable_creation(self, func):
        '''Method for setting the function for creating consistent variables'''
        self._create_const_variables = func    

    def set_variable_creation(self, func):
        '''Method for setting function for creating inconsistent variables'''
        self._create_variables = func

    
    def generate_mc_q(self, seed):
        '''
        Outputs MC question as string
        '''
        #TODO
        #q_format_seed would probably involve changing NL around questions
        #do formatting with seed here? Unclear what formatting would be rn
        #maybe change it to NL format seed (consistent w/ answer) instead?
        self.init(self.correct_seed) 
        correct_q = self.generate_q(self.correct_seed)
        return "Select the best answer to the following question: " + correct_q
        
    def generate_mc_a(self, num_answers, a_format_seed, incorrect_seed=0):
        '''
        Outputs MC answer as list of strings
        '''
        answers = []
        self.init(self.correct_seed)
        correct_answer = self.generate_a(self.correct_seed)
        answers.append(correct_answer)
        incorrect_gen = np.random.RandomState(incorrect_seed)
        for n in range(num_answers-1):
            seed = incorrect_gen.randint(1000)
            self.init(seed)
            answers.append(self.generate_a(seed))
            #generate incorrect answers
        #permute answer order based on a_format_seed
        format_gen = np.random.RandomState(a_format_seed)
        format_gen.shuffle(answers)
        return answers
        
            

    def generate_q(self, seed):
        '''Take the question expression and turn it into a formatted string'''
        raise NotImplementedError
    
    def generate_a(self, seed):
        '''Take the answer expression and turn it into a formatted string'''
        raise NotImplementedError

    def perm(self, elements_list):
        raise NotImplementedError




class QA():
    
    '''
    General expression class for a type of question or answer. Enforces no duplicate assignments of names or sympy variables. 
    '''

    def __init__(self):
        pass

    def set_expression(self, func):
        '''
        Set function for outputting the pure mathematical expressions for the instance. Question creator defines func.
        '''
        self.create_expression = func
    
    def create_expression(self):
        raise NotImplementedError

class Question(QA):
    
    def __init__(self):
        QA.__init__(self)

class Answer(QA):
    
    def __init__(self):
        QA.__init__(self)



def main():
    pass

if __name__ == "__main__":
    main()
