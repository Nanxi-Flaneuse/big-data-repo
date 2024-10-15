#!/usr/bin/env python
import sys, re
import random
from valence import clean_text, get_word_valence, get_sent_dict
import fileinput
import os

# is there something wrong with how I'm reading the file
# to precess all the prz speeches in hadoop, can I use tar files instead of untarring all of the tar files?

def main(argv):

    ##### to be uncommented ###########
    try:
        try:
            file = os.environ['mapreduce_map_input_file']
        except KeyError:
            file = os.environ['map_input_file']
        name = file.split('/')[-1]
        prez_name = name.split('_')[0]

    except:
        prez_name = 'adams'
    # prez_name = file[:-17]
    line = sys.stdin.readline()
    # pattern = re.compile("[a-zA-Z][a-zA-Z0-9]*")
    try:
        while line:
            line = clean_text(line).split()
            for word in line:
                # print("LongValueSum:" + 'adams' + "\t" + str(get_word_valence(word)))
                ##### to be uncommented ###########
                print("LongValueSum:" + prez_name + "\t" + str(get_word_valence(word)))
            line = sys.stdin.readline()
    except EOFError as error:
        return None

if __name__ == "__main__":
    # print(sentiment_dictionary.keys())
    main(sys.argv)
    # print(os.environ['USER'])


