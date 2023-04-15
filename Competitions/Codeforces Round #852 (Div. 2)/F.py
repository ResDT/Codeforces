def main():
    n, q = map(int, input().split())
    array = list(map(int, input().split()))

    for i in range(q):
        minimum = float("inf")
        start, end = map(int, input().split())
        test_list = sorted(array[start - 1:end])

        for place in range(len(test_list) - 1):
            minimum = min(test_list[place + 1] - test_list[place], minimum)

        print(minimum)


main()
