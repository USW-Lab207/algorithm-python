import sys
input=sys.stdin.readline
arr={'A','B','C','D','E','F'}
t=int(input())
for i in range(t):
  k=0
  s=input().strip()
  if s[0] in arr:
    if s[0]!='A':
      s=s[1:]
    if s[0]=='A':
      while s[0]=='A':
        s=s.replace('A','',1)
    else:
      k=1
    if s[0]=='F':
      while s[0]=='F':
        s=s.replace('F','',1)
    else:
      k=1
    if s[0]=='C':
      while len(s)>0 and s[0]=='C':
        s=s.replace('C','',1)
    else:
      k=1
    if len(s)>1:
      k=1
    else:
      if len(s)==0:
        k=0
      else:
        if s[0] in arr:
          k=0
        else:
          k=1
  else:
    k=1
  if k==1:
    print('Good')
  else:
    print('Infected!')