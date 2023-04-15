def x_symmetry(row_1, row_2, n):
    return sum(row_1[place] ^ row_2[n - 1 - place] for place in range(n))

def symmetry(matrix, k, n):
    amount = 0
    
    for row_place in range(n // 2):
        amount += x_symmetry(matrix[row_place], matrix[n - 1 - row_place], n)

        if amount > k:
            return "NO"

    if n % 2:
        amount += x_symmetry(matrix[n//2], matrix[n//2], n) // 2

    return (
        "YES" if k >= amount and not (k-amount) % 2
        else "NO"
    )


def main():
    t = int(input())

    for step in range(t):
        n, k = map(int, input().split())
        matrix = [list(map(int, input().split())) for row in range(n)]

        print(symmetry(matrix, k, n))


main()
