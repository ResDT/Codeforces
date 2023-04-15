def main():
    t = int(input())

    for step in range(t):
        s = input()
        a = int(s)
        b = [int(i) for i in s.strip()]
        
        b.sort()

        print(
            -1 if not a % 1111
            else 6 if b[0] == b[1] == b[2] or b[1] == b[2] == b[3]
            else 4
        )


main()
