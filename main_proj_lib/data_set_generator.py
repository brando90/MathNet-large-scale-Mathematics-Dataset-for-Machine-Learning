import os
import sys
import glob
from qagen.qagen import *
from qagen import utils

def make_qa_to_data_set(path_to_qa, number_examples,qa_format_type, nb_questions=1, nb_answers=5):
    '''
    Generates a data set from a path to qa file.
    The type of q,a are generated according to the qa_format_type of qa's.
    Generates at most number_examples examples.
    The qa_format_type indicates if its a NL+Symy, vNL+vSymy, MC etc.
    '''
     
    # TODO The library should be careful of not generating repeated examples?
    # also there should not be a infinit loop if it keeps trying to generate
    # unique examples CHECK THIS.
    taxonomy_base = os.path.abspath('../math_taxonomy/')
    classes = utils.get_classes(os.path.join(taxonomy_base, path_to_qa))
    qa = classes[0]
    qa = qa()
    dataset = []
    for n in range(number_examples):
        #try:
            #generate qa based on format
        if qa_format_type == 'many_to_many':
            q, a = qa.generate_many_to_many(nb_questions=nb_questions, nb_answers=nb_answers, seed=n)
        elif qa_format_type == 'many_to_one':
            q, a = qa.generate_many_to_one(nb_questions=nb_questions, seed_output_format=n)
        #except:
            #print(str(qa) + 'skipped due to error')
        dataset.append((q, a)) 
    assert len(dataset) == len(set(dataset))
    return dataset 
    

def make_subject_to_data_set(path_to_folder,number_examples,qa_format_type, recursive=False, nb_questions=1, nb_answers=5):
     
    '''
    Generates data sets from a path to a math subject.
    The type of q,a are generated according to the qa_format_type of qa's.
    Generates at most number_examples examples. The library should be careful
    of not generating repeated examples? CHECK THIS.
    The qa_format_type indicates if its a NL+Symy, vNL+vSymy, MC etc.
    '''
    
    taxonomy_base = os.path.abspath('../math_taxonomy/')
    folder_path = os.path.join(taxonomy_base, path_to_qa)
    filenames = glob.iglob(folder_path+'*.py', recursive)
    dataset = []
    for filename in filenames:
        file_dataset = make_qa_to_data_set(filename, number_examples, qa_format_type)    
        dataset.append(file_dataset)
    return dataset


## utils

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

# old library
# def make_qa_to_data_set(question,answer,assignments,nb_data_points, location,question_fname,answer_fname,file_extension='.txt'):
#     '''
#     Creates a data set file based on question,answer given.
#     Data set files will be saved as location/question_name_id and location/answer_name_id.
#     '''
#     print('in make_qa_to_data_set')
#     for i in range(nb_data_points):
#         print('i ', i)
#         seed = int.from_bytes(os.urandom(4), sys.byteorder) # TODO do we need this?
#         q,a = make_qa_pair(question,answer,assignments,seed)
#         print(q,a)
#         #
#         loc_q = os.path.join(location,question_fname+str(i)+file_extension)
#         loc_a = os.path.join(location,answer_fname+str(i)+file_extension)
#         with open(loc_q,mode='w') as question_file, open(loc_a,mode='w') as answer_file:
#             question_file.write(q)
#             answer_file.write(str(a))
#
#
# def make_qa_to_data_set(question,answer,assignments,nb_data_points, location,question_fname,answer_fname,file_extension='.txt'):
#     '''
#     Creates a data set file based on question,answer given.
#     Data set files will be saved as location/question_name_id and location/answer_name_id.
#     '''
#     print('in make_qa_to_data_set')
#     for i in range(nb_data_points):
#         print('i ', i)
#         seed = int.from_bytes(os.urandom(4), sys.byteorder) # TODO do we need this?
#         q,a = make_qa_pair(question,answer,assignments,seed)
#         print(q,a)
#         #
#         loc_q = os.path.join(location,question_fname+str(i)+file_extension)
#         loc_a = os.path.join(location,answer_fname+str(i)+file_extension)
#         with open(loc_q,mode='w') as question_file, open(loc_a,mode='w') as answer_file:
#             question_file.write(q)
#             answer_file.write(str(a))

if __name__ == "__main__":
    #example of usage
    make_qa_to_data_set('mathematics/algebra/money_question.py', 1, 'many_to_one')    
