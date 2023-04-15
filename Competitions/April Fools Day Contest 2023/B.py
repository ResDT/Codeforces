def main():
    n = int(input())
    good = [1, 3, 5, 7, 11, 13]
    bad = [15]

    print(
        "YES" if n in good
        else "NO"
    )


main()
