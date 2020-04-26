'''
Created on Jan 3, 2018

@author: Wolf
'''

from src.validator import *

def playerAttack(boardPlayer,boardPlayerTarget,boardComputer):
    esc=1
    while esc==1:
        print("These are your planes:")
        print("")
        boardPlayer.list()
        print("These are your targets:")
        print("")
        boardPlayerTarget.list()
        #boardComputer.list()
        print("")
        print("These are your commands:")
        print("1. Attack the enemy.")
        print("2. Abort the mission.")
        print("")
        print("What to do ?")
        cd=input("Your command: ")
        if cd=='1':
            print("Please enter some coordinates that you haven't already entered with a value between 0 and 7.")
            x=int(input("Enter the coordinate x: "))
            if validCoord(x)==True:
                y=int(input("Enter the coordinate y: "))
                if validCoord(y)==True:
                    if boardPlayerTarget.table[x][y]==0:
                        if boardComputer.table[x][y]==0:
                            boardPlayerTarget.table[x][y]=-1
                            boardComputer.table[x][y]=-1
                        elif boardComputer.table[x][y]==1 or boardComputer.table[x][y]==2:
                            boardPlayerTarget.table[x][y]=-2
                            boardComputer.table[x][y]=-2
                            if isGameWon(boardComputer.table)==1:
                                return 1
                        elif boardComputer.table[x][y]==3:
                            boardPlayerTarget.table[x][y]=-2
                            boardComputer.table[x][y]=-2
                            for i in range(0,8):
                                for j in range(0,8):
                                    if boardComputer.table[i][j]==1:
                                        boardComputer.table[i][j]=-2
                                        boardPlayerTarget.table[i][j]=-2
                            if isGameWon(boardComputer.table)==1:
                                return 1
                        elif boardComputer.table[x][y]==4:
                            boardPlayerTarget.table[x][y]=-2
                            boardComputer.table[x][y]=-2
                            for i in range(0,8):
                                for j in range(0,8):
                                    if boardComputer.table[i][j]==2:
                                        boardComputer.table[i][j]=-2
                                        boardPlayerTarget.table[i][j]=-2
                            if isGameWon(boardComputer.table)==1:
                                return 1
                        esc=0
                        print("Legend: ")
                        print("X means plane missed")
                        print("Y means that that part of the plane has been destroyed")
                    else:
                        print("Error: you have already entered those coordinates!")
                else:
                    print("Error: invalid y, it has to be between 0 and 7!")
            else:
                print("Error: invalid x, it has to be between 0 and 7!")
        elif cd=='2':
            return 1
        else:
            print("Error: invalid command!")
    return 0