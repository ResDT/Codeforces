def main():
    t = int(input())

    for step in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        maximum = second_maximum = float("-inf")
        minimum = second_minimum = float("inf")

        for number in a:
            if number >= maximum:
                maximum = number
            elif number > second_maximum:
                second_maximum = number

            if number <= minimum:
                minimum = number
            elif number < second_minimum:
                second_minimum = number

        print(maximum, second_maximum, minimum, second_minimum)
        print(max(maximum * second_maximum, minimum * second_minimum))


main()
