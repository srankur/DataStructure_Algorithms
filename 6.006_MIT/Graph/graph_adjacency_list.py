import queue


WHITE = 'white'
GRAY  = 'gray'
BLACK = 'black'

'''
Disjoint Set Properties and actions
1# CREATE-SET(x) – creates a new set with one element {x}.

2# MERGE-SETS(x, y) – merge into one set the set that contains element x and the set that contains element y 
(x and y are in different sets). The original sets will be destroyed.

3# FIND-SET(x) – returns the representative or a pointer to the representative of the set that contains element x.

'''

def MakeSet(node):
    node.parent = node
    node.rank = 0

def find(node):
    if node.parent == node:
        return node
    else:
        node.parent = find(node.parent)
        return node.parent


def union(node_x, node_y):
    x_root = find(node_x)
    y_root = find(node_y)

    if x_root.rank > y_root.rank:
        y_root.parent = x_root
    elif x_root.rank < y_root.rank:
        x_root.parent = y_root
    elif x_root != y_root:
        y_root.parent = x_root
        x_root.rank += 1


class vertex():
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        self.distance = 0
        self.color = WHITE
        self.predecessor = None
        self.discovery_time = 0
        self.finish_time = 0

    def addNeighbour(self, nbr, weight = 0):
        self.connectedTo[nbr] = weight

    def getId(self):
        return self.id

    def getConnections(self):
        return self.connectedTo.keys()

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

    def setDistance(self, distance):
        self.distance = distance

    def getDistance(self):
        return self.distance

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def setPredecessor(self, Predecessor):
        self.predecessor = Predecessor

    def getPredecessor(self):
        return self.predecessor

    def set_discovery_time(self,time):
        self.discovery_time = time

    def get_discovery_time(self):
        return self.discovery_time

    def set_finish_time(self, time):
        self.finish_time = time

    def get_finish_time(self):
        return self.finish_time

#    def __str__(self):
 #       return str(self.id) + ' Connected to -> ' + str([x.id for x in self.connectedTo])


class Graph():
    def __init__(self):
        self.vertList = {}
        self.NumofVertices = 0
        self.time = 0

    def addVertex(self,key):
        newVertex = vertex(key)
        self.vertList[key] = newVertex
        self.NumofVertices += 1
        return newVertex

    def addEdge(self, sourceVertex, nbrVertex, Cost = 0):
        if sourceVertex not in self.vertList:
            nv = self.addVertex(sourceVertex)
        if nbrVertex not in self.vertList:
            nv = self.addVertex(nbrVertex)
        self.vertList[sourceVertex].addNeighbour(self.vertList[nbrVertex],Cost)

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

    def BFS(self, graph, startVertex):
        vertexQ = queue.Queue()
        startVertex.setDistance(0)
        startVertex.setPredecessor(None)
        vertexQ.put(startVertex)
        while (vertexQ.qsize() >0):
            current_vertex = vertexQ.get()
            for nbr in current_vertex.getConnections():
                if nbr.getColor() is WHITE:
                    nbr.setColor(GRAY)
                    nbr.setDistance(current_vertex.getDistance() + 1)
                    nbr.setPredecessor(current_vertex)
                    vertexQ.put(nbr)
            print("ID:%s " % current_vertex.getId())
            current_vertex.setColor(BLACK)


    def dfs_rec(self):
        for avertex in self:
            avertex.setColor(WHITE)
            avertex.setPredecessor(-1)

        for avertex in self:
            if avertex.getColor() is WHITE:
                self._dfs_rec(avertex)

    def _dfs_rec(self,startvertex):
        #print(("DFS_INT::Vertex %s, color %s") % (startvertex.getId(), startvertex.getColor()))
        startvertex.setColor(GRAY)
        #print("Node:%s" % (startvertex))
        self.time += 1
        for next_vertex in startvertex.getConnections():
            next_vertex.setPredecessor(startvertex)
            if next_vertex.getColor() == WHITE:
                #print("DFS_INT::Pred:%s -> Node:%s" % (next_vertex.getPredecessor(), next_vertex.getId()))
                self._dfs_rec(next_vertex)
        startvertex.setColor(BLACK)
        startvertex.set_finish_time(self.time)


    def cycle_detection_rec(self):
        for avertex in self:
            avertex.setColor(WHITE)
            avertex.setPredecessor(-1)
        for avertex in self:
            if avertex.getColor() is WHITE:
                cycle = self._cycle_detection_rec(avertex)
                if cycle.items() :
                    for k, v in cycle.items():
                        print("Cycle @: %s -> %s" % (k, v))



    def _cycle_detection_rec(self,start_vertex):
        cycle = {}
        start_vertex.setColor(GRAY)
        for next_vertex in start_vertex.getConnections():
            #next_vertex.setPredecessor(start_vertex)
            if next_vertex.getColor() is WHITE:
                next_vertex.setPredecessor(start_vertex)
                potentialcycle = self._cycle_detection_rec(next_vertex)
                if potentialcycle.items():
                    cycle = potentialcycle
            elif next_vertex.getColor() is GRAY:
                next_vertex.setPredecessor(start_vertex)
                cycle[next_vertex.getId()] = [next_vertex.getPredecessor().getPredecessor().getId(),next_vertex.getPredecessor().getId(),next_vertex.getId()]
                print(cycle)
                #return cycle
        start_vertex.setColor(BLACK)
        return cycle




    '''
    Using by Rank: check whether a graph is cyclic or not. And helps connect or join two subsets.
    Find => Subroutine of union to check if the elements belong to a different set or if the sets are disjoint 
     
    '''
    def KruskalMST(self):
        result =[]
        #Step-1: Sort all the edge on the weighted order
        Edges = []
        for vertex_key, vertex_object in self.vertList.items():
            for nbr_vertice, distance in vertex_object.connectedTo.items():
            #Preparing a new list of Edge Taking Vertex object from graph, Key(nbr)From vertex and its distance
               Edges.append((vertex_object,nbr_vertice , distance))
        sorted_edges = sorted(Edges, key=lambda item: item[2])


        #Create subset of each vertex.

        [MakeSet(value) for value in self.vertList.values()]


        for i,(x,y,w) in enumerate(sorted_edges):
            print("SortedEdge: { %s }----> { %s }----> Weigth:{ %s }" % (x.getId(), y.getId(),w))


        #Run the loop while edges are less than Vertices -1 times
        edge_count = 0
        iter_count = 0

        while edge_count < len(self.vertList.values()) -1:
            u,v,w = sorted_edges[iter_count]
            iter_count +=1
            x = find(u)
            y = find(v)
            #print("Parent of X=",x.getId(),"\tParent of Y=",y.getId())
            if x!= y:
                edge_count += 1
                result.append((u,v,w))
                union(x,y)
        for index,(x,y,w) in enumerate(result):
            print("MST Edges ::%s --> %s::\t %s" %(x.getId(),y.getId(),w))



#Driver Code
g = Graph()
cityList = ["Bellevue","Redmond","Kirkland", "Portland","Hillsborro","Bethany","Seattle"]
for i, city in enumerate (cityList):
    g.addVertex(city)

'''
g.addEdge(0,1,5)
g.addEdge(0,5,2)
g.addEdge(1,2,4)
g.addEdge(2,3,9)
g.addEdge(3,4,7)
g.addEdge(3,5,3)
g.addEdge(4,0,1)
g.addEdge(5,4,8)
g.addEdge(5,2,1)
'''

#Cycle Data
'''
g.addEdge(1,2,5)
g.addEdge(1,3,2)
g.addEdge(2,3,4)
#g.addEdge(3,1,4)
g.addEdge(4,1,9)
g.addEdge(4,5,7)
g.addEdge(5,6,3)
g.addEdge(6,4,1)
'''

g.addEdge("Bellevue","Seattle",15)
g.addEdge("Bellevue","Redmond",5)
g.addEdge("Bellevue","Portland",200)
g.addEdge("Kirkland","Redmond",3)
g.addEdge("Seattle","Redmond",20)
g.addEdge("Redmond","Renton",9)
g.addEdge("Portland","Hillsborro",5)
g.addEdge("Portland","Bethany",10)
g.addEdge("Hillsborro","Bellevue",190)
g.addEdge("Bethany","Bellevue",186)
g.addEdge("Bethany","Portland",8)
#Self Loop
g.addEdge("Renton", "Renton", 0)
#Pointing Each-Other
g.addEdge("Redmond", "Kirkland", 7)

#g.BFS(g,g.getVertex(2))

#g.dfs_rec()

#g.cycle_detection_rec()

g.KruskalMST()

#for v in g.vertList:
 #  print("Vertex{%s}"% v)
  #  for w in v.getConnections():
       #print("( %s , %s )" % (v.getId(), w.getId()))
   #     pass



