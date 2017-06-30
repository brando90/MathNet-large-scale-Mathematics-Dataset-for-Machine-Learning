from qagen import *
from qagen.qagen import *
import numpy as np

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
        #Q.args = locals() #so that we can access passed arguments for testing
        #define some short cuts
        seqg, perg, choiceg = s.seqg, s.perg, s.choiceg
        s.use_latex = True
        permutable_part = perg(seqg(Eq(x,x_val),','),seqg(Eq(y,y_val),','),seqg(Eq(z,z_val),','))
        #print(permutable_part)
        #pdb.set_trace()
        animal_list = perg( goats+',', lambs+',', dogs)
        question1 = seqg(Mary+' had ',
        permutable_part, animal_list,' respectively. Each was decreased by',Eq(d,d_val),'by the wolf named '+Gary+'.')
        q = choiceg(question1)
        return q

    def A(s, x_val,y_val,z_val,d_val, x,y,z,d,Mary,Gary,goats,lambs,dogs):
        #A.args = locals() #so that we can access passed arguments for testing 
        #define some short cuts
        seqg, perg, choiceg = s.seqg, s.perg, s.choiceg
        
        permutable_part = perg(seqg(Eq(x-d,x_val-d_val),','),seqg(Eq(y-d,y_val-d_val),','),seqg(Eq(z-d,z_val-d_val),','))
        animal_list = perg( goats+',', lambs+',', dogs)
        ans_vnl_vsympy = seqg(Mary+' has ',permutable_part, animal_list, 'left and each was decreased by the wolf named '+Gary+'.')
        ans_vnl_vsympy2 = seqg('The wolf named '+Gary+' decreased each of '+Mary+'\'s ',animal_list,' and she now has ',permutable_part,' ',animal_list,' left.')
        a = choiceg(ans_vnl_vsympy,ans_vnl_vsympy2)
        return a


