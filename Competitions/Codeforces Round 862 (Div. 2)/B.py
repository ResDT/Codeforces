def main():
    t = int(input())

    for step in range(t):
        n = int(input())
        s = input()
        minimum = min(s)
        minimum_index = s.rfind(minimum)

        print(minimum + s[:minimum_index] + s[minimum_index + 1:])


main()
