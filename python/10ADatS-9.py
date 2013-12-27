def main():
  prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
  }
  #
  stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
  }
  total = 0
  for item in stock:
    total+= (stock[item] * prices[item])
    print total

if __name__ == "__main__":
  main()
