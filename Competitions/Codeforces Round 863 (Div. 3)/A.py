def main():
    t = int(input())

    for step in range(t):
        n, d = map(int, input().split())
        number = input()
        flag = True

        for place, digit in enumerate(number):
            if int(digit) >= d or not flag:
                print(digit, end="")
            elif d > int(digit):
                print(d, digit, sep="", end="")

                flag = False

        if flag:
            print(d, end="")

        print()


main()
