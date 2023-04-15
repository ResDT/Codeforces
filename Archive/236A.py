def main():
    string = input().lower()

    print(
        "IGNORE HIM!" if len(set(string)) % 2
        else "CHAT WITH HER!"
    )


main()
