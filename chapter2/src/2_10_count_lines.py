import argparse
import os

def importingargs():
    """
    importing args
    """
    parser = argparse.ArgumentParser(
        description="Searching the different first literals")
    parser.add_argument(
        "--inputfilepath", help="This is the filepath of input file")
    parser.add_argument("--linesnum",help="This is the lines num",type=int)
    args = parser.parse_args()
    assert args.inputfilepath,"inputfilepath is not found"
    assert type(args.linesnum) == int, "linesnum must be int"
    return args.inputfilepath,args.linesnum

def countfilelines(inputfilepath,linesnumshell):
    #: count the lines num
    linesnum = len([1 for line in open(inputfilepath,"r")])

    #: check the this program is correct or not
    assert linesnum == linesnumshell,"This define is not correct"
    print("lines num by shell  : %s" % linesnumshell)
    print("lines num by python : %s" % linesnum)

def main():
    inputfilepath,linesnum = importingargs()
    countfilelines(inputfilepath,linesnum)

if __name__ == "__main__":
    main()
