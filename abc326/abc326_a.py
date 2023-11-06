x,y = map(int, input().split())

if(x > y):
    # 下る場合
    if(3 >= x - y):
        print("Yes")
    else:
        print("No")
else:
    # 上る場合
    if(y - x <= 2):
        print("Yes")
    else:
        print("No")