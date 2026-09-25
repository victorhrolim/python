class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.__preco = preco
        self.quantidade = quantidade

    def get_preco(self):
        return self.__preco

    def set_preco(self, novo_preco):
        if novo_preco > 0:
                self.__preco = novo_preco
        else:
            print("preço inválido")

    def exibir_info(self):
        print(f"{self.nome} - R$ {self.get_preco():.2f} (quantidade: {self.quantidade})")

    def __str__(self):
        return f"Produto: {self.nome} - R$ {self.get_preco():.2f}"

    @staticmethod
    def calcular_desconto(preco, percentual):
        return preco - (preco * percentual / 100)

class ProdutoPerecivel(Produto):
    def __init__(self, nome, preco, quantidade, validade):
        super().__init__(nome, preco, quantidade)
        self.validade = validade
    
    def exibir_info(self):
        print(f"{self.nome} - R$ {self.get_preco()} (quantidade: {self.quantidade}) - validade: {self.validade}")

class Estoque:
    def __init__(self):
        self.produtos = []

    def adicionar(self, produto):
        self.produtos.append(produto)

    def listar(self):
        for produto in self.produtos:
             produto.exibir_info()

estoque = Estoque()
estoque.adicionar(Produto("farinha", 3.00, 9))
estoque.adicionar(ProdutoPerecivel("uva", 8.00, 50, "30-09-2026"))
estoque.listar()
chocolate = Produto("chocolate", 7.00, 5)
print(chocolate)
preco_com_desconto = Produto.calcular_desconto(55, 12)
print(preco_com_desconto)

class Robo:
    def falar(self):
        return "blip blop"

class Relogio:
    def falar(self):
        return "tic tac"

def fazer_falar(objeto):
    print(objeto.falar())

fazer_falar(Robo())
fazer_falar(Relogio())

class Carro:
    def __init__(self, modelo, velocidade = 0):
        self.modelo = modelo
        self.__velocidade = velocidade
    @property
    def velocidade(self):
        return self.__velocidade

    @velocidade.setter
    def velocidade(self, valor):
        if valor > 0:
            self.__velocidade = valor
        else:
            print("velocidade não pode ser negativa")

carro = Carro("Strada")
carro.velocidade = 55
print(carro.velocidade)
carro.velocidade = -20
print(carro.velocidade)
