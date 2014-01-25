def main():
    my_dict = {"Name": "Chris", "Age": 28, "BDFL": True}
    print my_dict.keys()
    print my_dict.values()

    for key in my_dict.keys():
        print key,my_dict[key]


if __name__ == "__main__":
    main()