"""Utilities for parsing PTB text files."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import collections
import os
import pdb

import tensorflow as tf



def _read_words(filename):
    '''
    returns an array of strings with each word:

    E.g: ['solve', 'x', ',', 'Eq(a,', 'b)', ',', 'Eq(x,', '2*b)', ',', 'Eq(a,', '19)', ',', 'can', 'you', 'do', 'it?']
    '''
    # TODO: doesn't seem that its processing the equations correctly
    with tf.gfile.GFile(filename, "r") as f:
        return f.read().decode("utf-8").replace("\n", "<eos>").split()


def _build_vocab(filename):
    '''
    Makes dict mapping {(word,word_id)}.
    '''
    data = _read_words(filename) # array of words: ['solve', 'x', ',', 'Eq(a,', 'b)', ',', 'Eq(x,', '2*b)', ',', 'Eq(a,', '19)', ',', 'can', 'you', 'do', 'it?']

    counter = collections.Counter(data) # {word:count} creates a dictionary mapping word to counts: e.g. Counter({',': 4, 'Eq(a,': 2, 'solve': 1, 'x': 1, 'b)': 1, 'Eq(x,': 1, '2*b)': 1, '19)': 1, 'can': 1, 'you': 1, 'do': 1, 'it?': 1})
    word_to_occurance = counter.items() # counter.items() returns a list of dict's (key, value) tuple pairs e.g.dict_items([('solve', 1), ('x', 1), (',', 4), ('Eq(a,', 2), ('b)', 1), ('Eq(x,', 1), ('2*b)', 1), ('19)', 1), ('can', 1), ('you', 1), ('do', 1), ('it?', 1)])
    word_to_occurance_list = list(counter.items()) #    [ (word,count) ] unosrted list
    # sorts based on (minus) count number first then based on word
    count_pairs = sorted(word_to_occurance_list, key=lambda x: (-x[1], x[0])) # [ (word,count) ] sorted based on -count then on word e.g. [(',', 4), ('Eq(a,', 2), ('19)', 1), ('2*b)', 1), ('Eq(x,', 1), ('b)', 1), ('can', 1), ('do', 1), ('it?', 1), ('solve', 1), ('x', 1), ('you', 1)] key parameter to specify a function to be called on each list element prior to making comparisons.

    # The single star * unpacks the sequence/collection into positional arguments
    # zip pairs up element ith in one list with element ith in another. Sort of performing a transpose.
    words, _ = list(zip(*count_pairs)) # pairs up words, collect all the words, throw away the counts

    #makes a dict mapping words to their (arbitrary) id.
    word_to_id = dict(zip(words, range(len(words)))) # [(word,word_id)]
    return word_to_id


def _file_to_word_ids(filename, word_to_id):
    '''
    Convert a file to an array of its word ids if they exist in word_to_id.
    given file with 'Hello world' -> [id0,id1] where idk is an int.

    Args:
        filename -  file to get ids from
        word_to_id - dictionary mapping word to its id {word,word_id}
    '''
    data = _read_words(filename) # returns array of words ['word']
    return [word_to_id[word] for word in data if word in word_to_id]


def qa_raw_data(data_path,train_fname,val_fname,test_fname):
    """Load raw data from data directory "data_path".
    Reads text files, converts strings to integer ids,
    and performs mini-batching of the inputs.

    Args:
        data_path: string path to the directory where simple-examples.tgz has
            been extracted.
    Returns:
        tuple (train_data, valid_data, test_data, vocabulary)
        where each of the data objects can be passed to PTBIterator.
    """

    train_path = os.path.join(data_path, train_fname)
    valid_path = os.path.join(data_path, val_fname)
    test_path = os.path.join(data_path, test_fname)

    word_to_id = _build_vocab(train_path) # makes {(word,word_id)}
    train_data = _file_to_word_ids(train_path, word_to_id) # array of word is [word_id]
    valid_data = _file_to_word_ids(valid_path, word_to_id) # array of word is [word_id]
    test_data = _file_to_word_ids(test_path, word_to_id) # array of word is [word_id]
    vocabulary = len(word_to_id) # only need the length to know all the ids of the words
    
    return train_data, valid_data, test_data, vocabulary
