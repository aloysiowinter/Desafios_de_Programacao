n = int(input())

for i in range(n):
    w = input()
    if len(w) > 10:
        l1 = w[0]               #primeiro caractere
        l2 = w[-1]              #ultimo caractere
        m = str(len(w) - 2)     #meio
        c = l1+m+l2             #concatenação
        print(c)
    else:
        print(w)