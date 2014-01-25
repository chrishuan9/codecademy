def main():
    #evens_to_50 = [i for i in range(51) if i % 2 == 0]
    #print evens_to_50

    #even_squares = [j ** 2 for j in range(1,11) if j % 2 == 0]
    #print even_squares

    cubes_by_four = [i for i in range(1,11) if i**4 % 4 == 0]
    print cubes_by_four


if __name__ == "__main__":
    main()