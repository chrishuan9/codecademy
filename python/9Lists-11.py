def main():
    #Like Lists, Dictionaries are "mutable
    #An empty pair of curly braces {} is an empty dictionary, just like an empty pair of [] is an empty list.
    menu = {} # Empty dictionary
    menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
    print menu['Chicken Alfredo']
    # Your code here: Add some dish-price pairs to menu!
    menu["Chicken Teriyaki"] = 12.99
    menu["Chicken Chop sue"] = 9.99
    menu["Fried Rice"] = 7.99
    #print out the menu
    print "There are " + str(len(menu)) + " items on the menu."
    print menu

if __name__ == "__main__":
    main()
