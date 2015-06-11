import argparse
import subprocess

def importingargs():
    """
    importing args
    """
    parser = argparse.ArgumentParser(
        description="Searching the different first literals")
    parser.add_argument(
        "--inputfilepath", help="This is the filepath of input file")
    args = parser.parse_args()
    assert args.inputfilepath,"inputfilepath is not found"
    return args.inputfilepath

def countfilelines(inputfilepath):
    linenum = len([1 for line in open(inputfilepath,"r")])

    #: The correct number of line num of hightemp.txt
    correctlinenum = 24
    #: check the this program is correct or not
    assert linenum == correctlinenum,"This define is not correct"
    print("line:%s" % linenum)

def main():
    inputfilepath = importingargs()
    countfilelines(inputfilepath)

if __name__ == "__main__":
    main()
