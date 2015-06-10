# -*- coding:utf-8 -*-

import argparse


def importingargs():
    """
    importing args
    """
    parser = argparse.ArgumentParser(
        description="Searching the different first literals")
    parser.add_argument(
        "--inputfilepath", help="This is the filepath of input file")
    parser.add_argument(
        "--outputfilepath", help="This is the filepath of output file")
    args = parser.parse_args()
    return args.inputfilepath, args.outputfilepath


def importingfile(filepath):
    """
    import file
    """
    assert(filepath is not None)
    inputfile = open(filepath, "r")
    inputlist = list()
    for line in inputfile:
        inputlist.append(line.strip())
    inputfile.close()
    assert inputfile.closed, "input file is not closed"

    return inputlist


def search_diff_first_literal(inputlist):
    """
    searching the first different literals
    """
    difflist = list(set([item.split("\t")[0] + "\n" for item in inputlist]))
    assert sorted(difflist) == sorted(["愛知県\n", "愛媛県\n", "岐阜県\n", "群馬県\n", "高知県\n", "埼玉県\n",
                                       "山形県\n", "山梨県\n", "静岡県\n", "千葉県\n", "大阪府\n", "和歌山県\n"]), "result is not correct"
    return difflist


def outputting(outputfilepath, difflist):
    """
    outputting into outpufile
    """
    assert outputfilepath is not None, "outputfilepath is None"
    outputfile = open(outputfilepath, "w")
    outputfile.write("".join(difflist))
    outputfile.close()
    assert outputfile.close, "output file is not closed"


def main():
    """
    main
    """
    print("START")
    inputfilepath, outputfilepath = importingargs()
    inputfile = importingfile(inputfilepath)
    difflist = search_diff_first_literal(inputfile)
    outputting(outputfilepath, difflist)
    print("ALL FINISHED")

if __name__ == "__main__":
    main()
