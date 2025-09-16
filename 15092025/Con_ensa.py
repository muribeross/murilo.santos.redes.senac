#1. Resolver o Nível 1 (só fumaça).
#2. Expandir para o Nível 2 (fumaça OU botão + chave).
#3. Completar o Nível 3 (incluindo movimento sem chave).
#4. Implementar o Nível 4 em Python e verificar todas as combinações de entradas.

# Nível 1 — Apenas a condição de fumaça

def alarme_nivel1(F):
    return int(F)  # Se F=1, alarme toca. Se F=0, não toca.

print("Nível 1 — Só fumaça")
print("F | A")
print("------")
for F in [0, 1]:
    A = alarme_nivel1(F)
    print(f"{F} | {A}")
print()

# Nível 2 — Fumaça OU (B AND C)

def alarme_nivel2(F, B, C):
    return int(F or (B and C))

print("Nível 2 — Fumaça + Botão e Chave")
print("F B C | A")
print("---------")
for F in [0, 1]:
    for B in [0, 1]:
        for C in [0, 1]:
            A = alarme_nivel2(F, B, C)
            print(f"{F} {B} {C} | {A}")
print()

# Nível 3 — Inclui movimento sem chave

def alarme_nivel3(F, B, C, M):
    return int(F or (B and C) or (M and not C))

print("Nível 3 — Inclui movimento")
print("F B C M | A")
print("-----------")
for F in [0, 1]:
    for B in [0, 1]:
        for C in [0, 1]:
            for M in [0, 1]:
                A = alarme_nivel3(F, B, C, M)
                print(f"{F} {B} {C} {M} | {A}")
print()

# Nível 4 — Código Final com tabela verdade completa

def alarme(F, B, C, M):
    return int(F or (B and C) or (M and not C))

print("Nível 4 — Tabela Verdade Completa")
print("F B C M | A")
print("-----------")
for F in [0, 1]:
    for B in [0, 1]:
        for C in [0, 1]:
            for M in [0, 1]:
                A = alarme(F, B, C, M)
                print(f"{F} {B} {C} {M} | {A}")
