# -*- coding:utf-8 -*-

import json
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

def import_jsonfile(inputfilepath):
    """
    Read file 
    """
    with open(inputfilepath,"r") as f:
        inputlist = [ line.strip() for line in f.readlines() ]

    return inputlist

def extract_target_json_data(inputlist, target):
    """
    Extracting of jsondata 
    """

    for tmpdata in inputlist:
        jsondata = json.loads(tmpdata)
        if jsondata['title'] == target:
            return jsondata['text']


def output(outputfilepath,outputdata):
    """
    Outputting
    """

    with open(outputfilepath,"w") as of:
        of.write(outputdata)

def main():
    print("Start")
    inputfilepath, outputfilepath = importingargs()
    inputlist = import_jsonfile(inputfilepath)
    outputdata = extract_target_json_data(inputlist,'イギリス')
    output(outputfilepath,outputdata)
    print("Finish")

if __name__ == "__main__":
    main()
