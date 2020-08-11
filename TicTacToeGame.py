def displayBoard(board):
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])

def playerInput():
    marker=''
    while not(marker=='X' or marker=='O'):
        marker=input("Player1: choose x or o : ").upper()
    if marker=='X':
        return ('X','O')
    else:
        return ('O','X')

def placeMarker(board,marker,position):
    board[position]=marker

def winCheck(board,marker):
    return ((board[7]==marker and board[8]==marker and board[9]==marker) or
            (board[4]==marker and board[5]==marker and board[6]==marker) or
            (board[1]==marker and board[2]==marker and board[3]==marker) or 
            (board[1]==marker and board[4]==marker and board[7]==marker) or
            (board[2]==marker and board[5]==marker and board[8]==marker) or
            (board[3]==marker and board[6]==marker and board[9]==marker) or
            (board[1]==marker and board[5]==marker and board[9]==marker) or 
            (board[7]==marker and board[5]==marker and board[3]==marker))

import random
def chooseFirst():
    flip=random.randint(0,1)
    if flip==0:
        return 'Player 1'
    else:
        return 'Player 2'

def spaceCheck(board,position):
    return board[position]==' '

def fullBoardCheck(board):
    for i in range(1,10):
        if spaceCheck(board,i):
            return False
        #Board is full we return True
        else:
            return True

def playerChoice(board):
    position=0
    while position not in[1,2,3,4,5,6,7,8,9] or not spaceCheck(board,position):
        position=int(input("Choose a position. (1-9) "))
    return position

def replay():
    choice=input("Play again? Enter Yes or No: ")
    return choice=='yes'
print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1Marker, player2Marker = playerInput()
    turn = chooseFirst()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            displayBoard(theBoard)
            position = playerChoice(theBoard)
            placeMarker(theBoard, player1Marker, position)

            if winCheck(theBoard, player1Marker):
                displayBoard(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if fullBoardCheck(theBoard):
                    displayBoard(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            displayBoard(theBoard)
            position = playerChoice(theBoard)
            placeMarker(theBoard, player2Marker, position)

            if winCheck(theBoard, player2Marker):
                displayBoard(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if fullBoardCheck(theBoard):
                    displayBoard(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
