def main():
    t = int(input())

    for step in range(t):
        a, b, c = map(int, input().split())

        print(
            "+" if a + b == c
            else "-"
        )


main()
