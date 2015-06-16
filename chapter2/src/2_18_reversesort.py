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
    parser.add_argument(
        "--resultshellpath", help="This is the path of result shell script")
    parser.add_argument("--outputfilepath", help="This is the outputfilepath")
    args = parser.parse_args()
    assert os.path.exists(args.inputfilepath), "inputfilepath is not found"
    assert os.path.exists(
        args.resultshellpath), "%s is not found" % args.resultshellpath

    return args.inputfilepath, args.resultshellpath, args.outputfilepath


def reversesortbycol3(inputfilepath):
    """
    Read the file and sort by DESC by col3
    """
    resultlist = list()
    #: reading the inputfile
    inputlist = [line.split("\t") for line in open(inputfilepath, "r")]

    inputlist.sort(key = lambda x:x[2],reverse = True)

    resultlist = list()
    for itemlist in inputlist:
        tmpnum = 0
        outstr = ""
        for item in itemlist:
            tmpnum = tmpnum +1
            if tmpnum != len(itemlist):
                outstr = outstr + item + "\t"
            else:
                outstr = outstr + item
        resultlist.append(outstr)

    return resultlist

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
    inputfilepath, resultshellpath, outputfilepath = importingargs()
    resultlist = reversesortbycol3(inputfilepath)
    output(resultshellpath, outputfilepath, resultlist)
    print("Finished")

if __name__ == "__main__":
    main()
