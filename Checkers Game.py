from random import randint

board = []

for x in range(8):
    board.append(["O"] * 8)

def print_board(board):
    for row in board:
        print (" ".join(row))

end_game = raw_input ("Press Enter to End the Game")