def find_x(n, a):
    for x in range(28):
        b = [a_i ^ x for a_i in a]
        xor_sum = 0

        for b_i in b:
            if b_i < 0 or b_i > 27:
                break

            xor_sum ^= b_i
        else:
            if not xor_sum:
                return x

    return -1


def main():
    t = int(input())

    for step in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        print(
            -1 if any(a_i < 0 or a_i > 27 for a_i in a)
            else find_x(n, a)
        )


main()
