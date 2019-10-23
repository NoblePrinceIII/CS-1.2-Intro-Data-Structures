import sys
import random

mylist=[]

def random_word(mylist):
    random.shuffle(mylist)
    return mylist


if __name__ == '__main__':
    for arg in range(1, len(sys.argv)):
        mylist.append(sys.argv[arg])

    print(mylist)

    mylist = random_word(mylist)

    print(mylist)
