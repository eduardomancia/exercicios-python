positivo = 0


while True :
    numero = int(input("Digite outro (0 para parar) "))
    if numero == 0 :
        break
    if numero > 0 :
        positivo += 1

print(f"A quantidade de números positivos é de{positivo} ")