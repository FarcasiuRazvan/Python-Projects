'1','Razvan','913''''
Created on Dec 5, 2017

@author: Wolf
'''
import unittest
from repository_student import *
from controller_student import *

class Tests(unittest.TestCase):
    
    def setUp(self):
        self.repo=repo_student
    def testAddStudent(self):
        controller=controller_student(self.repo)
        controller.add('1','Razvan','913')
        
        self.assertEqual(len(controller.getAll()),1,"error")
        

        
if __name__ =="__main__":
    unittest.main()