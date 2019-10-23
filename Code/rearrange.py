import sys
import random

mylist=[]
# randomizes my list
def random_word(mylist):
    random.shuffle(mylist)
    return mylist

# adds word to list and then randomizes list
if __name__ == '__main__':
    for arg in range(1, len(sys.argv)):
        mylist.append(sys.argv[arg])

    mylist = random_word(mylist)

    print(mylist)
