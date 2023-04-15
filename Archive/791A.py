from math import log, floor

def main():
    a, b = map(int, input().split())

    print(floor(log(b / a, 1.5) + 1))


main()
