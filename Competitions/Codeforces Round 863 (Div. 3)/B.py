def main():
    t = int(input())

    for step in range(t):
        n, x_1, y_1, x_2, y_2 = map(int, input().split())
        check_1 = (
            min(x_1, n - y_1 + 1) if x_1 < y_1
            else min(y_1, n - x_1 + 1)
        )
        check_2 = (
            min(x_2, n - y_2 + 1) if x_2 < y_2
            else min(y_2, n - x_2 + 1)
        )

        print(abs(check_1 - check_2))


main()
