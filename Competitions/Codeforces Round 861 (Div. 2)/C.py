from math import log

def main():
    t = int(input())

    for step in range(t):
        l, r = map(int, input().split())

        l_lenth = int(log(l, 10)) + 1
        test = int(str(l // 10**(l_lenth-1)) * l_lenth)

        if l <= test <= r:
            print(test)

            continue

        test = int(str(l // 10**(l_lenth-1) + 1) * l_lenth)

        if test <= r:
            print(test)

            continue

        minimum_subtraction = float("inf")
        minimum_number = 0

        for number in range(l, r + 1):
            number_list = set(str(number))
            margin = int(max(number_list)) - int(min(number_list))

            if margin < minimum_subtraction:
                minimum_subtraction = margin
                minimum_number = number

        print(minimum_number)


main()
