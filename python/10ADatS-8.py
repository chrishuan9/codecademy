def main():
  #dictionary definition see: http://docs.python.org/2/tutorial/datastructures.html#dictionaries
  http://docs.python.org/2/tutorial/datastructures.html#dictionaries
  prices={"banana":4,"apple":2,"orange":1.5,"pear":3}
  stock={"banana":6,"apple":0,"orange":32,"pear":15}
  #
  for item in prices:
    print item
    print "price: " + str(prices[item])
    print "stock: " + str(stock[item])

if __name__ == "__main__":
    main()
