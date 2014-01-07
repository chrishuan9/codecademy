def main():
	print digit_sum(1234)

def digit_sum(x):
    digits = []
    while abs(x) > 0:
        digits.append(x % 10) #rightmost digit from the number
        x = x // 10 #remove rightmost digit from the number
    return sum(digits)
    

if __name__ == "__main__":
	main()