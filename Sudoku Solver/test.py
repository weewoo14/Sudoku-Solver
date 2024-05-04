t = int(input())
for test in range(t):
    n,s = map(int,input().split())
    total = (n * (n+1))//2
    diff = total-s
    if diff % 2 == 0:
        p1,p2 = diff//2, diff//2
        print(min(p1,n-p2+1 )-1)
    else:
        p1,p2 = diff//2, diff//2 + 1
        print(min(p1,n-p2+1))