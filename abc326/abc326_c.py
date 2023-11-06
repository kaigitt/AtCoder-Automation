N,M = map(int, input().split())

nums = []
nums = list(map(int, input().split()))

nums.sort()
nums.append(9000000000000)

res = 0
r = 0

for i in range(0, N):
    while(nums[r] < nums[i] + M):
        r += 1
    res = max(res, r-i)

print(res)