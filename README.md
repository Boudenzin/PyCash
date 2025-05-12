# PyCash

O **PyCash** é um sistema simples desenvolvido em Python que simula o funcionamento de uma caixa registradora de supermercado. O objetivo principal é processar produtos, calcular o valor total da compra, permitir diferentes formas de pagamento e registrar transações em banco de dados. O projeto evoluiu de uma estrutura procedural para uma aplicação com interface gráfica utilizando **Tkinter** e conexão com **MySQL**.

---

## Funcionalidades

- **Cadastro de Produtos**: Utiliza códigos de barras para identificar produtos, nomes e preços.
- **Cálculo Automático**: Soma o valor total dos produtos registrados.
- **Formas de Pagamento**: Suporta pagamento em dinheiro, crédito e débito.
- **Simulação de Maquininha**: Validação de senha para pagamentos com cartão.
- **Troco Automático**: Calcula o troco para pagamentos em dinheiro.
- **Interface Gráfica (GUI)**: Desenvolvida com Tkinter para facilitar a usabilidade.
- **Armazenamento de Transações**: As compras realizadas são salvas no banco de dados.
- **Testes Automatizados**: Cobertura básica com `unittest` para garantir integridade do sistema.

---

## Tecnologias Utilizadas

- **Linguagem**: Python
- **Interface**: Tkinter
- **Banco de Dados**: MySQL
- **Bibliotecas**:
  - `mysql-connector-python`
  - `tkinter`
  - `unittest`
  - `dotenv`

---

## Como Executar o Projeto

### Pré-requisitos

- Python 3.x instalado
- Banco de dados MySQL ativo
- Criar o arquivo `.env` com as credenciais:
```

DB_HOST=localhost
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_NAME=nome_do_banco

````

- Instalar dependências:
```bash
pip install mysql-connector-python python-dotenv
````

### Passos

1. Clone o repositório:

   ```bash
   git clone https://github.com/Boudenzin/PyCash.git
   cd PyCash
   ```

2. Configure o banco de dados com as tabelas:

   ```sql
   CREATE DATABASE CaixaDB;
   USE CaixaDB;
   CREATE TABLE produtos (
       codigo_barras VARCHAR(13) PRIMARY KEY,
       nome VARCHAR(100) NOT NULL,
       preco DECIMAL(10, 2) NOT NULL
   );
   INSERT INTO produtos (codigo_barras, nome, preco) VALUES
   ('7123456789012', 'Macarrão Espaguete', 2.99),
   ('7987654321098', 'Molho de Tomate', 1.49),
   ('7456789012345', 'Arroz Integral', 3.25),
   ('7321098765432', 'Feijão Preto', 2.75),
   ('7567890123456', 'Leite Desnatado', 1.99),
   ('7890123456789', 'Pão de Forma Integral', 4.49),
   ('7234567890123', 'Iogurte Natural', 2.29),
   ('7678901234567', 'Cereal Matinal', 3.99),
   ('7345678901234', 'Salmão Fresco', 10.99),
   ('7789012345678', 'Maçãs Gala', 0.79);

   ```

3. Execute a interface gráfica:

   ```bash
   python main.py
   ```

4. (Opcional) Execute os testes automatizados:

   ```bash
   python teste.py
   ```

---

## Estrutura do Projeto

* `main.py` – Interface principal do caixa registradora com Tkinter.
* `db.py` – Gerenciamento da conexão com MySQL.
* `teste.py` – Testes automatizados com `unittest`.

---

## Próximos Objetivos

1. ✅ **Interface Gráfica com Tkinter**
2. ✅ **Banco de Dados com MySQL**
3. 🔲 **Armazenamento de Transações**
4. ✅ **Testes Automatizados com `unittest`**
6. 🔲 **Geração de Relatórios de Vendas**
8. 🔲 **Deploy em Servidor/Nuvem**

---

## Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
