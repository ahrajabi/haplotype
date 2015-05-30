
class SingleNode(object):
        def __init__(self):
            self._NID = None
            self._TYPE = 0
            self._PARENT = None
            self._EDGES = list()
            self._STRING = None
        
        def show(self, value):
            if value == "Details":
                s = str(self.NID) + ": " + self.String + "("+str(self.Parent)+")" + "-" + self.Type
            elif value == "Edges":
                s = str()
                for n, i in enumerate(self.Edges):
                    s+= str(n) + '(' + str(i) + ') '

            return s
        
        @property
        def Type(self):
            return {0:"NEW", 1:"ORIGINAL", 2:"ARTIFICIAL", -1:"DELETED"}[self._TYPE]
        @Type.setter
        def Type(self, value):
            self._TYPE = {"NEW":0, "ORIGINAL":1, "ARTIFICIAL":2, "DELETED":-1}[value]

        @property
        def Parent(self):
            return self._PARENT

        @Parent.setter
        def Parent(self, value):
            self._PARENT = value
        @property
        def Edges(self):
            return self._EDGES

        @property
        def String(self):
            return self._STRING
        @String.setter
        def String(self, value):
            self._STRING = value

        @property
        def NID(self):
            return self._NID
        @NID.setter
        def NID(self, value):
            self._NID = value
        
        def addEdge(self, ONode):
            if self.Edges != None:
                diff = sum(ch1 != ch2 for ch1, ch2 in zip(self.String, ONode.String))
                self.addEdgeValue(ONode.NID, diff)
                ONode.addEdgeValue(self.NID, diff)

        def addEdgeValue(self , ONID , diff):
            if ONID > len(self.Edges)-1 :
                self.Edges.extend((ONID-len(self.Edges)+1)*[0])
            self.Edges[ONID] = diff


        def DistanceTo(self, ONID):
            return self.Edges[ONID]







