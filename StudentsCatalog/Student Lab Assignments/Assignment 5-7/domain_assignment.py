'''
Created on Nov 26, 2017

@author: RAZVI
'''

class assignment:
    '''
    This class will define an asssignment.
    '''


    def __init__(self, ida, desc, deadline):
        '''
        Constructor
        '''
        self.ida=ida
        self.desc=str(desc)
        self.deadline=str(deadline)
    def __str__(self):
        '''
        The assignment wil be represented in memory as for exemple : "1. Matematica 2/7/2008"
        '''
        return str(self.ida)+','+str(self.desc)+','+str(self.deadline)

