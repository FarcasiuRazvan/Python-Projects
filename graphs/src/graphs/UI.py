'''
Created on Apr 5, 2018

@author: Wolf
'''

from graph import *

def printMenu():
    print("1 - Get number of vertices.")
    print("2 - Check edge.")
    print("3 - Get indegree and outdegree.")
    print("4 - Iterate outbound edges.")
    print("5 - Iterate inbound edges.")
    print("6 - Get the cost of an edge.")
    print("7 - Update cost of an edge.")
    print("8 - Lowest length path between them, by using a forward breadth-first search from the starting vertex.")
    print("0 - Exit.")
    
def run():
    filename="try.txt"          #for testing 154(k),710(m)
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
        elif cmd=='0':
            print("The program stopped.")
            break
        else:
            print("Error command!")         
                
run() 
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    