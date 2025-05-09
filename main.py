import tkinter as tk
from tkinter import ttk, messagebox
import bibCaixa
from db import conectar

TIPOS_PAGAMENTO = ["CRÉDITO", "DÉBITO", "DINHEIRO"]

def buscar_produto(codigo):
    conexao = conectar()
    if not conexao:
        messagebox.showerror("Erro de Banco", "Não foi possível conectar ao banco de dados.")
        return None

    cursor = conexao.cursor()
    cursor.execute("SELECT nome, preco FROM produtos WHERE codigo_barras = %s", (codigo,))
    resultado = cursor.fetchone()
    cursor.close()
    conexao.close()
    return resultado  # retorna (nome, preco) ou None

class TelaInicial:
    def __init__(self, root, iniciar_caixa_callback):
        self.root = root
        self.root.title("Bem-vindo")
        centralizar_janela(self.root, 400, 200)

        frame_central = tk.Frame(self.root)
        frame_central.pack(expand=True)
        
        self.label = tk.Label(frame_central, text="Bem-vindo ao Mercado Bom Todo!\nDigite seu nome para começar:")
        self.label.pack(pady=10)
        
        self.nome_entry = tk.Entry(frame_central)
        self.nome_entry.pack()

        self.botao_iniciar = tk.Button(frame_central, text="Iniciar", command=self.iniciar)
        self.botao_iniciar.pack(pady=10)

        self.iniciar_caixa_callback = iniciar_caixa_callback

    def iniciar(self):
        nome = self.nome_entry.get().strip().title()
        if nome:
            saudacao = bibCaixa.saudacao()
            messagebox.showinfo("Saudação", f"{saudacao}, {nome}!")
            self.root.destroy()  # Fecha tela de boas-vindas
            self.iniciar_caixa_callback(nome)  # Passa nome para a próxima tela
        else:
            messagebox.showwarning("Aviso", "Por favor, insira seu nome.")

class CaixaRegistradora:
    def __init__(self, nome_vendedor, root):
        self.root = root
        self.root.title("Caixa Registradora")
        centralizar_janela(self.root, largura=600, altura=400)
        self.total = 0
        self.nome_vendedor = nome_vendedor
        self.itens = []

        self.setup_ui()
        
    def setup_ui(self):
        # Frame principal horizontal
        frame_principal = tk.Frame(self.root)
        frame_principal.pack(padx=10, pady=10)

        # Frame esquerdo - formulário
        frame_esquerdo = tk.Frame(frame_principal)
        frame_esquerdo.grid(row=0, column=0, padx=10)

        # Frame direito - lista de produtos
        frame_direito = tk.Frame(frame_principal)
        frame_direito.grid(row=0, column=1, padx=10)

        # === FORMULÁRIO ===
        tk.Label(frame_esquerdo, text="Código de Barras:").grid(row=0, column=0, sticky="e")
        self.codigo_entry = tk.Entry(frame_esquerdo)
        self.codigo_entry.grid(row=0, column=1)

        tk.Label(frame_esquerdo, text="Unidades:").grid(row=1, column=0, sticky="e")
        self.unidades_entry = tk.Entry(frame_esquerdo)
        self.unidades_entry.grid(row=1, column=1)

        tk.Button(frame_esquerdo, text="Adicionar Produto", command=self.adicionar_produto)\
            .grid(row=2, column=0, columnspan=2, pady=5)

        self.lista = tk.Text(frame_esquerdo, height=10, width=40)
        self.lista.grid(row=3, column=0, columnspan=2, pady=5)

        self.total_var = tk.StringVar(value="Total: R$ 0.00")
        tk.Label(frame_esquerdo, textvariable=self.total_var).grid(row=4, column=0, columnspan=2)

        tk.Label(frame_esquerdo, text="Pagamento:").grid(row=5, column=0)
        self.pagamento_combo = ttk.Combobox(frame_esquerdo, values=TIPOS_PAGAMENTO, state="readonly")
        self.pagamento_combo.grid(row=5, column=1)
        self.pagamento_combo.current(0)

        tk.Label(frame_esquerdo, text="Valor Pago (Dinheiro):").grid(row=6, column=0)
        self.valor_pago_entry = tk.Entry(frame_esquerdo)
        self.valor_pago_entry.grid(row=6, column=1)

        tk.Button(frame_esquerdo, text="Finalizar Compra", command=self.finalizar_compra)\
            .grid(row=7, column=0, columnspan=2, pady=5)

        # === LISTA DE PRODUTOS ===
        tk.Label(frame_direito, text="Clique para adicionar:").pack()
        self.lista_produtos = tk.Listbox(frame_direito, height=20, width=35)
        self.lista_produtos.pack()

        # Preencher Listbox com produtos do dicionário global PRODUTOS
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT codigo_barras, nome FROM produtos")
        produtos = cursor.fetchall()
        conexao.close()

        for codigo, nome in produtos:
            self.lista_produtos.insert(tk.END, f"{codigo} - {nome}")

        self.lista_produtos.bind('<<ListboxSelect>>', self.adicionar_por_lista)

    def adicionar_por_lista(self, event):
        selecao = event.widget.curselection()
        if selecao:
            item = event.widget.get(selecao[0])
            codigo = item.split(" - ")[0].strip()

            # Preenche o campo e adiciona 1 unidade automaticamente
            self.codigo_entry.delete(0, tk.END)
            self.codigo_entry.insert(0, codigo)

            self.unidades_entry.delete(0, tk.END)
            self.unidades_entry.insert(0, "1")

            self.adicionar_produto()

    def adicionar_produto(self):
        codigo = self.codigo_entry.get()
        unidades = self.unidades_entry.get()

        produto = buscar_produto(codigo)
        if not produto:
            messagebox.showerror("Erro", "Produto não encontrado.")
            return

        try:
            unidades = int(unidades)
            if unidades <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Erro", "Unidades inválidas.")
            return

        nome, preco = produto
        subtotal = preco * unidades
        self.total += subtotal
        self.itens.append((codigo, nome, unidades, preco))

        self.lista.insert(tk.END, f"{unidades}x {nome} - R$ {preco:.2f} cada\n")
        self.total_var.set(f"Total: R$ {self.total:.2f}")

        self.codigo_entry.delete(0, tk.END)
        self.unidades_entry.delete(0, tk.END)

    def finalizar_compra(self):
        metodo = self.pagamento_combo.get()

        if metodo == "DINHEIRO":
            try:
                valor_pago = float(self.valor_pago_entry.get())
                if valor_pago < self.total:
                    faltando = self.total - valor_pago
                    messagebox.showwarning("Pagamento insuficiente", f"Faltam R$ {faltando:.2f}")
                    return
                troco = valor_pago - self.total
                messagebox.showinfo("Compra Finalizada", f"Troco: R$ {troco:.2f}")
            except ValueError:
                messagebox.showerror("Erro", "Digite um valor em dinheiro válido.")
                return
        else:
            messagebox.showinfo("Compra Finalizada", f"Pagamento em {metodo} confirmado.")

        self.resetar()

    def resetar(self):
        self.lista.delete("1.0", tk.END)
        self.total = 0
        self.itens.clear()
        self.total_var.set("Total: R$ 0.00")
        self.valor_pago_entry.delete(0, tk.END)

def centralizar_janela(janela, largura=400, altura=200):
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    x = (largura_tela // 2) - (largura // 2)
    y = (altura_tela // 2) - (altura // 2)
    janela.geometry(f"{largura}x{altura}+{x}+{y}")

def iniciar_caixa(nome_vendedor):
    nova_janela = tk.Tk()
    app = CaixaRegistradora(nome_vendedor, nova_janela)
    nova_janela.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = TelaInicial(root, iniciar_caixa)
    root.mainloop()
