def main():
"""Arbitrary number of arguments
This exercise goes over how to take an arbitrary number of arguments in a function."""

m = 5
n = 13

def add_function(*args):
  return sum(args)

print add_function(m, n)



if __name__ == "__main__":
  main()
