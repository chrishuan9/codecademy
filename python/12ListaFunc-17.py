import string

def main():

	n = ["Michael", "Lieberman"]

	print join_strings(n)

def join_strings(n):
    return string.join(n,"")


if __name__ == "__main__":
  main()
