from random import randint
'''
a=157.93
b=5.
print(a)
print(b)
c=1e9
print(c)
#d=1NF
#print(d)
e=3954e-3
print(e)
print(0.3+0.6)
print(round(0.3+0.6,2))
'''
'''
arr1=[]
for _ in range(10):
    arr1.append(randint(1,10))
print(arr1)
'''
'''b=list()
n=10
a=[0]*n'''
#list comprehension
'''arr2=[i*i for i in range(11) if i%2==0]
print(arr2)'''
'''
n=3 #행
m=4 #열
arr3=[[0]*m for _ in range(n)]
print(arr3)

#[[0]*m for _ in range(n)]
#[[0]]

arr4=[1,2,3,4,5,5,5]
remove_set={3,5}

result=[i for i in arr4 if i not in remove_set]
print(result)
'''
s1='abc'
s2='도레미'
print(s1+s2)
print(s2*3)
tup1=(1,2,3)
print(tup1)
tup1[1]=9







