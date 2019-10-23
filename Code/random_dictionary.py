import sys
import random

# opens text file from location 
f = open("/usr/share/dict/words", "r")

word_list=f.readlines()

# Checks words in list and prints randomize words in range
for i in range(int(sys.argv[1])):
    print(word_list[random.randint(0, len(word_list-1))] )