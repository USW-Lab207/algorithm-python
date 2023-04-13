croati = list(input())
count = len(croati)
for i in range(len(croati)):
    if i+1 < len(croati):
        if croati[i] == "l" and croati[i+1] == "j":
            count -= 1
        elif croati[i] == "n" and croati[i+1] == "j":
            count -= 1
    if i+2 < len(croati):
        if croati[i] == "d" and croati[i + 1] == "z" and croati[i +2] == "=":
            count -= 1
    if croati[i] == "=":
        count -= 1
    if croati[i] == "-":
        count -= 1
print(count)