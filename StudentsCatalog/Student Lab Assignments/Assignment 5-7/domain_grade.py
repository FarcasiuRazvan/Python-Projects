'''
Created on Nov 27, 2017

@author: RAZVI

from domain_assignment import *
from domain_student import *
'''



class grade(object):
    '''
    This class will define a grade.
    '''


    def __init__(self, ids, ida, gr ):
        '''
        Constructor
        '''
        self.ids=ids
        self.ida=ida
        self.gr=int(gr)
    
    def __str__(self):
        '''
        The grade wil be returned as for exemple : 
        
            The Student: 1
            Assignment: 2
            Grade: Ungraded
        Grade is "Ungraded" if self.gr=0 and it means that assignment is not finished yet.
        
            The Student: 1
            Assignment 
            Status: Not Given
        If assignment status is "Not Given" then the value of Grade will be 0 and it will not be returned.
        
            
        '''
        '''
        if self.ida=='0':
            return 'The Student: '+str(self.ids)+'\nAssignment '+'\nStatus: Not Given'
        elif self.gr==0:
            return 'The Student: '+str(self.ids)+'\nAssignment: '+str(self.ida)+'\nStatus: Given \nGrade: Ungraded'
        else:
            return 'The Student: '+str(self.ids)+'\nAssignment: '+str(self.ida)+'\nStatus: Given \nGrade: '+str(self.gr)
        '''
        return str(self.ids)+','+str(self.ida)+','+str(self.gr)
        




