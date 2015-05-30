import random
import sys
import pprint
import heapq
from .Node import SingleNode

class GNode(object):
    def __init__(self):
        self.Nodes = list()
        self.ParentCounter = 0
        self.ArtificialNodes = list()
        self.Edges = list()
        self.Details = {'ARTIFICIAL':0,'ORIGINAL':0}

    def addNode(self, nstring, ntype):
        if self.isExistNode(nstring) == True:
            return
        new = SingleNode()
        new.String = nstring
        new.Type = ntype
        new.NID = new.Parent = len(self.Nodes)
        self.Nodes.append(new)

        if ntype == 'ARTIFICIAL' :
            self.ArtificialNodes.append(new.NID)

        self.Details[ntype] += 1

        for NID, Node in enumerate(self.Nodes):
            self.Nodes[new.NID].addEdge(Node)
            weight = self.Nodes[new.NID].Edges[NID]
            if weight > 0 :
                self.Edges.append( (weight ,sorted([NID , new.NID])))
            
        for NID, Node in enumerate(self.Nodes):
            if NID != new.NID and new.DistanceTo(NID) == 1 and not self.set_same(NID, new.NID):
                self.set_merge(new.NID, NID)

    def isExistNode(self, nstring):
        for NID, Node in enumerate(self.Nodes):
            if Node.Type != "DELETED" and Node.String == nstring:
                ValueError("This node is exist")
                return True
        return False

    def set_find(self, y):
        if self.Nodes[y].Parent == y:
            return y
        self.Nodes[y].Parent = self.set_find(self.Nodes[y].Parent)
        return self.Nodes[y].Parent

    def set_same(self, x, y):
        return self.set_find(x) == self.set_find(y)

    def set_merge(self, x, y):
        self.Nodes[self.set_find(x)].Parent = self.set_find(y)
    def ComponentNumber(self):
        s = set()
        for i , n in enumerate(self.Nodes):
            s.add(self.set_find(i))
        print s
        return len(s)
            
        
    def size(self):
        return sys.getsizeof(self)

    def linkTwoNode(self, nid1, nid2, lType):
        if self.set_same(nid1,nid2):
            raise ValueError("Two parents are on same components.")
        elif self.Nodes[nid1].Type == 'DELETED' or self.Nodes[nid2].Type == 'DELETED' :
            raise ValueError("One of the node was removed before.")
        else:
            if lType == 'direct':
                nidl1 = list(self.Nodes[nid1].String)
                nidl2 = list(self.Nodes[nid2].String)
                for i, (s1, s2) in enumerate(zip(nidl1 ,nidl2)):
                    if s1 != s2:
                        nidl1[i] = s2
                        self.addNode(''.join(nidl1), "ARTIFICIAL")

            if lType == 'random': #TODO: Not worked

                nidl1 = list(self.Nodes[nid1].String)
                nidl2 = list(self.Nodes[nid2].String)
                shu = zip(nidl1, nidl2, range(len(nidl1)))
                random.shuffle(shu)
                for (_S1, _S2, indi) in shu:
                    if _S1 != _S2:
                        nidl1[indi] = _S2
                        self.addNode(''.join(nidl1), "ARTIFICIAL")






    def log(self , ltype ):
        if ltype == "CLEAR":
            open('log/log' , 'w').close()
        if ltype == "NODE":
            logfile = open('log/log' , "a")
            for i in self.Nodes:
                print i.show("Details")
        #        print i.show("Edges")
                print ""
            logfile.close()
        if ltype == "PERFORMANCE":
            print self.Details


