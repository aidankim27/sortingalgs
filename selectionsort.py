nums = input()
listnum=nums.split()
newlistnum=[]
for i in listnum:
    newlistnum.extend([int(i)])

def smallest(list1):
    track=10000
    i=len(list1)
    for z in range(len(list1)):
        for j in range(len(list1)-i,len(list1)):
            b=len(list1)-i
            if  list1[j]<track:
                track=list1[j]
        print(track)
        position=list1.index(track)
        pnum=list1.pop(position)
        list1.insert(b,pnum)        
        track=10000
        i-=1

smallest(newlistnum)
print(newlistnum)