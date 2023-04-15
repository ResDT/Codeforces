def amount_of_obstacles(x, y, n, m):
    amount = 4

    if x == 1 or x == n:
        amount -= 1

    if y == 1 or y == m:
        amount -= 1

    return amount


def main():
    t = int(input())

    for step in range(t):
        n, m = map(int, input().split())
        x_1, y_1, x_2, y_2 = map(int, input().split())

        print(min(amount_of_obstacles(x_1, y_1, n, m), amount_of_obstacles(x_2, y_2, n, m)))


main()
