N, K = map(str, input().split())

num = list(N)

def basen_to_10(num_n, n): # n進数→10進数に変換
    if num_n == 0:
        return 0
    num_10 = 0
    for s in str(num_n):
        num_10 *= n
        num_10 += int(s)
    return num_10

def base10_to_n(num_10, n):  # 10進数→n進数に変換
    if num_10 == 0:
        return 0
    str_n = ""
    while num_10:
        if num_10 % n >= 10:
            return -1
        str_n += str(num_10 % n)
        num_10 //= n
    return int(str_n[::-1])

for _ in range(int(K)):
    N = basen_to_10(N, 8)
    N = base10_to_n(N, 9)
    N = int(str(N).replace('8', '5'))
    
print(N)

