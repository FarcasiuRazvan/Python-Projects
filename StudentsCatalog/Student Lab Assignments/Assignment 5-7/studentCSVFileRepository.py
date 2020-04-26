'''
Created on Dec 12, 2017

@author: Wolf
'''
from repository_student import *
from domain_student import *
from RepositoryException import *

class studentCSVFileRepository(repo_student):
    '''
    classdocs
    '''


    def __init__(self, fileName="student.txt"):
        '''
        Constructor
        '''
        repo_student.__init__(self)
        self.__fName = fileName
        self.__loadFromFile()
        
    def add(self, student):
        x=repo_student.add(self,student)
        self.__storeToFile()
        return x
        
    def remove(self,ids):
        x=repo_student.remove(self,ids)
        self.__storeToFile()
        return x
        
    def updateGroup(self,student):
        repo_student.updateGroup(self,student)
        self.__storeToFile()
        
    def updateName(self, x):
        repo_student.updateName(self, x)
        self.__storeToFile()
        
    def __loadFromFile(self):
        try:
            f=open(self.__fName,"r")
            line= f.readline().strip()
            while line!="":
                attrs = line.split(",")
                stud=student(attrs[0],attrs[1],attrs[2])
                repo_student.add(self,stud)
                line=f.readline().strip()
        except IOError:
            raise RepositoryException("Error saving file!")
        finally:
            f.close()
            
    def __storeToFile(self):
        f= open(self.__fName, "w")
        students=repo_student.getAll(self)
        for stud in students:
            strf = str(stud.ids)+","+str(stud.name)+","+str(stud.group)+"\n"
            f.write(strf)
        f.close()
        
