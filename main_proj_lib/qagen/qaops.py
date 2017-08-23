import random
import sympy
import inspect
import string
from faker import Factory
import sympy

import pdb

import qagen.utils
from qagen.delayed_execution import *

#ans = 'Mary had  x = 2 , y = 3 , z = 4 , goats, lambs, dogs  respectively. Each was decreased by d = 1 by the wolf named Gary.'

class QAOps:
    '''
    Class that has operations that act of questions and answers.
    '''

    def __init__(self):
        self.sympy_vars = []
        self.names = []
        self.use_latex = True
        self.debug = False
        self.latex_visualize = False
        self.generator_unit_test = False
        self.fake = Factory.create()

    #register library, provide seeding func for library, provide state_getting for library

    #how to enforce usage only of libraries that are registered?

    #seedall seeds all

    def seqg(self,*args):
        '''
        Returns a sequentialls generated sentence.

        Essentially concatenates all the arguments into a string.
        '''
        #print(self.generator_unit_test)
        # a unit test to help the user make sure they are using seqg
        if self.generator_unit_test:
            return DelayedExecution(self,self.seqg,*args)
        # do seqg
        args = self._preprocess_args(args)
        args = self.convert_to_list_of_string(args)
        out = ' '.join(args)
        return out

    def perg(self,*args):
        '''
        Returns a sequentialls generated sentence.

        Essentially concatenates all the arguments into a string but randomly permutes things.
        '''
        #print(self.generator_unit_test)
        # a unit test to help the user make sure they are using perg
        if self.generator_unit_test:
            return DelayedExecution(self,self.perg,*args)
        # perg
        args = self._preprocess_args(args)
        if not self.debug:
            args = random.sample( args, len(args) ) # Return a len(args) length list of unique elements chosen from args
        args = self.convert_to_list_of_string(args)
        return ' '.join(args)

    def choiceg(self,*args):
        '''
        Given a list of choices in the arguments, chooses one.
        '''
        #print(self.generator_unit_test)
        # a unit test to help the user make sure they are using choiceg
        if self.generator_unit_test:
            return DelayedExecution(self,self.choiceg,*args)
        # choiceg
        args = self._preprocess_args(args)
        if not self.debug:
            args = random.sample(args,1) # samples a single element randomly from args
            return args[0]
        else:
            return args[0]

    def _preprocess_args(self,args):
        # step 1: resolve inputs
        args = [self._preprocess_arg(arg) for arg in args]
        #kwargs = {k: self._preprocess_arg(v) for k, v in kwargs.items()}
        return tuple(args)

    def _preprocess_kargs(self,**kwargs):
        # step 1: resolve inputs
        #args = [self._preprocess_arg(arg) for arg in args]
        kwargs = {k: self._preprocess_arg(v) for k, v in kwargs.items()}
        return kwargs

    def _preprocess_arg(self, arg):
        '''
        Preprocesses the the current argument arg.

        arg - the arg to resolve
        '''
        if isinstance(arg, sympy.Expr):
            # go through all the possible assignments and try to substitute them with the current expression
            # TODO extend functionality, the aim will be to help give more variaty by applying some sympy functions
            return arg
        elif isinstance(arg, DelayedExecution):
            executed_de = arg()
            #print('-------> DE:{}|'.format(executed_de))
            #ans = 'Mary had  x = 2 , y = 3 , z = 4 , goats, lambs, dogs  respectively. Each was decreased by d = 1 by the wolf named Gary.'
            return executed_de
        else:
            return arg

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

    def sympy2text(self,sympy_var):
        '''
        Converts sympy expression to text.
        '''
        # TODO: improve this!
        if self.use_latex:
            str_symp_var = sympy.latex(sympy_var)
            if self.latex_visualize:
                str_symp_var = '$%s$' % (str_symp_var,)
        else:
            #str_symp_var = srepr(sympy_var) #TODO why do we have this? it seems to make things be displayed weirdly
            str_symp_var = str(sympy_var)
        return str_symp_var

    ##
    #TODO: Test cases for get_symbols
    def get_symbols(self, num, symbols_str=None, symbols_list=None, uppercase=False, greek_letters=True, integer=False):
        '''
        Gets n=num random symbols, either from given string of symbols separated by spaces (sympy format) or generates them randomly.
        '''
        # TODO: greek_letters
        # TODO: we could eventually extend it to also have like x_1 x_2 x_3
        if symbols_str != None or symbols_list != None:
            if symbols_str != None:
                symbols = sympy.symbols(symbols_str, integer=integer)
            else:
                symbols = symbols_list
            if set(symbols).issubset(set(self.sympy_vars)):
                # if the error is user provided then we warn them
                raise ValueError('Your list {} should not be a subset of the names already defined: {}'.format(symbols,self.sympy_vars))
                # TODO if this is true then library starts using x_1,x_2,...etc to avoid issue
        else: #if given list of possible symbol choices
            if uppercase:
                letters = list(string.ascii_letters)
            else:
                letters = list(string.ascii_lowercase)
            symbols = sympy.symbols(" ".join(letters), integer=integer)
        if set(symbols).issubset(self.sympy_vars):
            # TODO if this is true then library starts using x_1,x_2,...etc to avoid issue, note at this point
            # the user is relying on use so we can do whatever we want
            pass
        choices_for_symbols = [x for x in symbols if x not in self.sympy_vars]#constrain possible symbols to those not yet assigned
        symbols = random.sample(choices_for_symbols, num) # Return a k length list of unique elements chosen from the population sequence.
        self.sympy_vars += symbols
        return tuple(symbols)

    #TODO: Test cases for get_names
    def get_names(self, num, names_list=None, full_name=True):
        '''
        Get n=num names from list of given names, or draw them randomly using Faker
        '''
        #
        if names_list == None: #if no given list, generate using faker
            names = []
            while len(names) < num:
                full_name_str = self.fake.name()
                name = full_name_str if full_name else full_name_str.split(" ")[0]
                if name in self.names:
                    # faker probably has enough long enough list no collisons?
                    continue
                self.names.append(name)
                names.append(name)
        else:
            # if names_list is a subset of self.names
            if set(names_list).issubset(self.names):
                # TODO check this
                raise ValueError('Your list {} should not be a subset of the names already defined: {}'.format(names_list,self.names))
            # TODO: how does this guarantee no collisions? distinct objects
            choices_for_names = [x for x in names_list if x not in self.names]#constrain possible symbols to those not yet assigned
            names = random.sample(choices_for_names, num) # Return a k length list of unique elements chosen from the population sequence.
            self.names += (names)
        return tuple(names)

    def get_name(self):
        return self.get_names(1)[0]

    def get_symbol(self):
        return self.get_symbols(1)

    def register_qa_variables(self, variables):
        # add args to duplicate checker lists
        for var in variables:
            if isinstance(var, sympy.Expr): #if its of Sympy type
                self.sympy_vars.append(var)
            else:
                self.names.append(var)
