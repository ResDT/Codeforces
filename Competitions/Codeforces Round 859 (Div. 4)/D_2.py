def main():
    t = int(input())
 
    for step in range(t):
        n, q = map(int, input().split())
        a = list(map(int, input().split()))
        a_sum = sum(a)
 
        for step_ in range(q):
            l, r, k = map(int, input().split())
            
            print(
                "YES" if need_change == (sum(a[l-1:r]) + k*(r-l+1)) % 2
                else "NO"
            )
 


main()
