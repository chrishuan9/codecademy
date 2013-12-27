def main():
    #You can also use a for loop on a dictionary to loop through its keys
    #Note that dictionaries are unordered, meaning that any time you loop through a dictionary, you will go through every key, 
    #but you are not guaranteed to get them in any particular order.
    webster = {
        "Aardvark" : "A star of a popular children's cartoon show.",
        "Baa" : "The sound a goat makes.",
        "Carpet": "Goes on the floor.",
        "Dab": "A small amount."
    }
    # Add your code below!
    for key in webster:
        print webster[key]

if __name__ == "__main__":
    main()
