from datetime import date       # Import this for date
import getpass                  # Import this for username
import random                   # import this to use random

######################################################################
#                                                                    #
#   Author: Sorochi Iwuji                                            #
#   Date Written: 04/12/2022                                         #
#   Purpose: This is a program that creates a TicTacToe game         #
#                                                                    #
######################################################################

# This shows todays date and active user as a string so it will all be in one line at the top
print(str(getpass.getuser()) + '            ' + str(date.today()))

# This prints no matter what, and can be placed somewhere else if needed
print('Welcome to Tic Tac Toe!') 

# This allows the next couple of lines from 22-32 to perfom the specific task of creating the game board
def drawBoard(board):

    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def inputPlayerLetter():
    # This lets the player pick a letter either X or O, as well as gives the computer their own letter
    letter = ''
    # This allows no matter how many times I use another character or letter it will always loop right back to the print statement, till the function is satisfied
    while not (letter == 'X' or letter == 'O'): 
        # This asks the player which letter they would like to be
        print('Would you like to be X or O?')
        # This forces anylowercase O or X to be uppercase so the transition would be smoother
        letter = input().upper() 
    # This lets the computer know that if I choose an X, that the computer is O 'else' it's the other way round
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    # This alows for the random decision of which player would go first
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def playAgain():
    # This allows the player the option to play again, if the player inputed a word that starts with 'y'
    print('Would you like to play again? (yes or no)')
    return input().lower().startswith('y')

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
    # Both the computer and the player get a letter, and if the player wins this statements becomes true, as well as the spelling shortcut saves time. These are possoble ways to win a total of 8.
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
    (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
    (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
    (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

# This allows us to copy the board from the beginning without any of the previous lettters within it, and return it to the duplicate
def getBoardCopy(board):
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard

# This allows if the space picked is free then there is to be a return 'true' on the previous board
def isSpaceFree(board, move):
    return board[move] == ' '

def getPlayerMove(board):
    # This lets the player make a choice on their move
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)


def chooseRandomMoveFromList(board, movesList):
    possibleMoves = []
    # This returns a valid move from the passed list on the previous board not picked, from player
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    # This returns none if its not a valid move, from player
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

# This gives you the next board with the computers choice of position picked, determines where to move and return that move
def getComputerMove(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # Here are the algorithms for possible moves the Tic Tac Toe AI can make
    # This lets the computer see possible moves if it can win in the next move
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i

    # This lets the computer see a possible win i have in the next move, and stops it
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    # This allows the computer to take one of the corners at random if it is free
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    # This allows the computer to take the free space if it is free
    if isSpaceFree(board, 5):
        return 5

    # This allows the computer to move on one of the sides at random if it is free
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
    # This returns true if every space of the board has been taken, otherwise it will return false
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

while True:
    # Resets the game/ board
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True
    # This is a loop during the game
    while gameIsPlaying: 
        if turn == 'player':
            # Player’s turn.
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            # If this statement is true then the player wins else it is a tie or else the computers turn
            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Hooray! You have won the game!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'

        else:
            # Computer’s turn.
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            # If this statement is true then the computter wins else it is a tie or else the players turn
            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('The computer has beaten you! You lose.')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'

    if not playAgain(): #This is the other option for not playing another round of tic tac toe
        break #This allows us to break from the loop of the game
