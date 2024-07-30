numero = int(input("Digite um número para ver sua tabuada: "))
print(f"Tabuada do {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
print("Segundo ano do ensino médio e ainda não decorou a tabuda? Que feio!")
