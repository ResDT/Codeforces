def main():
    n, k = map(int, input().split())

    while k:
        if not n % 10:
            n //= 10
            k -= 1
        else:
            n, k = n - min(n % 10, k), k - min(n % 10, k)

    print(n)


main()
