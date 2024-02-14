number_of_statements = int(input())

x = 0
for _ in range(number_of_statements):
    statement = input()

    if "++" in statement:
        x += 1
    elif "--" in statement:
        x -= 1
    else:
        print("not an statement")

print(str(x))