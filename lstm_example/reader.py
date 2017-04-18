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
  data = _read_words(filename) # array of words: ['solve', 'x', ',', 'Eq(a,', 'b)', ',', 'Eq(x,', '2*b)', ',', 'Eq(a,', '19)', ',', 'can', 'you', 'do', 'it?']
  #pdb.set_trace()

  counter = collections.Counter(data)
  pdb.set_trace()
  count_pairs = sorted(counter.items(), key=lambda x: (-x[1], x[0]))

  words, _ = list(zip(*count_pairs))
  word_to_id = dict(zip(words, range(len(words))))

  return word_to_id


def _file_to_word_ids(filename, word_to_id):
  data = _read_words(filename)
  return [word_to_id[word] for word in data if word in word_to_id]


def qa_raw_data(data_path=None):
  """Load raw data from data directory "data_path".
  Reads text files, converts strings to integer ids,
  and performs mini-batching of the inputs.
  The dataset comes from Tomas Mikolov's webpage:
  http://www.fit.vutbr.cz/~imikolov/rnnlm/simple-examples.tgz
  Args:
    data_path: string path to the directory where simple-examples.tgz has
      been extracted.
  Returns:
    tuple (train_data, valid_data, test_data, vocabulary)
    where each of the data objects can be passed to PTBIterator.
  """

  train_path = os.path.join(data_path, "simple_algebra_question0.txt")
  valid_path = os.path.join(data_path, "simple_algebra_question1.txt")
  test_path = os.path.join(data_path, "simple_algebra_question2.txt")

  word_to_id = _build_vocab(train_path)
  train_data = _file_to_word_ids(train_path, word_to_id)
  valid_data = _file_to_word_ids(valid_path, word_to_id)
  test_data = _file_to_word_ids(test_path, word_to_id)
  vocabulary = len(word_to_id)


  return train_data, valid_data, test_data, vocabulary
