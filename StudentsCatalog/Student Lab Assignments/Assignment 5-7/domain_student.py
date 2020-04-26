'''
Created on Nov 26, 2017

@author: RAZVI
'''


class student:
    '''
    This class will define a student.
    '''
    def __init__(self, ids, name, group):
        '''
        Constructor
        '''
        self.ids=ids
        self.name=str(name)
        self.group=str(group)
    
    def __str__(self):
        '''
        The student wil be represented in memory as for exemple : "1. Razvan 913"
        '''
        return str(self.ids)+','+str(self.name)+','+str(self.group)
    
