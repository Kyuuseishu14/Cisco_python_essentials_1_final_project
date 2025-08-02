from random import randrange

def display_board(board):
    for i in range(3): 
        print(3*("+" + 7 * "-"), end = "+\n")
        print(3*("|" + 7 * " "), end = "|\n")
        for j in range(3):
            print("|" + 3 * " " + str(board[i][j]) + 3 * " ", end = "")
        print("|")
        print(3*("|" + 7 * " "), end = "|\n")
    print(3*("+" + 7 * "-"), end = "+\n")
    
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.


def enter_move(board):
    free_moves = make_list_of_free_fields(board)
    try:
        player_move = int(input("Please enter your move:"))
    except:
        print("Please enter a valid integer move")
        enter_move(board)
    if player_move not in free_moves.keys():
        print("This square is not available")
        enter_move(board)
    else:
        move = free_moves[player_move]
        board[move[0]][move[1]] = "O"
        if victory_for(board, "O") == True:
            return print("O has won the game")
        else:
            return draw_move(board)
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.


def make_list_of_free_fields(board):
    free_moves = {}
    for i in range(3):
        for j in range(3):
            if type(board[i][j]) is int:
                free_moves[board[i][j]] = (i, j)
            else:
                continue
    return free_moves
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.


def victory_for(board, sign):
    #horizontal check
    for i in range(3):
        if board[i][0] == sign and board[i][1] == sign and board[i][2] == sign:
            return True
        else:
            continue
    #vertical check
    for i in range(3):
        if board[0][i] == sign and board[1][i] == sign and board[2][i] == sign:
            return True
        else:
            continue
    #diagonal check
    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return True
    if board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        return True
    return False
    
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game


def draw_move(board):
    free_moves = make_list_of_free_fields(board)
    if 5 in free_moves.keys():
        move = free_moves[5]
        board[move[0]][move[1]] = "X"
        if victory_for(board, "X") == True:
            return print("X has won the game")
        display_board(board)
        return enter_move(board)
    else:
        comp_move = randrange(1, 9)
        if comp_move in free_moves.keys():
            move = free_moves[comp_move]
            board[move[0]][move[1]] = "X"
            if victory_for(board, "X") == True:
                return print("X has won the game")
            display_board(board)
            return enter_move(board)
        elif comp_move not in free_moves.keys():
            draw_move(board)
    # The function draws the computer's move and updates the board.

default_board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
board = default_board.copy()
draw_move(board)
