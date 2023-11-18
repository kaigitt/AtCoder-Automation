import itertools

N = int(input())

member = [i+1 for i in range(N)]

times = []
for i in range(N):
    tmp = list(map(int, input().split()))
    times.append(tmp)

M = int(input())

unlike_match = [[0 for x in range(N)] for j in range(N)]
for m in range(M):
    a, b = map(int, input().split())
    unlike_match[a-1][b-1] = 1
    unlike_match[b-1][a-1] = 1


min_time = 10 ** 9
for i in itertools.permutations(member):
    flag = True
    for j in range(N-1):
        if(unlike_match[i[j]-1][i[j+1]-1] == 1):
            flag = False
    
    total = 0
    if(flag):
        for j in range(N):
            total += times[i[j]-1][j]
    
    if(total == 0):
        pass
    else:
        min_time = min(total, min_time)

if(min_time == 10 ** 9):
    print(-1)
else:
    print(min_time)
        
        