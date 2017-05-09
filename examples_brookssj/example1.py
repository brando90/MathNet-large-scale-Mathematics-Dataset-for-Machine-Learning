# -*- coding: utf-8 -*-
"""
Created on Mon May  8 19:21:15 2017

@author: skyla
"""

import sys
sys.path.insert(0, 'C:\\Users\\skyla\\Desktop\\eit_proj1-master\\main_proj_lib\qaflow')
from sympy import *
import random

from qaflow import *
from qaflow.question_answer import *

def example1():
    ##find the determinant of A, A=({2, 3}, {1,5}), can you do it?
    question = seqg('')