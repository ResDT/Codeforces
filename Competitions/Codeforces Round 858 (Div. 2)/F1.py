#from math import gcd

def master(array, sum_, number_k):
    for k in range(number_k):
        flag = 0

        for element in array:
            if not flag:
                for denominator in range(element, 0, -1):
                    if array.count(element) > 1 or denominator in array and not (element % denominator) and element != denominator:
                        array.remove(element)

                        sum_ -= element
                        flag = 1

                        break
            else:
                break

    return sum_


def main():
    t = int(input())

    for number in range(t):
        n, m, k = map(int, input().split())
        a = list(map(int, input().split()))
        a_sum = sum(a)

        print(master(a, a_sum, k))





main()
