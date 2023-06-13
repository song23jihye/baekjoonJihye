#n, m, k = map(int, input().split())
#data = list(int,input().split)

n,k = (4,9) #map(int,input().split(' '))
things = (3,2,1,3,1,4,1,3,2) #list(map(int,input().split(' ')))
cnt = 0 
nowusing=[]

for i in range(k):
    if i < n:
        nowusing.append(things[i]) #빈자리에 추가
    else:
        tmp={}
        for i in range(n):
            tmp[nowusing[n]] = things.index(nowusing[n])
        things.index(things[i])


'''
nowusing=[things[i] for i in range(n)] #플러그개수만큼 일단 꽂음
for x in range(n,len(things)):#len(things) ->k #다음에 올것~끝
    if (things[x] not in nowusing): 
        #nowusing중에 안쓰이면 out, 쓰이면 새 요소를 포함하여(먼저오는 n개를 골라) 다시쓰이는 위치 비교 
        # 먼저 쓰이는 것들 먼저 위치
        #nowusing[n-1]=things[x]
        tmp=nowusing.append(things[x])

        print(things[x])
        print(nowusing)
        del(tmp[0])
        #cnt+=1
#print(cnt)


#새로운 요소면 things와 nowusing대조 #(things[x] in nowusing[x+1:len(nowusing)]'''