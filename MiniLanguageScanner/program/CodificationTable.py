'''
Created on Oct 28, 2019

@author: WOLF
'''

class CodificationTable(object):
    '''
    The codification table will contain all the reserved words and symbols.
    '''

    codificationTable=[]
    
    def __init__(self):
        '''
        Constructor
        '''
    def add_table(self,table):
        self.codificationTable=table
        
    def add(self, element):
        self.codificationTable.append(element)
    
    '''
    get_code will return the position in the array of the element given as an input.
    '''
    def get_code(self, element):
        for i in range(0,len(self.codificationTable)):
            if self.codificationTable[i]==element:
                return i
        