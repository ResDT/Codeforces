def main():
    t = int(input())
    flag = True
    
    for step in range(t):
        result = 1
        step_ = (
            t if flag
            else t - 1
        )

        for number in range(step_):
            result *= int(input())

        print(result)

        flag = not flag


main()
