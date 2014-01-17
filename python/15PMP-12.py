def main():
    print purify([1, 2, 1, 1])

def purify(numbers):
    resultlist = []
    for element in numbers:
        if element % 2 == 0 :
            resultlist.append(element)
    return resultlist


if __name__ == "__main__":
    main()
