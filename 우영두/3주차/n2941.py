arr=input()
res=0
res+=arr.count('c=')+arr.count('c-')+arr.count('dz=')+arr.count('lj')\
     +arr.count('nj')+arr.count('s=')+arr.count('z=')
print(len(arr) - res)
