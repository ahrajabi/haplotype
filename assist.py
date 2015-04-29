import datetime


def hamming_distance(s1, s2):
    if len(s1) != len(s2):
        raise ValueError("Undefined for sequences of unequal length, {} and {}" , s1 , s2)
    return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))

'''
def set_print_components(node , par):
    text_file = open('log/node_{}.txt'.format(datetime.datetime.now()) , 'a' )
    label = False
    for cnt in range(len(node)+5):
        label = False
        for cnt2 , j in enumerate(node):
            if set_find(par , cnt2) == cnt:
                if label == False:
                    label = True
		    text_file.write("\n%d\n" % cnt)
		text_file.write("{0} {1}\n".format(cnt2 , j  ))
    text_file.close()
    
'''
def connect(nid1 , nid2 ):
	ret = []
	if len(nid1) != len(nid2) :
		raise ValueError("Connect: Two string are not equal size.")
	nidl1 = list(nid1)
	nidl2 = list(nid2)
	for it, (ch1,ch2) in enumerate( zip(nidl1 , nidl2) ):
		if ch1 != ch2 :
			nidl1[it] = ch2;
			ret.append(''.join(nidl1))
	ret.pop()
	return ret

def dfs_connect( mat , mark , i  ):
	mark[i] = 1
	for j in mat[i]:
		if mark[j] == 0:
			dfs_connect(mat , mark , j )

def isConnect( node ):
	nodeSize = len(node)
	mat = list()
	for i in range(nodeSize):
		temp = list()
		for j in range(nodeSize):
			if i != j and hamming_distance( node[i] , node[j] ) < 2 :
				temp.append(j)
		mat.append(temp)
	comp = 0
	mark = [0]*nodeSize
	for i in range(nodeSize):
		if mark[i] == 0:
			comp += 1
			dfs_connect(mat , mark , i )
	return comp



