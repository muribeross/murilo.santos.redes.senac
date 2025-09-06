#  Exercício Prático (Sugestão para alunos)

# 1. Crie o sistema de cadastro inicial (como acima).
# 2. Implemente as funções para calcular médias, exibir dados e listar alunos ativos.
# 3. Teste a inserção de novos alunos e execute as funções para verificar o correto uso dos tipos de dados (`int`, `float`, `str`, `bool`, `list`, `dict`).
# 4. Adapte para permitir remoção ou alteração de dados de alunos.

alunos = []

# Cadastar aluno
def cadastrar_aluno(nome: str, idade: int, notas: list[float], ativo: bool = True):
    aluno = {
        "nome": nome,
        "idade": idade,
        "notas": notas,
        "ativo": ativo
    }
    alunos.append(aluno)
    print(f"Aluno {nome} cadastrado com sucesso!")


# Media
def calcular_media(aluno: dict) -> float:
    if len(aluno["notas"]) == 0:
        return 0.0
    return sum(aluno["notas"]) / len(aluno["notas"])


# Mostrar dados
def exibir_aluno(aluno: dict):
    media = calcular_media(aluno)
    print(f"Nome: {aluno['nome']}")
    print(f"Idade: {aluno['idade']}")
    print(f"Notas: {aluno['notas']}")
    print(f"Média: {media:.2f}")
    print(f"Ativo: {'Sim' if aluno['ativo'] else 'Não'}")
    print("-" * 30)


# Alunos ativos
def listar_ativos():
    print("\n--- Alunos Ativos ---")
    for aluno in alunos:
        if aluno["ativo"]:
            exibir_aluno(aluno)


# Remover aluno
def remover_aluno(nome: str):
    for aluno in alunos:
        if aluno["nome"].lower() == nome.lower():
            alunos.remove(aluno)
            print(f"Aluno {nome} removido com sucesso!")
            return
    print("Aluno não encontrado.")


# Alterar dados
def alterar_aluno(nome: str, nova_idade=None, novas_notas=None, ativo=None):
    for aluno in alunos:
        if aluno["nome"].lower() == nome.lower():
            if nova_idade is not None:
                aluno["idade"] = nova_idade
            if novas_notas is not None:
                aluno["notas"] = novas_notas
            if ativo is not None:
                aluno["ativo"] = ativo
            print(f"Dados do aluno {nome} atualizados com sucesso!")
            return
    print("Aluno não encontrado.")


#base de dados
cadastrar_aluno("Ana", 20, [8.0, 9.0, 7.5])
cadastrar_aluno("Pedro", 22, [6.0, 5.5, 7.0], ativo=True)
cadastrar_aluno("Mariana", 19, [9.0, 9.5, 10.0], ativo=False)

print("\n--- Todos os alunos ---")
for aluno in alunos:
    exibir_aluno(aluno)

# Lista só ativos
listar_ativos()

# Alterando dados
alterar_aluno("Pedro", nova_idade=23, novas_notas=[7.5, 8.0, 9.0])

# Remove aluno
remover_aluno("Ana")

# Lista ativos
listar_ativos()