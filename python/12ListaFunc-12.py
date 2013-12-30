def main():
n = [3, 5, 7]
# Add your function here
print list_extender(n)


def list_extender(lst):
    lst.append(9)
    return lst


if __name__ == "__main__":
  main()
