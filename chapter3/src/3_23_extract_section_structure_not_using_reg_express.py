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

def extract_section(line):
    """
    Extract section level
    """
    sec_lv = 1
    while(True):
        if line.startswith("="*(sec_lv+1),0) and line.endswith("="*(sec_lv+1),0):
            sec_lv = sec_lv +1
            flag = True
        else:
            sec_lv = sec_lv -1
            break

    if sec_lv == 0:
        return False
    else:
        outstr = str(sec_lv) + ":" + line.split("=")[sec_lv+1] + "\n"
        return outstr

def extract_section_structure(inputlist):
    outputlist = [ extract_section(tmp) for tmp in inputlist if extract_section(tmp) ]
    return outputlist

def output(outputfilepath,outputlist):
    with open(outputfilepath,"w") as of:
        of.write("".join(outputlist))

def main():
    print("Start")
    inputfilepath, outputfilepath = importingargs()
    inputlist = importingfile(inputfilepath)
    outputlist = extract_section_structure(inputlist)
    output(outputfilepath,outputlist)
    print("Finish")

if __name__ == "__main__":
    main()

