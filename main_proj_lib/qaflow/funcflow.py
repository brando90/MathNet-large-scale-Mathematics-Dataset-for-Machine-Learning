from sympy import *
import random
import collections

import pdb

class DelayedExecution:
    '''
    Given a function and all its arguments, builds an object that stores the
    function and its all its arguments to be called later. Essentially stores
    the execution of a function and its arguments for some future call.
    '''
    def __init__(self, func, *args, **kwargs):
        '''
        Builds a delayed execution functio. i.e. it makes func
        static/paused/delayed w.r.t to all its arguments (*args, **kwargs).
        '''
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def __repr__(self):
        '''
        for printing the delayed executed function
        '''
        return str((self.func, self.args, self.kwargs))

    def __add__(self, other):
        '''
        Overloading add function for DelayedExecution class to allow for '+' operator to be used to create questions (E.g., Q() + 'solve' + x + perg( Eq(a,b),Eq(x,2*b),Eq(a,8)) + 'can you do it?'). 

        This resolves recursively upon execute(), base case relies on evaluation of primitives to strings.
        '''
        if isinstance(other, DelayedExecution):
            '''
            if other is also instance of DelayedExecution, create new DelayedExecution object whose delayed function is the addition of self and other, using the '+' operator.
            '''
            func = lambda x, y: x + y
            return DelayedExecution(func, x=self, y=other)
        elif isinstance(other, str) or isinstance(other, Basic):
            '''
            elif other is string or Sympy expression, create new DelayedExecution object whose delayed function is the addition of self and str of other, using the '+' operator.           
            '''
            func = lambda x, y: x + [y]
            return DelayedExecution(func, x=self, y=other)
            

    def __radd__(self, other):
        '''
        Overloading radd function for DelayedExecution class to allow for '+' operator to be used to create questions (E.g., Q() + 'solve' + x + perg( Eq(a,b),Eq(x,2*b),Eq(a,8)) + 'can you do it?'). Same as above, but for cases where self is on right hand side.
        '''
        
        if isinstance(other, DelayedExecution):
            func = lambda x, y: y + x
            return DelayedExecution(func, x=self, y=other)
        elif isinstance(other, str) or isinstance(other, Basic):
            func = lambda x, y: [y] + x
            return DelayedExecution(func, x=self, y=other)
        
    def execute(self, assignments={}):
        '''
        Executes the delayed function.
        To do this it goes through all its arguments and resolves them.
        Resolving means that it figures out what type of arguments they arguments
        they are and handles them properly.
        '''
        # step 1: resolve inputs
        #assignments = {hash(str(key)): assignments[key] for key in assignments.keys()}
        #assignments[hash(str("assignments"))] = [assignments]
        args = [self._resolve(arg, assignments) for arg in self.args]
        kwargs = {k: self._resolve(v, assignments) for k, v in self.kwargs.items()}
        # step 2: resolve function call
        return self.func(*args, **kwargs)

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

def func_flow(func):
    '''
    decorates func: now when the original func is called, it returns an object
    storing the **delayed execution** of func (and its arguments).
    '''
    def wrapper(*args, **kwargs):
        return DelayedExecution(func, *args, **kwargs)
    return wrapper

##

def convert_to_list_of_string(args, use_latex=False):
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
        if isinstance(arg, Basic):
            args_out.append( sympy2text(arg, use_latex) )
        elif isinstance(arg, (list, tuple)): #for nested lists that happen with nested perg or seqg
            string_list = convert_to_list_of_string(arg, use_latex) #call convert_to_list_of_string recursively
            args_out += string_list
        else:
            args_out.append( str(arg) )
    return args_out

## decorations (note if you don't know what decorations are look at the
##decoration explanation file or google it), note I wrote at the end of the decorated functions what decorators do
@func_flow
def seqg(*args):
    '''
    Returns a sequentialls generated sentence as a list

    '''
    #args = convert_to_list_of_string(args)
    #return ' '.join(args) # concatenates the
    return args
#seqg = func_flow(seqg) #<- this is what decorators do

@func_flow
def perg(*args):
    '''
    Returns a permuted list of the arguments
    '''
    args = random.sample( args, len(args) ) # Return a len(args) length list of unique elements chosen from args
    #args = convert_to_list_of_string(args)
    #return ' '.join(args)
    return args
#perg = func_flow(perg)  #<- this is what decorators do

@func_flow
def choiceg(*args):
    '''
    Given a list of choices in the arguments, chooses one.
    '''
    args = random.sample( args, 1 ) # samples a single element randomly from args
    return args[0]
#choiceg = func_flow(choiceg)

def sympy2text(sympy_var, use_latex=False):
    '''
    Converts sympy expression to text.
    '''
    # TODO: improve this!
    if use_latex:
        str_symp_var = '$' + latex(sympy_var) + '$'
    else:
        #str_symp_var = srepr(sympy_var) #TODO why do we have this? it seems to make things be displayed weirdly
        str_symp_var = str(sympy_var)
    return str_symp_var
