import numpy as np

class DemoMC(QA):

    def __init__(self, seed_pod):
        QA.__init__(self, seed_pod)
    
    def generate_mc_q(self, question_format_seed):
        np.random.seed(question_format_seed)

    def generate_mc_a(self, answer_format_seed):
        np.random.seed(answer_format_seed)
    
class DemoQuestion(DemoMC):

    def __init__(self, seed_pod):
        DemoMC.__init__(self, seed_pod)
   
    def create_question(self):#should generate question variables and output to generate_mc_q
    
    def create_answer(self):
 


