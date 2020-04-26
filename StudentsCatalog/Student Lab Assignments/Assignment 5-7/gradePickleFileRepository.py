'''
Created on Dec 12, 2017

@author: Wolf
'''
from repository_grade import *
from domain_grade import *
from RepositoryException import *
import pickle

class gradePickleFileRepository(repo_grade):
    '''
    classdocs
    '''
    def __init__(self, fileName="grade.pickle"):
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
    