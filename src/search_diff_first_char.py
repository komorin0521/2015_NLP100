# -*- coding:utf-8 -*-

import sys


def importingargs():
    """
    importing args
    """
    args = sys.argv
    for arg in args[1:]:
        arg = arg.split("=")
        if arg[0] == "--inputfilepath":
            inputfilepath = arg[1]
        elif arg[0] == "--outputfilepath":
            outputfilepath = arg[1]
        else:
            print(arg[0]+"is not acceptable")
            sys.exit()
    return inputfilepath, outputfilepath


def importingfile(filepath):
    """
    import file
    """
    if filepath == None:
        print("File path is not defined")
        sys.exit()
    else:
        inputfile = open(filepath, "r")
    return inputfile


def search_dif_first_char(inputfile):
    """
    searching difference of first character
    """
    diflist = list()
    for line in inputfile.readlines():
        line = line.strip()
        if (line[0:3] in diflist) == False:
            diflist.append(line[0:3])
    return diflist


def outputting(outputfilepath, diflist):
    """
    outputting into outpufile
    """
    outputfile = open(outputfilepath, "w")

    for item in diflist:
        outputfile.write(item + "\n")
    outputfile.close()


def main():
    """
    main
    """
    print("START")
    inputfilepath, outputfilepath = importingargs()
    inputfile = importingfile(inputfilepath)
    diflist = search_dif_first_char(inputfile)
    outputting(outputfilepath, diflist)
    print("ALL FINISHED")

if __name__ == "__main__":
    main()
