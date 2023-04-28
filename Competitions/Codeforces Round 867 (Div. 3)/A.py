def main():
    q = int(input())

    for step in range(q):
        n, t = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))

        for place in range(n):
            a[place] += place

        matrix = list(zip(a, b))
        able = list(filter(lambda element: element[0] <= t, matrix))

        print(
            matrix.index(max(able, key=lambda element: element[1])) + 1 if len(able)
            else -1
        )


main()
