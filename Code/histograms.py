# import sys
# import re

# # # opens file
# f = 'word.txt'
# file=open(f)


# source_text = 'word.txt'

# def book(source_text):
#     '''Opens text file and arranges words into a readable list '''    
#     #Opens text file
#     with open (source_text, 'r') as f:
#         words = f.read()
#         scrubbed_words = re.sub(r'[^a-zA-Z\s]', '', words)
#     return scrubbed_words.split(" ")


# def histogram():
#     '''returns dictionary'''
#     di = dict()
#     for lin in file:
#         lin = lin.rstrip()
#         wds = lin.split()
#     # print(wds)
#         for w in wds:
#             if w in di:
#                 di[w] = di[w] + 1
#             else:
#                 di[w]=1
#             print(w, di[w])

#     print(di)


# def histogram_list(source_text):
#     '''Takes text argument and returns a histogram data structure in a list form'''
#     words = book(file)
#     histogram = []

#     for word in words:
#         for item in histogram:
#             if item[0] == word:
#                 item[1] += 1
#                 break
#         else: histogram.append([word, 1])
#     return histogram

# histogram_list(source_text)
import sys
import re

source_code= 'word.txt'

def book(source_code):
    '''Opens text file and arranges words into a readable list '''    
    #Opens text file
    with open (source_code, 'r') as f:
        words = f.read()
        scrubbed_words = re.sub(r'[^a-zA-Z\s]', '', words)
    return scrubbed_words.split(" ")


def histogram(source_code):
    '''Takes text argument and returns a histogram data structure in a dictionary form'''
    histogram = {}
    words = book(source_code) 
    for word in words:
        histogram[word] = histogram.get(word, 0) + 1 
    return histogram

def histogram_list(source_code):
    '''histogram returns list'''
    words = book(source_code)
    histogram = []
    for word in words:
        for item in histogram:
            if item[0] == word:
                item[1] += 1
                break
        else: histogram.append([word, 1])
    return histogram

def histogram_tuples(source_code):
    '''histogram returns tuples'''
    words = histogram_list(source_code)
    histogram = []

    for item in words:
        histogram.append(tuple(item))

    return histogram


def unique_words(source_code):
    ''' returns the total count of unique words in the histogram '''
    histogram = {}

    words = book(source_code)

    for word in words:
        if word in histogram:
            histogram[word] = histogram[word] + 1
        else: 
            histogram[word] = 1
    print(len(histogram))

def frequency():
    pass

if __name__ == '__main__':
    unique_words(source_code)
     
    