N, Q = map(int, input().split())

A = list(map(int, input().split()))

r_cnt = 0
for i in range(Q):
    t, x, y = map(int, input().split())
    x, y = x-r_cnt, y-r_cnt
    
    if(t == 1):
        A[x-1], A[y-1] = A[y-1], A[x-1]
    elif(t == 2):
        r_cnt += 1
        if(r_cnt == N):
            r_cnt = 0
    elif(t == 3):
        print(A[x-1])
