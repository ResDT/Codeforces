def operations(n):
    return (
        [] if n == 1 or not n % 2
        else operations((n+1) // 2) + ["1"] if (n+1) % 4
        else operations((n-1) // 2) + ["2"]
    )


def main():
    t = int(input())

    for step in range(t):
        n = int(input())
        operation_list = operations(n)

        if n % 2 and len(operation_list) <= 40:
            print(len(operation_list), " ".join(operation_list), sep="\n")
        else:
            print(-1)


main()
