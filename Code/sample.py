
import sys
import random
import re
from histograms import histogram

source_code = 'word.txt'

def read(source_code):
    '''opens and splits word file '''
    with open(source_code, 'r') as file:
        words = file.read()
        # makes sure words are alphabets
        scrubbed_words= re.sub(r'[^a-zA-Z\s]', ' ' , words)
        words = scrubbed_words.split()
        return words

def random_word(words):
    '''randomizes words'''
    random_word = random.choice(words)
    return random_word

def sample_list(histogram):
    '''appends dictionary item to list'''
    words = []
    for key, value in histogram.items():
        for i in range(value):
            words.append(key)
    print(words)
    return words

def frequency(histogram, count):
    ''' checks random words in sample list then pulls out words from dictionary and increments '''
    new_dict = {}
    for i in range(count):
        random_words = random_word(sample_list(histogram))
        new_dict[random_words] = new_dict.get(random_words, 0) + 1

    print(new_dict)

if __name__ == "__main__":
    word_list = read(source_code)
    print(random_word(word_list))
    hist = histogram("word.txt")
    sample_list(hist)
    frequency(hist, 10)