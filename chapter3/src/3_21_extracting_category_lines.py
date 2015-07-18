# -*- coding:utf-8 -*-

import argparse
import os

def importingargs():
    """
    importing args
    """
    parser = argparse.ArgumentParser(
        description="Reverse the file by DESC by col3")
    parser.add_argument(
        "--inputfilepath", help="This is the filepath of input file")
    parser.add_argument("--outputfilepath", help="This is the outputfilepath")

    args = parser.parse_args()
    assert os.path.exists(args.inputfilepath), "inputfilepath is not found"

    return args.inputfilepath, args.outputfilepath

def importingfile(inputfilepath):
    """
    Read file
    """
    with open(inputfilepath,"r") as f:
        inputlist = [ line.strip() for line in f.readlines() ]

    return inputlist

def extract_category_lines(inputlist):
    """
    Extracting of jsondata 
    """

    outputlist = [ line + "\n" for line in inputlist if 'Category' in line ]

    return outputlist

def output(outputfilepath,outputlist):
    """
    Outputting
    """

    with open(outputfilepath,"w") as of:
        of.write("".join(outputlist))

def main():
    print("Start")
    inputfilepath, outputfilepath = importingargs()
    inputlist = importingfile(inputfilepath)
    outputlist = extract_category_lines(inputlist)
    output(outputfilepath,outputlist)
    print("Finish")

if __name__ == "__main__":
    main()
