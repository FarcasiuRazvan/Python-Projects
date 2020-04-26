'''
Created on Oct 28, 2019

@author: WOLF
'''

class SymbolTable(object):
    '''
    The symbol table consist of 3 arrays, one for the symbols and 2 more for the position in the tree, left and right.
    '''
    
    symbols=[]
    posLeft=[]
    posRight=[]

    def __init__(self):
        '''
        Constructor
        '''
    '''
    add_symbol will get a string "name" as input and add it to the symbol array, put -1 in the left array and -1 in the right array
    signifieing the position that follows this element in the ordered binary tree, then the program will order the tree.
    '''
    def add_symbol(self, name):
        if name not in self.symbols:
            self.symbols.append(name)
            self.posLeft.append(-1)
            self.posRight.append(-1)
            self.order_tree()
    
    '''
    order_tree will order the tree based on the new element that was added prior to this function call.
    '''
    def order_tree(self):
        i=0
        while i < len(self.symbols):
            
                if str(self.symbols[len(self.symbols)-1])>str(self.symbols[i]) and self.posRight[i]==-1:
                    self.posRight[i]=len(self.symbols)-1
                    i=len(self.symbols)
                elif str(self.symbols[len(self.symbols)-1])>str(self.symbols[i]) and self.posRight[i]!=-1:
                    i=self.posRight[i]
                    
                elif str(self.symbols[len(self.symbols)-1])<str(self.symbols[i]) and self.posLeft[i]==-1:
                    self.posLeft[i]=len(self.symbols)-1
                    i=len(self.symbols)
                elif str(self.symbols[len(self.symbols)-1])<str(self.symbols[i]) and self.posLeft[i]!=-1:
                    i=self.posLeft[i]
                    
                else:
                    i+=1
        
    def to_string(self):
        string=""
        for i in range(0,len(self.symbols)):
            string+=" "+str(i)+" "+str(self.symbols[i])+" "+str(self.posLeft[i])+" "+str(self.posRight[i])+"\n"
            
        return string
        
    '''
    position function will return the position of the symbol in the symbols table.
    '''
    def position(self,symbol):
        for i in range(0,len(self.symbols)):
            if self.symbols[i]==symbol:
                return i
        
    
        