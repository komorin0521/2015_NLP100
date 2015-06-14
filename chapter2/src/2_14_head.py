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
    parser.add_argument("--headnum", help="head num", type=int)
    args = parser.parse_args()
    assert os.path.exists(
        args.inputfilepath), "%s is not found" % args.inputfilepath
    assert os.path.exists(
        args.resultshellpath), "%s is not found" % args.resultshellpath
    assert args.headnum >= 0, "The head num must be more than zero"

    return args.inputfilepath, args.resultshellpath, args.outputfilepath, args.headnum


def exactheadnum(inputfilepath, headnum):
    """
    Read the file and exact the hedanum lines
    """
    #: reading the inputfile
    resultlist = [line for line in open(inputfilepath, "r")]

    return resultlist[:headnum]


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
    inputfilepath, resultshellpath, outputfilepath, headnum = importingargs()
    resultlist = exactheadnum(inputfilepath, headnum)
    output(resultshellpath, outputfilepath, resultlist)
    print("Finished")

if __name__ == "__main__":
    main()
