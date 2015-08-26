# -*- coding:utf-8 -*-

import pprint
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

def extract_basic_info(inputlist):
    infodict = dict()
    tmp = None
    for item in inputlist:
        if re.match('}}',item):
            break
        else:
            if re.match('\|.*? = .*',item) is not None:
                tmp = re.match('\|.*? = .*',item).group(0)
                print(tmp)
                tmp = tmp.split(' = ')
                infodict[tmp[0].lstrip('\|')] = tmp[1].strip()
            else:
                if tmp is not None:
                    infodict[tmp[0].lstrip('\|')] =  infodict[tmp[0].lstrip('\|')] + '\n' + item
 
    return infodict

def output(outputfilepath,infodict):

    outstr = "{" + "\n"
    for k,v in infodict.items():
        outstr = outstr + k + " : " + v + "\n"
    outstr = outstr + "}"

    with open(outputfilepath,"w") as of:
        of.write(outstr)

def main():
    print("Start")
    inputfilepath, outputfilepath = importingargs()
    inputlist = importingfile(inputfilepath)
    infodict = extract_basic_info(inputlist)
    pprint.pprint(infodict)
    print(len(infodict.keys()))
    output(outputfilepath,infodict)
    print("Finish")

if __name__ == "__main__":
    main()

