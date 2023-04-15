s=input()
ca2=['c=','c-','d-','lj','nj','s=','z=']
ca3=['dz=']
length=len(s)
while len(s)>2:
    temp=s
    for k in range(7):
        if s[0] + s[1] + s[2] == ca3[0]:
            s = s.replace(s[0] + s[1] + s[2], '', 1)
            length = length - 2
            break
        elif s[0] + s[1] ==ca2[k]:
            s=s.replace(s[0]+s[1],'',1)
            length=length-1
            break
    if temp==s:
        s=s.replace(s[0],'',1)
if len(s)==2:
    for i in range(7):
        if s==ca2[i]:
            length=length-1
print(length)