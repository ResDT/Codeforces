def main():
    amount = int(input())

    for step in range(amount):
        n, x, p = map(int, input().split())
        start = (1 - (n-x)%n) / n
        end = (p*(p+1)/2 - (n-x)%n) / (2*n)
        print(start, end)

        if end >= 0 and (end - start >= 1 or not (start % 1 and end % 1)):
            print("YES")
        else:
            print("NO")


main()
