first_line = input()
first_line_split = first_line.split()
m = int(first_line_split[0])
n = int(first_line_split[1])

sum = m//2 * n      #quantos dados é possivel na vertical

sum += m%2 * n//2   #caso tenha sobrado uma linha quantos dados é possivel encaicar na horizontal na ultima linha

print(int(sum))
