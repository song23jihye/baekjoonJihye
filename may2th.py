import time
from random import randint
sum=0

arr=[]
for _ in range(10000):
    arr.append(randint(1,100))
start_t=time.time()

for i in range(len(arr)):
    min_idx=i
    for j in range(i+1,len(arr)):
        if arr[min_idx]>arr[j]:
            min_idx=j
    arr[i], arr[min_idx]=arr[min_idx], arr[i]

end_t=time.time()
print('선택정렬 time측정: ',end_t-start_t)

arr=[]
for _ in range(10000):
    arr.append(randint(1,100))
start_t=time.time()
arr.sort()
end_t=time.time()
print('기본 정렬 라이브러리 time측정: ',end_t-start_t) 


