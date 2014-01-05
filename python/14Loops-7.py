def main():
	import random

	print "Lucky Numbers! 3 numbers will be generated."
	print "If one of them is a '5', you lose!"

	count = 0
	while count < 3:
		""" If the loop exits as the result of a break, the else will           not be executed. """
		num = random.randint(1, 6)
		print num
		if num == 5:
			print "Sorry, you lose!"
			break
		count += 1
	else:
		print "You win!"
		
if if __name__ == "__main__":
  main()