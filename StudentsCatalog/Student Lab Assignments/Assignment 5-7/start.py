'''
Created on Nov 27, 2017

@author: RAZVI
'''
import unittest

from .studentCSVFileRepository import *
from .assignmentCSVFileRepository import *
from .gradeCSVFileRepository import *

from .studentPickleFileRepository import *
from .assignmentPickleFileRepository import *
from .gradePickleFileRepository import *

from .controller_assignment import *
from .controller_student import *
from .controller_grade import *

from .testCases import *

from .repository_assignment import *
from .repository_student import *
from .repository_grade import *

from .UI import *

from .validator import *
from .controller_undo import *
from .domain_grade import *

SETTINGS_FILE = "settings_text.properties"
#SETTINGS_FILE = "settings_binary.properties"

def readSettings():
    '''
    Reads the program's settings file
    output:
        A dictionary containing the program settings
    '''
    f = open(SETTINGS_FILE, "r")
    lines = f.read().split("\n")
    settings = {}
    
    for line in lines:
        setting = line.split("=")
        if len(setting) > 1:
            settings[setting[0]] = setting[1]
    f.close()
    return settings

settings = readSettings()

repo_student = None
repo_assignment = None
repo_grade = None

if 'CSV' == settings['repository']:
    repo_student = studentCSVFileRepository(settings['students'])
    repo_assignment = assignmentCSVFileRepository(settings['assignments'])
    repo_grade = gradeCSVFileRepository(settings['grades'])

if 'binary' == settings['repository']:
    repo_student = studentPickleFileRepository(settings['students'])
    repo_assignment = assignmentPickleFileRepository(settings['assignments'])
    repo_grade = gradePickleFileRepository(settings['grades'])

class Tests(unittest.TestCase):
        
    def testAddStudent(self):
        funf.add('1','Razvan','913')
        funf.add('2','x','912')
        self.assertEqual(len(funf.getAll()),67,"error")
        
    def testRemoveStudent(self):
        funf.remove('1')
        funf.remove('2')
        self.assertEqual(len(funf.getAll()),65,"error")
        
    def testAddAssignment(self):
        fung.add('1','Mate','2/3/2017')
        fung.add('2','Romana','3/4/2017')
        self.assertEqual(len(fung.getAll()),37,"error")
    
    def testRemoveAssignment(self):
        fung.remove('2')
        fung.remove('1')
        self.assertEqual(len(fung.getAll()),35,"error")
        
    def testListOrderedGivenAssignment(self):
        originalgrade=grade('10','0',0)
        newgrade=grade('10','1',0)
        stdasg.updateAssignment(originalgrade,newgrade)
        
        originalgrade=grade('20','0',0)
        newgrade=grade('20','1',0)
        stdasg.updateAssignment(originalgrade,newgrade)
        
        originalgrade=grade('30','0',0)
        newgrade=grade('30','1',0)
        stdasg.updateAssignment(originalgrade,newgrade)
        
        originalgrade=grade('40','0',0)
        newgrade=grade('40','2',0)
        stdasg.updateAssignment(originalgrade,newgrade)
        
        
        originalgrade=grade('10','1',0)
        newgrade=grade('10','1',10)
        stdasg.updateGrade(originalgrade,newgrade)
        
        originalgrade=grade('20','1',0)
        newgrade=grade('20','1',7)
        stdasg.updateGrade(originalgrade,newgrade)
        
        originalgrade=grade('30','1',0)
        newgrade=grade('30','1',8)
        stdasg.updateGrade(originalgrade,newgrade)
        
        originalgrade=grade('40','2',0)
        newgrade=grade('40','2',7)
        stdasg.updateGrade(originalgrade,newgrade)
        
        self.assertEqual(len(stdasg.listOrderedAVG(funf,'1')),3,"error")
        
        originalgrade=grade('40','0',0)
        newgrade=grade('40','1',0)
        stdasg.updateAssignment(originalgrade,newgrade)
        
        originalgrade=grade('40','1',0)
        newgrade=grade('40','1',7)
        stdasg.updateGrade(originalgrade,newgrade)
        
        self.assertEqual(len(stdasg.listOrderedAVG(funf,'1')),4,"error")
    
#testCases(repo_student,repo_assignment,repo_grade)
valid=validator(repo_student,repo_assignment,repo_grade)

undo=UndoController()

stdasg=controller_grade(repo_grade,undo)
funf=controller_student(repo_student,stdasg,undo)
fung=controller_assignment(repo_assignment,stdasg,undo)

x=UI(funf,fung,stdasg,valid,undo)
'''
if __name__ =="__main__":
    unittest.main()
'''
x.menu()
