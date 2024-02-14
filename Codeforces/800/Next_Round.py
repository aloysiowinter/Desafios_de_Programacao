
first_line = input()
first_line_split = first_line.split()

n = int(first_line_split[0])
k = int(first_line_split[1])

second_line = input()
second_line_split = second_line.split()

cont = 0
for i in range(n):
    if int(second_line_split[i]) >= int(second_line_split[k-1]) and int(second_line_split[i]) > 0:
        cont += 1

print(str(cont))