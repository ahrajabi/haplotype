#!/bin/python

import numpy
from assist import *
from GNode import *

par = []
node = []
details = {}

cat = []

def decodeFile(filename):
    cnt2 = 0
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
    details , node = decodeFile('file.txt')
    obj = GNode()
    obj.addNode('111' , 'original')
    obj.addNode('000' , 'original')
    obj.addNode('110' , 'original')
    '''
    for i in node:
        obj.addNode( i , 'original' )
'''

    print obj.Node
'''
    HammingDistance = []   
    for cnt , i in enumerate(node):
        par.append( cnt)
        cat.append(True)


    for cnt1 , i in enumerate(node):
        for cnt2, j in enumerate(node):
            if cnt2 > cnt1 :
                HammingDistance.append( (hamming_distance(i , j) ,  i , j , cnt1 , cnt2 , 0))
    HammingDistance.sort()
    for cnt , i in enumerate(HammingDistance):
        if i[0] < 2 and not set_same(par , i[3] , i[4]) :
            set_merge(par , cat , i[3] , i[4] )

    mainn = GNode(node , par , cat)
    mainn2 = GNode(node , par , cat )

    mainn.linkComponents( 'MST' )
    mainn.printLog()

    mainn2.linkComponents()
    mainn2.printLog()
''' 


if __name__ == '__main__' : 
    main()
    print "Done, :)"



