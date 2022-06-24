binary = input("write the binary: ")
decimal = []

for bit in binary[::-1]:
    bit = int(bit) * 2 ** len(decimal)
    decimal.append(bit)

print(f"{binary} in decimal is {sum(decimal)}")