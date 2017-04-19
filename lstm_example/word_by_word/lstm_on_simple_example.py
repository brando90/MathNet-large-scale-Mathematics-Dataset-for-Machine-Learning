import reader

import pdb

flags = tf.flags

flag_name = 'model'
default_value = 'small'
docstring = "A type of model. Possible options are: small, medium, large."
flags.DEFINE_string(flag_name,default_value,docstring)

FLAGS = flags.FLAGS

class SmallConfig(object):
"""Small config."""
    init_scale = 0.1
    learning_rate = 1.0
    max_grad_norm = 5
    num_layers = 2
    num_steps = 20
    hidden_size = 200
    max_epoch = 4
    max_max_epoch = 13
    keep_prob = 1.0
    lr_decay = 0.5
    batch_size = 20
    vocab_size = 10000

def get_config():
    if FLAGS.model == "small":
        return SmallConfig()

def main():
    #if not FLAGS.data_path:
    #    raise ValueError("Must set --data_path to PTB data directory")
    data_path = '/Users/brandomiranda/Dropbox (MIT)/eit_proj1_data/data'
    train_fname,val_fname,test_fname = 'ptb.train.txt', 'ptb.valid.txt', 'ptb.test.txt'
    data_path = '/Users/brandomiranda/Dropbox (MIT)/eit_proj1_data/simple_algebra_question'
    train_fname,val_fname,test_fname = 'simple_algebra_question0.txt', 'simple_algebra_question1.txt', 'simple_algebra_question2.txt'
    if not data_path:
        raise ValueError("Must set --data_path to PTB data directory")

    # converts the data sets into array of word id's
    # [word_id],[word_id],[word_id], vocabulary
    train_data, valid_data, test_data, vocabulary = reader.qa_raw_data(data_path,train_fname,val_fname,test_fname) # each data set is returned in a word id array

    config = get_config()
    eval_config = get_config()
    eval_config.batch_size = 1
    eval_config.num_steps = 1

    with tf.Graph().as_default():
        minval, maxval = -config.init_scale, config.init_scale
        initializer = tf.random_uniform_initializer(minval, maxval)





if __name__ == '__main__':
    #main()
    tf.app.run()
