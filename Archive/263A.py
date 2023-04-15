def main():
    matrix = [list(map(int, input().split())) for row in range(5)]

    for row_number in range(len(matrix)):
        if 1 in matrix[row_number]:
            one_row_number = row_number
            one_column_number = matrix[row_number].index(1)

            break

    print(abs(2 - one_row_number) + abs(2 - one_column_number))


main()
