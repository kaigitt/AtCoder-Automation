N = int(input())

T = 0 # 基準時

count = [0 for _ in range(24)]

for i in range(N):
    w,x = map(int, input().split())
    count[x] += w

max_paticipant = 0

for i in range(24):
    tmp = 0
    for j in range(9):
        tmp += count[(i+j) % 24]
    max_paticipant = max(max_paticipant, tmp)

print(max_paticipant)