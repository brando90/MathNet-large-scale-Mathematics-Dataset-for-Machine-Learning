from sympy import *
import unittest

from qagen.delayed_execution import *
#from . import qagen

def run_unit_test_for_user(qa_constructor,*args,user_defined_unit_test=None,**kwargs):
    '''
    Runs some tests to help the user have a reliable question answer class.

    qa_constructor = the users class name
    '''
    #TODO add feature user defined unit tests
    runner = unittest.TextTestRunner()
    #
    test_suite = unittest.TestSuite()
    # add tests
    # TODO: is it possible to not have to add tests individually like this but
    # instead just have one single class with the test rather than having to make
    # multiple classes for each test?
    test_suite.addTest( Test_author_and_description_and_keywords(qa_constructor,arg,kwargs) )
    test_suite.addTest( Test_basic_user_test(qa_constructor,arg,kwargs) )
    test_suite.addTest( Test_basic_uses_generators(qa_constructor,arg,kwargs) )
    test_suite.addTest( Test_seed_all_provides_variation(qa_constructor,arg,kwargs) )
    test_suite.addTest( Test_all_funcs_with_seed_are_deterministic(qa_constructor,arg,kwargs) )
    test_suite.addTest( Test_user_does_not_set_latex_flag_in_Q_or_A(qa_constructor,arg,kwargs) )
    test_suite.addTest( Test_user_has_random_np_faker_seeded(qa_constructor,arg,kwargs) )
    runner.run(test_suite)

class Test_author_and_description_and_keywords(unittest.TestCase):
    '''
    Tests that the author, description and keywords are not empty.
    '''

    def __init__(self,qa_constructor,args,kwargs):
        super().__init__()
        self.qa_constructor = qa_constructor
        self.args = args
        self.kwargs = kwargs

    def runTest (self):
        # test cases and run them
        self.test_author_and_description_and_keywords()

    def test_author_and_description_and_keywords(self):
        #print('---')
        qagenerator = self.qa_constructor()
        self.assertNotEqual(qagenerator.author, None)
        self.assertNotEqual(qagenerator.description, None)
        self.assertNotEqual(qagenerator.keywords, None)
        self.assertTrue(len(qagenerator.keywords) > 0)

class Test_basic_user_test(unittest.TestCase):
    '''
    Tests that the description question can be generated by the user's framework.
    '''

    def __init__(self,qa_constructor,args,kwargs):
        super().__init__()
        self.qa_constructor = qa_constructor
        self.args = args
        self.kwargs = kwargs

    def runTest (self):
        qagenerator = self.qa_constructor()
        qagenerator.debug = True
        q,a = qagenerator.get_single_qa(seed=1)
        #print(q)
        #print('>>qagenerator.generator_unit_test: ',qagenerator.generator_unit_test)
        self.assertEqual(qagenerator.description,q)

class Test_basic_uses_generators(unittest.TestCase):
    '''
    Tests that the user at least returns a generator (seqg,perg,choiceg).
    The goal of this test is to have users always use seqq, perg, choiceg,
    so that the framework can process the users arguments correctly.
    The user should not be concatenting strings by itself for example. users
    should not be using strings to represent equations only sympy. This test
    is aimed to help checking that.
    '''

    def __init__(self,qa_constructor,args,kwargs):
        super().__init__()
        self.qa_constructor = qa_constructor
        self.args = args
        self.kwargs = kwargs

    def runTest (self):
        qagenerator = self.qa_constructor()
        qagenerator.debug = False
        qagenerator.generator_unit_test = True
        q,a = qagenerator.get_single_qa(seed=1)
        #
        q_is_de = isinstance(q, DelayedExecution)
        a_is_de = isinstance(a, DelayedExecution)
        if q_is_de or a_is_de:
            gen_ops = 'seqg, perg, choiceg '
            warning_string = 'Your {} is not returning a {} generator. Make sure you do for the framework to work correctly.'
            if not q_is_de:
                #print(warning_string.join('question',gen_ops))
                raise ValueError(warning_string.format('question',gen_ops))
            if not a_is_de:
                #print(warning_string.join('answer',gen_ops))
                raise ValueError(warning_string.format('answer',gen_ops))
        self.assertEqual( type(q()),str )
        self.assertEqual( type(a()),str )
        #
        qagenerator.debug = True
        q,a = qagenerator.get_single_qa(seed=1)
        qs = q()
        self.assertEqual(qs,qagenerator.description)

class Test_seed_all_provides_variation(unittest.TestCase):
    '''
    Checks that different questions can be made (i.e. there is variation in creating q,a's)
    If this test does not pass it means that framework is not able to generate variation to
    your question for some reason. Usually it means you did not have all 3 seeding
    functions that the template provides.
    Note: this test checks that the user implemented seed all not ridicuously wrongly.
    '''
    def __init__(self,qa_constructor,args,kwargs):
        super().__init__()
        self.qa_constructor = qa_constructor
        self.args = args
        self.kwargs = kwargs

    def runTest (self):
        # TODO how do I stop hardcoding the tests here, just go over your
        qagenerator = self.qa_constructor()
        seed = 0 # random.randint()
        q_original,a_original = qagenerator.get_single_qa(seed=seed)
        for i in range(1,501):
            seed = i
            qagenerator._seed_all(seed)
            q,a = qagenerator.get_single_qa(seed=seed)
            self.assertNotEqual( q,q_original )
            self.assertNotEqual( a,a_original )

class Test_all_funcs_with_seed_are_deterministic(unittest.TestCase):
    '''
    Checks that given a seed the framework and your code indeed behave deterministically.
    If this does not pass then your code is random in a way the framework cannot
    control. This is bad.
    '''

    def __init__(self,qa_constructor,args,kwargs):
        super().__init__()
        self.qa_constructor = qa_constructor
        self.args = args
        self.kwargs = kwargs

    def runTest (self):
        print()
        # given the same seed that it always does the same thing if its deterministic
        for seed in range(5):
            qagenerator = self.qa_constructor()
            q_original,a_original = qagenerator.get_single_qa(seed=seed)
            for i in range(100):
                # set the same seed as the original
                qagenerator._seed_all(seed)
                # get variables for qa and register them for the current q,a
                variables, variables_consistent = qagenerator._create_all_variables()
                # get concrete qa strings
                q = qagenerator.Q(*variables,*variables_consistent)
                a = qagenerator.A(*variables,*variables_consistent)
                # should be the same as the original because it should be deterministic
                self.assertEqual( q,q_original )
                self.assertEqual( a,a_original )

class Test_user_does_not_set_latex_flag_in_Q_or_A(unittest.TestCase):
    '''
    Checks that the user is not artificially setting the latex flag within their
    implementation of Q or A.
    '''

    def __init__(self,qa_constructor,args,kwargs):
        super().__init__()
        self.qa_constructor = qa_constructor
        self.args = args
        self.kwargs = kwargs

    def runTest (self):
        qagenerator = self.qa_constructor()
        #
        seed = 0 # random.randint()
        original_latex_flag = qagenerator.use_latex
        q_original,a_original = qagenerator.get_single_qa(seed=seed)
        # the latex flag should still be as original
        self.assertEqual(original_latex_flag,qagenerator.use_latex)
        #
        qagenerator.use_latex = True
        seed = 1 # random.randint()
        original_latex_flag = qagenerator.use_latex
        q_original,a_original = qagenerator.get_single_qa(seed=seed)
        # the latex flag should still be as original
        self.assertEqual(original_latex_flag,qagenerator.use_latex)
        #
        qagenerator.use_latex = False
        seed = 2 # random.randint()
        original_latex_flag = qagenerator.use_latex
        q_original,a_original = qagenerator.get_single_qa(seed=seed)
        # the latex flag should still be as original
        self.assertEqual(original_latex_flag,qagenerator.use_latex)

class Test_user_has_random_np_faker_seeded(unittest.TestCase):
    '''
    Checks that the user is seeding random, faker and numpy.
    '''

    def __init__(self,qa_constructor,args,kwargs):
        super().__init__()
        self.qa_constructor = qa_constructor
        self.args = args
        self.kwargs = kwargs

    def runTest (self):
        # TODO write test for random and numpy.
        qagenerator = self.qa_constructor()
        # check that the symbols that are extracted are indeed different
        qag = self.qa_constructor()
        seed = 0
        qag._seed_all(seed)
        a1,b1 = qag.get_symbols(2)
        qag._seed_all(seed)
        qag.sympy_vars = [] # you need this because the qa stores things to avoid duplicates, so you need to clean it
        a2,b2 = qag.get_symbols(2)
        # since the seeding function should work, it should act deterministically
        self.assertEqual(a1,a2)
        self.assertEqual(b1,b2)
        # check
        qag = self.qa_constructor()
        seed = 0
        qag._seed_all(seed)
        original_nameA1,original_nameB1 = qag.get_names(2)
        qag._seed_all(seed)
        qag.names = [] # you need this because the qa stores things to avoid duplicates, so you need to clean it
        original_nameA2,original_nameB2 = qag.get_names(2)
        # since the seeding function should work, it should act deterministically
        self.assertEqual(original_nameA1,original_nameA2)
        self.assertEqual(original_nameB1,original_nameB2)


###

class Test_MC(unittest.TestCase):

    def __init__(self,qa_constructor,args,kwargs):
        super().__init__()
        self.qa_constructor = qa_constructor
        self.args = args
        self.kwargs = kwargs

    def runTest (self):
        # TODO
        pass

class Test_one_to_many_constant_format(unittest.TestCase):

    def __init__(self,qa_constructor,args,kwargs):
        super().__init__()
        self.qa_constructor = qa_constructor
        self.args = args
        self.kwargs = kwargs

    def runTest (self):
        # TODO
        pass

class Test_many_to_many(unittest.TestCase):

    def __init__(self,qa_constructor,args,kwargs):
        super().__init__()
        self.qa_constructor = qa_constructor
        self.args = args
        self.kwargs = kwargs

    def runTest (self):
        # TODO
        pass

class Test_random_modules_registered(unittest.TestCase):
    def __init__(self, qa_constructor, args, kwargs):
        super().__init__()
        self.qa_constructor = qa_constructor
        self.args = args
        self.kwargs = kwargs

    def runTest(self):
        pass

class Test_seeding_func(unittest.TestCase):
    def __init__(self, qa_constructor, args, kwargs):
        super().__init__()
        self.qa_constructor = qa_constructor
        self.args = args
        self.kwargs = kwargs

    def runTest(self):
        pass

class Test_generate_many_to_one_consistent_format(unittest.TestCase):
    def __init__(self, qa_constructor, args, kwargs):
        super().__init__()
        self.qa_constructor = qa_constructor
        self.args = args
        self.kwargs = kwargs

    def runTest(self):
        pass


    # it would be nice to add some tests where we create a lot of questions
    # and see if the users code breaks
    #
    #
    # def test_total_number_variables_is_larger_than_user_options(self):
    #     #TODO
    #     pass
    #
    # def test_total_number_variables_is_not_subset_than_user_options(self):
    #     #TODO
    #     pass

if __name__ == '__main__':
    unittest.main()
