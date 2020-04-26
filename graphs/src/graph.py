'''
Created on Mar 15, 2018

@author: Wolf
'''
import random
import time
from _overlapped import NULL
from itertools import permutations

class Graph(object):
    '''
    classdocs
    '''
    def __init__(self, filename):
        '''
        Constructor
        '''
        
        self._filename=filename
        self._dictOut={}
        self._dictIn={}
        self._visited=[]
            
        self.__readFromFile()

    def addEdge(self, source,target,cost):
        '''
        Adds an edge from source to target to the graph.
        '''
        if source in range(self.getNrVertices()) and target in range(self.getNrVertices()) and not self.isEdge(source, target):
            self._dictOut[source].append([target,cost])
            self._dictIn[target].append([source,cost])

    def parseX(self):
        '''
        Returns an iterable that parses the set of vertices of the Graph
        '''
        return self._dictOut.keys()
    
    def parseNout(self,x):
        '''
        Returns an iterable that parses the set of unbound neighbours of x
        '''
        if x not in self._dictOut.keys():
            raise ValueError("Error: this is not a vertex!")
        return self._dictOut[x]
    
    def parseNin(self,x):
        '''
        Returns an iterable that parses the set of inbound neighbours of x
        '''
        if x not in self._dictOut.keys():
            raise ValueError("Error: this is not a vertex!")
        
        return self._dictIn[x]
    
    def isEdge(self,start,end):
        '''
        Returns True if there is an edge from x to y in the graph 
        '''
        if start not in self._dictOut.keys():
            raise ValueError("Error: Start vetex is not valid!")
        if end not in self._dictOut.keys():
            raise ValueError("Error: Ending vertex is not valid!")
        
        for i in self._dictOut[start]:
            if i[0]==end:
                return True
        return False
    
    def getEdges(self):
        e=[]
        for s in self._dictOut.keys():
            for n in self._dictOut[s]:
                e.append((s,n))
        return e
    
    def getNrVertices(self):
        '''
        Return the number of vertices of the graph.
        '''
        
        return len(self._dictOut.keys())
    
    def inDegree(self,x):
        '''
        Get the in degree of vertex x.
        '''
        
        if x not in self._dictIn.keys():
            raise ValueError("Error: this is not a vertex !")
        return len(self.parseNin(x))
    
    def outDegree(self,x):
        '''
        Get the out degree of vertex x.
        '''
        
        if x not in self._dictIn.keys():
            raise ValueError("Error: this is not a vertex !")
        return len(self.parseNout(x))
    
    def iterateOut(self,x):
        '''
        Iterate through the set of outbound edges of a specified vertex.
        For each outbound edge, the iterator provides the target vertex.
        '''
        if x not in self._dictOut.keys():
            raise ValueError("Error: this is not a vertex !")
        return iter([y for y in self._dictOut[x]])
    
    def iterateIn(self,x):
        '''
        Iterate through the set of inbound edges of a specified vertex.
        For each inbound edge, the iterator provides the source vertex.
        '''
        if x not in self._dictOut.keys():
            raise ValueError("Error: this is not a vertex !")
        return iter([y for y in self._dictIn[x]])
    
    def getCost(self,start,end):
        for i in self._dictOut[start]:
            if i[0]==end:
                return i[1]
                
    def setCost(self,start,end,newCost):
        for i in self._dictOut[start]:
            if i[0]==end:
                i[1]=newCost
    
    def __readFromFile(self):
        f=open(self._filename,"r")
        line= f.readline().strip().split(" ")
        
        self._dictOut[0]=int(line[0])
        self._dictIn[0]=int(line[1])

        for i in range(0,int(line[0])):
            self._dictIn[i]=[]
            self._dictOut[i]=[]
            
        for i in range(0,int(line[1])):
            line=f.readline().strip()
            attrs=line.split(" ")
            self.addEdge(int(attrs[0]), int(attrs[1]), int(attrs[2]))
            

        f.close()
        
    def breadth_first(self,nod1,nod2):
        queue =[]
        prev={}
        dist={}
        ok=1
        for i in range(0,len(self._visited)):
            self._visited[i]=0
        queue.append(nod2)
        self._visited.append(nod2)
        dist[nod2] = 0
        while queue:
            x=queue[0]
            queue.pop(0)
            for y in self.parseNin(x):
                if y[0] not in self._visited:
                    queue.append(y[0])
                    self._visited.append(y[0])
                    
                    dist[y[0]]=dist[x] +1
                    prev[y[0]] = x
                    if(y[0]==nod1):
                        nod=nod1
                        while nod!=nod2:
                            print("[",nod,",", prev[nod],"]")
                            nod=prev[nod]
                            
                        ok=0
                        break
        if ok==1:
            print("There is no path between the vertexes you entered!")
    
    def distMatrixMultiplication(self,cost):
        w={}
        for i in self.parseX():
            for j,c in self.parseNout(i):
                w[(i,j)]=cost[(i,j)]
            w[(i,i)]=0
        n=len(self.parseX())
        k=1
        print(w)
        while k<=n:
            q={}
            for i in self.parseX():
                for j in self.parseX():
                    candidates=[w[i,z]+w[z,j] for z in self.parseX() if((i,z)in w and (z,j)in w)]
                    if len(candidates)>0:
                        q[i,j]=min(candidates)
                        if i==j and q[i,j]<0:
                            print("Error: there are negative cost cycles in the graph!")
                            return {}
                            

            k=2*k
            w=q 
            print(w)
        return w 
    
    def distMatrixHamiltonian(self,cost):
        w={}
        for i in self.parseX():
            for j,c in self.parseNout(i):
                w[(i,j)]=cost[(i,j)]
            w[(i,i)]=0
        n=len(self.parseX())
        k=1
        print(w)
        while k<=n:
            q={}
            for i in self.parseX():
                for j in self.parseX():
                    candidates=[w[i,z]+w[z,j] for z in self.parseX() if((i,z)in w and (z,j)in w)]
                    if len(candidates)>0:
                        q[i,j]=min(candidates)
                        if i==j and q[i,j]<0:
                            print("Error: there are negative cost cycles in the graph!")
                            return {}
                            

            k=2*k
            w=q 
            print(w)
        return w 
    
    def TSP(self):
        a=[]
        minim=1000
        rezultat=list
        for i in range(0,self.getNrVertices()):
            a.append(i)
        perm = permutations(a)
        for i in list(perm):
            j=0
            ok=1
            cost=0
            while j<self.getNrVertices()-1:
                if not self.isEdge(i[j], i[j+1]):
                    ok=0
                    j=self.getNrVertices()
                else:
                    cost=cost+self.getCost(i[j], i[j+1])
                    j=j+1
            if ok!=0 and self.isEdge(i[j], i[0]):
                if minim>cost+self.getCost(i[j], i[0]):
                    minim=cost+self.getCost(i[j], i[0])
                    print(self.getCost(i[j], i[0]),i[j], i[0])
                    rezultat=i
                    print(rezultat)
                    print(minim)
        print(rezultat[0],rezultat[1],rezultat[2],rezultat[3],rezultat[4],rezultat[0])        
                
                
    
    def retrievePathFromMatrix(self,cost,distMatrix,s,t):
        path=[]
        path.append(s)
        if (s,t) not in distMatrix : 
            print("Error: there is no path between the two vertices you entered! ")
            return []
        while s!=t:
            for i,c in self.parseNout(s):
                if (i,t) in distMatrix and cost[s,i]+distMatrix[i,t]==distMatrix[s,t]:
                    path.append(i)
                    s=i 
                    break
        return path

    def topoSortDfs(self,node,viz,onPath,result):
        viz.add(node)
        onPath.add(node)
    
        for y,c in self.parseNout(node):
            if y in viz:
                continue
            if y in onPath:
                return False
            if not self.topoSortDfs(y,viz,onPath,result):
                return False
        onPath.remove(node)
        result.append(node)
        
        return True
    
    def toposort(self):
        viz=set()
        onPath=set()
        result=[]
    
        for x in self.parseX():
            if not x in viz:
                if not self.topoSortDfs(x,viz,onPath,result):
                    return None
            
        result.reverse()
    
        return result
               
    def schedule(self, duration):
        earliestStart = {}
        earliestFinish = {}
    
        sorted = self.toposort()
        print (sorted)

        totalTime=0;
        for node in sorted:
            earliestStart[node] = 0
            for y,c in self.parseNin(node):
                earliestStart[node] = max(earliestStart[node], 
                          earliestStart[y] + duration[y])
                earliestFinish[node] = earliestStart[node] + duration[node]
                if earliestFinish[node]>totalTime: 
                    totalTime=earliestFinish[node]
                    
        latestStart = {}
        latestFinish = {}
    
        for node in reversed(sorted):
            latestFinish[node] = totalTime
            for y,c in self.parseNout(node):
                latestFinish[node] = min(latestFinish[node], latestStart[y])
            latestStart[node] = latestFinish[node] - duration[node]    

        critical = []
    
        for x in self.parseX():
            if latestStart[x] == earliestStart[x]:
                critical.append(x)

        print("earliestStart: " , earliestStart) 
        print("earliestFinish: " , earliestFinish)
        print("totalTime: " , totalTime)
        print("latestStart: " , latestStart) 
        print("latestFinish: " , latestFinish)
        print("critical: " , critical)
               