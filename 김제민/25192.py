n = int(input())
log = []
gol = {}
cou = 0
for _ in range(n):
    id = input()
    if id == 'ENTER':
        gol = set(log)
        cou += len(gol)
        gol = {}
        log = []
    else:
        log.append(id)
gol = set(log)
cou += len(gol)

print(cou)