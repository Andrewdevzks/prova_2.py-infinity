num_alunos = int(input("Digite o número de alunos: "))

total_media = 0  # Para calcular a média geral da turma

for i in range(num_alunos):
    nome = input(f"Digite o nome do aluno {i + 1}: ")
    notas = []
    
    for j in range(3):
        nota = float(input(f"Digite a nota {j + 1} de {nome}: "))
        notas.append(nota)
    
    media = sum(notas) / 3
    total_media += media
    
    status = "Aprovado" if media >= 7.0 else "Reprovado"
    
    print(f"\nAluno: {nome}")
    print(f"Notas: {notas}")
    print(f"Média: {media:.2f}")
    print(f"Status: {status}\n")

media_geral = total_media / num_alunos
print(f"Média geral da turma: {media_geral:.2f}")