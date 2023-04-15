def main():
    s = input()
    subtraction = 0

    for letter in s:
        subtraction += (
            1 if letter.isupper()
            else -1
        )

    print(
        s.upper() if subtraction > 0
        else s.lower()
    )


main()
