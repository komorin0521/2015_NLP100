# -*- coding:utf-8 -*-

import argparse
import sys

def importingargs():
    """
    importing args
    """
    parser = argparse.ArgumentParser(description = "Searching the different first literals")
    parser.add_argument("--inputfilepath",help="This is the filepath of input file")
    parser.add_argument("--outputfilepath",help="This is the filepath of output file")
    args = parser.parse_args()
    return args.inputfilepath,args.outputfilepath

def importingfile(filepath):
    """
    import file
    """
    assert(filepath is not None)
    inputfile = open(filepath, "r")
    inputlist = list()
    for line in inputfile:
        inputlist.append(line.strip())
    return inputlist


def search_dif_first_char(inputlist):
    """
    searching the first different literals
    """
    difflist = list(set([item.split("\t")[0]+"\n" for item in inputlist]))
    return difflist


def outputting(outputfilepath, difflist):
    """
    outputting into outpufile
    """
    assert outputfilepath is not None,"outputfilepath is None"
    outputfile = open(outputfilepath, "w")
    outputfile.write("".join(difflist))
    outputfile.close()

def main():
    """
    main
    """
    print("START")
    inputfilepath, outputfilepath = importingargs()
    inputfile = importingfile(inputfilepath)
    diflist = search_dif_first_char(inputfile)
    outputting(outputfilepath, diflist)
    print("ALL FINISHED")

if __name__ == "__main__":
    main()
