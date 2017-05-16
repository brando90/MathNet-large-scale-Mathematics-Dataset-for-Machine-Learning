# -*- coding: utf-8 -*-
"""
Created on Mon May 15 22:15:13 2017

@author: skyla
"""

from sympy import *
import random

from qaflow import *
from qaflow.question_answer import *

def example1():
    t,v,a=symbols('t v a')
    ##find the distance traveled in t seconds, initial velocity is v m/s, acceleration is a m/s^2
    #question = seqg('find the distance traveled in ', t , 'seconds: ','initial velocity is ', v, 'm/s, ','acceleration is ', a, 'm/s^2')
    vel_part = seqg('initial velocity is ', v)
    acc_part = seqg('acceleration is ', a, 'm/s^2')
    permutable_part = perg(vel_part, acc_part)
    question = seqg('find the distance traveled in ', t , 'seconds if ', permutable_part )
    assignments = {}
    sym_list=[t, v, a]
    for i in sym_list:
        assignments[i] = [random.randint(0,50) for j in range(100)]

    @func_flow
    def find_dist(t, v, a):
        return v*t+.5*a*t**2

    answer = find_dist(t, v, a)
    #q,a = make_qa_pair(question,answer,assignments, seed=2)
    q,a = make_qa_pair(question,answer,assignments)
    print('question: %s \nanswer: %s'%(q,a))

if __name__ == '__main__':
    example1()
