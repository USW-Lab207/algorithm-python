import sys
n=int(sys.stdin.readline())
arr={"ENTER"}
sum=0
for i in range(n):
    s=sys.stdin.readline().strip()
    if s=="ENTER":
        arr.clear()
    elif s!="ENTER" and s not in arr:
        arr.add(s)
        sum+=1
print(sum)