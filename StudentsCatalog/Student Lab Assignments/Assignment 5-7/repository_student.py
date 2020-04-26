'''
Created on Nov 26, 2017

@author: RAZVI
'''
from domain_student import *
from assignment9 import *

class repo_student:
    '''
    repo_student will define a list of students.
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.list=myList()
        
    def add(self, stud):
        self.list.append(stud)
        
    def verifyIDS(self,ids):
        for i in self.list:
            if i.ids==ids:
                return True
        return False
        
    def verifyGroup(self,group):
        for i in self.list:
            if i.group==group:
                return True
        return False
    
    def getAll(self):
        return self.list
    
    def getStudent(self,ids):
        for i in self.list:
            if i.ids==ids:
                return i
    
    def getGroup(self,ids):
        for i in self.list:
            if i.ids==ids:
                return i.group
            
    def getName(self,ids):
        for i in self.list:
            if i.ids==ids:
                return i.name
            
    def remove(self,ids):
        for i in self.list:
            if i.ids==ids:
                j=i
                self.list.remove(i)
                return j
        
    def updateName(self,x):
        for i in self.list:
            if i.ids==x.ids:
                i.name=x.name
                
    def updateGroup(self,x):
        for i in self.list:
            if i.ids==x.ids:
                i.group=x.group 
    
    def filter(self):
        return filter(self.list,self.fct)
            
    def fct(self,a):
        if int(a.ids)%2==0:
            return True
        else:
            return False

    