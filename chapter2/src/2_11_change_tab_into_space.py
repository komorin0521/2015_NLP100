import argparse
import os

def importingargs():
    """
    importing args
    """
    parser = argparse.ArgumentParser(
        description="Change tab into space")
    parser.add_argument(
        "--inputfilepath", help="This is the filepath of input file")
    parser.add_argument("--resultshellpath",help="This is the path of result shell script")
    parser.add_argument("--outputfilepath",help="This is the outputfilepath")
    args = parser.parse_args()
    assert os.path.exists(args.inputfilepath),"inputfilepath is not found"
    assert os.path.exists(args.resultshellpath),"%s is not found" % args.resultshellpath

    return args.inputfilepath,args.resultshellpath,args.outputfilepath

def changetabintospace(inputfilepath):
    resultlist = list()
    inputlist = [ line.strip() for line in open(inputfilepath,"r") ]
    for line in inputlist:
        line = line.split("\t")
        outstr = ""
        for item in line:
            outstr = outstr + item + " "
        outstr = outstr.strip()
        outstr = outstr + "\n"
        resultlist.append(outstr)

    return resultlist

def output(resultshellpath,outputfilepath,resultlist):

    resultshelllist = [ line for line in open(resultshellpath,"r") ]

    assert resultlist == resultshelllist,"This program is not correct"

    with open(outputfilepath,"w") as outputfile:
        outputfile.write("".join(resultlist))

def main():
    print("Start")
    inputfilepath,resultshellpath,outputfilepath = importingargs()
    resultlist = changetabintospace(inputfilepath)
    output(resultshellpath,outputfilepath,resultlist)
    print("Finished")

if __name__ == "__main__":
    main()
