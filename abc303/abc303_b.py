N,M = map(int, input().split())

unlike = [[False for _ in range(N)] for _ in range(N)]

for i in range(M):
    tmp = list(map(int, input().split()))
    for i in range(N-1):
        unlike[tmp[i]-1][tmp[i+1]-1] = True
        unlike[tmp[i+1]-1][tmp[i]-1] = True

res = 0
for i in range(N):
    for j in range(N):
        if(i != j):
            if(unlike[i][j] == False):
                res += 1

print(res // 2)