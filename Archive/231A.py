def main():
    amount = int(input())
    task_amount = 0

    for step in range(amount):
        peter, basil, tonya = map(int, input().split())
        task_amount += int(peter + basil + tonya >= 2)

    print(task_amount)


main()
