# PyCash

O **PyCash** é um sistema simples desenvolvido em Python que simula o funcionamento de uma caixa registradora de supermercado. O objetivo principal é processar produtos, calcular o valor total da compra e permitir diferentes formas de pagamento (crédito, débito e dinheiro). O projeto foi criado como parte do aprendizado em Python, com planos de evoluir para um sistema mais completo e com interface gráfica no futuro.

---

## Funcionalidades

- **Cadastro de Produtos**: Utiliza códigos de barras para identificar produtos, nomes e preços.
- **Cálculo Automático**: Soma o valor total dos produtos registrados.
- **Formas de Pagamento**: Suporta pagamento em dinheiro, crédito e débito.
- **Simulação de Maquininha**: Validação de senha para pagamentos com cartão.
- **Troco Automático**: Calcula o troco para pagamentos em dinheiro.

---

## Tecnologias Utilizadas

- **Linguagem**: Python
- **Bibliotecas**: `random` (para gerar códigos de barras aleatórios).
- **Estrutura**: Programação procedural com uso de listas e loops.

---

## Como Executar o Projeto

### Pré-requisitos
- Python 3.x instalado.
- Um ambiente de desenvolvimento (IDE como PyCharm, VS Code, ou terminal).

### Passos para Execução

1. Clone o repositório:
   ```bash
   git clone https://github.com/Boudenzin/PyCash.git
   
2. Navegue até o diretório do projeto:
   ```bash
   cd PyCash
   ```

3. Execute o arquivo Python:
   ```bash
   python caixaregistradora2.py
   ```

4. Siga as instruções no terminal:
   - Insira os códigos de barras dos produtos.
   - Escolha a forma de pagamento.
   - Siga os passos para finalizar a compra.

---

## Estrutura do Código

O código está organizado da seguinte forma:

- **Listas de Dados**:
  - `codigos`: Armazena os códigos de barras dos produtos.
  - `produtos`: Armazena os nomes dos produtos.
  - `precos`: Armazena os preços dos produtos.
  - `tiposdepagamento`: Define as formas de pagamento aceitas.

- **Lógica Principal**:
  - Geração de códigos de barras aleatórios.
  - Verificação de produtos cadastrados.
  - Cálculo do valor total da compra.
  - Processamento de pagamentos (crédito, débito e dinheiro).

---

## Próximos Objetivos

Futuras metas a serem alcançadas pelo projeto

1. **Interface Gráfica**:
   - Implementar uma interface gráfica usando bibliotecas como `Tkinter` ✅

2. **Banco de Dados**:
   - Substituir as listas por um banco de dados (SQLite, MySQL) para armazenar produtos ✅ e transações.

3. **Leitor de Código de Barras**:
   - Integrar um leitor de código de barras real para automação do processo.

4. **Relatórios**:
   - Gerar relatórios de vendas diárias, mensais e anuais.

5. **Autenticação de Usuários**:
   - Adicionar um sistema de login para funcionários e administradores.

6. **Testes Automatizados**:
   - Implementar testes unitários com `unittest` ou `pytest` para garantir a qualidade do código.

7. **Deploy**:
   - Publicar o sistema em um servidor ou plataforma na nuvem para acesso remoto.

## Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.


