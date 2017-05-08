from sympy import *
import random

from qaflow import *
from qaflow.question_answer import *

'''
Mathphobia is a rare disease in which the victim has the delusion that he or she is being subjected to intense examination.
A person selected uniformly at random has Mathphobia with probability 0.228158.
A person without Mathphobia has shaky arm with probability 0.561340.
A person with Mathphobia has shaky arm with probability 0.883911.
What is the probability that a person selected uniformly at random has has Mathphobia, given that he or she has shaky arm?

'''

def get_list_silly_diseases():
    # TODO: one way to improve this could be to loop through some encyclopedia of words or something and have a bunch of phobia things.
    silly_disease_names = ['Mathphobia', 'Biophobia', 'Chemphobia','Enginerphobia']
    silly_disease_names += ['Brainphobia', 'CSphobia', 'Statsphobia','Probailityphobia']
    return silly_disease_names

def symptoms_list():
    symptoms = ['shaky arms','runny nose','inflated cheek','sore arm','dry eye']
    symptoms += ['purple pinky finger','fever','fatigue','muscle aches','coughing']
    symptoms += ['joint warmth', 'hand numbness','watery eye','white tongue']
    return symptoms

def example():
    disease = 'Mathphobia'
    symptom = 'shaky arms'
    p_d = 1.0/50
    p_s_d = 9.0/10
    p_s_nd = 1.0/20
    beginning_q = seqg( disease, "is a rare disease in which the victim has the delusion that he or she is being subjected to intense examination." )
    perm1 = segq('A person selected uniformly at random has ',disease, ' with probability ', p_d) #P(disease)
    perm2 = segq('A person without ', disease,'has ',symptom, 'with probability,' p_s_nd) # P(Symptom|No disease)
    perm3 = segq('A person with ', disease,' has ',symptom, ' with probability ,' p_s_d) # P(Symptom|disease)
    end_q = segq('What is the probability that a person selected uniformly at random, ',disease,', given that he or she has',symptom,'?')
    permutable_part = perg(perm1,perm2,perm3)

    assignments = {}
    assignments[disease] = get_list_silly_diseases()
    assignments[symptom] = symptoms_list()
    lb, ub = 0, 1
    assignments[p_d] = [random.uniform(lb, ub) for i in range(1000)]
    assignments[p_s_d] = [random.uniform(lb, ub) for i in range(1000)]
    assignments[p_s_nd] = [random.uniform(lb, ub) for i in range(1000)]
    question = seqg(beginning_q,permutable_part,end_q)
    #
    @func_flow
    def my_mult(a,b):
        return a*b
    #
    num = segq('( Pr[',symptom,'|',disease,']*','Pr[',disease,']' ) # Pr[S|D]*Pr[D]
    den2 = segq('Pr[',symptom,'])')
    den1 = segq('Pr[',symptom,'|',disease,']*Pr[',disease,']+Pr[',symptom,'| no',disease,']*Pr[ no',disease,']') # Pr[S] = Pr[S|D]*Pr[D] + Pr[S|nD]*Pr[nD]
    ans1 = seqg( num,'/',den1,'=',num,'/',den2 )
    possible_answers = [ans1]
    ans = choiceg(*possible_answers)

def example_make_dataset():
    '''
    Makes data set and saves
    '''
    #location = '/Users/brandomiranda/Dropbox (MIT)/eit_proj1_data/probability_example'
    location = '../../data'
    question_name = 'probability_disease_question'
    answer_name = 'probability_disease_answer'
    # TODO


if __name__ == '__main__':
    example()
