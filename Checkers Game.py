from random import randint

board = []

for x in range(8):
    board.append(["-"] * 8)

#- will be for no team, X for x team, O for o team

def print_board(board):
    for row in board:
        print (" ".join(row))
		
print_board(board)
