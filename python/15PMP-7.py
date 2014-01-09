def main():
  reverse("abcd")


def reverse(text):
    result = []
    for ch in text:
        result.insert(0,ch)
    return ''.join(result)

if __name__ = "__main__":
  main()
