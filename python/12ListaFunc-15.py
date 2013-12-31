def main():
	print my_function(range(3)) # Add your range between the parentheses!

"""The Python range() function is just a shortcut for generating a list, so you can use ranges in all the same places you can use lists.

A range can take 1, 2 or 3 arguments. If you use one argument, it starts the range at zero and increments by 1 until the size reaches 1 less than the range. 

For instance:

range(1) # => [0]
range(2) # => [0,1]

If you use two arguments, the first argument is the start for the range and the second argument is the same as above:

range(1,3) # => [1,2]

If you use 3 arguments, the range's first argument is the number the list starts at, the second number is where the list ends, and the third argument is how much you should increment by instead of the default increment of 1. For instance:

range(2,8,3) # => [2,5]
range(2,9,3) # => [2,5,8]


"""

def my_function(x):
    for i in range(0, len(x)):
        x[i] = x[i] * 2
    return x

if __name__ == "__main__":
  main()
