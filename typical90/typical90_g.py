from bisect import bisect_left

N = int(input())

A = list(map(int, input().split()))
A.sort()

INF = 2 ** 60

Q = int(input())
for i in range(Q):
    score = int(input())
    r = bisect_left(A, score)
    
    res = INF
    if(r < N):
        res = min(res, abs(score - A[r]))
    if(r > 0):
        res = min(res, abs(score - A[r-1]))
    print(res)