def main():
    amount = int(input())

    for step in range(amount):
        string = input()
        lenth = len(string)

        print(
            f"{string[0]}{lenth - 2}{string[-1]}" if lenth > 10
            else string
        )


main()
