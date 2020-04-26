'''
Created on Nov 27, 2017

@author: RAZVI
'''

from domain_assignment import *
from repository_assignment import *
from controller_undo import *

class controller_assignment(object):
    '''
    This class is the controller for the repository of assignments.
    '''
    def __init__(self, repository,stdasg,undo):
        '''
        Constructor
        '''
        self.repo=repository
        self.stdasg=stdasg
        self.undo=undo
    
    def add(self,ida,description,deadline,recordForUndo=True):
        
        x=assignment(ida,description,deadline)
        self.repo.add(x)
            
        if recordForUndo == False :
            return
            
        while self.undo._index < len(self.undo._history)-1:
            self.undo._history.pop()
            
        undo=FunctionCall(self.remove, x.ida, False)
        redo=FunctionCall(self.add, x.ida,x.desc,x.deadline,False)
        operation= Operation(redo, undo)
            
        self.undo.recordOperation(operation)
            
        return x
            
    def remove(self,ida,recordForUndo=True):
        
        
        x=self.repo.remove(ida)
        
        assignmentgrades=self.stdasg.removeIDA(ida)
        
        
        if recordForUndo == False:
            return
        
        while self.undo._index < len(self.undo._history)-1:
            self.undo._history.pop()
        cascadedOperation=CascadedOperation()
        
        
        undo=FunctionCall(self.add, x.ida, x.desc, x.deadline, False)
        redo=FunctionCall(self.remove, x.ida, False)
        
        operation=Operation(redo,undo)
        cascadedOperation.add(operation)
        
        for i in assignmentgrades:
            undo=FunctionCall(self.stdasg.addGrade,i.ids,i.ida,i.gr,False)
            redo=FunctionCall(self.stdasg.removeGrade,i.ids,i.ida,i.gr,False) 
            operation = Operation(redo,undo)
            cascadedOperation.add(operation)
            
        self.undo.recordOperation(cascadedOperation)
        
        return x
        
    def verifyIDA(self,ida):
        if self.repo.verifyIDA(ida)==True:
            return True
        else:
            return False
        
    def getDesc(self,ida):    
        return self.repo.getDesc(ida)
    
    def getDeadline(self,ida):
        return self.repo.getDeadline(ida)
    
    def getAssignment(self,ida):
        return self.repo.getAssignment(ida)
    
    def getAll(self):
        return self.repo.getAll()
        
    def update(self,ida,c,originalName,newName, recordForUndo=True):
        if c=='1':
            self.repo.updateDesc(assignment(ida,newName,self.repo.getDeadline(ida)))
            
            if recordForUndo == False:
                return
            while self.undo._index < len(self.undo._history)-1:
                self.undo._history.pop()
            
            undo=FunctionCall(self.update,ida, '1', newName, originalName , False)
            redo=FunctionCall(self.update,ida, '1', originalName, newName , False)
        
            operation=Operation(redo,undo)
        
            self.undo.recordOperation(operation)
            
            
        elif c=='2':
            self.repo.updateDeadline(assignment(ida,self.repo.getDesc(ida),newName))
            
            if recordForUndo == False:
                return
            while self.undo._index < len(self.undo._history)-1:
                self.undo._history.pop()
            
            undo=FunctionCall(self.update,ida, '2', newName, originalName , False)
            redo=FunctionCall(self.update,ida, '2', originalName, newName , False)
        
            operation=Operation(redo,undo)
        
            self.undo.recordOperation(operation)
            
    def printList(self):
        return self.repo.getAll()
        
    