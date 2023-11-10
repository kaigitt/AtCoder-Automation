N, M = map(int, input().split())

graph = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a-1].append(b)
    graph[b-1].append(a)
    
res = 0
for i in range(N):
    count = 0
    for j in graph[i]:
        if(count > 1):
            continue
        if(i+1 > j):
            count += 1
    if(count == 1):
        res += 1
        
print(res)


