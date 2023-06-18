n=int(input())
n=1000-n
ans=0
coins=[500,100,50,10,5,1]
while(1):
    for i in coins:
        ans+=n//i
        n%=i
    if n==0:
        break
print(ans)