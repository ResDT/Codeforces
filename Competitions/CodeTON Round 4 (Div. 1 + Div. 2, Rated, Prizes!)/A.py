def main():
    t = int(input())

    for step in range(t):
        n = int(input())
        array = input().split()

        for i, element in enumerate(array):
            if int(element) <= i + 1:
                print("YES")

                break
        else:
            print("NO")


main()
