n = int(input())

cont = 0
for i in range(n):
    problem = input()
    cont2 = 0
    for k in problem:
        if k == '1':
            cont2 += 1
    if cont2 > 1:
        cont += 1
print(str(cont))