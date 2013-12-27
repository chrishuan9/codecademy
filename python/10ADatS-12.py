def main():
  shopping_list = ["banana", "orange", "apple"]
  #
  stock = { "banana": 6,
           "apple": 0,
           "orange": 32,
           "pear": 15
          }
  #
  prices = { "banana": 4,
            "apple": 2,
            "orange": 1.5,
            "pear": 3
           }
  # Write your code below!

# Write your code below!
def compute_bill(shoppinglist):
    total = 0
    for item in shoppinglist:
        #check if in stock
        if (stock[item] > 0):
            total += prices[item]
            stock[item] -= 1
    return total

if __name__ == "__main__":
  main()
