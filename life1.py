## First try implementing game of life

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib import colors

def makeBoard(n,m,l=[]):
    ### Creates a n x m dimensional matix of zeros
    board = np.zeros( (n,m) )
    for x in l:
        board[x[0]][x[1]] = 1
    return board


def countNb(board,k,l):
    ### Returns the number of nbs of a live cell
    nb = -board[k][l]
    for i in range(k-1,k+2):
        for j in range(l-1,l+2):
            if  i >= 0 and i < len(board) and j >= 0 and j < len(board[0]):
                nb += board[i][j]
    return nb



def step(board):
    dim = board.shape
    newBoard = makeBoard(dim[0],dim[1])

    for i in range(0,dim[0]):
        for j in range(0,dim[1]):
            nb = countNb(board,i,j)
            if nb == 2:
                newBoard[i][j] += board[i][j]
            elif nb == 3:
                newBoard[i][j] = 1
            elif nb > 3:
                newBoard[i][j] = 0

    return newBoard



l = [(1,2), (2,2), (3,2) ] + [(20,20),(20,21),(20,22),(21,22)] + [(40,10),(41,10),(39,11),(42,11),(43,12)]


b = makeBoard(50,50,l) 

def sim(frame):
    global b

    if frame>0:
        b = step(b)
    im.set_array(b)
    return im,
    

fig = plt.figure()
ax = fig.add_subplot()
ax.axis('off')
im = ax.imshow(b, cmap='Greys', interpolation='nearest')

anim = animation.FuncAnimation(fig, sim, frames=100, interval=1000, blit=True, repeat=False)
plt.show()


