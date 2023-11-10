
n=int(input())
a,b,c=map(int,input().split())
 
ans=9999
for i in range(ans):
  for j in range(ans-i): 
    k=(n-(a*i+b*j))//c
    if n==a*i+b*j+c*k and k>=0: 
      ans=min(ans,i+j+k)
print(ans)   