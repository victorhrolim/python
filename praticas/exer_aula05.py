semana = ("segunda", "terca", "quarta", "quinta", "sexta", "sabado", "domingo")

print(semana[0])
print(semana[-1])
print(len(semana))

print(semana[0:4])

ponto = (3, 7)
x, y = ponto
print(x)
print(y)

a = 10
b = 20

a, b = b, a

print(a, b)

produto = {
    "comida": "pastel",
    "preco": 9.50,
    "quantidade": 14
}
print(produto)

produto["preco"] *= 1.10
print(f"Novo preco R$ {produto['preco']:.2f}")

produto["categoria"] = "fritos"

print(produto)

print(produto.get("marca"))
print(produto.get("marca", "não informada"))

agenda = {}

while True:
    print("1. Add contato")
    print("2. Buscar contato")
    print("3. Remover contato")
    print("4. Listas todos")
    print("0. Sair")

    opcao = int(input("Digite sua opção: "))


    if opcao == 0:
        print("obrigado pela consulta.")
        break

    if opcao == 4:
        if len(agenda) == 0:
            print("Lista vazia")
        else:
            for nome, telefone in agenda.items():
                print(f"Nome: {nome} - Telefone: {telefone}")
        print("Esses são todos os seus contatos.")
        continue


    nome = input("Digite o nome do contato: ")

    if opcao == 1:
        telefone = int(input("Digite o telefone do contato: "))
        agenda[nome] = telefone
        print("Contato adicionado!")


    elif opcao == 2:
        if nome in agenda:
            print(f"Contato: {nome} - Telefone: {agenda[nome]}")
        else:
            print("O contato não existe")


    elif opcao == 3:
        if nome in agenda:
            del agenda[nome]
        else:
            print(f"Contato '{nome}' não existe na agenda")
    else:
        print("Opção inválida, tente novamente!")
