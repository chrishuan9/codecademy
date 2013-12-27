def main():
    #List indices begin with 0, not 1! You access the first item in a list like this: list_name[0]. The second item in a list is at index 1: list_name[1]. Computer scientists love to start counting from zero.
    numbers = [5, 6, 7, 8]
    print "Adding the numbers at indices 0 and 2..."
    print numbers[0] + numbers[2]
    print "Adding the numbers at indices 1 and 3..."
    print numbers[1] + numbers[3]
if __name__ == "__main__":
    main()
