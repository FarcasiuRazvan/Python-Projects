'''
Created on Nov 27, 2017

@author: RAZVI
'''

from assignment9 import *

class repo_grade:
    '''
    repo_grade will define a list of students with their assignments and their grades
    '''
    def __init__(self):
        '''
        Constructor
        '''
        self.list=myList()
        
    def add(self, nr):
        self.list.append(nr)
        return nr
        
    def verifyIDS(self,ids):
        for i in self.list:
            if i.ids==ids:
                return True
        return False
    
    def verifyIDA(self,ida):
        for i in self.list:
            if i.ida==ida:
                return True
        return False
    
    def verifyIDS_IDA(self,ids,ida):
        '''
        It will verify if the student with id='ids' have the assignment with id='ida'
        '''
        for i in self.list:
            if i.ids==ids and i.ida==ida:
                return True
        return False
        
    def getAll(self):
        return self.list
    
    def getIDA(self,ids):
        for i in self.list:
            if i.ids==ids:
                return i.ida
            
    def getPosIDA(self,ida):
        for i in self.list:
            if i.ida==ida:
                return i.ids
            
    def getGrade(self,ids,ida):
        for i in self.list:
            if i.ids==ids and i.ida==ida:
                return i.gr
            
    def getClassGrade(self,ids,ida):
        for i in self.list:
            if i.ids==ids and i.ida==ida:
                return i
            
    def remove(self,ids,ida):
        for i in self.list:
            if i.ids==ids and i.ida==ida:
                j=i
                self.list.remove(i)
                return j
    
    def removeIDA(self,ida):
        for i in self.list:
            if i.ida==ida:
                self.list.remove(i)
    
    def updateIDA(self,ids,ida):
        for i in self.list:
            if i.ids == ids:
                j=i
                i.ida=ida
                return j
        
    def updateGrade(self,ids,ida,gr):
        for i in self.list:
            if i.ids==ids and i.ida==ida:
                j=i
                i.gr=gr
                return j
        
                

                
    