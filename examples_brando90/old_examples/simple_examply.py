from sympy import *
import random

from qaflow import *
from qaflow.question_answer import *

def example1():
    ## solve x,  a = b,  x = 2*b, a = 8, can you do it?
    question = seqg('solve x ,', perg( 'a = b, ' , 'x = 2*b, ' , 'x = 8, ' ),'can you do it?')
    answer = choiceg( 'x = 2*8', 'x = 16', 'x = 2*8 = 16' )
    q,a = make_qa_pair(question,answer,seed=3)
    print('question: %s \nanswer: %s'%(q,a))

def example2():
    x,y,a,b, X = symbols('x y a b X')
    e,f,g,h = symbols('e f g h')
    ## solve x,  a = b,  x = 2*b, a = 8, can you do it?
    question = seqg(seqg('solve ',x,', '), perg( seqg(Eq(a,b),', ') , seqg(Eq(x,2*b),', ') , seqg(Eq(a,8),', ') ), 'can you do it?')
    ## pssible alternative replacements for symbols
    replacements = {}
    replacements[a] = [a,e,f,g,h]
    replacements[x] = [x,X]
    replacements[8] = [random.randint(0,200) for i in range(100)]
    ## generator for a choice of answer
    ans1 = seqg(x,' = ',2,'*',8)
    ans2 = seqg(x,'=',2,'*',8)
    answer = choiceg( ans1,ans2 )
    q,a = make_qa_pair(question,answer,replacements,seed=4)
    print('question: %s \nanswer: %s'%(q,a))


def example3():
    x,y,a,b, X = symbols('x y a b X')
    e,f,g,h = symbols('e f g h')
    ## solve x,  a = b,  x = 2*b, a = 8, can you do it?
    question = seqg(seqg('solve ',x,', '), perg( seqg(Eq(a,b),', ') , seqg(Eq(x,2*b),', ') , seqg(Eq(a,8),', ') ), 'can you do it?')
    ## pssible alternative replacements for symbols
    replacements = {}
    replacements[a] = [a,e,f,g,h]
    replacements[x] = [x,X]
    replacements[8] = [random.randint(0,200) for i in range(100)]
    ## possible answer(s)
    ans1 = seqg(x,' = ',2,'*',8)
    ans2 = seqg(x,'=',2,'*',8)
    ans3 = DelayedExecution(lambda a,b: a*b,2,8)
    @func_flow
    def my_mult(a,b):
        return a*b
    ans4 = seqg(x, ' = ', seqg( my_mult(2,8) ) )
    ## generator for a choice of answer
    answer = choiceg( ans1,ans2,ans3,ans4 )
    q,a = make_qa_pair(question,answer,replacements,seed=5)
    #print('question: %s \nanswer: %s'%(q,a))
    return question,answer,replacements

def example4():
    '''
    Makes data set and saves to dropbox
    '''
    print('--> Making data set')
    # specify where to save it and name of question and answer
    location = '/Users/brandomiranda/Dropbox (MIT)/eit_proj1_data/simple_algebra_question'
    question_name = 'simple_algebra_question'
    answer_name = 'simple_algebra_answer'
    # makes directory structure if it doesn't exist already
    make_and_check_dir(path=location)
    # get question, answer parameters
    nb_data_points = 500
    question,answer,replacements = example3()
    # make data set
    make_qa_to_data_set(question,answer,replacements,nb_data_points, location,question_name,answer_name)


if __name__ == '__main__':
    #example1()
    #example2()
    #example3()
    example4()
