'''
Created on Apr 5, 2018

@author: Wolf
'''

from graph import *
from pip._vendor.pyparsing import _MAX_INT
from itertools import permutations

def printMenu():
    print("1 - Get number of vertices.")
    print("2 - Check edge.")
    print("3 - Get indegree and outdegree.")
    print("4 - Iterate outbound edges.")
    print("5 - Iterate inbound edges.")
    print("6 - Get the cost of an edge.")
    print("7 - Update cost of an edge.")
    print("8 - Lowest length path between them, by using a forward breadth-first search from the starting vertex.")
    print("9 - Lowest walk between two given vertices, using multiplication of matrices.")
    print("10")
    print("11 - Minimum cost Hamiltonian cycle.")
    print("0 - Exit.")
    
def run():
    filename="tryulet.txt"          #for testing 154(k),710(m)
    g=Graph(filename)
    
    while True:
        printMenu()
        cmd=input("Your command: ")
        if cmd=='1':
            print(g.getNrVertices())
        elif cmd=='2':
            start = int(input("Start vertex: "))
            end=int(input("End vertex: "))
            try:
                res=g.isEdge(start,end);
                if res==False:
                    print("There is no edge between ",start," and ",end)
                else:
                    print("There is an edge between ",start," and ",end)
            except ValueError as e:
                print(e)
                
        elif cmd=='3':
            x= int(input("Give vertex: "))
            try:
                resIn=g.inDegree(x)
                resOut=g.outDegree(x)
                print("In degree: ", resIn," Out degree: ", resOut)
            except ValueError as e:
                print(e)
            
        elif cmd=='4':
            x=int(input("Give vertex: "))
            try:
                iterOut=g.iterateOut(x)
                for _ in range (g.outDegree(x)):
                    print(next(iterOut))
            except ValueError as e:
                print(e)
                    
        elif cmd=='5':
            x=int(input("Give vertex: "))
            try:
                iterIn=g.iterateIn(x)
                for _ in range(g.inDegree(x)):
                    print(next(iterIn))
            except ValueError as e:
                print(e)
        
        elif cmd=='6':
            start= int(input("Start vertex: "))
            end= int(input("End vertex: "))
            try:
                cost= g.getCost(start,end)
                if cost is None:
                    print("There is no cost attached to the given edge.")
                else:
                    print("The cost of [",start,",",end,"] is: ",str(cost))
            except ValueError as e:
                print(e)
                
        elif cmd=='7':
            start = int(input("Start vertex: "))
            end= int(input("End vertex: "))
            newCost=int(input("The new cost: "))
            try:
                g.setCost(start,end,newCost)
                print("Start vertex: ",start," End vertex: ", end," Cost: ",newCost," successfully updated.")
            except ValueError as e:
                print(e)
        elif cmd=='8':
            try:
                n=int(input("Enter the start vertex: "))
                m=int(input("Enter the end vertex: "))
                if n<g.getNrVertices() and m<g.getNrVertices() and n>-1 and m>-1:
                    g.breadth_first(m,n)
                else:
                    print("Error: you entered a wrong vertex.")
            except ValueError as e:
                print("Error: you entered a wrong vertex.")
        elif cmd=='9':
            try:
                n=int(input("Enter the start vertex: "))
                m=int(input("Enter the end vertex: "))
                cost={}
                
                for i in g.parseX():
                    for j in g.parseX():
                        cost[(i,j)]=g.getCost(i, j)
                        
                distMatrix=g.distMatrixMultiplication(cost)
                
                if distMatrix=={}:
                    print("Error: there are negative cost cycles in the graph!")
                    
                elif (n,m) not in distMatrix : 
                    print("Error: there is no path between the two vertices you entered! ")
                    
                else:
                    print("the cost is : ",distMatrix[n,m])
                    print(g.retrievePathFromMatrix(cost, distMatrix, n, m))
                    
            except ValueError as e:
                print("Error: you entered a wrong vertex.")
        elif cmd=='10':
            duration={0:3, 1:1, 2:3, 3:3, 4:2, 5:5}
            g.schedule(duration)
        elif cmd=='11':
            try:
                n=int(input("Enter the start-end vertex: "))
                cost={}
                
                for i in g.parseX():
                    for j in g.parseX():
                        cost[(i,j)]=g.getCost(i, j)
                        
                distMatrix=g.distMatrixHamiltonian(cost)
                
                if distMatrix=={}:
                    print("Error: there are negative cost cycles in the graph!")
                    
                elif (n,n) not in distMatrix : 
                    print("Error: there is no path between the two vertices you entered! ")
                    
                else:
                    minim=_MAX_INT
                    minz=g.parseX()
                    for z in g.parseX():
                        
                        if (n,z)in distMatrix and (z,n)in distMatrix:
                            #print(n,"-",z," ",distMatrix[n,z],"-",distMatrix[z,n]," cost: ",distMatrix[n,z]+distMatrix[z,n])
                            distance=distMatrix[n,z]+distMatrix[z,n]
                            if distance<minim and n!=z:
                                minz=z
                                sum=len(g.retrievePathFromMatrix(cost, distMatrix, n, minz))+len(g.retrievePathFromMatrix(cost, distMatrix, minz, n))
                                print(len(g.retrievePathFromMatrix(cost, distMatrix, n, minz)),"+",len(g.retrievePathFromMatrix(cost, distMatrix, minz, n)),"=",sum," ",g.getNrVertices())
                                if len(g.retrievePathFromMatrix(cost, distMatrix, n, minz))+len(g.retrievePathFromMatrix(cost, distMatrix, minz, n))-2==g.getNrVertices() :
                                        minim=distance
                    if minim!=_MAX_INT:
                        print("the cost is : ",minim)
                        print(g.retrievePathFromMatrix(cost, distMatrix, n, minz),g.retrievePathFromMatrix(cost, distMatrix, minz, n))
                    else:
                        print("It doesn't exists.")
                    
            except ValueError as e:
                print("Error: you entered a wrong vertex.")
        elif cmd=='12':
            g.TSP();
        elif cmd=='0':
            print("The program stopped.")
            break
        else:
            print("Error command!")         
                
run() 
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    