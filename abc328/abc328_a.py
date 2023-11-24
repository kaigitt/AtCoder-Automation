N, M = map(int, input().split())
A = list(map(int, input().split()))

total = 0
for i in range(N):
    if(A[i] <= M):
        total += A[i]

print(total)