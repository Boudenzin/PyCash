import tkinter as tk
from tkinter import ttk, messagebox
import bibCaixa

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
        centralizar_janela(self.root, largura=550, altura=350)
        self.total = 0
        self.nome_vendedor = nome_vendedor
        self.itens = []

        self.setup_ui()
        
    def setup_ui(self):
        # Código de barras
        tk.Label(self.root, text="Código de Barras:").grid(row=0, column=0, sticky="e")
        self.codigo_entry = tk.Entry(self.root)
        self.codigo_entry.grid(row=0, column=1)

        # Unidades
        tk.Label(self.root, text="Unidades:").grid(row=1, column=0, sticky="e")
        self.unidades_entry = tk.Entry(self.root)
        self.unidades_entry.grid(row=1, column=1)

        # Botão adicionar
        tk.Button(self.root, text="Adicionar Produto", command=self.adicionar_produto).grid(row=2, column=0, columnspan=2)

        # Lista de produtos
        self.lista = tk.Text(self.root, height=10, width=50)
        self.lista.grid(row=3, column=0, columnspan=2)

        # Total
        self.total_var = tk.StringVar()
        self.total_var.set("Total: R$ 0.00")
        tk.Label(self.root, textvariable=self.total_var).grid(row=4, column=0, columnspan=2)

        # Forma de pagamento
        tk.Label(self.root, text="Pagamento:").grid(row=5, column=0)
        self.pagamento_combo = ttk.Combobox(self.root, values=TIPOS_PAGAMENTO, state="readonly")
        self.pagamento_combo.grid(row=5, column=1)
        self.pagamento_combo.current(0)

        # Valor em dinheiro
        tk.Label(self.root, text="Valor Pago (Dinheiro):").grid(row=6, column=0)
        self.valor_pago_entry = tk.Entry(self.root)
        self.valor_pago_entry.grid(row=6, column=1)

        # Botão finalizar
        tk.Button(self.root, text="Finalizar Compra", command=self.finalizar_compra).grid(row=7, column=0, columnspan=2)

    def adicionar_produto(self):
        codigo = self.codigo_entry.get()
        unidades = self.unidades_entry.get()

        if codigo not in PRODUTOS:
            messagebox.showerror("Erro", "Produto não encontrado.")
            return

        try:
            unidades = int(unidades)
            if unidades <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Erro", "Unidades inválidas.")
            return

        nome, preco = PRODUTOS[codigo]
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
