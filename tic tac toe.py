board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']
game_still_going = True
current_player = 'X'
winner = None
options = [str(i) for i in range(1, 10)]


def display_board():
    print(board[0] + '  |  ' + board[1] + '  |  ' + board[2])
    print(board[3] + '  |  ' + board[4] + '  |  ' + board[5])
    print(board[6] + '  |  ' + board[7] + '  |  ' + board[8])


def play_game():
    # Display initial board
    display_board()
    print()

    while game_still_going:
        # handle a single player
        handle_turn(current_player)

        # check the game had ended
        check_if_game_over()

        # flip the player from x to o and vice versa.
        flip_player()

    # The game ends.
    if winner == 'X' or winner == 'O':
        print(winner, 'won.')
    elif winner is None:
        print('Tie.')


def handle_turn(player):

    print(player + "'s turn.")
    pos = input('Choose a position(1-9): ')

    valid = True
    while valid:
        while pos not in options:
            pos = input('Choose a position(1-9): ')

        pos = int(pos) - 1

        if board[pos] == '-':
            valid = False
        else:
            print("You can't go there. Go again")

    board[pos] = player
    display_board()
    print('\n')

def check_if_game_over():
    check_for_winner()
    check_if_tie()


def check_for_winner():
    # making winner as a global variable
    global winner

    # check rows,
    row_winner = check_rows()

    # check columns,
    cols_winner = check_cols()

    # check diagonals
    diagonal_winner = check_diagonal()

    if row_winner:
        winner = row_winner
    elif cols_winner:
        winner = cols_winner
    elif diagonal_winner:
        winner = diagonal_winner


def check_rows():
    global game_still_going
    # returns the winner x or o
    row_1 = board[0] == board[1] == board[2] != '-'
    row_2 = board[3] == board[4] == board[5] != '-'
    row_3 = board[6] == board[7] == board[8] != '-'

    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


def check_cols():
    global game_still_going
    # returns the winner x or o
    cols_1 = board[0] == board[3] == board[6] != '-'
    cols_2 = board[1] == board[4] == board[7] != '-'
    cols_3 = board[2] == board[5] == board[8] != '-'

    if cols_1 or cols_2 or cols_3:
        game_still_going = False
    if cols_1:
        return board[0]
    elif cols_2:
        return board[1]
    elif cols_3:
        return board[2]
    return

def check_diagonal():
    global game_still_going
    # returns the winner x or o
    diag_1 = board[0] == board[4] == board[8] != '-'
    diag_2 = board[6] == board[4] == board[2] != '-'

    if diag_1 or diag_2:
        game_still_going = False
    if diag_1:
        return board[0]
    elif diag_2:
        return board[6]
    return


def check_if_tie():
    # checking for tie
    global game_still_going
    if '-' not in board:
        game_still_going = False

def flip_player():
    # literally flipping the player
    global current_player
    # If current player is x then switch to o
    if current_player == 'X':
        current_player = 'O'
    # If current player is o then switch to x
    elif current_player == 'O':
        current_player = 'X'

# This is the function which calls the whole function.
play_game()