'''
Created on Dec 12, 2017

@author: Wolf
'''
from repository_student import *
from domain_student import *
from RepositoryException import *
import pickle

class studentPickleFileRepository(repo_student):
    '''
    classdocs
    '''


    def __init__(self, fileName="students.pickle"):
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
        f = open(self.__fName, "rb")
        
        """
        You cannot unpickle an empty file
            - EOFError means the file is empty
            - Exception means no file, not accessible and so on...
            - finally makes sure we close the input file, regardless of error
        """
        try:
            self.list= pickle.load(f)
        except EOFError:
            self.list = []
        except Exception as e:
            raise e
        finally:
            f.close()
            
    def __storeToFile(self):
        f = open(self.__fName, "wb")
        pickle.dump(self.list, f)
        f.close()