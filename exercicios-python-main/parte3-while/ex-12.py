soma = 0

while True:
    numero = int(input("Escreva seu número: "))
    if numero == 0 :
        break

    soma += numero

print(f"A soma é: {soma}")
