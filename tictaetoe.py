
# making board
board =     ["_","_","_",
            "_","_","_",
            "_","_","_"]

# boolean for loop
game_still_going = True

# this is for winner
winner = None 

# current player
current_player = "x"

# display the board
def display_board():
     print(board[0]+" | "+board[1]+" | "+board[2])
     print(board[3]+" | "+board[4]+" | "+board[5])
     print(board[6]+" | "+board[7]+" | "+board[8])

# start the game
def playgame():
    display_board()
   

# starting the loop 
    while game_still_going:

        print("\n"+current_player+"'s turn")
         
        # handling the turn
        handle_turn(current_player)

        # checking game_over
        check_if_game_over()

        # flip player
        flip_player()
    
    # conditions for winner 
    if winner == "x" or winner == "o":
        print("\n"+winner + " won")
    elif winner == None :
        print("tie")


def handle_turn(player):
    # taking the input for filling the gap
    position = input("\nChoose a position from 1-9:- ")

    valid = False

    while valid == False:

        while position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9'] :
            position = input('\ninvalid input please Choose a position from 1-9:- ')

        position = int(position) - 1

        if board[position] =='_':
            valid = True
        else:
            print("you cannot go there again")

    board[position] = player
    display_board()

def check_if_game_over():
    check_for_winner()
    check_if_tie()
    return


def flip_player():
    global current_player

    if current_player == "x":
        current_player = 'o'
    elif current_player=='o':
        current_player = 'x'
    return


def check_for_winner():

    global winner
    # check rows 
    row_winner = check_rows()
    # check columns
    column_winner = check_columns()
    # check diagonals
    diagonals_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonals_winner:
        winner = diagonals_winner
     
    else:
        winner = None

    return

def check_columns():
    # set the global variables
    global game_still_going

    # check if any of the rows have all the same value (and is not empty )
    column_1 = board[0] == board[3]== board[6] !="_"
    column_2 = board[1] == board[4]== board[7] !="_"
    column_3 = board[2] == board[5]== board[8] !="_"

    # if any column does have a match , flag that there a win
    if column_1 or column_2 or column_3:
        game_still_going = False


    # return the winner (x or o)
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return

def check_rows():
    # set the global variables
    global game_still_going

    # check if any of the rows have all the same value (and is not empty )
    row_1 = board[0] == board[1]== board[2] !="_"
    row_2 = board[3] == board[4]== board[5] !="_"
    row_3 = board[6] == board[7]== board[8] !="_"

    # if any row does have a match , flag that there a win
    if row_1 or row_2 or row_3:
        game_still_going = False


    # return the winner (x or o)
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]

    return
    

def check_diagonals():
    # set the global variables
    global game_still_going

    # check if any of the rows have all the same value (and is not empty )
    diagonal_1 = board[0] == board[4]== board[8] !="_"
    diagonal_2 = board[2] == board[4]== board[6] !="_"
    

    # if any diagonal does have a match , flag that there a win
    if diagonal_1 or diagonal_2 :
        game_still_going = False


    # return the winner (x or o)
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    
    
    return

def check_if_tie():
    global game_still_going
    if "_" not in board:
        game_still_going = False
    return


playgame()

# 

#board
# display board
# play game
    # handle turn
# check win 
    # check row 
    # check column 
    # check diagnols
# check tie
# flip the players    


#

