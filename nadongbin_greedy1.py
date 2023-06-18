#92page - 큰 수의 법칙
'''n,m,k=map(int,input().split())

nums=list(map(int,input().split()))
nums.sort(reverse=True)

dumps=nums[0]*k+nums[1]
ans=dumps*(m//(k+1))
ans+=nums[0]*(m%(k+1))
print(ans)'''

#96page - 숫자 카드 게임
'''n,m = map(int,input().split())
ans=0
for _ in range(n):
    a=list(map(int,input().split()))
    a.sort()
    newans=a[0]
    if newans>ans:
        ans=newans
print(ans)'''

#99page - 1이 될 때까지
'''cnt=0
n,k = map(int,input().split())
while(n!=1):
    if n%k!=0:
        n-=1
        cnt+=1
    else:
        n//=k
        cnt+=1
print(cnt)'''
#1로 만들기_silver3_1463
cnt=0
n,k = map(int,input().split())
while(n!=1):
    if n%k!=0:
        n-=1
        cnt+=1
    else:
        n//=k
        cnt+=1
print(cnt)

