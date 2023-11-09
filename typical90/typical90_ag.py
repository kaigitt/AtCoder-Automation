H,W = map(int, input().split())

led_h = H / 2 if H % 2 == 0 else H // 2 + 1
led_w = W / 2 if W % 2 == 0 else W // 2 + 1

print(H * W if H == 1 or W == 1 else int(led_h * led_w))