'''
Created on Jan 2, 2018

@author: Wolf
'''

class board(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.table=[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]

    def addPlane(self,x,y,orientation,cabin,plane):
        if orientation==1:
            self.table[x][y]=cabin
            self.table[x+1][y-2]=plane
            self.table[x+1][y-1]=plane
            self.table[x+1][y]=plane
            self.table[x+1][y+1]=plane
            self.table[x+1][y+2]=plane
            self.table[x+2][y]=plane
            self.table[x+3][y-1]=plane
            self.table[x+3][y]=plane
            self.table[x+3][y+1]=plane
        elif orientation==2:
            self.table[x][y]=cabin
            self.table[x-2][y-1]=plane
            self.table[x-1][y-1]=plane
            self.table[x][y-1]=plane
            self.table[x+1][y-1]=plane
            self.table[x+2][y-1]=plane
            self.table[x][y-2]=plane
            self.table[x-1][y-3]=plane
            self.table[x][y-3]=plane
            self.table[x+1][y-3]=plane
        elif orientation==3:
            self.table[x][y]=cabin
            self.table[x-1][y-2]=plane
            self.table[x-1][y-1]=plane
            self.table[x-1][y]=plane
            self.table[x-1][y+1]=plane
            self.table[x-1][y+2]=plane
            self.table[x-2][y]=plane
            self.table[x-3][y-1]=plane
            self.table[x-3][y]=plane
            self.table[x-3][y+1]=plane
        elif orientation==4:
            self.table[x][y]=cabin
            self.table[x-2][y+1]=plane
            self.table[x-1][y+1]=plane
            self.table[x][y+1]=plane
            self.table[x+1][y+1]=plane
            self.table[x+2][y+1]=plane
            self.table[x][y+2]=plane
            self.table[x-1][y+3]=plane
            self.table[x][y+3]=plane
            self.table[x+1][y+3]=plane
            
        elif orientation==5:
            self.table[x][y]=cabin
            self.table[x-1][y]=plane
            self.table[x-2][y]=plane
            self.table[x-3][y]=plane
            self.table[x-1][y-1]=plane
            self.table[x-1][y-2]=plane
            self.table[x-1][y+1]=plane
            self.table[x-1][y+2]=plane
            self.table[x-3][y-1]=plane
            self.table[x-3][y+1]=plane
        
    def list(self):
        print("    0   1   2   3   4   5   6   7")
        print("")
        for i in range(0,8):
            if self.table[i][0]==-1:
                unu='X'
            elif self.table[i][0]==-2:
                unu='Y'
            else:
                unu=self.table[i][0]
                
            if self.table[i][1]==-1:
                doi='X'
            elif self.table[i][1]==-2:
                doi='Y'
            else:
                doi=self.table[i][1]
                
            if self.table[i][2]==-1:
                trei='X'
            elif self.table[i][2]==-2:
                trei='Y'
            else:
                trei=self.table[i][2]
                
            if self.table[i][3]==-1:
                patru='X'
            elif self.table[i][3]==-2:
                patru='Y'
            else:
                patru=self.table[i][3]
                
            if self.table[i][4]==-1:
                cinci='X'
            elif self.table[i][4]==-2:
                cinci='Y'
            else:
                cinci=self.table[i][4]
                
            if self.table[i][5]==-1:
                sase='X'
            elif self.table[i][5]==-2:
                sase='Y'
            else:
                sase=self.table[i][5]
                
            if self.table[i][6]==-1:
                sapte='X'
            elif self.table[i][6]==-2:
                sapte='Y'
            else:
                sapte=self.table[i][6]
            
            if self.table[i][7]==-1:
                opt='X'
            elif self.table[i][7]==-2:
                opt='Y'
            else:
                opt=self.table[i][7]
            print(i," ",unu,"|",doi,"|",trei,"|",patru,"|",cinci,"|",sase,"|",sapte,"|",opt)
            print("    -----------------------------")

            