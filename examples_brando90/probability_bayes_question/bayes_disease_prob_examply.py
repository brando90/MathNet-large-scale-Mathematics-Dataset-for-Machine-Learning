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

def example():

    part1 = seqg( "Mathphobia", "is a rare disease in which the victim has the delusion that he or she is being subjected to intense examination." )
    perm1 = segq('A person selected uniformly at random has','Mathphobia', 'with probability ', 0.2)
    permutable_part = perg(perm1,perm2,perm3)

    assignments = {}
    assignments["Mathphobia"] = get_list_silly_diseases()
    assignments[0.2] = get_list_prob_vals()
    pass


def example_make_dataset():
    '''
    Makes data set and saves to dropbox
    '''
    location = '/Users/brandomiranda/Dropbox (MIT)/eit_proj1_data/probability_example'
    question_name = 'probability_disease_question'
    answer_name = 'probability_disease_answer'
    # TODO


if __name__ == '__main__':
    example()
