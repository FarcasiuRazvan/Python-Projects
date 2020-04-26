'''
Created on Nov 27, 2017

@author: RAZVI
'''

from repository_student import *
from domain_student import *
from controller_undo import *

class controller_student(object):
    '''
    This class is the controller for the repository of students.
    '''
    def __init__(self, repository,stdasg,undo):
        '''
        Constructor
        '''
        self.repo=repository
        self.stdasg=stdasg
        self.undo=undo
    
    def add(self,ids,name,group, recordForUndo=True):
        
            x=student(ids,name,group)
            self.repo.add(x)
            
            if recordForUndo == False :
                return
            
            while self.undo._index < len(self.undo._history)-1:
                self.undo._history.pop()
            
            undo=FunctionCall(self.remove, x.ids, False)
            redo=FunctionCall(self.add, x.ids, x.name, x.group, False)
            operation= Operation(redo, undo)
            
            self.undo.recordOperation(operation)
            
            return x
    
    def getStudent(self,ids):
        return self.repo.getStudent(ids)
            
    def verifyGroup(self,group):
        if self.repo.verifyGroup(group)==True:
            return True
        else:
            return False
    def getGroup(self,ids):
        return self.repo.getGroup(ids)
    def getName(self,ids):
        return self.repo.getName(ids)
    def getAll(self):
        return self.repo.getAll()
    
    
    def remove(self,ids, recordForUndo=True):
        
        x=self.repo.remove(ids)
        
        assignmentgrades=self.stdasg.removeIDS(ids)
        
        
        if recordForUndo == False:
            return
        
        while self.undo._index < len(self.undo._history)-1:
            self.undo._history.pop()
        cascadedOperation=CascadedOperation()
        
        
        undo=FunctionCall(self.add, x.ids, x.name, x.group, False)
        redo=FunctionCall(self.remove, x.ids, False)
        
        operation=Operation(redo,undo)
        cascadedOperation.add(operation)
        
        for i in assignmentgrades:
            undo=FunctionCall(self.stdasg.addGrade,i.ids,i.ida,i.gr,False)
            redo=FunctionCall(self.stdasg.removeGrade,i.ids,i.ida,i.gr,False) 
            operation = Operation(redo,undo)
            cascadedOperation.add(operation)
            
        self.undo.recordOperation(cascadedOperation)
        
        return x
        
        
        
    def update(self,ids,c,originalName,newName, recordForUndo=True):
        
        if c=='1':
            self.repo.updateName(student(ids,newName,self.repo.getGroup(ids)))
            
            if recordForUndo == False:
                return
            while self.undo._index < len(self.undo._history)-1:
                self.undo._history.pop()
            
            undo=FunctionCall(self.update,ids, '1', newName, originalName , False)
            redo=FunctionCall(self.update,ids, '1', originalName, newName , False)
        
            operation=Operation(redo,undo)
        
            self.undo.recordOperation(operation)
            
            return student(ids,originalName,self.repo.getGroup(ids))
            
            
        elif c=='2':
            self.repo.updateGroup(student(ids,self.repo.getName(ids),newName))
            
            if recordForUndo == False:
                return
            while self.undo._index < len(self.undo._history)-1:
                self.undo._history.pop()
            
            undo=FunctionCall(self.update,ids, '2', newName, originalName , False)
            redo=FunctionCall(self.update,ids, '2', originalName, newName , False)
        
            operation=Operation(redo,undo)
        
            self.undo.recordOperation(operation)
            
            return student(ids,self.repo.getName(ids),originalName)
            
            
            
            
    def printList(self):
        return self.repo.getAll()
    
    def filter(self):
        return self.repo.filter()
        
        
    
        