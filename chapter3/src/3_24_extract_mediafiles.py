# -*- coding:utf-8 -*-

import argparse
import os
import re

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


#def extract_mediafiles(inputlist):
#    outputlist = [ tmp.split(":")[1].split("|")[0] + "\n" for tmp in inputlist if tmp.startswith("ファイル",0) ]
#    return outputlist

def extract_mediafiles(inputlist):

    outputlist = [ re.match('.*?(File|ファイル).*?\.(jpg|jpeg|svg)',tmp,re.I).group(0).split(':')[1] for tmp in inputlist if re.match('.*?(File|ファイル).*?\.(jpg|jpeg|svg)',tmp,re.I) ]

    return outputlist

def output(outputfilepath,outputlist):
    with open(outputfilepath,"w") as of:
        of.write("\n".join(outputlist))

def main():
    print("Start")
    inputfilepath, outputfilepath = importingargs()
    inputlist = importingfile(inputfilepath)
    outputlist = extract_mediafiles(inputlist)

    output(outputfilepath,outputlist)
    print("Finish")

if __name__ == "__main__":
    main()

