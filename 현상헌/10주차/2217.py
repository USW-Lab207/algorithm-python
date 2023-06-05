import sys
input=sys.stdin.readline
n=int(input())
arr=[0]*n
for i in range(n):
    arr[i]=int(input())
arr.sort()
arr=arr[::-1]
for j in range(n):
    arr[j]=arr[j]*(j+1)
print(max(arr))