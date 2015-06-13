# -*- coding:utf-8 -*-

import argparse
import os

def importingargs():
    """
    importing args
    """
    parser = argparse.ArgumentParser(
        description="Searching the different first literals")
    parser.add_argument(
        "--inputfilepath", help="This is the filepath of input file")
    parser.add_argument(
        "--diffcol1shellfilepath", help="This is the filepath of diffcol1shellfilepath")
    parser.add_argument(
        "--outputfilepath", help="This is the filepath of output file")
    args = parser.parse_args()
    assert os.path.exists(args.inputfilepath),"%s is not found" % args.inputfilepath
    assert os.path.exists(args.diffcol1shellfilepath), "%s is not found" % args.diffcol1shellfilepath

    return args.inputfilepath, args.diffcol1shellfilepath,args.outputfilepath


def importingfile(filepath):
    """
    import file
    """
    assert(filepath is not None)
    inputlist = [ line.strip() for line in open(filepath,"r") ]
    return inputlist


def search_diff_first_literal(inputlist):
    """
    searching the first different literals
    """
    difflist = list(set([item.split("\t")[0] + "\n" for item in inputlist]))

    return difflist


def outputting(outputfilepath, diffcol1shellfilepath,difflist):
    """
    outputting into outpufile
    """
    
    #: read the line col1 list from diffcol1shellfilepath
    diffshelllist = [ "%s\n" % line.strip() for line in open(diffcol1shellfilepath,"r") ]

    #: check the program is correct or not
    assert sorted(difflist) == sorted(diffshelllist),"This program is not correct"
    
    with open(outputfilepath,"w") as outputfile:
        outputfile.write("".join(difflist))

def main():
    """
    main
    """
    print("START")
    inputfilepath, diffcol1shellfilepath,outputfilepath = importingargs()
    inputfile = importingfile(inputfilepath)
    difflist = search_diff_first_literal(inputfile)
    outputting(outputfilepath, diffcol1shellfilepath,difflist)
    print("ALL FINISHED")

if __name__ == "__main__":
    main()
