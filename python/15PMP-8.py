"""Instructions
Let's write a function called anti_vowel that takes one string, text, as input and returns the text with all of the vowels removed.

For example: anti_vowel("Hey You!") should return "Hy Y!".

Don't count Y as a vowel.
Make sure to remove lowercase and uppercase vowels."""

def main():
    print anti_vowel("Hey You!")


def anti_vowel(input):
    result = ""
    vowels = ["A","a","E","e","I","i","O","o","U","u"]
    for ch in input:
        if ch in vowels:
            print "found vowel"
        else:
            result+=ch
    return result




if __name__ == "__main__":
    main()