from sympy import *
import random
import collections

import pdb

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

def convert_to_list_of_string(args):
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
            args_out.append( sympy2text(arg) )
        else:
            args_out.append( str(arg) )
    return args_out

def seqg(*args):
    '''
    Returns a sequentialls generated sentence.

    Essentially concatenates all the arguments into a string.
    '''
    args = convert_to_list_of_string(args)
    return ' '.join(args) # concatenates the

def perg(*args):
    '''
    Returns a sequentialls generated sentence.

    Essentially concatenates all the arguments into a string but randomly permutes things.
    '''
    args = random.sample( args, len(args) ) # Return a len(args) length list of unique elements chosen from args
    args = convert_to_list_of_string(args)
    return ' '.join(args)

def choiceg(*args):
    '''
    Given a list of choices in the arguments, chooses one.
    '''
    args = random.sample( args, 1 ) # samples a single element randomly from args
    return args[0]

def sympy2text(sympy_var, use_latex=False):
    '''
    Converts sympy expression to text.
    '''
    # TODO: improve this!
    if use_latex:
        str_symp_var = latex(sympy_var)
    else:
        #str_symp_var = srepr(sympy_var) #TODO why do we have this? it seems to make things be displayed weirdly
        str_symp_var = str(sympy_var)
    return str_symp_var
