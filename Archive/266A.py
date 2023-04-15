from itertools import groupby

def main():
    n = int(input())
    S = input()

    print(len(S) - len([letter[0] for letter in groupby(S)]))


main()
