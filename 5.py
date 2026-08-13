class Produto:
    def __init__(self, nome: str, preco: float, estoque: int):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def reduzir_estoque(self, quantidade: int):
        if quantidade <= self.estoque:
            self.estoque -= quantidade
            return True
        print(f"Estoque insuficiente para '{self.nome}'. Disponível: {self.estoque}")
        return False


class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []  # Lista que guardará tuplas no formato: (produto, quantidade)

    def adicionar_ao_carrinho(self, produto: Produto, quantidade: int):
        if quantidade <= 0:
            print("A quantidade deve ser maior que zero.")
            return

        if quantidade <= produto.estoque:
            self.produtos.append((produto, quantidade))
            print(f"{quantidade}x '{produto.nome}' adicionado(s) ao carrinho.")
        else:
            print(f"Não foi possível adicionar '{produto.nome}'. Estoque atual: {produto.estoque}")

    def mostrar_carrinho(self):
        if not self.produtos:
            print("\nO carrinho está vazio.")
            return

        print("\n--- ITENS NO CARRINHO ---")
        total_geral = 0.0

        for produto, quantidade in self.produtos:
            subtotal = produto.preco * quantidade
            total_geral += subtotal
            print(f"• {produto.nome} | Qtd: {quantidade} | Preço Un.: R$ {produto.preco:.2f} | Subtotal: R$ {subtotal:.2f}")

        print(f"Total a pagar: R$ {total_geral:.2f}")
        print("-" * 30)

    def finalizar_compra(self):
        if not self.produtos:
            print("\nNão há itens no carrinho para finalizar a compra.")
            return

        print("\nProcessando compra e atualizando estoques...")
        for produto, quantidade in self.produtos:
            produto.reduzir_estoque(quantidade)

        self.produtos.clear()
        print("Compra realizada com sucesso! Carrinho esvaziado.")



if __name__ == "__main__":
    # 1. Criando produtos
    p1 = Produto("Mouse Gamer", 150.00, 10)
    p2 = Produto("Teclado Mecânico", 350.00, 5)
    p3 = Produto("Monitor 144Hz", 1200.00, 2)

    
    carrinho = CarrinhoDeCompras()

    
    carrinho.adicionar_ao_carrinho(p1, 2)
    carrinho.adicionar_ao_carrinho(p2, 1)
    
    carrinho.adicionar_ao_carrinho(p3, 5)  # Deve barrar por ter apenas 2 em estoque

    
    carrinho.mostrar_carrinho()


    carrinho.finalizar_compra()

    
    print(f"\nEstoque restante de '{p1.nome}': {p1.estoque}")
    print(f"Estoque restante de '{p2.nome}': {p2.estoque}")