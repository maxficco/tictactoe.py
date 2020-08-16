board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

def print_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])
def show_rules():
    print('''
Welcome to Max's Tic Tac Toe!

    How to Play:
    1. Here is the Board
        1 | 2 | 3
        4 | 5 | 6
        7 | 8 | 9
    2. Start with player X's turn, and type which corresponding number
       you would like to place your X
    3. Next, player O will go
    4. First player to three in a row wins!

    ''')
show_rules()

turn = "playerx"
running = True
xsolved = False
osolved = False
tie = False
while running:
    print_board()
    #check for tie
    for index in range(0,9):
        tie = True
        if board[index] == "-":
            tie = False
    #check for X win scenario
    if board[0] == "X" and board[1] == "X" and board[2] == "X":
        xsolved = True
    if board[3] == "X" and board[4] == "X" and board[5] == "X":
        xsolved = True
    if board[6] == "X" and board[7] == "X" and board[8] == "X":
        xsolved = True
    if board[0] == "X" and board[3] == "X" and board[6] == "X":
        xsolved = True
    if board[1] == "X" and board[4] == "X" and board[7] == "X":
        xsolved = True
    if board[2] == "X" and board[5] == "X" and board[8] == "X":
        xsolved = True
    if board[0] == "X" and board[4] == "X" and board[8] == "X":
        xsolved = True
    if board[2] == "X" and board[4] == "X" and board[6] == "X":
        xsolved = True
    #check for O win scenario
    if board[0] == "O" and board[1] == "O" and board[2] == "O":
        xsolved = True
    if board[3] == "O" and board[4] == "O" and board[5] == "O":
        xsolved = True
    if board[6] == "O" and board[7] == "O" and board[8] == "O":
        xsolved = True
    if board[0] == "O" and board[3] == "O" and board[6] == "O":
        xsolved = True
    if board[1] == "O" and board[4] == "O" and board[7] == "O":
        xsolved = True
    if board[2] == "O" and board[5] == "O" and board[8] == "O":
        xsolved = True
    if board[0] == "O" and board[4] == "O" and board[8] == "O":
        xsolved = True
    if board[2] == "O" and board[4] == "O" and board[6] == "O":
        xsolved = True
    if xsolved == True:
        print("Game Over! Player X Wins!")
        running = False
    elif osolved == True:
        print("Game Over! Player O Wins!")
        running = False
    elif tie == True:
        print("Game Over! Tie!")
        running = False
    else:
        if turn == "playerx":
            player_x_move = input("Player X's Turn: ")
            location = int(player_x_move) - 1
            board[location] = "X"
            turn = "playero"
        elif turn == "playero":
            player_o_move = input("Player O's Turn: ")
            location = int(player_o_move) - 1
            board[location] = "O"
            turn = "playerx"
