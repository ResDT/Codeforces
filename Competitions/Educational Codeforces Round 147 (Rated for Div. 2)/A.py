def main():
    t = int(input())

    for step in range(t):
        s = input()
        question_marks = s.count("?")

        print(
            0 if s[0] == "0"
            else 1 if not question_marks
            else 10 ** question_marks if s[0] != "?"
            else 10**(question_marks-1) * 9
        )


main()
