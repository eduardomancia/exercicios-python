nota1 = int(input("Digite sua primeira nota"))
nota2 = int(input("Digite sua segunda nota"))
nota3 = int(input("Digite sua terceira nota"))

media = (nota1+ nota2 + nota3) / 3

if media >= 6:
    print("Você foi aprovado")
elif media >= 4 and media <= 5.9:
    print("Você está de recuperação")
else:
    print("Você está reprovado")