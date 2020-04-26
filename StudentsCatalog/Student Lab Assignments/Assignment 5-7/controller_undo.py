'''
Created on Dec 4, 2017

@author: RAZVI
'''

class UndoController:
    def __init__(self):
        self._history = []
        self._index = -1    

    def recordOperation(self, cascadedOp):
        '''
        Record the operation for undo/redo
        '''
        self._history.append(cascadedOp)
        self._index+=1
        
    def undo(self):
        '''
        Undo the last operation
        Return True if successful, False otherwise
        '''
        if self._index == -1:
            return False
        operation=self._history[self._index]
        self._index -=1
        operation.undo()
        return True
    
    def redo(self):
        '''
        Redo the last operation
        Return True if successful, False otherwise
        '''
        if self._index == len(self._history)-1:
            return False
        self._index+=1
        operation=self._history[self._index]
        operation.redo()
        return True

class FunctionCall:
    def __init__(self, functionRef, *parameters):
        self._functionRef = functionRef
        self._parameters = parameters

    def call(self):
        self._functionRef(*self._parameters)

class Operation:
    def __init__(self, functionDo, functionUndo):
        self._functionDo = functionDo
        self._functionUndo = functionUndo

    def undo(self):
        self._functionUndo.call()

    def redo(self):
        self._functionDo.call()
        
class CascadedOperation:
    def __init__(self, op=None):
        self._operations = []
        
        if op != None:
            self.add(op)
            
    def add(self, op):
        self._operations.append(op)
        
    def getList(self):
        return self._operations

    def undo(self):
        for i in range(len(self._operations) - 1, -1, -1):
            self._operations[i].undo()

    def redo(self):
        for i in range(len(self._operations) - 1, -1, -1):
            self._operations[i].redo()