import unittest

from funcflow import *

class Test_problem(unittest.TestCase):

    def test_example1(self):
        question = seqg('solve x ,', perg( 'a = b, ' , 'x = 2*b, ' , 'x = 8, ' ),'can you do it?')
        print(question.execute())
        #self.assertEqual(question.execute(), 'solve x , a = b,  x = 2*b,  x = 8,  can you do it?' )

if __name__ == '__main__':
    unittest.main()
