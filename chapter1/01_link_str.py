#!/usr/bin/env python
#coding:utf-8

import sys

def add_str(str1, str2):
    if len(str1) != len(str2):
        raise NameError('str1 and str2 is not same length')
        sys.exit(1)
    else:
        outstr = ''
        num = len(str1)
        for i in range(0, num):
            outstr += str1[i] + str2[i]
        return outstr

x = 'パトカー'
y = 'タクシー'

print(add_str(x,y))
