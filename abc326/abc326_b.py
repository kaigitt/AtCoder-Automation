N = int(input())

while N < 1000:
    
    h_place = N // 100
    t_place = N // 10 - h_place * 10
    o_place = N % 10

    if(h_place * t_place == o_place):
        print(N)
        break
    
    N += 1
    