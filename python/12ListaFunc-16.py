def main():
	
	n = [3, 5, 7]

	count = n[0] + n[1] + n[2]

	print count
	
	print total(n)

def total(list):
    count = 0
    for item in list:
        count += item
    return count
    

if __name__ == "__main__":
  main()
