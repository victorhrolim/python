# exercício lista 1

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.__preco = preco
        self.quantidade = quantidade

    def valor_total(self):
        return self.__preco * self.quantidade

    def get_preco(self):
        return self.__preco

    def set_preco(self, novo_preco):
        if novo_preco > 0:
            self.__preco = novo_preco
        else:
            print("preço inválido")

produto1 = Produto("Arroz", 10.50, 5)
produto2 = Produto("Feijão", 8.00, 3)

print(f"O produto é: {produto1.nome}, o preço é: {produto1.get_preco()} a quantidade é de: {produto1.quantidade}. O valor total é de: {produto1.valor_total()}")
print(f"O produto é: {produto2.nome}, o preço é: {produto2.get_preco()} a quantidade é de: {produto2.quantidade}. O valor total é de: {produto2.valor_total()}")

produto1.set_preco(120)
print(produto1.get_preco())
produto1.set_preco(-5)
print(produto1.get_preco())

# exercício lista 2

cardapio = {"X-Burguer": 18.00,
            "X-Salada": 20.00,
            "Batata": 12.00,
            "Refrigerante": 6.50,
            "Suco": 8.00}

class Pedido:
    def __init__(self, cliente, cardapio):
        self.cliente = cliente
        self.__cardapio = cardapio
        self.__itens = {}
        self.__desconto = 0
        self.__fechado = False

    def adicionar_item(self, nome, quantidade = 1):
        if self.__fechado:
            print("Pedido fechado, não foi possível adicionar o item.")
        elif nome not in self.__cardapio:
            print(f"O item {nome} não existe no cardápio.")
        elif quantidade <= 0:
            print("Quantidade inválida.")
        elif nome in self.__itens:
            self.__itens[nome] += quantidade
        else:
            self.__itens[nome] = quantidade

    def remover_item(self, nome):
        if self.__fechado:
            print("Pedido fechado.")
        elif nome not in self.__itens:
            print(f"{nome} não está no pedido.")
        else:
            del self.__itens[nome]

    def sub_total(self):
        total = 0
        for nome, quantidade in self.__itens.items():
            total += self.__cardapio[nome] * quantidade
        return total

    def aplicar_cupom(self, codigo):
        if self.__desconto > 0:
            print("Já existe um cupom neste pedido.")
        elif codigo == "PROMO10":
            self.__desconto = 10
        elif codigo == "COMBO15":
            if self.sub_total() >= 50:
                self.__desconto = 15
            else:
                print("Cupom 'COMBO15' exige valor minimo de 50,00 reais.")
        else:
            print("Cupom inválido.")

    def total(self):
        return self.sub_total()  * (1 - self.__desconto / 100)

    def fechar(self):
        if not self.__itens:
            print("Pedido vazio")
        else:
            self.__fechado = True

    def imprimir_nota(self):
        print(f"\n===== NOTA - Cliente: {self.cliente} =====")
        for nome, quantidade in self.__itens.items():
            valor = self.__cardapio[nome] * quantidade
            print(f"{quantidade}x {nome:<15} R$ {valor:.2f}")
        print(f"Subtotal: R$ {self.sub_total():.2f}")
        if self.__desconto > 0:
            valor_desc = self.sub_total() * self.__desconto / 100
            print(f"Desconto ({self.__desconto}%): -R$ {valor_desc:.2f}")
        print(f"Total: R$ {self.total():.2f}")

    def get_fechado(self):
        return self.__fechado

    def get_desconto(self):
        return self.__desconto

pedido = Pedido("Rolim", cardapio)
pedido.adicionar_item("X-Burguer", 2)
pedido.adicionar_item("Batata", 1)
pedido.adicionar_item("Pizza", 1)
pedido.adicionar_item("Refrigerante", 2)
pedido.adicionar_item("X-Burguer", 1)

pedido.remover_item("Batata")

pedido.aplicar_cupom("COMBO15")
pedido.aplicar_cupom("PROMO10")

pedido.fechar()
pedido.adicionar_item("Suco")
pedido.imprimir_nota()
