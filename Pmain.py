#!/bin/python

import sys
from classes.GNode import *
from classes.SuperGraph import *
import pprint

def decodeFile(filename):
    cnt2 = 0
    details = dict()
    node = list()
    ff = open( filename , 'r')
    for cnt , i in enumerate(ff.readlines()):
        if cnt == 0:
            details['NumberOfHaplo'] = int(i)
        elif cnt == 1:
            details['LenghtOfHaplo'] = int(i)
        elif cnt == 2:
            details['Base'] = int(i)
        elif(len(i) > 1) :
            t = False
            tt = i.rstrip('\n')

            for nn in node:
                if tt == nn:
                    t = True

            if t == False:
                cnt2 += 1
                node.append(tt)
    return details , node


def main():
    details , nodes = decodeFile('sample/file.txt')

    sol = SuperGraph(nodes)
    sol.test()

if __name__ == '__main__' : 
    main()
    print "Done, :)"



