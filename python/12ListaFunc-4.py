def main():
"""This exercise will expand on ways to remove items from a list. You actually have a few options. For a list called n: 
    n.pop(index) will remove the item at index from the list and return it to you:
    n.remove(item) will remove the actual item if it finds it
    del(n[1]) is like .pop in that it will remove the item at the given index, but it won't return it"""
    n = [1, 3, 5]
    # Remove the first item in the list here
    n.pop(0)
    print n



if __name__ == "__main__":
    main()
