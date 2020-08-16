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

def playgame():
    show_rules()
    print_board()
    playerXmove = input("Player X's Turn: ")
    print(playerXmove)


playgame()
