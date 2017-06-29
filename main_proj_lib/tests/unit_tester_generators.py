
class QA_unit_tester_example(QAGen):

    def __init__(self):
        '''
        Initializer for your QA question.
        '''
        super().__init__()
        self.author = 'unit_test'
        self.description = ''' '''
        # keywords about the question that could help to make this more searchable in the future
        self.keywords = ['unit_test']
        self.use_latex = True

    def seed_all(self,seed):
        random.seed(seed)
        np.random.seed(seed)
        self.fake.random.seed(seed)

    def init_consistent_qa_variables(self):
        if self.debug:
            x,y,z,d = symbols('x y z d')
            Mary, Gary = 'Mary', 'Gary'
            goats,lambs,dogs = 'goats','lambs','dogs'
        else:
            x,y,z,d = self.get_symbols(4)
            Mary, Gary = self.get_names(2)
            farm_animals = utils.get_farm_animals()
            goats,lambs,dogs = self.get_names(3,names_list=farm_animals)
        return x,y,z,d,Mary,Gary,goats,lambs,dogs

    def init_qa_variables(self):
        if self.debug:
            x_val,y_val,z_val = 2,3,4
            d_val = 1
        else:
            x_val,y_val,z_val = np.random.randint(1,1000,[3])
            d_val = np.random.randint(1,np.min([x_val,y_val,z_val]))
        return x_val,y_val,z_val,d_val

    def Q(s, x_val,y_val,z_val,d_val, x,y,z,d,Mary,Gary,goats,lambs,dogs):
        Q.args = locals() #so that we can access passed arguments for testing
        #define some short cuts
        seqg, perg, choiceg = s.seqg, s.perg, s.choiceg
        return

    def A(s, x_val,y_val,z_val,d_val, x,y,z,d,Mary,Gary,goats,lambs,dogs):
        A.args = locals() #so that we can access passed arguments for testing 
        #define some short cuts
        seqg, perg, choiceg = s.seqg, s.perg, s.choiceg
        #
        return


