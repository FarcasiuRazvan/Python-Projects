'''
Created on Jan 2, 2018

@author: Wolf
'''
from src.UI import *
from src.validator import *
from src.board import *

'''
boardplayer, boardcomputer, boardplayerTarget, boardcomputerTarget
'''
boardplayer=board()
boardcomputer=board()
boardplayerTarget=board()
boardcomputerTarget=board()
x=UI(boardplayer, boardcomputer, boardplayerTarget, boardcomputerTarget)
x.menu()