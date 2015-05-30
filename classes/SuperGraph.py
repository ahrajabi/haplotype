from .GNode import GNode
import copy
import random
from random import shuffle
class SuperGraph(object):
    Main = None

    def __init__(self, nodes):
        self.Main = GNode()
        self.addMultipleNodes(self.Main ,nodes ,'ORIGINAL')

    def test(self):
        obj = copy.deepcopy(self.Main)
        mini = 100000
        obj2 = obj
        self.Run(obj, 'greedy' , 'direct')
        obj.log("PERFORMANCE")
        for i in range(100): 
            obj = self.Reduce(obj , 'random', 0.1)
            self.Run(obj , 'greedy' , 'random')
            if len(obj.ArtificialNodes) < mini:
                mini = len(obj.ArtificialNodes)
            else:
                obj = obj2
            obj2 = obj
            obj.log("PERFORMANCE")
        print obj.ComponentNumber()

    def Run(self, obj, method, connectway):
        if method == "greedy":
            obj.Edges.sort()
            for e in obj.Edges:
                if not obj.set_same(e[1][0], e[1][1]):
                    obj.linkTwoNode(e[1][0], e[1][1], connectway)

        if method == "random":
            r = list(obj.Edges)

            shuffle(r)
            for e in r:
                 if not obj.set_same(e[1][0], e[1][1]):
                    obj.linkTwoNode(e[1][0], e[1][1], connectway)

    def Reduce(self, obj, method, numPercent):
          ret = copy.deepcopy(self.Main)
          if method == 'random':
              ArtNodes = list(obj.ArtificialNodes)
              shuffle(ArtNodes)
              number = int(len(ArtNodes) * numPercent)
              for i in ArtNodes[0:number]:
                  ret.addNode(obj.Nodes[i].String,'ARTIFICIAL')
              return ret







    def addMultipleNodes(self ,obj ,nodes, ntype):
        for i in nodes:
            obj.addNode(i, ntype)


