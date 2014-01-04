def main():
	board = []
	for i in range(0,5):
		board.append(["O"] * 5)
	
	print_board(board)


def print_board(board):
    separator = " "
    for list in board:
        print separator.join(list)
        


if __name__ == "__main__":
  main()
