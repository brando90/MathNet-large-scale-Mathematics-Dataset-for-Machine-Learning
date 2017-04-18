import reader

def main():
    data_path = '/Users/brandomiranda/Dropbox (MIT)/eit_proj1_data/simple_algebra_question'
    filename = 'simple_algebra_question0'

    if not data_path:
        raise ValueError("Must set --data_path to PTB data directory")

    raw_data = reader.qa_raw_data(data_path)
    train_data, valid_data, test_data, _ = raw_data
    print(train_data)
    print(valid_data)
    print(test_data)


if __name__ == '__main__':
    main()
