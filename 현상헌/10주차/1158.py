import sys
input=sys.stdin.readline
n,k=map(int,input().split())
d=list(i for i in range(1,n+1))
d1=[]
cnt=0
while d:
    cnt+=k-1
    if cnt>=len(d):
        cnt%=len(d)
    d1.append(d.pop(cnt))
d1=map(str,d1)
print('<{}>'.format(', '.join(d1)))