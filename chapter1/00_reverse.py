#!/usr/bin/env python


def reverse(inputstr):
    strnum = len(inputstr)
    outlist = [ None for i in range(0,strnum) ]
    for i, s in enumerate(inputstr):
        outlist[strnum - (i+1) ] = s
    outstr = ''.join(outlist)
    return outstr

inputstr = 'stressed'

print(reverse(inputstr))
