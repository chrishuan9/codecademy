from random import randint

def main():

	board = []

	for x in range(0, 5):
		board.append(["O"] * 5)
		
	print_board(board)
	
	ship_row = random_row(board)
	ship_col = random_col(board)
	guess_row = int(raw_input("Guess Row:"))
	guess_col = int(raw_input("Guess Col:"))

	print ship_row
	print ship_col

	# Write your code below!
	if guess_row == ship_row and guess_col == ship_col:
		print "Congratulations!You sank my battleship!"
	else:
		if guess_row > (len(board[0]) - 1) or guess_col > (len(board[0]) - 1):
			print "Oops, that's not even in the ocean."
		else:
		if guess_row > (len(board[0]) - 1) or guess_col > (len(board[0]) - 1):
			print "Oops, that's not even in the ocean."
		elif board[int(guess_row)][int(guess_col)] == "X":
			print "You guessed that one already."
		else:
			print "You missed my battleship!"
			#change the list element to indicate an incorrect guess
			board[int(guess_row)][int(guess_col)] = "X"


def print_board(board):
    for row in board:
        print " ".join(row)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

if __name__ == "__main__":
  main()
