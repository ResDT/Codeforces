def main():
    first_string = input().lower()
    second_string = input().lower()

    print(
        -1 if first_string < second_string
        else int(first_string > second_string)
    )


main()
