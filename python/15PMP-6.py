def main():

  print is_prime(2)
  print is_prime(5)
  print is_prime(11)
  print is_prime(4)
  print is_prime(18)
  print is_prime(21)
  print is_prime(-2)



def is_prime(x):
    result = True
    if x == 1: return False
    if x > 0:
      for i in range(1,abs(x)):
          if abs(x) % i == 0 and i != 1:
              result = False
    else:
      for i in range(x,0):
        if x % i == 0:
            result = False
    return result


if __name__ == "__main__":
	main()

