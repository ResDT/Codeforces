def main():
    k, n, w = map(int, input().split())
    price = k * w * (1+w) // 2

    print(
        price - n if n < price
        else 0
    )


main()
