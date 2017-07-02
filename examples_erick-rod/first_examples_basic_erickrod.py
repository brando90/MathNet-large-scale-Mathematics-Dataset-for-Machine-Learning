
from sympy import *
import random
import qaflow
from qaflow import *
from qaflow.question_answer import *
#Delay executions 
def example1():
    ## solve x,  a = b,  x = 2*b, a = 8, can you do it?
    R_1, R_2, R_3, R_4, R_5 = symbols('R_1 R_2 R_3 R_4 R_5')
    ques1 = seqg(Eq(R_1,R_2),', ')
    ques2 = seqg(Eq(R_1,128),', ')
    ques3 = seqg("1/",R_3," = ","1/",R_2," + ","1/",R_1,", ")
    question = seqg('solve ', R_3 ,', ', perg(ques1,ques2,ques3))
    answer = choiceg(seqg( R_3, ' = ',64), seqg(R_3,' = ',2**-1/128**-1),seqg( R_3 ,'= 128/2'))
    q,a = make_qa_pair(question,answer,seed=7)
    print('question: %s \nanswer: %s'%(q,a))
    
def example2():
    x,y,a,b,c,X = symbols('x y a b c X')
    
example1()