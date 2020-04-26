'''
Created on Dec 30, 2017

@author: Wolf
'''
  
def validCoord(coord):
    if coord>=0 and coord<=7:
        return True
    else:
        return False
        
def validPlane(x,y,table,orientation):
    '''
    Plane orientation is up.
    '''
    if orientation==1:
        if  x>4 or y<2 or y>5 or table[x][y]!=0 or table[x+1][y]!=0 or table[x+2][y]!=0 or table[x+3][y]!=0 or table[x+1][y-1]!=0 or table[x+1][y-2]!=0 or table[x+1][y+1]!=0 or table[x+1][y+2]!=0 or table[x+3][y-1]!=0 or table[x+3][y+1]!=0:
            return False
            
        else:
            return True
            
    '''
    Plane orientation is to the right.
    '''
    if orientation==2:
        if x<2 or x>5 or y<3 or table[x][y]!=0 or table[x][y-1]!=0 or table[x-1][y-1]!=0 or table[x-2][y-1]!=0 or table[x][y-2]!=0 or table[x][y-3]!=0 or table[x-1][y-3]!=0 or table[x+1][y-3]!=0 or table[x+1][y-1]!=0 or table[x+2][y-1]!=0:
            return False
        else:
            return True
    '''
    Plane orientation is down.
    '''
    if orientation==3:
        if x<3 or y<2 or y>5 or table[x][y]!=0 or table[x-1][y]!=0 or table[x-1][y-1]!=0 or table[x-1][y-2]!=0 or table[x-1][y+1]!=0 or table[x-1][y+2]!=0 or table[x-2][y]!=0 or table[x-3][y]!=0 or table[x-3][y-1]!=0 or table[x-3][y+1]!=0:
            return False
        else:
            return True
    '''
    Plane orientation is to the left.
    '''
    if orientation==4:
        if x<2 or x>5 or y>4 or table[x][y]!=0 or table[x][y+1]!=0 or table[x-1][y+1]!=0 or table[x-2][y+1]!=0 or table[x+1][y+1]!=0 or table[x+2][y+1]!=0 or table[x][y+2]!=0 or table[x-1][y+3]!=0 or table[x+1][y+3]!=0 or table[x][y+3]!=0:
            return False
        else:
            return True
            
def isGameWon(table):
    for i in range(0,8,1):
        for j in range(0,8,1):
            if table[i][j]!=0 and table[i][j]!=-1 and table[i][j]!=-2:
                return 0
    return 1
            
            
            
            
            