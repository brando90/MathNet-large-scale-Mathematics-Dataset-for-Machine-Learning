# modified from the demo provided by https://github.com/Linusp/soph
from __future__ import print_function

import os
import re
import string
from itertools import dropwhile

import click
import numpy as np
from keras.layers.recurrent import GRU
from keras.layers.wrappers import TimeDistributed
from keras.models import Sequential, model_from_json
from keras.layers.core import Dense, RepeatVector

## LINUX
from pathlib import Path
import sys
from os.path import expanduser
home_path = expanduser("~")
# sys.path.insert(0, home_path + '/tensorflow_versions/tf-0.12.1/')
## 

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = 'models'

MAX_NUMEXAMPLE = 5000
X_FILE = home_path + '/Dropbox/eit_proj1_data/algebra1/make_var_subj_pilot/make_subject_pilot_problem_'
Y_FILE = home_path + '/Dropbox/eit_proj1_data/algebra1/make_var_subj_pilot/make_subject_pilot_soln_'
XY_FILE_EXT = '.txt'


MODEL_STRUCT_FILE = 'model_struct.json'
MODEL_WEIGHTS_FILE = 'model_weights.h5'
DATA_PATH = 'data'
# WORDS_FILE = 'words.txt'
BEGIN_SYMBOL = '^'
END_SYMBOL = '$'
CHAR_SET = set(string.digits + string.ascii_lowercase + BEGIN_SYMBOL + END_SYMBOL +  string.punctuation + ' ')
CHAR_NUM = len(CHAR_SET)
CHAR_TO_INDICES = {c:i for i, c in enumerate(CHAR_SET)}
INDICES_TO_CHAR = {i:c for c, i in CHAR_TO_INDICES.iteritems()}
MAX_INPUT_LEN = CHAR_NUM+1
MAX_OUTPUT_LEN = CHAR_NUM+1
NON_ALPHA_PAT = re.compile('[^a-z]')



def vectorize(word, seq_len, vec_size):
    vec = np.zeros((seq_len, vec_size), dtype=int)
    for i, ch in enumerate(word):
        vec[i, CHAR_TO_INDICES[ch]] = 1

    for i in range(len(word), seq_len):
        vec[i, CHAR_TO_INDICES[END_SYMBOL]] = 1

    return vec


def build_data():
    words_file = os.path.join(PROJECT_ROOT, DATA_PATH, WORDS_FILE)
    # words = [
    #     w.lower().strip() for w in open(words_file, 'r').readlines()
    #     if w.strip() != '' and not NON_ALPHA_PAT.findall(w.lower().strip())
    # ]
    words = []
    for ii in range(0, MAX_NUMEXAMPLE):
        if Path(X_FILE + str(ii) + XY_FILE_EXT).is_file():
            x_string = open(X_FILE + str(ii) + XY_FILE_EXT, 'r').read().lower()
            y_string = open(Y_FILE + str(ii) + XY_FILE_EXT, 'r').read().lower()
            words.append([x_string,y_string])
    
    plain_x = []
    plain_y = []
    for w in words:
        plain_x.append(BEGIN_SYMBOL + w[0])
        plain_y.append(BEGIN_SYMBOL + w[1])

    # train_x and train_y must be 3-D
    train_x = np.zeros((len(words), MAX_INPUT_LEN, CHAR_NUM), dtype=int)
    train_y = np.zeros((len(words), MAX_OUTPUT_LEN, CHAR_NUM), dtype=int)
    for i in range(len(words)):
        train_x[i] = vectorize(plain_x[i], MAX_INPUT_LEN, CHAR_NUM)
        train_y[i] = vectorize(plain_y[i], MAX_OUTPUT_LEN, CHAR_NUM)

    return train_x, train_y


def build_model_from_file(struct_file, weights_file):
    model = model_from_json(open(struct_file, 'r').read())
    model.compile(loss="mse", optimizer='adam')
    model.load_weights(weights_file)

    return model


def build_model(input_size, seq_len, hidden_size):
    """build a sequence to sequence model"""
    model = Sequential()
    model.add(GRU(input_dim=input_size, output_dim=hidden_size, return_sequences=False))
    model.add(Dense(hidden_size, activation="relu"))
    model.add(RepeatVector(seq_len))
    model.add(GRU(hidden_size, return_sequences=True))
    model.add(TimeDistributed(Dense(output_dim=input_size, activation="linear")))
    model.compile(loss="mse", optimizer='adam')

    return model


def save_model_to_file(model, struct_file, weights_file):
    # save model structure
    model_struct = model.to_json()
    open(struct_file, 'w').write(model_struct)

    # save model weights
    model.save_weights(weights_file, overwrite=True)


@click.group()
def cli():
    pass


@cli.command()
@click.option('--epoch', default=100, help='number of epoch to train model')
@click.option('-m', '--model_path', default=os.path.join(PROJECT_ROOT, MODEL_PATH), help='model files to save')
def train(epoch, model_path):
    x, y = build_data()
    indices = len(x) / 10
    test_x = x[:indices]
    test_y = y[:indices]
    train_x = x[indices:]
    train_y = y[indices:]

    model = build_model(CHAR_NUM, MAX_OUTPUT_LEN, 128)

    model.fit(train_x, train_y, validation_data=(test_x, test_y), batch_size=128, nb_epoch=epoch)

    struct_file = os.path.join(model_path, MODEL_STRUCT_FILE)
    weights_file = os.path.join(model_path, MODEL_WEIGHTS_FILE)

    save_model_to_file(model, struct_file, weights_file)



@cli.command()
@click.option('-m', '--model_path', default=os.path.join(PROJECT_ROOT, MODEL_PATH), help='model files to read')
@click.argument('word')
def test(model_path, word):
    struct_file = os.path.join(model_path, MODEL_STRUCT_FILE)
    weights_file = os.path.join(model_path, MODEL_WEIGHTS_FILE)

    model = build_model_from_file(struct_file, weights_file)

    x = np.zeros((1, MAX_INPUT_LEN, CHAR_NUM), dtype=int)

    # print(open(word, 'r').read())
     
    x_string = BEGIN_SYMBOL + open(word, 'r').read().lower() + END_SYMBOL
    
    # word = BEGIN_SYMBOL + word.lower().strip() + END_SYMBOL

    print('\n\nInput is: \n\n' + x_string + '\n\n')
    
    x[0] = vectorize(x_string, MAX_INPUT_LEN, CHAR_NUM)

    pred = model.predict(x)[0]

    print('Prediction is: \n\n') 
    
    print(pred)

    print([
        INDICES_TO_CHAR[i] for i in pred.argmax(axis=1)
        if INDICES_TO_CHAR[i] not in (BEGIN_SYMBOL, END_SYMBOL)
    ])
    
    print(''.join([
        INDICES_TO_CHAR[i] for i in pred.argmax(axis=1)
        if INDICES_TO_CHAR[i] not in (BEGIN_SYMBOL, END_SYMBOL)
    ]))


if __name__ == '__main__':
    cli()



