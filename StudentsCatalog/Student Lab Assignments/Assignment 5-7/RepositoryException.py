'''
Created on Dec 12, 2017

@author: Wolf
'''

class RepositoryException(Exception):
    '''
    classdocs
    '''


    def __init__(self, message):
        '''
        Constructor
        '''
        self._message= message
    
    def getMessage(self):
        return self._message
    def __str__(self):
        return self._message