def even(array, n):
    even = (
        True if not n % 2
        else not array[n // 2] % 2
    )

    for place in range((n-1)//2 - n%2 + 1):
        if (array[place]+array[n - 1 - place]) % 2:
            even = not even

    return even


def main():
    t = int(input())
 
    for step in range(t):
        n, q = map(int, input().split())
        a = list(map(int, input().split()))
        need_change = even(a, n)
 
        for step_ in range(q):
            l, r, k = map(int, input().split())
            
            print(
                "YES" if need_change == (even(a[l-1:r], r - l + 1) == k * (r-l+1) % 2) # Вторая часть в скобках - остаток от деления, если вторая часть равна единице, то вторая часть нечетно!
                else "NO"
            )
 


main()
