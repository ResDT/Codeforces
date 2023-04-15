def number_of_square(n, x, y):
    for number in range(n // 2, 0, -1):
        if number <= x <= n - number + 1 and number <= y <= n - number + 1:
            return number


def main():
    t = int(input())

    for step in range(t):
        n, x_1, y_1, x_2, y_2 = map(int, input().split())

        print(abs(number_of_square(n, x_1, y_1) - number_of_square(n, x_2, y_2)))


main()
