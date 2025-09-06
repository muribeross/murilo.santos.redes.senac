# ===== Especificações =====
LIMITES = {
    "Brix": (10.5, 11.2),
    "pH": (2.3, 2.6),
    "Nível": (195, 205)
}

# Armazém dos registros
inspecoes = []

# Função para validar cada medição
def validar_medido(parametro, valor):
    minimo, maximo = LIMITES[parametro]
    if valor < minimo:
        return "BAIXO"
    elif valor > maximo:
        return "ALTO"
    else:
        return "OK"

# Função para ler números com validação
def ler_float(mensagem):
    while True:
        entrada = input(mensagem)
        if entrada.lower() == "sair":
            return None
        try:
            return float(entrada)
        except ValueError:
            print("Valor inválido! Digite um número ou 'sair' para encerrar.")

# Realiza inspeção
def realizar_inspecao():
    print("\n=== Nova Inspeção ===")
    lote = input("Informe o número do lote: ")
    if lote.lower() == "sair":
        return False

    linha = input("Informe a linha de produção: ")
    if linha.lower() == "sair":
        return False

    brix = ler_float("Digite a medição de Brix: ")
    if brix is None:
        return False

    ph = ler_float("Digite a medição de pH: ")
    if ph is None:
        return False

    nivel = ler_float("Digite a medição de Nível (mL): ")
    if nivel is None:
        return False

    # Validar cada dado
    status_brix = validar_medido("Brix", brix)
    status_ph = validar_medido("pH", ph)
    status_nivel = validar_medido("Nível", nivel)

    # Registrar resultado
    registro = {
        "lote": lote,
        "linha": linha,
        "Brix": (brix, status_brix),
        "pH": (ph, status_ph),
        "Nível": (nivel, status_nivel)
    }

    inspecoes.append(registro)
    print("Inspeção registrada com sucesso!\n")
    return True

# Gera relatório final
def gerar_relatorio():
    print("\n===== RELATÓRIO FINAL =====")
    print(f"Total de inspeções realizadas: {len(inspecoes)}\n")

    total_problemas = 0

    for idx, reg in enumerate(inspecoes, start=1):
        print(f"Inspeção {idx} - Lote {reg['lote']} | Linha {reg['linha']}")
        for parametro in ["Brix", "pH", "Nível"]:
            valor, status = reg[parametro]
            if status == "OK":
                print(f" ✅ {parametro}: {valor} Correto")
            else:
                print(f" ⚠️ {parametro}: {valor} Problema ({status})")
                total_problemas += 1
        print("-" * 40)

    print(f"Total de parâmetros fora do padrão: {total_problemas}")

# Loop principal
while True:
    if not realizar_inspecao():
        break
    continuar = input("Deseja realizar outra inspeção? (s/n ou 'sair'): ").lower()
    if continuar not in ("s", "sim"):
        break

gerar_relatorio()
