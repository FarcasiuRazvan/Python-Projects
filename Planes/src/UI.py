'''
Created on Dec 30, 2017

@author: Wolf
'''

from src.validator import *
from random import randint
from src.Computer import *

class UI(object):
    '''
    classdocs
    '''


    def __init__(self, boardplayer, boardcomputer, boardplayerTarget, boardcomputerTarget):
        '''
        Constructor
        '''
        self.boardPlayer=boardplayer
        self.boardComputer=boardcomputer
        self.boardPlayerTarget=boardplayerTarget
        self.boardComputerTarget=boardcomputerTarget
    
    def menu(self):
        print("1.Start a new game.")
        print("2. Exit.")
        cmd=input("Enter your command :")
        if cmd=='1':
            self.boardPlayer.list()
            print("Set your planes.")
            print("First plane.")
            ok=1
            command=1
            while ok==1:
                x=int(input("Enter the coordinate x of the plane's cabin: "))
                if validCoord(x)==True:
                    y=int(input("Enter the coordinate y of the plane's cabin: "))
                    if validCoord(y)==True:
                        print("The plane can be oriented :")
                        print("1. Up")
                        print("2. Right")
                        print("3. Down")
                        print("4. Left")
                        orientation=int(input("Enter the orientation of the plane: "))
                        if orientation==1 or orientation==2 or orientation==3 or orientation==4:
                            if validPlane(x,y,self.boardPlayer.table,orientation)==True:
                                ok=0
                                self.boardPlayer.addPlane(x,y,orientation,3,1)
                                self.boardPlayer.list()
                            else:
                                print("Error: the plane does not fit in the board!")
                        else:
                            print("Error: invalid orientation key, it has to be 1,2,3 or 4!")
                    else:
                        print("Error: invalid y, it has to be between 0 and 7!")
                else:
                    print("Error: invalid x, it has to be between 0 and 7!")
                if ok==1:
                    print("Do you want to exit the game ?")
                    print("Yes or No ?")
                    c=input("Answer: ")
                    if c=='Yes' or c=='yes':
                        command=0
                        break
            if command==1:
                ok=1
                print("Wait a moment such that the computer will set it's first plane...")
                oki=0
                while oki==0:
                    xc=randint(0,7)
                    yc=randint(0,7)
                    orientation=randint(1,4)
                    if validPlane(xc,yc,self.boardComputer.table,orientation)==True:
                                oki=1
                                self.boardComputer.addPlane(xc,yc,orientation,3,1)
                print("Second plane.")
                
            else:
                ok=0
            while ok==1:
                x=int(input("Enter the coordinate x of the plane's cabin: "))
                if validCoord(x)==True:
                    y=int(input("Enter the coordinate y of the plane's cabin: "))
                    if validCoord(y)==True:
                        print("The plane can be oriented :")
                        print("1. Up")
                        print("2. Right")
                        print("3. Down")
                        print("4. Left")
                        orientation=int(input("Enter the orientation of the plane: "))
                        if orientation==1 or orientation==2 or orientation==3 or orientation==4:
                            if validPlane(x,y,self.boardPlayer.table,orientation)==True:
                                ok=0
                                self.boardPlayer.addPlane(x,y,orientation,4,2)
                                self.boardPlayer.list()
                            else:
                                print("Error: The plane couldn't been created, it intersects with the other plane or it does not fit in the board!")
                                print("Choose other coordinates for the second plane.")
                        else:
                            print("Error: invalid orientation key, it has to be 1,2,3 or 4!")
                    else:
                        print("Error: invalid y, it has to be between 0 and 7!")
                else:
                    print("Error: invalid x, it has to be between 0 and 7!")
                if ok==1:
                    print("Do you want to exit the game ?")
                    print("Yes or No ?")
                    c=input("Answer: ")
                    if c=='Yes' or c=='yes':
                        command=0
                        break
            
            if command==1:
                print("Wait a moment such that the computer will set it's second plane...")
                oki=0
                while oki==0:
                    xc=randint(0,7)
                    yc=randint(0,7)
                    orientation=randint(1,4)
                    if validPlane(xc,yc,self.boardComputer.table,orientation)==True:
                                oki=1
                                self.boardComputer.addPlane(xc,yc,orientation,4,2)
                
                print("Now that you set your planes, the game can begin!")
                
                computerAttack(self.boardPlayer,self.boardComputerTarget,self.boardPlayerTarget,self.boardComputer)
                
                if isGameWon(self.boardComputer.table)==0:
                    if isGameWon(self.boardPlayer.table)==1:
                        self.boardComputer.list()
                        print("The game ended because the computer won.")
                    else:
                        print("The game ended because the player abort.")
                        print("You may either chose to abort the game or you entered the coordinates of a target twice.")
                else:
                    self.boardComputer.list()
                    print("The game ended because the player won.")

            print("THE END")
                
        elif cmd=='2':
            pass
        else:
            print("Error: Invalid command!")