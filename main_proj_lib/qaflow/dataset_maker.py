import os
import sys
from qaflow.question_answer import *

def make_and_check_dir(path):
    '''
        tries to make dir/file, if it exists already does nothing else creates it.
    '''
    try:
        os.makedirs(path)
    except OSError:
        # uncomment to make it raise an error when path is not a directory
        #if not os.path.isdir(path):
        #    raise
        pass

def make_qa_to_data_set(question,answer,assignments,nb_data_points, location,question_name,answer_name):
    '''
    Creates a data set file based on question,answer given.
    Data set files will be saved as location/question_name_id and location/answer_name_id.
    '''
    print('in make_qa_to_data_set')
    for i in range(nb_data_points):
        print('i ', i)
        seed = int.from_bytes(os.urandom(4), sys.byteorder) # TODO do we need this?
        q,a = make_qa_pair(question,answer,assignments,seed)
        print(q,a)
        #
        loc_q = location+'/'+question_name+str(i)
        loc_a = location+'/'+answer_name+str(i)
        with open(loc_q,mode='w') as question_file, open(loc_a,mode='w') as answer_file:
            question_file.write(q)
            answer_file.write(str(a))
