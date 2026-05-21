from vetor import Array



print("\n" + "=" * 45)
print("        SISTEMA DE NOTAS DE ALUNOS")
print("=" * 45)


nomes   = Array()
nota_p1 = Array()
nota_p2 = Array()
nota_p3 = Array()

turma = [
    ("Ana",    8.5, 7.0, 9.0),
    ("Bruno",  5.0, 4.5, 6.0),
    ("Carla",  9.5, 8.0, 9.5),
    ("Diego",  3.0, 5.5, 4.0),
    ("Elena",  7.0, 8.5, 7.5),
]

for nome, p1, p2, p3 in turma:
    nomes.append(nome)
    nota_p1.append(p1)
    nota_p2.append(p2)
    nota_p3.append(p3)

print(f"\n{'Nome':<10} {'P1':>5} {'P2':>5} {'P3':>5} {'Média':>7} {'Situação'}")
print("-" * 45)

aprovados = Array()
reprovados = Array()

for i in range(nomes.size()):
    media = (nota_p1.get(i) + nota_p2.get(i) + nota_p3.get(i)) / 3
    situacao = "Aprovado" if media >= 6.0 else "Reprovado"

    print(f"{nomes.get(i):<10} {nota_p1.get(i):>5.1f} "
            f"{nota_p2.get(i):>5.1f} {nota_p3.get(i):>5.1f} "
            f"{media:>7.2f}  {situacao}")

    if media >= 6.0:
        aprovados.append(nomes.get(i))
    else:
        reprovados.append(nomes.get(i))

print(f"\nAprovados ({aprovados.size()}):   {aprovados.data}")
print(f"Reprovados ({reprovados.size()}): {reprovados.data}")
