n=input()
n=n.strip()
n=n.split(" ")
nums=[]
for i in n:
    nums.extend([int(i)])
print(nums)

def insertionsort(listnum):
    for i in range(1,len(listnum)):
        for j in range(i, 0, -1):
            if listnum[j-1] > listnum[j]:
                temp = listnum[j]
                listnum[j] = listnum[j-1]
                listnum[j-1] = temp
            else:
                break


insertionsort(nums)
print(nums)