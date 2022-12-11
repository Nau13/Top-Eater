import numpy as np

BLUE = (0,0,255)
RED = (255,0,0)
BLACK = (0,0,0)

COL_COUNT =7
ROW_COUNT =6
temp = np.zeros((1,ROW_COUNT))
def create_board():
    board = np.zeros((ROW_COUNT,COL_COUNT))
    return board

def dropPiece(board,row,col,piece):
  board[row][col]=piece

def printBoard():
  print(np.flip(board,0))
  
def isValidLocation(board,col):
  return board[5][col]==0

def getNextOpenRow(board,col):
    for r in range(ROW_COUNT):
        if board[r][col]==0:
            return r
  
def winningMove(board):
  count1=0
  count2=0
  for c in range(COL_COUNT):
    for r in range(ROW_COUNT):
      if board[r][c]==1:
        count1+=1
      elif board[r][c]==2:
        count2+=1

  if count1>count2:
    print("Player 1 wins!\nPlayer 1 got "+str(count1)+" token. PLayer 2 got "+str(count2)+" token.")
  elif count1<count2:
    print("Player 2 wins!\nPlayer 1 got "+str(count1)+" token. PLayer 2 got "+str(count2)+" token.")
  elif count1==count2:
    print("Tie.\nPlayer 1 got "+str(count1)+" token. PLayer 2 got "+str(count2)+" token.")

def eat(board, row, col,piece):
  if col>=1:
    if board[row][col-2]==piece :
      board[row][col-1]=piece
        
  if col<5:
    if board[row][col+2]==piece:
      board[row][col+1]=piece
  
board=create_board()
game_over=False
printBoard()
turn =0

while not game_over:
  
    #ask Player 1 input
    if turn==0:
        col = int(input("Player 1 make your selection(0-6):"))
        if isValidLocation(board,col):
          row = getNextOpenRow(board,col)
          dropPiece(board, row, col, 1)
          eat(board, row, col, 1)
          if row==5:
            game_over=True
    #ask Player 2 input
    else:
        col = int(input("Player 2 make your selection(0-6):"))
        if isValidLocation(board,col):
          row = getNextOpenRow(board,col)
          dropPiece(board, row, col, 2)
          eat(board, row, col, 2)
          if row==5:
            game_over=True

    
    printBoard()
    turn+=1
    turn=turn%2
winningMove(board)