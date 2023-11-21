N = int(input())

total = []
for i in range(N):
    total.append(sum(list(map(int, input().split()))))

res = 1
for i in range(N):
    res = (res * total[i]) % (10**9+7)

print(res)