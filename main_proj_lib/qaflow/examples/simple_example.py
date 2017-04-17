from funcflow import *
from sympy import *

x,y,a,b = symbols('x y a b')

def example1():
    ## solve x,  a = b,  x = 2*b, a = 8, can you do it?
    question = seqg('solve x ,', perg( 'a = b, ' , 'x = 2*b, ' , 'x = 8, ' ),'can you do it?')
    print(question.execute())

def example2(x,y,a,b):
    ## solve x,  a = b,  x = 2*b, a = 8, can you do it?
    question = seqg(seqg('solve ',x,', '), perg( seqg(Eq(x,y),', ') , seqg(Eq(x,2*b),', ') , seqg(Eq(x,8),', ') ),'can you do it?')
    print(question.execute())

def example3(x,y):
    permutable_part = perg( seqg(Eq(x,y),', ') , seqg(Eq(x,2*b),', ') , seqg(Eq(x,8),', ') )
    question = seqg(seqg('solve ',x,', '), permutable_part,'can you do it?')
    #
    x_eq_y = seqg(Eq(x,y),',')
    x_eq_2b = seqg(Eq(x,2*b),',')
    x_eq_8 = seqg(Eq(x,8),',')
    permutable_part = perg( x_eq_y , x_eq_2b , x_eq_8 )
    first_part = seqg('solve ',x,', ')
    question = seqg(first_part, permutable_part, 'can you do it?')
    print(question.execute())

example1()
example2(x,y,a,b)
