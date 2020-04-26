'''
Created on Nov 26, 2017

@author: RAZVI
'''
from domain_student import *
from domain_assignment import *
from domain_grade import *
from repository_assignment import *
from repository_student import *

'''
from controller import *
'''

class UI:
    '''
    UI or user interface is a class for user.
    '''


    def __init__(self, funf,fung,stdasg,valid,undo):
        '''
        Constructor
        '''
        self.funf = funf
        self.fung = fung
        self.stdasg = stdasg
        self.valid=valid
        self.undo=undo
    
    def menu(self):
        
        while True:
            print("\n1.  Print students.")
            print("2.  Add student.")
            print("3.  Remove student.")
            print("4.  Update student.")
            print("5.  Print assignments.")
            print("6.  Add assignment.")
            print("7.  Remove assignment.")
            print("8.  Update assignment.")
            print("9.  Give an assignment to one or more students.")
            print("    Show the register of students and their assignments.")
            print("10. Undo.")
            print("11. Redo.")
            print("12. Exit.")
            cmd = int(input("Enter option: "))
            '''
            Student
            '''
            if cmd==1:
                for i in self.funf.printList():
                    print(i)
                
            elif cmd==2:
                print("Student exemple : '1. Razvan 913'")
                ids = input("Enter an id: ")
                if self.valid.verifyIDSstudent(ids)==True:
                    print("Error: student id already exists !")
                else:
                    name = input("Enter a name: ")
                    group = input("Enter a group: ")
                    self.funf.add(ids,name,group)
                   
            elif cmd==3:
                ids = input("Enter an id: ")
                if self.valid.verifyIDSstudent(ids)==True:
                    self.funf.remove(ids)
                else:
                    print("Error: student id does not exist !")

            elif cmd==4:
                ids = input("Enter the id of the student you want to update: ")
                if self.valid.verifyIDSstudent(ids)==False:
                    print("Error: student id does not exists !")
                else:
                    print(self.funf.getStudent(ids))
                    print("What do you want to update ?")
                    print("1. Name")
                    print("2. Group")
                    c = input("Enter your option: ")
                    if c=='1':
                        newname = input("Enter a name: ")
                        originalName=self.funf.getName(ids)
                        self.funf.update(ids,c,originalName, newname)
                    elif c=='2':
                        newgroup = input("Enter a group: ")
                        originalGroup=self.funf.getGroup(ids)
                        self.funf.update(ids,c,originalGroup,newgroup)
                    else :
                        print("Error: Option invalidd!")
                
                '''
                Assignments
                '''
            elif cmd==5:
                for i in self.fung.printList():
                    print(i)
                
                
            elif cmd==6:
                print("Assignment exemple : '1. Matematica 2/7/2017' ")
                ida = input("Enter an id: ")
                if self.valid.verifyIDAassignment(ida)==True:
                    print("Error: assignment id already exists!")
                else:
                    description = input("Enter a description: ")
                    deadline = input("Enter a deadline: ")
                    self.fung.add(ida,description,deadline)
                    
                    
            elif cmd==7:
                ida=input("Enter an id: ")
                if self.valid.verifyIDAassignment(ida)==True:
                    self.fung.remove(ida)
                else:
                    print("Error: assignment id does not exist!")
                
                
            elif cmd==8:
                ida=input("Enter the id of the assignment you want to update: ")
                if self.valid.verifyIDAassignment(ida)==False:
                    print("Error: assignment id does not exists!")
                else:
                    print(self.fung.getAssignment(ida))
                    print("What do you want to update ?")
                    print("1. Description")
                    print("2. Deadline")
                    c=input("Enter your option: ")
                    if c=='1':
                        newname= input("Enter a description: ")
                        originalname=self.fung.getDesc(ida)
                        self.fung.update(ida,c,originalname,newname)
                    elif c=='2':
                        newname= input("Enter a deadline: ")
                        originalname=self.fung.getDeadline(ida)
                        self.fung.update(ida,c,originalname,newname)
                    else:
                        print("Error: Option invalid!")
                '''
                Grades
                '''
            elif cmd==9:
                print("Choose an operation: ")
                print("1. Give an assignment to one student.")
                print("2. Give an assignment to a group of students.")
                print("3. Show the register.")
                print("4. Give a grade to an assignment of a student.")
                print("5. List all the students ordered by their grade at a given assignment.")
                print("6. List all the students ordered alphabetically with a given assignment.")
                print("7. List all the students who have an ungraded assignment for which the deadline passed.")
                print("8. List all the students with their average grade in descending order by their average grade.")
                print("9. List all the assignments with their average grade in descending order by their average grade.")
                x=int(input("Enter your option: "))
                if x==1:
                    ids=input("Enter the id of the student: ")
                    if self.valid.verifyIDSstudent(ids)==False:
                        print("Error: The student does not exist!")
                    else:
                        ida=input("Enter the id of the assignment: ")
                        if self.valid.verifyIDAassignment(ida)==False:
                            print("Error: assignment does not exist!")
                        else:
                            if self.valid.verifyIDS_IDAgrade(ids,'0')==True:
                                originalgrade=grade(ids,'0',0)
                                newgrade=grade(ids,ida,0)
                                self.stdasg.updateAssignment(originalgrade,newgrade)
                            else:
                                if self.valid.verifyIDS_IDAgrade(ids,ida)==True:
                                    print("Error: this assignment has already been given to this student")
                                else:
                                    self.stdasg.addOneAssignment(ids,ida)
                elif x==2:
                    group=input("Enter the group of students: ")
                    if self.valid.verifyGroupStudent(group)==False:
                        print("Error: The group does not exist!")
                    else:
                        ida=input("Enter the id of the assignment: ")
                        if self.valid.verifyIDAassignment(ida)==False:
                            print("Error: assignment does not exist!")
                        else:
                            self.stdasg.addGroupAssignment(self.funf,self.fung,ida,group)
                elif x==3:
                    for i in self.stdasg.printList():
            
                        print("\nId Student: ",i.ids)
                        print("Student name: ",self.funf.getName(i.ids))
                        if i.ida=='0':
                            print("Assignment")
                            print("Status: Not Given")
                        elif i.gr==0:
                            print("The Student: ",i.ids,"\nAssignment: ",i.ida,"\nStatus: Given \nGrade: Ungraded")
                        else:
                            print("The Student: ",i.ids,"\nAssignment: ",i.ida,"\nStatus: Given \nGrade: ",i.gr)
                        print("")               
                elif x==4:
                    ids=input("Enter the id of the student: ")
                    if self.valid.verifyIDSstudent(ids)==False:
                        print("Error: The student does not exist!")
                    else:
                        ida=input("Enter the id of the assignment: ")
                        if self.valid.verifyIDS_IDAgrade(ids,ida)==False:
                            print("Error: student with id='ids' does not have the assignment you enetered!")
                        else:
                            if self.stdasg.getGrade(ids,ida)==0:
                                gr=int(input("Enter the grade of the assignment: "))
                                newgrade=grade(ids,ida,gr)
                                originalgrade=grade(ids,ida,0)
                                self.stdasg.updateGrade(originalgrade,newgrade)
                            else:
                                print("Error: the assignment has already received a grade")
                elif x==5:
                    ida=input("Enter the id of the assignment: ")
                    if self.valid.verifyIDAgrade(ida)==False:
                        print("Error: assignment does not exist!")
                    else:
                        for i in self.stdasg.listOrderedAVG(self.funf,ida):
                            print(i)
                            
                elif x==6:
                    ida=input("Enter the id of the assignment: ")
                    if self.valid.verifyIDAgrade(ida)==False:
                        print("Error: assignment does not exist!")
                    else:
                        for i in self.stdasg.listOrderedName(self.funf,ida):
                            print(i)
                    
                elif x==7:
                    currentday=input("Enter the currentday: ")
                    for i in self.stdasg.verifyDeadline(currentday,self.fung,self.funf):
                        print(i)
                        
                elif x==8:
                    x=self.stdasg.listGradeAVGStud(self.funf)
                    for i in x:
                        print(self.funf.getStudent(i[0])," with an average: ",i[1])
                elif x==9:
                    x=self.stdasg.listGradeAVGAssig(self.fung)
                    for i in x:
                        if i[1]!=0:
                            print(self.fung.getAssignment(i[0])," with an average: ",i[1])
                else:   
                    print("Error: option invalid!")
            elif cmd==10:
                if self.undo.undo() == False:
                    print("Error: no more operations for undo!")
            elif cmd==11:
                if self.undo.redo() == False:
                    print("Error: no more operations for redo!")
            elif cmd==12:
                for i in self.funf.filter():
                    print(i)
                
            else:
                print("Invalid option!")
                
                    
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        