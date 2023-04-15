def maximum_cost(array, current_start_place):
    cost = 1
    multiplication = array[-1]
    d = 1

    while current_start_place:
        if multiplication * array[current_start_place - 1] / (d+1) >= multiplication / d:
            cost += 1
            multiplication *= array[current_start_place]
            d += 1
            current_start_place -= 1
        else:
            break

    return cost


def main():
    amount = int(input())

    for step in range(amount):
        lenth = int(input())
        array = list(map(int, input().split()))

        for cut in range(1, lenth + 1):
            cutted = array[:cut]

            print(maximum_cost(cutted, cut - 1), end=" ")

        print()


main()
