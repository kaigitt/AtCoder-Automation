n, m = map(int, input().split())

products = []

for _ in range(n):
    price, num_features, *features = map(int, input().split())
    products.append((price, num_features, set(features)))

flag = False
for i in range(n):
    for j in range(n):
        if(i != j):
            # unpack
            pi, ci, fi = products[i]
            pj, cj, fj = products[j]
            if(pi >= pj and fi.issubset(fj) and (pi > pj or len(fj) > len(fi))):
                flag = True

if(flag): print("Yes")
else: print("No")