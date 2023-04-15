n,m=map(int,input().split())
arr=[i+1 for i in range(n)]
for i in range(m):
    x,y,z=map(int,input().split())
    temp=arr[z-1:y]
    for j in range(x-1,z-1):
        k=arr[j]
        temp.append(k)
    arr[x-1:y]=temp
print(*arr)