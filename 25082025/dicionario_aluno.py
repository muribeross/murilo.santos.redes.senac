aluno = {
    "nome": "Murilo",
    "idade": 18,
    "aprovado": False
}

print("Informações do aluno:")
print(f"Dicionário completo: {aluno}")
print(f"Nome do aluno: {aluno['nome']}")
print(f"Idade: {aluno['idade']} anos")
print(f"Situação: {'Aprovado' if aluno['aprovado'] else 'Reprovado'}")