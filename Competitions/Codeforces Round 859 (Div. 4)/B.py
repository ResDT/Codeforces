def main():
    t = int(input())

    for step in range(t):
        n = int(input())
        array = list(map(int, input().split()))
        even_sum = odd_sum = 0

        for number in array:
            if not (number % 2):
                even_sum += number
            else:
                odd_sum += number

        print(
            "YES" if even_sum > odd_sum
            else "NO"
        )


main()
