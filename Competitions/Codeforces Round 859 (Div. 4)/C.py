def main():
    t = int(input())

    for step in range(t):
        n = int(input())
        string = input()

        for letter in set(string):
            check = list(place % 2 for place in range(n) if string[place] == letter)

            if 0 in check and 1 in check:
                print("NO")

                break
        else:
            print("YES")
            


main()
