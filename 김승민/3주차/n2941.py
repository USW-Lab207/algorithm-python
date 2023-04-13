import sys

c_alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

string = sys.stdin.readline().rstrip()

for _ in c_alpha:
    if (_ in string):
        string = string.replace(_, 'o')

print(len(string))



