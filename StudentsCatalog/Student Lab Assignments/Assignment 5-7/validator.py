'''
Created on Dec 6, 2017

@author: Wolf
'''


class validator(object):
    '''
    This class will validate all the input data
    '''


    def __init__(self, repo_stud,repo_assig,repo_grade):
        '''
        Constructor
        '''
        self.stud=repo_stud 
        self.assig=repo_assig
        self.grade=repo_grade
        
    def verifyIDSstudent(self,ids):
        for i in self.stud.getAll():
            if i.ids==ids:
                return True
        return False
    
    def verifyGroupStudent(self,group):
        for i in self.stud.getAll():
            if i.group==group:
                return True
        return False
    
    def verifyIDAassignment(self,ida):
        for i in self.assig.getAll():
            if i.ida==ida:
                return True
        return False
    
    def verifyIDSgrade(self,ids):
        for i in self.grade.getAll():
            if i.ids==ids:
                return True
        return False
    
    def verifyIDAgrade(self,ida):
        for i in self.grade.getAll():
            if i.ida==ida:
                return True
        return False
    
    def verifyIDS_IDAgrade(self,ids,ida):
        for i in self.grade.getAll():
            if i.ids==ids and i.ida==ida:
                return True
        return False
        
    
        
    