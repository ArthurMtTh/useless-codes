decimal = int(input("write the decimal: "))
division = decimal
binary = []

while division > 0:
    binary.append(division%2)
    division = division//2

print(f"{decimal} in binary is {binary[::-1]}")