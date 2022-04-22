import os

dol = float(input("Qual valor do dolar que você deseja converter: US$"))
os.system('clear')

real = 4.77 * dol


print(f"O valor em real: R${real:.2f}")
