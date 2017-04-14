from sympy import *
import random

def _resolve(arg, assignments={}):
    if isinstance(arg, DelayedExecution):
        return arg.execute(assignments) # recursion
    elif isinstance(arg, Variable):
        return assignments[arg]
    elif isinstance(arg, Expr):
        arg = handle_sympy(arg,assignments)
        return sympy2text(arg)
    else:
        return arg

class DelayedExecution:
    # builds delayed execution objects
    def __init__(self, func, *args, **kwargs):
        # stores the function to make it static/paused/delayed
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def execute(self, assigments={}):
        # step 1: resolve inputs
        args = [_resolve(arg, assigments) for arg in self.args]
        kwargs = {k: _resolve(v, assigments) for k, v in self.kwargs.items()}
        # step 2: resolve function call
        return self.func(*args, **kwargs)

def func_flow(func):
    '''
    decorates func: now when the original func is called, it returns an object
    storing the **delayed execution** of func (and its arguments).
    '''
    def wrapper(*args, **kwargs):
        return DelayedExecution(func, *args, **kwargs)
    return wrapper

##

class Variable:
    def __hash__(self):
        return id(self)

@func_flow
def seqg(*args):
    return ' '.join(args) # concatenates the
#seqg = func_flow(seqg)

@func_flow
def perg(*args):
    args = random.sample( args, len(args) ) #
    return ' '.join(args)
#perg = func_flow(perg)

def sympy2text(sympy_var):
    return str(sympy_var)

def handle_sympy(arg,assigments):
    for key, substitution_opts in assigments:
        substitution = random.sample(substitution_opts,1)
        arg = arg.subs(key,substitution)
    return arg