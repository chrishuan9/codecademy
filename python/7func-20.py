from string import lower
#import string

def shut_down(s):
    lowercase = lower(s)
    if (lowercase == "yes"):
        return "Shutting down..."
    elif (lowercase == "no"):
        return "Shutdown aborted!"
    else:
        return "Sorry, I didn't understand you."

def main():
    # my code here
    print shut_down("yes")

if __name__ == "__main__":
    main()
