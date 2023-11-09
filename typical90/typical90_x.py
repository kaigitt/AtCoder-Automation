N, K = map(int, input().split())

# 貪欲法で考える
# リストを前から順に見ていき、その時点で入れ替えることが適切な場合、入れ替える
# 適切な入れ替えを行いちょうどK回になるか確認する

A = list(map(int, input().split()))
B = list(map(int, input().split()))

diff = [ abs(a - b) for a, b in zip(A,B)]

if(sum(diff) <= K and (K - sum(diff)) % 2 == 0):
    print("Yes")
else:
    print("No")