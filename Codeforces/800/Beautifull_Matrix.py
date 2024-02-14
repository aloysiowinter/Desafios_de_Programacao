print("Hello")
for l in range(5):
    line = input()
    line_split = line.split()
    for c in range(5):
        if line_split[c] == "1":
            l1 = l
            c1 = c

matriz = [[0 for _ in range(5)] for _ in range(5)]

print(str(matriz))