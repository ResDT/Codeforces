def main():
    amount = int(input())

    print(
        "YES" if not (amount % 2) and amount > 3
        else "NO"
    )


main()
