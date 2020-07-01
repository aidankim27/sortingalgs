def splt(lst,start,end):
    compare=lst[start]
    i=start
    j=end
    while i<=j:
        if lst[i]>compare:
            #lst[i] > compare
            while lst[j]>compare:
                j-=1
            # lst[j] <= compare
            if i<j:
                lst[i],lst[j]=lst[j],lst[i]
        i+=1
    lst[start],lst[j]=lst[j],lst[start]

    return j
   
list1=[5,4,6,7,8,4,4344,6,65,6,2,6,7]

def quicksort(L,s,e): 
    print(L, s, e)
    if s>=e:
        return L
    middle=splt(L,s,e)
    print("M: ", middle)
    quicksort(L,s,middle-1)
    quicksort(L,middle+1,e)

quicksort(list1,0,len(list1)-1)
print(list1)