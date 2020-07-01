def merge(l1,l2):
    m=[]
    while len(l1) and len(l2)!=0:
        if l1[0]<=l2[0]:
            m.extend([l1[0]])
            l1.remove(l1[0])
        else:
            m.extend([l2[0]])
            l2.remove(l2[0])
        if len(l1)==0:
            for i in l2:
                m.extend([i])
        if len(l2)==0:
            for i in l1:
                m.extend([i])       
    return m

def mergesort(L):
    if len(L)==1:
        return(L)
    l1=L[0:len(L)//2]
    l2=L[len(L)//2:len(L)]
   #print('split into ', l1,l2x )
    a = mergesort(l1)
    b = mergesort(l2)
    m =merge(a,b)
    return m

list1=[1,4,5,23,2,2,1,15,4,2,6,2]
m = mergesort(list1)
print(m)