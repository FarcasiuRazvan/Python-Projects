'''
Created on Nov 27, 2017

@author: RAZVI
'''

from domain_grade import *
from domain_student import *
from controller_undo import *
from assignment9 import *

class controller_grade(object):
    '''
    This class is the controller for the repository of grades.
    '''
    
    def __init__(self,repository,undo):
        '''
        Constructor
        '''
        self.repo=repository
        self.undo=undo
        
    def addOneAssignment(self,ids,ida,recordForUndo=True):
        x=grade(ids,ida,0)

        self.repo.add(grade(ids,ida,0))
        
        if recordForUndo == False :
            return
        
        while self.undo._index < len(self.undo._history)-1:
            self.undo._history.pop()
            
        undo=FunctionCall(self.removeGrade, ids,ida, False)
        redo=FunctionCall(self.addOneAssignment, ids, ida, False)
        
        operation= Operation(redo, undo)
            
        self.undo.recordOperation(operation)
        
        return x
                
    
    def addGroupAssignment(self,funf,fung,ida,group,recordForUndo=True):
        cascadedOperation=CascadedOperation()
        for i in funf.getAll():
            if i.group==group:
                if self.repo.verifyIDS_IDA(i.ids,'0')==True:
                    originalgrade=grade(i.ids,'0',0)
                    newgrade=grade(i.ids,ida,0)
                    self.repo.updateIDA(originalgrade.ids,newgrade.ida)
                    if recordForUndo == False :
                        return
        
                    while self.undo._index < len(self.undo._history)-1:
                        self.undo._history.pop()

                    undo=FunctionCall(self.updateAssignment, newgrade, originalgrade, False)
                    redo=FunctionCall(self.updateAssignment, originalgrade, newgrade, False)

                    operation=Operation(redo,undo)
                    cascadedOperation.add(operation)
                    
                else:
                    if self.repo.verifyIDS_IDA(i.ids,ida)==False:
                        
                        self.repo.add(grade(i.ids,ida,0))
        
                        if recordForUndo == False :
                            return
        
                        while self.undo._index < len(self.undo._history)-1:
                            self.undo._history.pop()
            
                        undo=FunctionCall(self.removeGrade, i.ids,ida, False)
                        redo=FunctionCall(self.addOneAssignment, i.ids, ida, False)
        
                        operation=Operation(redo,undo)
                        cascadedOperation.add(operation)
                        
                        
            
        self.undo.recordOperation(cascadedOperation)
                        
        
    
    def listStudWithAGivenAssignment(self,ida,funf):
        listid=[]
        for i in self.repo.getAll():
            if i.ida==ida:
                name=funf.getName(i.ids)
                group=funf.getGroup(i.ids)
                x=student(i.ids,name,group)
                listid.append(x)
        return listid

    def ida(self,ida1,ida2):
        if ida1==ida2:
            return True
        else:
            return False
                             
    def listOrderedName(self,funf,ida):
            sorting=self.listStudWithAGivenAssignment(ida,funf)
            #sorting=filter(self.repo.getAll(),self.ida)
            x=[]
            for i in sorting:
                x.append(i.name)
            sort(x)
            return x
        
                
    def listOrderedAVG(self,funf,ida):
        sorting=self.listStudWithAGivenAssignment(ida,funf)
        x=[]
        for i in sorting:
            x.append(grade(i.ids,ida,self.repo.getGrade(i.ids,ida)))    
        for i in range (0,len(x)-1):
            for j in range(i+1,len(x)):
                if x[i].gr < x[j].gr:
                    aux=x[i] 
                    x[i]=x[j] 
                    x[j]=aux
        return x
                
    def listGradeAVGAssig(self,fung):
        '''
        Make a lists of lists that will contain the id, the average grade and the number of students that has that assignment for every assignment.
        '''
        '''
        Put all the ids in x.
        '''
        x=[]
        for i in fung.getAll():
            y=[i.ida,0,0]
            x.append(y)
        '''
        Sum all grades and count all the students that has that assignment for every assignment and put them in x.
        '''
        for i in self.repo.getAll():
            for j in x:
                if j[0]==i.ida and i.gr!=0:
                    j[1]+=i.gr 
                    j[2]+=1
        
        '''
        Divide all the sums of grades of every assignment with the number of students that has those assignments and get the average of every assignment.
        '''
        for i in x:
            if i[2]!=0:
                i[1]=i[1]/i[2]
        '''
        Sort in descending order all the students by their average grade.
        '''
        for i in range(0,len(x)-1):
            for j in range(i+1,len(x)):
                if x[i][1]<x[j][1]:
                    aux=x[i]
                    x[i]=x[j]
                    x[j]=aux
        '''
        Print the ordered list.
        '''
        return x
    
    def listGradeAVGStud(self,funf):
        '''
        Make a list of lists that will contain the id, the average grade and the number of assignments for every student
        '''
        '''
        Put all the ids in x.
        '''
        x=[]
        for i in funf.getAll():
            y=[i.ids,0,0]
            x.append(y)
        '''
        Sum all the grades and count all the assignments and put them in x.
        '''
        for i in self.repo.getAll():
            for j in x:
                if j[0]==i.ids:
                    j[1]=j[1]+i.gr
                    j[2]+=1
        '''
        Divide all the sums of grades of every student with the number of their assignments and get the average of every student.
        '''
        for i in x:
            if i[2]!=0:
                i[1]=i[1]/i[2]
        '''
        Sort in descending order all the students by their average grade.
        '''
        for i in range(0,len(x)-1):
            for j in range(i+1,len(x)):
                if x[i][1]<x[j][1]:
                    aux=x[i]
                    x[i]=x[j]
                    x[j]=aux
        '''
        Print the ordered list.
        '''
        return x
            
    
    def printList(self):
        return self.repo.getAll()
    
    def addGrade(self,ids,ida,gr, recordForUndo=True):
        self.repo.add(grade(ids,ida,gr))
            
        if recordForUndo == False :
            return
            
        while self.undo._index < len(self.undo._history)-1:
            self.undo._history.pop()
            
        undo=FunctionCall(self.removeGrade, ids,ida,gr, False)
        redo=FunctionCall(self.addGrade, ids, ida, gr, False)
        operation= Operation(redo, undo)
            
        self.undo.recordOperation(operation)
            
        x=grade(ids,ida,gr)
        return x
    
    
    def updateGrade(self,originalgrade,newgrade, recordForUndo=True):

        self.repo.updateGrade(originalgrade.ids,originalgrade.ida,newgrade.gr)
            
        if recordForUndo == False :
            return
            
        while self.undo._index < len(self.undo._history)-1:
            self.undo._history.pop()
            
        undo=FunctionCall(self.updateGrade, newgrade, originalgrade, False)
        redo=FunctionCall(self.updateGrade, originalgrade, newgrade, False)
        operation= Operation(redo, undo)
            
        self.undo.recordOperation(operation)
            
        return originalgrade
    
    def updateAssignment(self,originalgrade,newgrade, recordForUndo=True):
        
        
        self.repo.updateIDA(originalgrade.ids,newgrade.ida)
        if recordForUndo == False :
            return
        
        while self.undo._index < len(self.undo._history)-1:
            self.undo._history.pop()

        undo=FunctionCall(self.updateAssignment, newgrade, originalgrade, False)
        redo=FunctionCall(self.updateAssignment, originalgrade, newgrade, False)

        operation= Operation(redo, undo)
            
        self.undo.recordOperation(operation)
            
        return originalgrade
    
    def convertDate(self,date):
        day=""
        month=""
        year=""
        cont=0
        for i in range (0,len(date)):
            if date[i]!='/' and cont==0:
                day=day+date[i]
            elif date[i]=='/':
                cont+=1
        cont=0
        for i in range (0,len(date)):
            if date[i]!='/' and cont==1:
                month=month+date[i]
            elif date[i]=='/':
                cont=cont+1
                
        cont=0
        for i in range (cont,len(date)):
            if date[i]!='/' and cont==2:
                year=year+date[i]
            elif date[i]=='/':
                cont+=1
        return (day,month,year)
            
    def verifyDeadline(self,currentday,fung,funf):
        currentday=self.convertDate(currentday)
        x=[]
        for i in self.repo.getAll():
            if i.ida!='0' and i.gr==0:
                deadline=fung.getDeadline(i.ida)
                deadline=self.convertDate(deadline)
                if deadline[2]>currentday[2]:
                    x.append(funf.getStudent(i.ids))
                elif deadline[2]==currentday[2]:
                    if deadline[1]>currentday[1]:
                        x.append(funf.getStudent(i.ids))
                    elif deadline[1]==currentday[1]:
                        if deadline[0]<currentday[0]:
                            x.append(funf.getStudent(i.ids))
        return x
    
    def getClassGrade(self,ids,ida):
        return self.repo.getClassGrade(ids,ida)
    
    def getGrade(self,ids,ida):
        return self.repo.getGrade(ids,ida)
    
    def getIDA(self,ids):
        return self.repo.getIDA(ids)
    
    def removeGrade(self,ids,ida,gr,recordForUndo=True):
        x=self.repo.remove(ids,ida)
        
        if recordForUndo == False:
            return
        
        while self.undo._index < len(self.undo._history)-1:
            self.undo._history.pop()
        
        undo=FunctionCall(self.addOneAssignment, x.ids, x.ida,x.gr,False)
        redo=FunctionCall(self.removeGrade, x.ids, x.ida,x.gr, False)
        
        operation=Operation(redo,undo)
            
        self.undo.recordOperation(operation)
        
        return x
        
                
    
    def removeIDA(self,ida):
        
        x=[]
        while self.repo.verifyIDA(ida)==True:
            ids=self.repo.getPosIDA(ida)
            for i in self.repo.getAll():
                if i.ids==ids and i.ida==ida:
                    x.append(i)
                    self.repo.getAll().remove(i)
        return x

                
                    
    def removeIDS(self,ids):
        
        x=[]
        while self.repo.verifyIDS(ids)==True:
            for i in self.repo.getAll():
                if i.ids==ids:
                    x.append(i)
                    self.repo.getAll().remove(i)
        
        return x
    

        

