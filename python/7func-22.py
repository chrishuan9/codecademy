import types

def distance_from_zero(par1):
    t1 = type(par1)
    if type(par1) is types.IntType or type(par1) is types.FloatType:
        return abs(par1)
    else:
        return "Not an integer or float!"


def main():
#my code here
    print distance_from_zero(-3.0)

if __name__ == "__main__":
    main()
