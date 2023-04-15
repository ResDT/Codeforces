def action(i, j, d):
    return (
        (i + 1, j + 1) if d == "DR"
        else (i + 1, j - 1) if d == "DL"
        else (i - 1, j + 1) if d == "UR"
        else (i - 1, j - 1)
    )

def change_direction(d, i, j, n, m):
    if i == 0:
        d = "D" + d[1]
    elif i == n:
        d = "U" + d[1]

    if j == 0:
        d = d[0] + "R"
    elif j == m:
        d = d[0] + "L"

    return d

def amount_of_bounces(n, m, i, j, i_end, j_end, d):
    stepped_cells = set()
    amount = 0
    check_bounce = {
        (0, "U"), (n, "D"),
        (0, "L"), (m, "R")
    }

    while (i, j, d) not in stepped_cells:
        if (i, j) == (i_end, j_end):
            return amount
        else:
            stepped_cells.add((i, j, d))

            if (i, d[0]) in check_bounce or (j, d[1]) in check_bounce:
                d = change_direction(d, i, j, n, m)
                amount += 1

            i, j = action(i, j, d)
    else:
        return -1


def main():
    t = int(input())

    for step in range(t):
        n, m, i_1, j_1, i_2, j_2, d = input().split()

        print(amount_of_bounces(int(n) - 1, int(m) - 1, int(i_1) - 1, int(j_1) - 1, int(i_2) - 1, int(j_2) - 1, d))


main()
