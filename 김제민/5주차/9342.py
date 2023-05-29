import re
p = re.compile('^[A-F]?A+F+C+[A-F]?$')
for i in range(int(input())):
    print('Good' if p.match(input()) == None else 'Infected!')