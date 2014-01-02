def main():

	board = []
	for i in range(0,5):
		board.append(["O"] * 5)
	
	print_board(board)

def print_board(board):
    for item in board:
        print item
        


if __name__ == "__main__":
  main()
