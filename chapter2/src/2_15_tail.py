import argparse
import os


def importingargs():
    """
    importing args
    """
    parser = argparse.ArgumentParser(
        description="Extract head N lines")
    parser.add_argument(
        "--inputfilepath", help="This is the filepath of input file")
    parser.add_argument(
        "--resultshellpath", help="This is the path of result shell script")
    parser.add_argument("--outputfilepath", help="This is the outputfilepath")
    parser.add_argument("--tailnum", help="tail num", type=int)
    args = parser.parse_args()
    assert os.path.exists(
        args.inputfilepath), "%s is not found" % args.inputfilepath
    assert os.path.exists(
        args.resultshellpath), "%s is not found" % args.resultshellpath
    assert args.tailnum >= 0, "The tail num must be more than zero"

    return args.inputfilepath, args.resultshellpath, args.outputfilepath, args.tailnum


def exacttailnum(inputfilepath, tailnum):
    """
    Read the file and exact the tail num lines
    """
    #: reading the inputfile
    resultlist = [line for line in open(inputfilepath, "r")]
    tailnum = len(resultlist) - tailnum
    return resultlist[tailnum:]


def output(resultshellpath, outputfilepath, resultlist):
    """
    Checking the program correct or not and outputting
    """

    resultshelllist = [line for line in open(resultshellpath, "r")]

    #: Checking the program is correct or not
    assert resultlist == resultshelllist, "This program is not correct"

    with open(outputfilepath, "w") as outputfile:
        outputfile.write("".join(resultlist))


def main():
    print("Start")
    inputfilepath, resultshellpath, outputfilepath, tailnum = importingargs()
    resultlist = exacttailnum(inputfilepath, tailnum)
    output(resultshellpath, outputfilepath, resultlist)
    print("Finished")

if __name__ == "__main__":
    main()
