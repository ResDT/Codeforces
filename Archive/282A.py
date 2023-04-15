def main():
    amount = int(input())
    x = 0

    for step in range(amount):
        x += (
            1 if input()[1] == "+"
            else -1
        )

    print(x)


main()
