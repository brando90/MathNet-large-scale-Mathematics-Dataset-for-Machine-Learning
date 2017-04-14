import unittest
from sympy import *

from funcflow import *

class Test_problem(unittest.TestCase):

    def test_example1(self):
        question = seqg('solve x ,', perg( 'a = b, ' , 'x = 2*b, ' , 'a = 8, ' ),'can you do it?')
        print(question.execute())
        #self.assertEqual(question.execute(), 'solve x , a = b,  x = 2*b,  a = 8,  can you do it?' )

    def test_example2(self):
        x,y,a,b = symbols('x y a b')
        ## solve x,  a = b,  x = 2*b, a = 8, can you do it?
        question = seqg(seqg('solve ',x,', '), perg( seqg(Eq(a,b),', ') , seqg(Eq(x,2*b),', ') , seqg(Eq(a,8),', ') ),'can you do it?')
        print(question.execute())

    def test_example3(self):
        x,y,a,b = symbols('x y a b')
        #
        permutable_part = perg( seqg(Eq(a,b),', ') , seqg(Eq(x,2*b),', ') , seqg(Eq(a,8),', ') )
        question = seqg(seqg('solve ',x,', '), permutable_part,'can you do it?')
        #
        a_eq_b = seqg(Eq(a,b),',')
        x_eq_2b = seqg(Eq(x,2*b),',')
        a_eq_8 = seqg(Eq(a,8),',')
        permutable_part = perg( a_eq_b , x_eq_2b , a_eq_8 )
        first_part = seqg('solve ',x,', ')
        question = seqg(first_part, permutable_part, 'can you do it?')
        print(question.execute())

    def test_example_subs_seq(self):
        x,y,a,b = symbols('x y a b')
        e,f,g,h = symbols('e f g h')
        ## solve x,  a = b,  x = 2*b, a = 8, can you do it?
        question = seqg(seqg('solve ',x,', '), seqg( seqg(Eq(a,b),', ') , seqg(Eq(x,2*b),', ') , seqg(Eq(a,8),', ') ),'can you do it?')
        assigments = {a:[e,f,g,h]}
        print(question.execute(assigments))

    def test_example_subs(self):
        x,y,a,b = symbols('x y a b')
        e,f,g,h = symbols('e f g h')
        ## solve x,  a = b,  x = 2*b, a = 8, can you do it?
        question = seqg(seqg('solve ',x,', '), perg( seqg(Eq(a,b),', ') , seqg(Eq(x,2*b),', ') , seqg(Eq(a,8),', ') ),'can you do it?')
        assigments = {a:[e,f,g,h]}
        print(question.execute(assigments))

if __name__ == '__main__':
    unit_test = Test_problem()
    #unittest.main()
    unit_test.test_example_subs_seq()
