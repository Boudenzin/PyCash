## Função que deine se o usuário receberá um bom dia, boa tarde ou boa noite, a ser usado no programa principa

# Importação da Biblioteca Datetime para saudação do usuário

from datetime import datetime, time

def saudacao():
    try:
        # Hora atual
        
        hora_atual = datetime.now().time()

        # Uso de tuples para definição dos horários da manhã, tarde e noite
        
        horario_manha = time(6, 0, 0)  # 6:00 AM
        horario_tarde = time(12, 0, 0)  # 12:00 PM
        horario_noite = time(18, 0, 0)  # 6:00 PM

        # Verificação do intervalo

        if ((horario_manha <= hora_atual) and (hora_atual < horario_tarde)):
            mensagem = "Bom dia"
        elif ((horario_tarde <= hora_atual) and (hora_atual < horario_noite)):
            mensagem = "Boa tarde"
        else:
            mensagem = "Boa noite"

        return mensagem

    except Exception as error:
        return f"Ocorreu um erro: {error}"
    


def helpPrint():

    print ("Olá, seja bem vindo(a) ao painel do usuário, o que você deseja fazer? ")  
    print ("Por favor, digite um número para cada opção desejada ")
    print ("1 - Para mostrar a lista de produtos")
    print ("2 - Para saber quais são os métodos de pagamento")



def helpExec(operacao, produtos, tipos_pagamento):

    if ((operacao != 1) and (operacao != 2)):
        print ("Essa opção não está na lista")
        return False
    elif (operacao == 1):
        print ("Todos os produtos:")
        for x in produtos:
            print (x)
        return True
    elif (operacao == 2):
        print (tipos_pagamento)
        return True

