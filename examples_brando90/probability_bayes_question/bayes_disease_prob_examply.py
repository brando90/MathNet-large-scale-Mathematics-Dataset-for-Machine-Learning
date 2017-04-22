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
    symptoms = ['shaky arm','runny nose','inflated cheek','sore arm','dry eye']
    symptoms += ['purple pinky finger','fever','fatigue','muscle aches','coughing']
    symptoms += ['joint warmth', 'hand numbness','watery eye','white tongue']
    return symptoms

def example():
    beginning_q = seqg( "Mathphobia", "is a rare disease in which the victim has the delusion that he or she is being subjected to intense examination." )
    perm1 = segq('A person selected uniformly at random has ','Mathphobia', ' with probability ', 0.2) #P(H)
    perm2 = segq('A person without ', 'Mathphobia','has ','shaky arm', 'with probability,' 0.5) # P(Symptom|No disease)
    perm3 = segq('A person with ', 'Mathphobia',' has ','shaky arm', ' with probability ,' 0.3) # P(Symptom|disease)
    end_q = segq('What is the probability that a person selected uniformly at random, ','Mathphobia',', given that he or she has','shaky arm','?')
    permutable_part = perg(perm1,perm2,perm3)

    assignments = {}
    assignments['Mathphobia'] = get_list_silly_diseases()
    assignments['shaky arm'] = symptoms_list()
    lb, ub = 0, 1
    assignments[0.2] = [random.uniform(lb, ub) for i in range(1000)]
    assignments[0.5] = [random.uniform(lb, ub) for i in range(1000)]
    assignments[0.5] = [random.uniform(lb, ub) for i in range(1000)]



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
