def main():
    n = int(input())
    s = input()

    print(
        "Anton" if s.count("A") > s.count("D")
        else "Danik" if s.count("D") > s.count("A")
        else "Friendship"
    )


main()
