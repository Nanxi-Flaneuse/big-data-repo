#!/usr/bin/env python
import sys, re
import random
from valence import clean_text, get_word_valence, get_sent_dict, sentiment_dictionary
import fileinput
import os



def main(argv):
    # for line in fileinput.input():
    #     if fileinput.isfirstline():
    #         filename = fileinput.filename()
    #         print("Filename:", filename)
    file = os.environ['mapreduce_map_input_file']
    prez_name = file[:-17]
    line = sys.stdin.readline()
    # pattern = re.compile("[a-zA-Z][a-zA-Z0-9]*")
    try:
        while line:
            # print(pattern.findall(line))
            line = clean_text(line)
            # print(line)
            for word in line:
                print(prez_name + "\t" + str(get_word_valence(word, sentiment_dictionary)))
            line = sys.stdin.readline()
    except EOFError as error:
        return None

if __name__ == "__main__":
    # print(sentiment_dictionary.keys())
    main(sys.argv)
