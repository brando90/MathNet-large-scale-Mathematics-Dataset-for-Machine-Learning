import random
from sympy import *
import inspect

import pdb

def language_permuters(func):
    '''
    Im a decorator
    '''
    #TODO
    print('here \n')
    # the following is the wrapper function
    def wrapper(*args,**kwargs):
        self = args[0]
        seqg, perg, choiceg = self.seqg, self.perg, self.choiceg
        # TODO: have maybe inspect set the names seqg, etc
        print( func )
        print( inspect.ismethod(func) )
        func.seqg = seqg
        print( dir(func) )
        print(  )
        return func(*args,**kwargs)
    return wrapper

class QAOps:
    '''
    Class that has operations that act of questions and answers.
    '''

    def __init__(self):
        self.sympy_vars = []
        self.names = []
        self.use_latex = True

    def seqg(self,*args):
        '''
        Returns a sequentialls generated sentence.

        Essentially concatenates all the arguments into a string.
        '''
        args = self.convert_to_list_of_string(args)
        return ' '.join(args) # concatenates the

    def perg(self,*args):
        '''
        Returns a sequentialls generated sentence.

        Essentially concatenates all the arguments into a string but randomly permutes things.
        '''
        args = random.sample( args, len(args) ) # Return a len(args) length list of unique elements chosen from args
        args = self.convert_to_list_of_string(args)
        return ' '.join(args)

    def choiceg(self,*args):
        '''
        Given a list of choices in the arguments, chooses one.
        '''
        args = random.sample( args, 1 ) # samples a single element randomly from args
        return args[0]

    def convert_to_list_of_string(self,args):
        '''
        Given a list of arguments from the framework, concatenates them into a string
        according to its type. Specifically, if something is of a sympy type, it will
        convert it using the framework's sympy2text rather than python default methods.

        argument
            args - array of arguments for the framework.
        return
            args - array of arguments for the framework in string form.

        '''
        args_out = []
        for arg in args:
            if isinstance(arg, Expr):
                args_out.append( self.sympy2text(arg) )
            else:
                args_out.append( str(arg) )
        return args_out

    def _resolve(self, arg, assignments={}):
        '''
        arg - the arg to resolve
        assignments - a dictionary mapping arg name (key) to its list of possible
        alternative options (values).

        Resolves the current argument arg. If assignments has an a key arg mapping
        to a list of valid alternative values, then one is chosen randomly to
        substitute the original arg. Make sure to include arg in the alternatives
        if you want it to be considered
        '''
        #print('->resolve arg: ', arg)
        #print('->resolve assignments: ', assignments)
        # choose a random alternative fto the arg if the key is in the assignments options
        if isinstance(arg, collections.Hashable) and arg in assignments:
        #if hash(str(arg)) in assignments:
            arg = random.sample(assignments[arg],1)[0]
        # resolve the arg after an alternative was chose
        if isinstance(arg, DelayedExecution):
            return arg.execute(assignments) # recursively execute arg
        # elif callable(arg): # doesn't wite work
        #     return DelayedExecution(arg, assignments)
        elif isinstance(arg, Expr):
            # go through all the possible assignments and try to substitute them with the current expression
            for key, substitution_options in assignments.items():
                substitution = random.sample(substitution_options,1)[0]
                arg = arg.subs(key,substitution) # note if key is not aprt of expr, the expr remains unchanged (note arg is an expression ath this point)
            return arg
        else:
            return arg

    def sympy2text(self,sympy_var):
        '''
        Converts sympy expression to text.
        '''
        # TODO: improve this!
        if self.use_latex:
            str_symp_var = latex(sympy_var)
        else:
            #str_symp_var = srepr(sympy_var) #TODO why do we have this? it seems to make things be displayed weirdly
            str_symp_var = str(sympy_var)
        return str_symp_var

    ##

    def get_symbols(self, num, symbols_str=None, uppercase=False, greek_letters=True):
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
