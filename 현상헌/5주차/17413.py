import sys
input=sys.stdin.readline
s=input().rstrip()
arr=[]
rs=[]
k=0
def push(x,y):
    for k in range(len(x)):
        y.append(x[k])

for i in range(len(s)):
    if s[i]=='<':
        arr=arr[::-1]
        push(arr,rs)
        arr=[]
        arr.append(s[i])
        k=1
    elif s[i]=='>':
        arr.append(s[i])
        push(arr,rs)
        arr=[]
        k=0
    elif s[i]==' ':
        if k==0:
            arr=arr[::-1]
            push(arr,rs)
            rs.append(' ')
            arr=[]
        else:
            arr.append(s[i])
    else:
        arr.append(s[i])
arr=arr[::-1]
push(arr,rs)
for j in range(len(rs)):
    print(rs[j],end='')