#!/usr/bin/python

import random
import sys

EMPTY = -1
SELF = 0
OPPONENT = 1

RIGHT = 0
UP_RIGHT = 1
UP = 2
UP_LEFT = 3
LEFT = 4
DOWN_LEFT = 5
DOWN = 6
DOWN_RIGHT = 7

NUM_ROWS = 8
NUM_COLS = 8

def playGame():
    while True:
        rand = int(NUM_COLS*random.random())
        visualizeBoard(board)
        submitMove(rand)
        updateBoard(board)

#DO NOT LOOK AT THE CODE BELOW UNLESS YOU ABSOLUTELY WANT TO

board = [[ EMPTY  for col in range(NUM_COLS) ] for row in range(NUM_ROWS)]
PLAYER_X = -1;
PLAYER_O = -1;

def init():
    playerCode = raw_input()[0]
    for row in range (0,2):
        config = raw_input()
        for col in range (0,NUM_COLS):
            if (config[col] == '.'):
                board[1-row][col] = EMPTY
            else:
                board[1-row][col] = SELF if config[col] == playerCode else OPPONENT
    
    if (playerCode == 'O'):
        PLAYER_X = OPPONENT
        PLAYER_O = SELF
        updateBoard(board)
    else:
        PLAYER_X = SELF
        PLAYER_O = OPPONENT
    return (PLAYER_O, PLAYER_X)

def heightOfColumn(ar, col):
    for row in range (0,NUM_ROWS):
        if ar[row][col] == EMPTY:
            return row
    return NUM_ROWS

def inBounds(ar, row, col):
    return row >= 0 and  row < len(ar) and col >= 0 and col < len(ar[0])

def visualizeBoard(ar):
    print >> sys.stderr, "   ",
    for col in range (0, NUM_COLS):
        print >> sys.stderr, "-",
    print >> sys.stderr, "\n",
    for row in range (NUM_ROWS-1,-1,-1):
        print >> sys.stderr, " %s|" % str(row),
        for col in range (0,NUM_COLS):
            if ar[row][col] == EMPTY:
                out = "."
            elif ar[row][col] == PLAYER_X:
                out = "X"
            else:
                out = "O"
            print >> sys.stderr, out,
        print >> sys.stderr, "|\n",
    print >> sys.stderr, "   ",

    for col in range(0,NUM_COLS):
        print >> sys.stderr, "-",
    print >> sys.stderr, "\n",
    print >> sys.stderr, "   ",

    for col in range(0,NUM_COLS):
        print >> sys.stderr, "%s" % col,

    print >> sys.stderr, "\n",
    sys.stderr.flush()

def submitMove(col):
    if (col >= 0 and col < NUM_COLS):
        sys.stdout.write(str(col))
        sys.stdout.flush()
        row = heightOfColumn(board,col)
        if inBounds(board,row,col):
            board[row][col] = SELF
    else:
        sys.stdout.write("D")
        sys.stdout.flush()

def updateBoard(ar):
    col = int(raw_input())
    row = heightOfColumn(ar,col)
    ar[row][col] = OPPONENT

def numberInARow(ar,row,col,dir):
    if (dir >= 0 and dir < 8 and inBounds(ar,row,col)):
        dr = array(0, 1, 1, 1, 0, -1, -1, -1)
        dc = array(1, 1, 0, -1, -1, -1, 0, 1)
    num = 1
    currRow = row+dr[dir]
    currCol = col+dc[dir]
    while (inBounds(ar,currRow,currCol) and ar[currRow][currCol] == ar[row][col]):
        currRow += dr[dir]
        currCol += dc[dir]
        num += 1

    return num

def maxInARow(ar,row,col):
    max = 0
    for dir in range(0,8):
        max = max(max,numberInARow(ar,row,col,dir))
    return max

def duplicateBoard(ar):
    nar = [[ 0 for col in range(len(ar[0])) ] for row in range(len(ar))]
    for i in range(0, len(ar)):
        for j in range(0, len(ar[0])):
            nar[i][j] = ar[i][j]
    return nar

    print PLAYER_X
if __name__ == "__main__":
    PLAYER_O,PLAYER_X = init()
    playGame()
