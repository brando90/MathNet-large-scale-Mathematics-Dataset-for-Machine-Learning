import random
import sympy
import inspect
import string
from faker import Factory
import sympy

import pdb

import qagen.utils as utils

# def language_permuters(func):
#     '''
#     Im a decorator
#     '''
#     #TODO have a way for users to avoid having to do self.seqg etc
#     print('here \n')
#     # the following is the wrapper function
#     def wrapper(*args,**kwargs):
#         self = args[0]
#         seqg, perg, choiceg = self.seqg, self.perg, self.choiceg
#         # TODO: have maybe inspect set the names seqg, etc
#         print( func )
#         print( inspect.ismethod(func) )
#         func.seqg = seqg
#         print( dir(func) )
#         print(  )
#         return func(*args,**kwargs)
#     return wrapper

class QAOps:
    '''
    Class that has operations that act of questions and answers.
    '''

    def __init__(self):
        self.sympy_vars = []
        self.names = []
        self.use_latex = True
        self.debug = False
        self.fake = Factory.create()

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
            if isinstance(arg, sympy.Expr):
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
        # TODO when is resolved being used?
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
    #TODO: case where user draws from default symbols, then provides own list of default symbols - possible collision without any way to check statically
    def get_symbols(self, num, symbols_str=None, symbols_list=None, uppercase=False, greek_letters=True):
        '''
        Gets n=num random symbols, either from given string of symbols separated by spaces (sympy format) or generates them randomly.
        '''
        if symbols_str != None or symbols_list != None:
            if symbols_str == None:
                symbols = sympy.symbols(symbols_str)
            else:
                symbols = symbols_list
        else: #if given list of possible symbol choices
            if uppercase:
                letters = list(string.ascii_letters)
            else:
                letters = list(string.ascii_lowercase)
            symbols = sympy.symbols(" ".join(letters))
        new_symbol_choices = [x for x in symbols if x not in self.sympy_vars]#constrain possible symbols to those not yet assigned
        symbols = random.sample(population, num) # Return a k length list of unique elements chosen from the population sequence.
        self.sympy_vars += symbols
        return tuple(symbols)
    
    def get_symbol(self):
        return self.get_symbols(1)
        
    #TODO: Test cases for get_names
    def get_names(self, num, names=None):
        '''
        Get n=num names from list of given names, or draw them randomly using Faker
        '''
        if names == None: #if no given list, generate using faker
            names = []
            while len(names) < num:
                name = self.fake.name()
                name = name.split(" ")[0]
                if name in self.names:
                    # TODO: how do we avoid infinite loops?
                    # faker probably has enough long enough list no collisons?
                    continue
                names.append(name)
            return tuple(names)
        else:
            duplicates = [x for x in names if x in self.names]
            if len(duplicates) > 0: #if assigned duplicates, throw error
                #TODO: isn't it better that it just keeps trying to generate
                # until no collision. We should avoid this continuous trying to
                # lead to an infinite loop
                raise DuplicateAssignmentError(duplicates)
            # TODO: how does this guarantee no collisions? distinct objects
            names_indices = self.random_gen.randint(0, len(names), num)
            names = [names[i] for i in names_indices]
            self.names += (names)
            return tuple(names)

    def get_name(self):
        return self.get_names(1)[0]

    def register_qa_variables(variables):
        # add args to duplicate checker lists
        for var in variables:
            if isinstance(var, Expr): #if its of Sympy type
                self.sympy_vars.append(var)
            else:
                self.name.append(var)
