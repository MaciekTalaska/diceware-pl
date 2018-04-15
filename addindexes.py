#! /usr/bin/env python3

import math
import itertools
import sys

def generate_dice_index_sequence(num_dices):
    digits = "123456"
    for index in itertools.product(digits, repeat=num_dices):
        s = ''.join(index)
        yield s

def get_file_lines_count(file):
    num_lines = sum(1 for lines in file)
    file.seek(0,0)
    return num_lines

def calculate_index_size(count):
    return int(math.ceil(math.log(count,6)))

def write_output(outputfile, collection):
    for (k,v) in collection:
        line = "{0}\t{1}".format(k,v)
        outputfile.write(line)
        print(line)
    file.close(outputfile)

def main(inputfilename):
    inputfile = open(inputfilename, "r")
    outputfilename = inputfilename + ".out"
    outputfile = open(outputfilename, "w")
    words_count = get_file_lines_count(inputfile)
    index_size = calculate_index_size(words_count)
    collection = zip(generate_dice_index_sequence(index_size), inputfile.readlines())
    print("collection size: {0}", len(collection))
    write_output(outputfile, collection)
    inputfile.close()

if __name__ == "__main__":
    if (len(sys.argv)) < 2:
        print("please provide input file name!")
        sys.exit(1)
    main(sys.argv[1])
