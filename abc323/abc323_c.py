N, M = map(int, input().split())

A = list(map(int, input().split()))

S = [input() for _ in range(N)]
    
now_sc = [x + 1 for x in range(N)]

for i in range(N):
    for j in range(M):
        if(S[i][j] == "o"):
            now_sc[i] += A[j]


mx = max(now_sc)

for i in range(N):
    nokori = [A[j] for j in range(M) if(S[i][j] == "x")]
    nokori.sort(reverse=True)
    
    ans = 0
    while now_sc[i] < mx:
        now_sc[i] += nokori[ans]
        ans += 1
    
    print(ans)
    
    
    