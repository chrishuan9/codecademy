def main():
    #
    #If your list is a jumbled mess, you may need to sort() it. 
    #my_list.sort() will sort the items in my_list in increasing numerical/alphabetical order.
    #
    start_list = [5, 3, 1, 2, 4]
    square_list = []
    #
    #It's worth noting that sort() does not return a new list; instead, your existing my_list is sorted in place 
    #(the sorted version replaces the unsorted version).
    #
    for number in start_list:
        square_list.append(number ** 2)
        square_list.sort()
        print square_list


if __name__ == "__main__":
    main()
