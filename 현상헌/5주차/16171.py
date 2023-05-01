import sys
input=sys.stdin.readline
s=input().strip()
k=input().strip()
for i in range(len(s)):
  if ord(s[i])>=0 and ord(s[i])<=57:
    s=s.replace(s[i],'0',1)
s=s.replace('0','')
if k in s:
  print(1)
else:
  print(0)