from itertools import groupby


def main():
    amount = int(input())

    for step in range(amount):
        lenth = int(input())
        string = input().lower()

        print(
            "YES" if "".join(letter for letter, mark in groupby(string)) == "meow"
            else "NO"
        )


main()
