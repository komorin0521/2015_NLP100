import argparse
import os

def importingargs():
    """
    importing args
    """
    parser = argparse.ArgumentParser(
        description="Split the columns and output the first colum into col1.txt and  the second colum into col2.txt")
    parser.add_argument(
        "--inputfilepath", help="This is the filepath of input file")
    parser.add_argument("--col1shellfilepath",help="This is the filepath of shell script col1")
    parser.add_argument("--col2shellfilepath",help="This is the filepath of shell script col2")
    args = parser.parse_args()
    assert args.inputfilepath, "inputfilepath is not found"
    assert args.col1shellfilepath,"col1shellfilepath is not found"
    assert args.col2shellfilepath,"col2shellfilepath is not found"
    return args.inputfilepath,args.col1shellfilepath,args.col2shellfilepath


def splitfilelines(inputfilepath):
    """
    read inputfile and split tab. Then the first colum into colums1 and the second column into colums2
    """

    columns1 = ["%s\n" % line.split("\t")[0]
                for line in open(inputfilepath, "r")]
    columns2 = ["%s\n" % line.split("\t")[1]
                for line in open(inputfilepath, "r")]

    return columns1, columns2


def output(columns1, columns2,col1shellfilepath,col2shellfilepath):
    """
    outputting colums1 into col1.txt and colums2 into col2.txt
    """

    #: cheking the result path "../result"
    resultpath = os.path.join("..", "result")
    if os.path.exists(resultpath) is False:
        os.mkdir(resultpath)

    #: output columns1 into col1.txt
    outputfilepathcolumns1 = os.path.join(resultpath, "col1.txt")
    with open(outputfilepathcolumns1, "w") as f1:
        f1.write("".join(columns1))

    #: output columns\2 into col2.txt
    outputfilepathcolumns2 = os.path.join(resultpath, "col2.txt")
    with open(outputfilepathcolumns2, "w") as f2:
        f2.write("".join(columns2))

    #: check the this program is correct or not
    outputcolumns1 = [ line for line in open(outputfilepathcolumns1, "r")]
    outputcolumns2 = [ line for line in open(outputfilepathcolumns2, "r")]

    columns1_correctlist = [ line for line in open(col1shellfilepath,"r") ]
    columns2_correctlist = [ line for line in open(col2shellfilepath,"r") ]


    assert sorted(outputcolumns1) == sorted(columns1_correctlist), "col1.txt is not correct"
    assert sorted(outputcolumns2) == sorted(
        columns2_correctlist), "col2.txt is not correct"


def main():
    print("Start")
    inputfilepath,col1shellfilepath,col2shellfilepath = importingargs()
    columns1, columns2 = splitfilelines(inputfilepath)
    output(columns1, columns2,col1shellfilepath,col2shellfilepath)
    print("Finished")

if __name__ == "__main__":
    main()
