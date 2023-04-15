def main():
    x = int(input())

    print(x//5 + (
        1 if x % 5
        else 0
    ))


main()
