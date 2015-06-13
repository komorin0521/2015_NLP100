import argparse
import os

def importingargs():
    """
    importing args
    """
    parser = argparse.ArgumentParser(
        description="Mearge col1.txt and col2.txt using tab")
    parser.add_argument(
        "--col1filepath", help="this is the filepath of col1.txt")
    parser.add_argument(
        "--col2filepath", help="this is the filepath of col2.txt")
    parser.add_argument("--mergeshellfilepath",help="This is the filepath of mergefile by shell script")
    
    parser.add_argument("--outputfilepath",help="This is the filepath of outputfilepath")
    args = parser.parse_args()
    assert os.path.exists(args.col1filepath),"%s is not found" % args.col1filepath
    assert os.path.exists(args.col2filepath),"%s is not found" % args.col2filepath
    assert os.path.exists(args.mergeshellfilepath),"%s is not found" % args.mergefilepath

    return args.col1filepath,args.col2filepath,args.mergeshellfilepath,args.outputfilepath


def mergecol1andcol2usingtab(col1filepath,col2filepath):
    """
    This function is merging col1.txt and col2.txt using tab
    """
    #: read line col1(2).txt into line1col1(2) and merge these using tab
    mergelist = [ "%s\t%s\n" % (linecol1.strip(),linecol2.strip()) for linecol1,linecol2 in zip(open(col1filepath,"r"),open(col2filepath,"r")) ]

    return mergelist

def output(mergelist,mergeshellfilepath,outputfilepath):
    """
    outputting mergelist into outoutfilepath
    """

    #: cheking the result is correct or not
    mergelistshell = [ "%s\n" % line.strip() for line in open(mergeshellfilepath,"r")]
    assert mergelist == mergelistshell, "The program is not correct"

    with open(outputfilepath,"w") as outputfile:
        outputfile.write("".join(mergelist))


def main():
    print("Start")
    col1filepath,col2filepath,mergeshellfilepath,outputfilepath = importingargs()
    mergelist = mergecol1andcol2usingtab(col1filepath,col2filepath)
    output(mergelist,mergeshellfilepath,outputfilepath)
    print("Finished")

if __name__ == "__main__":
    main()
