def main():
  print median([4,5,5,4])


def median(numbers):
	sortedlist = sorted(numbers)
	print(sortedlist)
	if len(sortedlist) % 2 == 0:
		print("list contains even number of elements")
		indexhigh = len(sortedlist)//2
		print ("Highindex %d") %(indexhigh)
		return (float(sortedlist[indexhigh]) + float(sortedlist[indexhigh-1])) / 2
	else:
		print("list contains odd number of elements")
		indexmedian = len(sortedlist)//2
		return sortedlist[indexmedian]


if __name__ == "__main__":
    main()
