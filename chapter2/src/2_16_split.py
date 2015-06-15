import argparse
import os
import math

def importingargs():
    """
    importing args
    """
    parser = argparse.ArgumentParser(
        description="Split input file by line splitnum")
    parser.add_argument(
        "--inputfilepath", help="This is the filepath of input file")
    parser.add_argument(
        "--resultshelldir", help="This is the path of result shell dir which has results files")
    parser.add_argument("--resultpythondir", help="This is the output directory")
    parser.add_argument("--splitnum", help="split num", type=int)
    args = parser.parse_args()
    assert os.path.exists(
        args.inputfilepath), "%s is not found" % args.inputfilepath
    assert os.path.exists(
        args.resultshelldir), "%s is not found" % args.resultshelldir
    assert os.path.exists(args.resultpythondir), "%s is not exists" % args.resultpythondir

    assert args.splitnum >= 0, "The tail num must be more than zero"
 
    return args.inputfilepath, args.resultshelldir, args.resultpythondir, args.splitnum


def split(inputfilepath, splitnum):
    """
    Read the file and exact the tail num lines
    """
    #: reading the inputfile
    inputlist = [line for line in open(inputfilepath, "r")]
    filenum = int(math.ceil(len(inputlist) / splitnum))
    resultlist = list()
    resultlist = [ sorted(inputlist[i*splitnum:(i+1)*splitnum]) for i in range(0,filenum) ]

    return resultlist
        

def output(resultshelldir, resultpythondir, resultlist):
    """
    Checking the program correct or not and outputting
    """
    filenames = os.listdir(resultshelldir)
    resultshelllist = list()
    for filename in filenames:
        filepath = resultshelldir + filename
        tmpresultshelllsist = [ line for line in open(filepath,"r")]
        resultshelllist.append(sorted(tmpresultshelllsist))

    #: cheking the program is correct or not
    assert sorted(resultlist) == sorted(resultshelllist), "This program is not correct"

    for i in range(0,len(resultlist)):
        outputfilepath = "%sresult_python%02d.txt" % (resultpythondir,i) 
        with open(outputfilepath, "w") as outputfile:
            outputfile.write("".join(resultlist[i]))


def main():
    print("Start")
    inputfilepath, resultshelldir, resultpythondir, splitnum = importingargs()
    resultlist = split(inputfilepath, splitnum)
    output(resultshelldir, resultpythondir, resultlist)
    print("Finished")

if __name__ == "__main__":
    main()
