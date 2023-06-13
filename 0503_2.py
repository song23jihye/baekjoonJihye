'''N=int(input())
while(N>0):
    a=int(N/500)
    N%=500
    b=int(N/100)
    N%=100
    c=int(N/50)
    N%=50
    d=int(N/10)
    N%=10
print('how many coins: ',a+b+c+d)
'''
'''
n=4260
counts=0

coin_types=[500,100,50,10]
for coin in coin_types:
    counts+=n//coin
    n%=coin'''
#// 연산자: 몫 ->정수

#print(5//3)
#print(5/3)
bong=[3,5]
cnt=0
bong.sort(reverse=True)
N=int(input())
start=N//bong[0]
for i in range(start,-1,-1):
    try:
        if (N-bong[0]*i)%bong[1]==0:
            cnt+=i
            cnt+=(N-i*bong[0])//bong[1]
            print(cnt)
            break
        else: 
            if i==0:
                print(-1)
    except ZeroDivisionError:
        if N%bong[1]==0:
            print(N//bong[1])
        else:
            print(-1)
'''
num = int(input())
count = 0
while num >= 0:
    if num % 5 == 0: #
        count += num//5
        print(count)
        break
    num -= 3
    count += 1
else:
    print(-1)'''
'''
N=int(input())
temp=0
k=N//5
while 1:
    if (N-k*5)%3 == 0:
        print((N-k*5)//3 + k)
        break
    if k == 0 and N%3 != 0:
        print(-1)
        break
    k-=1'''