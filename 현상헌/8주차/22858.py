import sys
input=sys.stdin.readline
n,k=map(int,input().split())
s=list(map(int,input().split()))
d=list(map(int,input().split()))
p=[k for k in range(n)]
for i in range(k):
    for j in range(n):
        p[d[j]-1]=s[j]
    for x in range(n):
        s[x]=p[x]
print(*p)