N, K = map(int, input().split())
scores = []
for i in range(N):
    score_full, score_parts = map(int, input().split())
    scores.append(score_parts)
    scores.append(score_full - score_parts)

scores.sort(reverse=True)

total = 0
for i in range(K):
    total += scores[i]

print(total)