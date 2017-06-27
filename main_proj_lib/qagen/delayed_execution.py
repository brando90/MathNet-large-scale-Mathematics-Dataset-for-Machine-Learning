from sympy import *
import random
import collections
import pdb

import pdb

class DelayedExecution:

    '''
    Given a function and all its arguments, builds an object that stores the
    function and its all its arguments to be called later. Essentially stores
    the execution of a function and its arguments for some future call.
    '''

    def __init__(self, gen_instance, func, *args, **kwargs):
        '''
        Builds a delayed execution functio. i.e. it makes func
        static/paused/delayed w.r.t to all its arguments (*args, **kwargs).
        '''
        self.gen_instance = gen_instance
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def __repr__(self):
        '''
        for printing the delayed executed function
        '''
        return str((self.func, self.args, self.kwargs))

    def __call__(self):
        original_state = self.gen_instance.generator_unit_test
        self.gen_instance.generator_unit_test = False # otherwise it keeps returning DE instead of executing the function
        str_ans = self.func(*self.args,**self.kwargs)
        self.gen_instance.generator_unit_test = original_state
        return str_ans

    # def __add__(self, other):
    #     '''
    #     Overloading add function for DelayedExecution class to allow for '+' operator to be used to create questions (E.g., Q() + 'solve' + x + perg( Eq(a,b),Eq(x,2*b),Eq(a,8)) + 'can you do it?').
    #
    #     This resolves recursively upon execute(), base case relies on evaluation of primitives to strings.
    #     '''
    #     if isinstance(other, DelayedExecution):
    #         '''
    #         if other is also instance of DelayedExecution, create new DelayedExecution object whose delayed function is the addition of self and other, using the '+' operator.
    #         '''
    #         func = lambda x, y: x + y
    #         return DelayedExecution(func, x=self, y=other)
    #     elif isinstance(other, str) or isinstance(other, Basic):
    #         '''
    #         elif other is string or Sympy expression, create new DelayedExecution object whose delayed function is the addition of self and str of other, using the '+' operator.
    #         '''
    #         func = lambda x, y: x + [y]
    #         return DelayedExecution(func, x=self, y=other)
    #
    #
    # def __radd__(self, other):
    #     '''
    #     Overloading radd function for DelayedExecution class to allow for '+' operator to be used to create questions (E.g., Q() + 'solve' + x + perg( Eq(a,b),Eq(x,2*b),Eq(a,8)) + 'can you do it?'). Same as above, but for cases where self is on right hand side.
    #     '''
    #
    #     if isinstance(other, DelayedExecution):
    #         func = lambda x, y: y + x
    #         return DelayedExecution(func, x=self, y=other)
    #     elif isinstance(other, str) or isinstance(other, Basic):
    #         func = lambda x, y: [y] + x
    #         return DelayedExecution(func, x=self, y=other)

def func_flow(func):
    '''
    decorates func: now when the original func is called, it returns an object
    storing the **delayed execution** of func (and its arguments).
    '''
    def wrapper(*args, **kwargs):
        return DelayedExecution(func, *args, **kwargs)
    return wrapper
