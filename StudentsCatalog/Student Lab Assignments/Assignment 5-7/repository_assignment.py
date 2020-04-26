'''
Created on Nov 26, 2017

@author: RAZVI
'''
from domain_assignment import *
from assignment9 import *

class repo_assignment:
    '''
    repo_assignment will define a list of students.
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.list=myList()
        
    def add(self, nr):
        self.list.append(nr)
    
    def verifyIDA(self,ida):
        for i in self.list:
            if i.ida==ida:
                return True
        return False
    
    def getAll(self):
        return self.list
    
    def getDesc(self,ida):
        for i in self.list:
            if i.ida==ida:
                return i.desc
            
    def getDeadline(self,ida):
        for i in self.list:
            if i.ida==ida:
                return i.deadline
    
    def getAssignment(self,ida):
        for i in self.list:
            if i.ida==ida:
                return i
            
    def remove(self,ida):
        for i in self.list:
            if i.ida==ida:
                j=i
                self.list.remove(i)
                return j
        
    def updateDesc(self,x):
        for i in self.list:
            if i.ida==x.ida:
                
                i.desc=x.desc
                
    def updateDeadline(self,x):
        for i in self.list:
            if i.ida==x.ida:
                i.deadline=x.deadline
                