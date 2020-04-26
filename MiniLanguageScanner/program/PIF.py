'''
Created on Oct 28, 2019

@author: WOLF
'''
from program.CodificationTable import *
from program.SymbolTable import *

class PIF(object):
    '''
    codificationTable is initialised at start and symbolsTable is build step by step.
    PIF will contain pairs of code from the codification table and the position from symbols table.
    '''
    codificationTable=CodificationTable()
    symbolsTable=SymbolTable()
    pif=[]

    def __init__(self, table):
        self.codificationTable.add_table(table)
        
    '''
    add_PIF will get an "element" which is a string(identifier, constant, reserved word or symbol) 
    - if it is an identifer/constant the program will add it to the symbol table and add 0/1 and the symbol table position to PIF table
    - if it is a reserved word or symbol the program will add it to PIF table with the position from the codification table 
    and -1 as symbol table position 
    '''
    def add_PIF(self,element,tipe):
        
        if tipe=="identifier" or tipe=="constant":
            self.symbolsTable.add_symbol(element)
        symbolTablePosition=self.symbolsTable.position(element)
        if symbolTablePosition==None:
            symbolTablePosition=-1
        
        code=self.codificationTable.get_code(tipe)
        self.pif.append((code,symbolTablePosition))
    
    def to_string(self):
        string=""
        for i in range(0,len(self.pif)):
            string+=str(self.pif[i][0])+" "+str(self.pif[i][1])+"\n"
        return string
    
    def to_string_SymbolTable(self):
        return self.symbolsTable.to_string()
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        