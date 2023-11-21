N, L = map(int, input().split())

dp = [0 for _ in range(N+2)]
dp[0] = 1

for i in range(1, N+1):
    if(i+1 < L):
        dp[i] = dp[i-1] % (10**9+7)
    else:
        dp[i] = (dp[i-1] + dp[i-L]) % (10**9+7)
    

print(dp[N])