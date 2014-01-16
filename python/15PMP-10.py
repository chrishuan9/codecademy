from string import replace

def main():
    print censor("this hack is wack hack", "hack")

def censor(text, word):
    return replace(text,word,"*"*len(word))


if __name__ == "__main__":
    main()
