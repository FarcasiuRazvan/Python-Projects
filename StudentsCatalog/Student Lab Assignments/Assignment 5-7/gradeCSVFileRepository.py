'''
Created on Dec 12, 2017

@author: Wolf
'''

from repository_grade import *
from domain_grade import *
from RepositoryException import *

class gradeCSVFileRepository(repo_grade):
    '''
    classdocs
    '''
    def __init__(self, fileName="grade.txt"):
        '''
        Constructor
        '''
        repo_grade.__init__(self)
        self.__fName = fileName
        self.__loadFromFile()
        
    def add(self, nr):
        x= repo_grade.add(self, nr)
        self.__storeToFile()
        return x
    
    def remove(self, ids, ida):
        x= repo_grade.remove(self, ids, ida)
        self.__storeToFile()
        return x 
    
    def removeIDA(self, ida):
        repo_grade.removeIDA(self, ida)
        self.__storeToFile()
        
    def updateGrade(self, ids, ida, gr):
        repo_grade.updateGrade(self, ids, ida, gr)
        self.__storeToFile()
        
    def updateIDA(self, ids, ida):
        repo_grade.updateIDA(self, ids, ida)
        self.__storeToFile()
        
    def __loadFromFile(self):
        try:
            f=open(self.__fName,"r")
            line= f.readline().strip()
            while line!="":
                attrs = line.split(",")
                gra=grade(attrs[0],attrs[1],attrs[2])
                repo_grade.add(self,gra)
                line=f.readline().strip()
        except IOError:
            raise RepositoryException("Error saving file!")
        finally:
            f.close()
            
    def __storeToFile(self):
        f= open(self.__fName, "w")
        grades=repo_grade.getAll(self)
        for gra in grades:
            strf = str(gra.ids)+","+str(gra.ida)+","+str(gra.gr)+"\n"
            f.write(strf)
        f.close()
    