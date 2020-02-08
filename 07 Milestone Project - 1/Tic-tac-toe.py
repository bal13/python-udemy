def clear_display():
    for num in range(100):
        print("\n")

def display_board(board):
    
    print("   |   |   ")
    print(f" {board[1]} | {board[2]} | {board[3]} ")
    print("   |   |   ")
    print("------------")
    print("   |   |   ")
    print(f" {board[4]} | {board[5]} | {board[6]} ")
    print("   |   |   ")
    print("------------")
    print("   |   |   ")
    print(f" {board[7]} | {board[8]} | {board[9]} ")
    print("   |   |   ")

#test_board = ['#','X','O','X','O','X','O','X','O','X']
#display_board(test_board)


def player_input():

    player1 = ""

    while True:
        player1 = input("Please pick a marker 'X' or 'O'").upper();
        if player1 == "X" or player1 == "O":
            return player1
        else:
            print("Wrong choice") 
    

#player_input()

def place_marker(board, marker, position):
    
    board[position] = marker

#place_marker(test_board,'$',8)
#display_board(test_board)

def win_check(board, mark):
    
    retVal = False

    if board[1] == mark and board[2] == mark and board[3] == mark:
        retVal = True
    elif board[4] == mark and board[5] == mark and board[6] == mark:
        retVal = True
    elif board[7] == mark and board[8] == mark and board[9] == mark:
        retVal = True
    elif board[1] == mark and board[4] == mark and board[7] == mark:
        retVal = True
    elif board[2] == mark and board[5] == mark and board[8] == mark:
        retVal = True
    elif board[3] == mark and board[6] == mark and board[9] == mark:
        retVal = True
    elif board[1] == mark and board[5] == mark and board[9] == mark:
        retVal = True
    elif board[3] == mark and board[5] == mark and board[7] == mark:
        retVal = True

    return retVal

#print(win_check(test_board,'X'))

import random

def choose_first():
    
    if random.randint(1,2) == 1:
        print("X starts!")
        return "X"
    else:
        print("O starts")
        return "O"
    
#print(choose_first())

def space_check(board, position):
    
    return board[position]==" "

#print(space_check(test_board, 9))

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

#print(full_board_check(test_board))


def player_choice(board):
    while True:
        player_place = int(input("Please pick a number from 1 to 9"))
        if player_place in range(1, 10) and space_check(board, player_place):
            return player_place
        else:
            print("Wrong choice")

#player_choice(test_board)

def replay():
    
    while True:
        replay = input("Do you want to replay? [yes, no]").upper();
        if replay == "YES":
            return True
        elif replay == "NO":
            return False
        else:
            print("Wrong choice") 

#replay()

print('Welcome to Tic Tac Toe!')

def switch_marker(current_marker):
    if current_marker == 'X':
        return 'O'
    else:
        return 'X'

while True:
    # Set the game up here
    board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    player1 = player_input()
    if(player1 == 'X'):
        player2 = 'O'
    else:
        player2 = 'X'
    print(f"Player 1: {player1}")
    print(f"Player 2: {player2}")
    current_marker = choose_first()


    while True:

        player_current_choice = player_choice(board)
        place_marker(board, current_marker, player_current_choice)
        display_board(board)
        if(win_check(board, current_marker)):
            
            print(f"{current_marker} has won the game!")
            break

        if full_board_check(board):
            print("Game is draw!")
            break

        current_marker = switch_marker(current_marker)
        clear_display()
        display_board(board)

        

    is_replay = replay()
    if not is_replay:
        print("Bye!")
        break