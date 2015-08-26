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

def remove_emphasis(line):
    if line.startswith("''",0) and line.endswith("''",0):
        return line.rstrip("'").lstrip("'")
    else:
        return line

def extract_basic_info(inputlist):
    infodict = dict()
    flag = False
    for item in inputlist:
        if flag is True:
            if item[0] == "|":
                item = item.lstrip("|").split("=")
                key = item[0].strip()
                value = item[1].strip()
                infodict[key] = remove(value)
            elif item[0] == "*":
                infodict[key] = infodict[key] + "\n" + item.strip()

            else:
                break

        elif "基礎情報" in item:
            flag = True


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
    output(outputfilepath,infodict)
    print("Finish")

if __name__ == "__main__":
    main()

