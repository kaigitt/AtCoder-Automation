N = int(input())

win = [(input().count('o'), i) for i in range(N)]


win.sort(key=lambda x: (-x[0], x[1]))


ans = [x[1] + 1 for x in win]
print(*ans)