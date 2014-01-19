def main():
  print factorial(4)


def factorial(x):
    result = x
    for i in range(1,x):
        result = result * i
    return result


if __name__ == "__main__":
    main()
