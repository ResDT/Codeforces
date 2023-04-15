def main():
    t = int(input())

    for step in range(t):
        l, r = map(int, input().split())
        maximum_subtraction = 0
        maximum_number = 0

        for number in range(r, l - 1, -1):
            number_list = set(map(int, set(str(number))))
            margin = max(number_list) - min(number_list)

            if margin == 9:
                print(number)

                break
            elif margin >= maximum_subtraction:
                maximum_subtraction = margin
                maximum_number = number
        else:
            print(maximum_number)


main()
