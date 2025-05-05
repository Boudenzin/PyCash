import tkinter as tk
from random import randint

# Lista com os códigos de barras, nomes dos produtos, preços e os tipos de pagamento

PRODUTOS = {
    "7123456789012": ("Macarrão Espaguete", 2.99),
    "7987654321098": ("Molho de Tomate", 1.49),
    "7456789012345": ("Arroz Integral", 3.25),
    "7321098765432": ("Feijão Preto", 2.75),
    "7567890123456": ("Leite Desnatado", 1.99),
    "7890123456789": ("Pão de Forma Integral", 4.49),
    "7234567890123": ("Iogurte Natural", 2.29),
    "7678901234567": ("Cereal Matinal", 3.99),
    "7345678901234": ("Salmão Fresco", 10.99),
    "7789012345678": ("Maças Gala", 0.79),
}

TIPOS_PAGAMENTO = ["CRÉDITO", "DÉBITO", "DINHEIRO"]

# Limite de quantos digitos a maquininha suporta para senha

LIMITE_SENHA = 4

def exibir_produtos(cod, unidade):
    """Exibe os produtos disponíveis."""
    nome, preco = PRODUTOS[cod]
    print(f"{cod}, {unidade}x {nome}, R$ {preco:.2f} UN")

def buscar_produto(cod):
    """Busca um produto pelo código."""
    return PRODUTOS.get(cod)
# Definição de Variavéis

def solicitar_codigo():
    """Solicita o código de barras do produto."""
    while True:
        codigo = input("Código de Barra do Produto: ").strip()
        if codigo.upper() == "HELP":
            print("Ajuda ainda não implementada.")
            continue
        if codigo in PRODUTOS:
            return codigo
        print("Código não encontrado, tente novamente.")

def solicitar_unidade(nome_produto):
    """Solicita a quantidade de unidades do produto."""
    while True:
        try:
            unidades = int(input(f"Quantas unidades de {nome_produto}: "))
            if unidades > 0:
                return unidades
            print("Quantidade inválida, deve ser maior que zero.")
        except ValueError:
            print("Entrada inválida, tente novamente.")

def registrar_venda():
    """Registra a venda de produtos."""
    total = 0
    while True:
        codigo = solicitar_codigo()
        nome_produto, preco = PRODUTOS[codigo]
        unidades = solicitar_unidade(nome_produto)
        exibir_produtos(codigo, unidades)
        total += preco * unidades

        continuar = input("Deseja registrar outro produto? (SIM/NÃO): ").strip().upper()
        if continuar != "SIM":
            break
    return total

def processar_pagamento(total):
    """Processa o pagamento."""
    print(f"Total: R$ {total:.2f}")
    metodo = input(f"Método de pagamento ({' / '.join(TIPOS_PAGAMENTO)}): ").strip().upper()

    while metodo not in TIPOS_PAGAMENTO:
        print("Método inválido, tente novamente.")
        metodo = input(f"Método de pagamento ({' / '.join(TIPOS_PAGAMENTO)}): ").strip().upper()

    if metodo in ["CRÉDITO", "DÉBITO"]:
        senha = input("Digite sua senha: ")
        while len(senha) > LIMITE_SENHA:
            senha = input(f"Senha inválida. Máximo {LIMITE_SENHA} dígitos. Tente novamente: ")
        print(f"Compra de R$ {total:.2f} efetuada com sucesso.")
    else:
        dinheiro = float(input("Valor pago em dinheiro: R$ "))
        while dinheiro < total:
            falta = total - dinheiro
            print(f"Falta R$ {falta:.2f}")
            dinheiro += float(input("Insira valor adicional: R$ "))
        troco = dinheiro - total
        print(f"Troco: R$ {troco:.2f}")

def main():
    print("Mercado Bom Todo")
    vendedor = input("VENDEDOR: ").strip().title()
    print(f"Bem-vindo, {vendedor}!")

    total_venda = registrar_venda()
    processar_pagamento(total_venda)


if __name__ == "__main__":
    main()