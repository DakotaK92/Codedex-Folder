pesos = int(input("What do you have left in pesos? "))
soles = int(input("What do you have left in soles? "))
reais = int(input("What do you have left in reais? "))

total = pesos * 0.00027 + soles * 0.30 + reais * 0.19

print(f"Total in USD: {total}")