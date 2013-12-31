import itertools

def main():
	n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
	# Add your function here
	print flatten(n)

def flatten(n):
    return list(itertools.chain(*n))



if __name__ == "__main__":
  main()
