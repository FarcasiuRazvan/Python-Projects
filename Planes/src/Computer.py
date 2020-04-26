'''
Created on Jan 3, 2018

@author: Wolf
'''
from random import randint
from src.Player import *

def fill(x,y,boardPlayer,boardComputerTarget,boardPlayerTarget,boardComputer,ok):
    if boardPlayer.table[x][y]==-2 and ok==0:
        if (x-1==0 and y==0)or(x-1==0 and y==7):
            pass
        elif x-1>=0 and boardPlayer.table[x-1][y]!=-2 and ok==0:
            ok=fill(x-1,y,boardPlayer,boardComputerTarget,boardPlayerTarget,boardComputer,ok)
            
        if (x==0 and y-1==0)or(x==7 and y-1==0):
            pass
        elif y-1>=0 and boardPlayer.table[x][y-1]!=-2 and ok==0:
            ok=fill(x,y-1,boardPlayer,boardComputerTarget,boardPlayerTarget,boardComputer,ok)
            
        if (x+1==7 and y==0)or(x+1==7 and y==7):
            pass
        elif x+1<8 and boardPlayer.table[x+1][y]!=-2 and ok==0:
            ok=fill(x+1,y,boardPlayer,boardComputerTarget,boardPlayerTarget,boardComputer,ok)
        
        if (x==0 and y+1==7)or(x==7 and y+1==7):
            pass
        elif y+1<8 and boardPlayer.table[x][y+1]!=-2 and ok==0:
            ok=fill(x,y+1,boardPlayer,boardComputerTarget,boardPlayerTarget,boardComputer,ok)
        
    elif boardPlayer.table[x][y]==0 and ok==0:
        ok=playerAttack(boardPlayer,boardPlayerTarget,boardComputer)
        if ok==0:
            boardComputerTarget.table[x][y]=-1
            boardPlayer.table[x][y]=-1
        
    elif (boardPlayer.table[x][y]==1 or boardPlayer.table[x][y]==2) and ok==0:
        ok=playerAttack(boardPlayer,boardPlayerTarget,boardComputer)
        if ok==0:
            boardComputerTarget.table[x][y]=-2
            boardPlayer.table[x][y]=-2
            ok=isGameWon(boardPlayer.table)
            ok=fill(x,y,boardPlayer,boardComputerTarget,boardPlayerTarget,boardComputer,ok)
        
    elif boardPlayer.table[x][y]==3 and ok==0:
        ok=playerAttack(boardPlayer,boardPlayerTarget,boardComputer)
        if ok==0:
            boardComputerTarget.table[x][y]=-2
            boardPlayer.table[x][y]=-2
            ok=isGameWon(boardPlayer.table)
            for i in range(0,8):
                for j in range(0,8):
                    if boardPlayer.table[i][j]==1:
                        boardPlayer.table[i][j]=-2
                        boardComputerTarget.table[i][j]=-2
            ok=isGameWon(boardPlayer.table)
        
    
    elif boardPlayer.table[x][y]==4 and ok==0:
        ok=playerAttack(boardPlayer,boardPlayerTarget,boardComputer)
        if ok==0:
            boardComputerTarget.table[x][y]=-2
            boardPlayer.table[x][y]=-2
            ok=isGameWon(boardPlayer.table)
            for i in range(0,8):
                for j in range(0,8):
                    if boardPlayer.table[i][j]==2:
                        boardPlayer.table[i][j]=-2
                        boardComputerTarget.table[i][j]=-2
            ok=isGameWon(boardPlayer.table)
          
    return ok

def computerAttack(boardPlayer,boardComputerTarget,boardPlayerTarget,boardComputer):
    direction=randint(1,4)
    ok=0
    if direction==1:
        for i in range(1,7):
            if boardPlayer.table[i][i]==0 and ok==0:
                ok=playerAttack(boardPlayer,boardPlayerTarget,boardComputer)
                if ok==0:
                    boardComputerTarget.table[i][i]=-1
                    boardPlayer.table[i][i]=-1
            elif ok==0 and (boardPlayer.table[i][i]==1 or boardPlayer.table[i][i]==2 or boardPlayer.table[i][i]==3 or boardPlayer.table[i][i]==4):
                ok=fill(i,i,boardPlayer,boardComputerTarget,boardPlayerTarget,boardComputer,0)
                if ok==0:
                    if isGameWon(boardComputer.table)==1 or isGameWon(boardPlayer.table)==1:
                        ok=1

                
        for i in range(1,7):
            if boardPlayer.table[i][7-i]==0 and ok==0:
                ok=playerAttack(boardPlayer,boardPlayerTarget,boardComputer)
                if ok==0:
                    boardComputerTarget.table[i][7-i]=-1
                    boardPlayer.table[i][7-i]=-1
            elif ok==0 and (boardPlayer.table[i][7-i]==1 or boardPlayer.table[i][7-i]==2 or boardPlayer.table[i][7-i]==3 or boardPlayer.table[i][7-i]==4):
                ok=fill(i,7-i,boardPlayer,boardComputerTarget,boardPlayerTarget,boardComputer,0)
                
    if direction==2:
        for i in range(1,7):
            if boardPlayer.table[i][7-i]==0 and ok==0:
                ok=playerAttack(boardPlayer,boardPlayerTarget,boardComputer)
                if ok==0:
                    boardComputerTarget.table[i][7-i]=-1
                    boardPlayer.table[i][7-i]=-1
            elif ok==0 and (boardPlayer.table[i][7-i]==1 or boardPlayer.table[i][7-i]==2 or boardPlayer.table[i][7-i]==3 or boardPlayer.table[i][7-i]==4):
                ok=fill(i,7-i,boardPlayer,boardComputerTarget,boardPlayerTarget,boardComputer,0)
                if ok==0:
                    if isGameWon(boardComputer.table)==1 or isGameWon(boardPlayer.table)==1:
                        ok=1
                
        for i in range(1,7):
            if boardPlayer.table[i][i]==0 and ok==0:
                ok=playerAttack(boardPlayer,boardPlayerTarget,boardComputer)
                if ok==0:
                    boardComputerTarget.table[i][i]=-1
                    boardPlayer.table[i][i]=-1
            elif ok==0 and (boardPlayer.table[i][i]==1 or boardPlayer.table[i][i]==2 or boardPlayer.table[i][i]==3 or boardPlayer.table[i][i]==4):
                ok=fill(i,i,boardPlayer,boardComputerTarget,boardPlayerTarget,boardComputer,0)
                
    if direction==3:
        for i in range(6,0,-1):
            if boardPlayer.table[i][i]==0 and ok==0:
                ok=playerAttack(boardPlayer,boardPlayerTarget,boardComputer)
                if ok==0:
                    boardComputerTarget.table[i][i]=-1
                    boardPlayer.table[i][i]=-1
            elif ok==0 and (boardPlayer.table[i][i]==1 or boardPlayer.table[i][i]==2 or boardPlayer.table[i][i]==3 or boardPlayer.table[i][i]==4):
                ok=fill(i,i,boardPlayer,boardComputerTarget,boardPlayerTarget,boardComputer,0)
                if ok==0:
                    if isGameWon(boardComputer.table)==1 or isGameWon(boardPlayer.table)==1:
                        ok=1
                
        for i in range(6,0,-1):
            if boardPlayer.table[i][7-i]==0 and ok==0:
                ok=playerAttack(boardPlayer,boardPlayerTarget,boardComputer)
                if ok==0:
                    boardComputerTarget.table[i][7-i]=-1
                    boardPlayer.table[i][7-i]=-1
            elif ok==0 and (boardPlayer.table[i][7-i]==1 or boardPlayer.table[i][7-i]==2 or boardPlayer.table[i][7-i]==3 or boardPlayer.table[i][7-i]==4):
                ok=fill(i,7-i,boardPlayer,boardComputerTarget,boardPlayerTarget,boardComputer,0)
    if direction==4:
        for i in range(6,0,-1):
            if boardPlayer.table[i][7-i]==0 and ok==0:
                ok=playerAttack(boardPlayer,boardPlayerTarget,boardComputer)
                if ok==0:
                    boardComputerTarget.table[i][7-i]=-1
                    boardPlayer.table[i][7-i]=-1
            elif ok==0 and (boardPlayer.table[i][7-i]==1 or boardPlayer.table[i][7-i]==2 or boardPlayer.table[i][7-i]==3 or boardPlayer.table[i][7-i]==4):
                ok=fill(i,7-i,boardPlayer,boardComputerTarget,boardPlayerTarget,boardComputer,0)
                if ok==0:
                    if isGameWon(boardComputer.table)==1 or isGameWon(boardPlayer.table)==1:
                        ok=1
                
        for i in range(6,0,-1):
            if boardPlayer.table[i][i]==0 and ok==0:
                ok=playerAttack(boardPlayer,boardPlayerTarget,boardComputer)
                if ok==0:
                    boardComputerTarget.table[i][i]=-1
                    boardPlayer.table[i][i]=-1
            elif ok==0 and (boardPlayer.table[i][i]==1 or boardPlayer.table[i][i]==2 or boardPlayer.table[i][i]==3 or boardPlayer.table[i][i]==4):
                ok=fill(i,i,boardPlayer,boardComputerTarget,boardPlayerTarget,boardComputer,0)
    