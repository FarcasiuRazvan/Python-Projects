'''
Created on Dec 12, 2017

@author: Wolf
'''
from repository_assignment import *
from domain_assignment import *
from RepositoryException import *
import pickle

class assignmentPickleFileRepository(repo_assignment):
    '''
    classdocs
    '''


    def __init__(self, fileName="assignment.pickle"):
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
        f = open(self.__fName, "rb")
        
        """
        You cannot unpickle an empty file
            - EOFError means the file is empty
            - Exception means no file, not accessible and so on...
            - finally makes sure we close the input file, regardless of error
        """
        try:
            self.list = pickle.load(f)
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