def main():
    lenth, pass_place = map(int, input().split())
    member_array = list(map(int, input().split()))
    pass_points = member_array[pass_place - 1]

    for place in range(lenth - 1, -1, -1):
        if member_array[place] >= pass_points and member_array[place]:
            print(place + 1)

            break
    else:
        print(0)


main()
