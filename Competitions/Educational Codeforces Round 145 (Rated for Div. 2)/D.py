def sorting(string):
    count_of_permutations = count_of_removals = 0

    while "10" in string:
        count_of_removals += string.count("100")
        string = string.replace("100", "00")

        count_of_removals += string.count("110")
        string = string.replace("110", "11")

        count_of_permutations += string.count("010")
        string = string.replace("010", "001")

    return count_of_permutations*10**12 + count_of_removals*(10**12 + 1)
    

def main():
    t = int(input())

    for step in range(t):
        string = input()

        print(sorting(string))


main()
# 6
# 00
# 0
# 0011
# 00101101
# 1001101
# 11111
