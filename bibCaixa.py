"""
Módulo bibCaixa
---------------

Este módulo oferece funções auxiliares para o sistema da caixa registradora, 
incluindo uma saudação com base no horário atual e uma interface de ajuda 
para comandos e listagem de informações.

Funções:
- saudacao(): Retorna uma saudação com base na hora atual.
- helpPrint(): Exibe instruções de ajuda para o usuário.
- helpExec(operacao, produtos, tipos_pagamento): Executa comandos de ajuda.
"""

from datetime import datetime, time


def saudacao():
    """
    Retorna uma saudação de acordo com o horário atual.

    Retorna:
        str: "Bom dia", "Boa tarde" ou "Boa noite", dependendo do horário.
             Caso ocorra algum erro, retorna uma mensagem de erro.
    """
    try:
        hora_atual = datetime.now().time()

        horario_manha = time(6, 0, 0)   # Das 6h às 11:59
        horario_tarde = time(12, 0, 0)  # Das 12h às 17:59
        horario_noite = time(18, 0, 0)  # Das 18h em diante

        if horario_manha <= hora_atual < horario_tarde:
            return "Bom dia"
        elif horario_tarde <= hora_atual < horario_noite:
            return "Boa tarde"
        else:
            return "Boa noite"

    except Exception as error:
        return f"Ocorreu um erro: {error}"


def helpPrint():
    """
    Imprime no console as opções disponíveis para o usuário
    no painel de ajuda.
    """
    print("Olá, seja bem-vindo(a) ao painel do usuário. O que você deseja fazer?")
    print("Por favor, digite um número para cada opção desejada:")
    print("1 - Mostrar a lista de produtos")
    print("2 - Mostrar os métodos de pagamento disponíveis")


def helpExec(operacao, produtos, tipos_pagamento):
    """
    Executa a operação de ajuda escolhida pelo usuário.

    Args:
        operacao (int): O número da operação escolhida (1 ou 2).
        produtos (dict): Dicionário de produtos disponíveis.
        tipos_pagamento (list): Lista com os tipos de pagamento aceitos.

    Retorna:
        bool: True se a operação foi executada corretamente, False se inválida.
    """
    if operacao == 1:
        print("Todos os produtos:")
        for codigo, (nome, preco) in produtos.items():
            print(f"{codigo} - {nome}: R$ {preco:.2f}")
        return True
    elif operacao == 2:
        print("Métodos de pagamento disponíveis:")
        for metodo in tipos_pagamento:
            print(f"- {metodo}")
        return True
    else:
        print("Essa opção não está na lista.")
        return False
