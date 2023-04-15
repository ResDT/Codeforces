def main():
    n = input()
    amount_of_lucky_numbers = n.count("4") + n.count("7")

    print(
        "YES" if "".join(set(str(amount_of_lucky_numbers))) in "4774"
        else "NO"
    )


main()
