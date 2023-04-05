t=int(input())
for i in range(t):
  m=int(input())
  q=m//25
  d=(m%25)//10
  n=((m%25)%10)//5
  p=((m%25)%10)%5
  print(q,d,n,p)