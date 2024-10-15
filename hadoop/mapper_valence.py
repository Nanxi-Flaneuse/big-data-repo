#!/usr/bin/env python
import sys, re
import random
from valence import clean_text, get_word_valence, get_sent_dict
import fileinput
import os



def main(argv):

    ##### to be uncommented ###########
    file = os.environ['mapreduce_map_input_file']
    prez_name = file[:-17]
    line = sys.stdin.readline()
    # pattern = re.compile("[a-zA-Z][a-zA-Z0-9]*")
    try:
        while line:
            # print(pattern.findall(line))
            line = clean_text(line).split()
            # print(line)
            for word in line:
                # print('adams' + "\t" + str(get_word_valence(word)))
                ##### to be uncommented ###########
                print(prez_name + "\t" + str(get_word_valence(word)))
            line = sys.stdin.readline()
    except EOFError as error:
        return None

if __name__ == "__main__":
    # print(sentiment_dictionary.keys())
    main(sys.argv)
    # print(os.environ['USER'])
