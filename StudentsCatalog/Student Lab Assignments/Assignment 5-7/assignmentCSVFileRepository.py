'''
Created on Dec 12, 2017

@author: Wolf
'''
from repository_assignment import *
from domain_assignment import *
from RepositoryException import *

class assignmentCSVFileRepository(repo_assignment):
    '''
    classdocs
    '''
    def __init__(self, fileName="assignment.txt"):
        '''
        Constructor
        '''
        repo_assignment.__init__(self)
        self.__fName = fileName
        self.__loadFromFile()
        
    def add(self, nr):
        x=repo_assignment.add(self, nr)
        self.__storeToFile()
        return x
    
    def remove(self, ida):
        x=repo_assignment.remove(self, ida)
        self.__storeToFile()
        return x
    
    def updateDesc(self, x):
        repo_assignment.updateDesc(self, x)
        self.__storeToFile()
        
    def updateDeadline(self, x):
        repo_assignment.updateDeadline(self, x)
        self.__storeToFile()
        
    def __loadFromFile(self):
        try:
            f=open(self.__fName,"r")
            line= f.readline().strip()
            while line!="":
                attrs = line.split(",")
                assig=assignment(attrs[0],attrs[1],attrs[2])
                repo_assignment.add(self,assig)
                line=f.readline().strip()
        except IOError:
            raise RepositoryException("Error saving file!")
        finally:
            f.close()
            
    def __storeToFile(self):
        f= open(self.__fName, "w")
        assignments=repo_assignment.getAll(self)
        for assig in assignments:
            strf = str(assig.ida)+","+str(assig.desc)+","+str(assig.deadline)+"\n"
            f.write(strf)
        f.close()
        
        
        