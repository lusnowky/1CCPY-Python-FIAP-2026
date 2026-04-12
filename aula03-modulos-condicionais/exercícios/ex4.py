nota_a = int(input("Nota 1: "))
nota_b = int(input("Nota 2: "))
nota_c = int(input("Nota 3: "))
nota_d = int(input("Nota 4: "))
print()

media = (nota_a + nota_b + nota_c + nota_d) / 4
print(f"Media do aluno: {media}")

if media >= 7:
    print("Aprovado")
elif media >= 5:
    print("Em recuperação")
else:
    print("Reprovado")