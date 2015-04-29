from assist import *
import random
import datetime
class GNode:
	def __init__(self):
		self.Node = dict()
		self.ParentCounter = 0

	def addNode(self , nstring , ntype):
		new = dict()
		new['string'] = nstring
		new['type'] = ntype
		self.ParentCounter += 1
		new['parent'] = self.ParentCounter
		new['edge'] = dict()

		for otherId , other in self.Node.iteritems():
		    new['edge'][otherId] = hamming_distance(other['string'] , new['string'] )
               	self.Node[self.ParentCounter] = new
                print self.Node
                '''
                for otherId , other in self.Node.iteritems():
                    if otherId is not self.ParentCounter and self.Node[self.ParentCounter]['edge'][otherId] == 1 and not self.set_same( self.ParentCounter , otherId ) :
                        self.set_merge( self.ParentCounter , otherId )
               '''

        def set_find(self , y):
            if self.Node[y] == y:
                return y
            self.Node[y]['parent'] =  self.set_find( self.Node[y]['parent'] )
            return self.Node[y]['parent']

        def set_same(self , x , y ):
            return self.set_find(x) == self.set_find(y)

        def set_merge(self , x , y):
            self.Node[ self.set_find(x) ]['parent'] = self.set_find(y)

'''
	
	def getParents(self):
		ret = list()
		for i in range(self.NodeNumber):
			if self.Cat[i] == True:
				ret.append(i)
		return ret

	def linkTwoComponents(self , nid1 , nid2 ):
		if set_same(self.node[] , nid1 , nid2):
			raise ValueError("Two parents are on same components.")
		else:
			addedNodes =  connect(self.Node[nid1] , self.Node[nid2] )
			added = list()

			for addedNode in addedNodes:
				if addedNode in self.Node:
					continue

				added.append(addedNode)
				self.addNode(addedNode)
			#todo
			self.ExtraNode[(nid1 , nid2)] = added
	

	def linkComponents(self , linkType = 'random'):
		if linkType == 'MST':
			edge = []
			for cnt1 , i in enumerate(self.Node):
				for cnt2 , j in enumerate(self.Node):
					if cnt2 > cnt1 :
						edge.append((hamming_distance(i,j) , i , j , cnt1 , cnt2 ))
			edge.sort()
			for cnt , i in enumerate( edge  ):
				if not set_same(self.Par , i[3] , i[4]):
					self.linkTwoComponents( i[3] , i[4]  )
			return



		NodeSize = len(self.Node)
		Parents = list(self.getParents())
		r = list(range(NodeSize))
		t = list(range(NodeSize))
		random.shuffle(r)
		random.shuffle(Parents)
		
		for parx in Parents:
			random.shuffle(r)
			for y in r:
				if not set_same(self.Par , parx , y ):
					x = 1
					for i in t:
						if set_same(self.Par , parx , i ):
							x = i
							break
					print datetime.datetime.now()
					self.linkTwoComponents(x , y )
					break


	def printLog(self):
		text_file = open("log/output.txt" , "a")
		text_file.write("\n\n - - NEW PRINT LOG - - \n")
		text_file.write("Number of Nodes {}\n".format(self.NodeNumber))
		text_file.write("Parents Are {}\n ".format(self.getParents()))
		set_print_components(self.Node , self.Par)
		text_file.write("\nParents are: \n")
		for cnt1 , i in  enumerate(self.Par):
			text_file.write( "({0} : {1}) ".format( cnt1 , i ))

		text_file.write("\nExtraNode are:\n")
		for i , j in self.ExtraNode.items():
			text_file.write("{0}:{1}\n".format(i , len(j)))
		text_file.write("\nNumber of components: {}\n".format(isConnect(self.Node)))
		text_file.close()


'''
