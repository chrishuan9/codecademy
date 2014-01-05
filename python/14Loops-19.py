def main():
	numbers = [4 , 5 , 6 , 7]

	print "You have..."

	for number in numbers:
		if number == 7:
			print "The lucky number seven"
			break
		print number
	else:
		print "Lucky, you won"
		
if __name__ == "__main__":
  main()