


class QAGen:

    def generate_MC(seed):
        variables_consistent = self.init_consistent(seed)
        q_str = self.Q(*variables,*variables_consistent,seed)
        ans_list = []
        for i in range():
            variables = Init(seed)
            a_str = A(*variables,*variables_consistent,seed)
            ans_list.append(a_str)
        mc = q_str, ans_list
        return mc
