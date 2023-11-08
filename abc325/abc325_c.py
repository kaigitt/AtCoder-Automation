from collections import deque

h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]
ans = 0
used = [[False] * w for _ in range(h)]

dx = [1, 0, -1, 0, 1, 1, -1, -1]
dy = [0, 1, 0, -1, 1, -1, 1, -1]

for i in range(h):
    for j in range(w):
        if(s[i][j] == "." or used[i][j]):
            continue
        
        que = deque()
        que.append((i, j))
        
        while que: # キューにデータがある場合
            x, y = que.popleft()
            for d in range(8): # 隣接する場所から探す
                nx = x + dx[d]
                ny = y + dy[d]
                if(0 <= nx < h and 0 <= ny < w and s[nx][ny] == "#" and not used[nx][ny]):
                    used[nx][ny] = True
                    que.append((nx, ny))
        ans += 1

print(ans)
                