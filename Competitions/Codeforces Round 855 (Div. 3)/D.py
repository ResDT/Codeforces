def main():
    t = int(input())

    for step in range(t):
        n = int(input())
        s = input()
        strings = set()

        for letter in set(s):
            while 3 * letter in s:
                s = s.replace(3 * letter, 2 * letter)

        for place in range(len(s) - 2):
            strings.add(s[:place] + s[place + 2:])

        strings.add(s[:-2])

        print(len(strings))


main()
