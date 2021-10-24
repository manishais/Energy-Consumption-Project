
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Jackson Hosea
#               Matthew Strode
#               Jennyfer Hoang
#               Manisha Subrahmanya
# Section:      566
# Assignment:   Lab7a_Act1.py
# Date:   Oct 19th, 2021      

from math import *

e = '.'                 # empty square
a = chr(9675)           # player 1
b = chr(9679)           # player 2

#  8 rows and columns
board = [
  [e,a,e,a,e,a,e,a],
  [a,e,a,e,a,e,a,e],
  [e,a,e,a,e,a,e,a],
  [e,e,e,e,e,e,e,e],
  [e,e,e,e,e,e,e,e],
  [b,e,b,e,b,e,b,e],
  [e,b,e,b,e,b,e,b],
  [b,e,b,e,b,e,b,e]
        ]
usermove = ''
# print out board
def boardPrint():
    for i in range(8):
        for j in range(8):
            print(board[i][j], end = ' ')
        print()

boardPrint()

diag = False
validPiece = False
pieceID = ''
while usermove!="stop":
    validPiece = False
    while validPiece !=True:
        print("Use numbers 1 - 8 to indicate the row and column")
        usermove = input("Enter the row and column of piece you want to move separated by space): ")
        if usermove == 'stop':
            break
        if len(usermove)==3:# checks for correctly formatted input by checking the characters in usermove
            #sets row and column for the piece being moved
            pieceRow = int(usermove[0])-1
            pieceCol = int(usermove[2])-1
            #checks if a checkers piece is on the index obtained by the user input. 
            if board[pieceRow][pieceCol] == chr(9675):
                pieceID = chr(9675)
                validPiece = True
            elif board[pieceRow][pieceCol] == chr(9679):
                pieceID = chr(9679)
                validPiece = True
            else:
                print("Error, please try again...")
           
        else:
            print("Error, please try again...")
            
        diag = False
        
    while usermove !='stop' and diag!=True :
        #asks for user input. If input is 'stop' then loop is ended
        usermove = input("Enter row and column you want to move to: ")
        if usermove == 'stop':
            break
        
        # checks for valid input format
        if len(usermove)==3:
            #sets index of position to be move to
            pieceRow2 = int(usermove[0])-1
            pieceCol2 = int(usermove[2])-1
            #checks if position being moved is diagonal from original positon and is on the board
            #if true, piece will move to that position and board will print
            #if false, prompt the user of the invalid move and will continue to ask for input until valid input is given
            if (pieceCol+1)%2!=0 and (pieceCol2+1)%2==0 and pieceRow!=pieceRow2 and 0<=pieceCol2<=7:
                diag = True
                board[pieceRow2][pieceCol2] = pieceID
                board[pieceRow][pieceCol] = e
                boardPrint()
            elif (pieceCol+1)%2==0 and (pieceCol2+1)%2!=0 and pieceRow!=pieceRow2 and 0<=pieceCol2<=7:
                diag = True
                board[pieceRow2][pieceCol2] = pieceID
                board[pieceRow][pieceCol] = e
                boardPrint()
            else:
                print("Invalid move! Please try again.")
        else:
            print("Invalid move! Please try again.")