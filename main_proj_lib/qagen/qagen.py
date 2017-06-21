import unittest

class QAFormat:

    def seed_all(self, seed):
        raise NotImplementedError

    def init_consistent_qa_variables(self, seed):
        raise NotImplementedError

    def init_qa_variables(self,*args,**kwargs):
        raise NotImplementedError

    def Q(self,*args,**kwargs):
        raise NotImplementedError

    def A(self,*args,**kwargs):
        raise NotImplementedError

class QAGen(QAFormat):

    def generate_MC(self,seed):
        self.seed_all(seed)
        # get variables for qq
        variables_consistent = self.init_consistent_qa_variables()
        variables = self.init_qa_variables()
        # set q and correct a
        q_str = self.Q(*variables,*variables_consistent)
        correct_a_str = self.A(*variables,*variables_consistent)
        # collect alternative answers
        ans_list = [correct_a_str]
        for i in range():
            #self.seed_all(seed)
            variables = self.init()
            a_str = self.A(*variables,*variables_consistent)
            ans_list.append(a_str)
        # randomize where the answer is
        args = random.sample( args, len(args) )
        mc = q_str, ans_list
        return mc

class TestStringMethods(unittest.TestCase):

    def test_MC(self):
        pass

if __name__ == '__main__':
    unittest.main()
