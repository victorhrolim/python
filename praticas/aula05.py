''' fatias de listas'''
# slicing - pedaço da lista
# pedaço: lista[inicio:fim:passo]
# retira o pedaço e cria uma nova lista
# forma negativa: lista[*:*:-1]

numeros = [10, 20, 30, 40, 50, 60, 70, 80]
print(numeros[:3:])
print(numeros[-2::])
print(numeros[::-1])
print(numeros[::2])

listainlista = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(listainlista[0])
print(listainlista[1])
print(listainlista[2])
print(listainlista[1][2])
print(listainlista[2][0])
print(listainlista[0][0] + listainlista[1][0] + listainlista[2][2])

''' laços de repetição '''
# while e for
# while = enquanto a condição for atendida
# for = limita a condição utilizando o in range()
# range(inicio, fim, passo) - não é obrigatório utilizar
# o fim não é mostrado
# continue - ignora a próxima etapa e volta para o inicio do laço

N = int(input("digite um numero: "))

while N != 0:
    print(N)
    N -= 1

print("fim da contagem")


while True:
    pergunta = input("digite um texto: ").lower()
    if pergunta == "sair":
        break
    print(pergunta .upper())
print("fim")


soma = 0
quantidade = 0

while True:
    valor = int(input("digite um numero: "))
    
    if valor == 0:
        if quantidade != 0:
            print(f"soma:{soma}")
            print(f"quantidade:{quantidade}")
            print(f"media: {soma / quantidade:.2f}")
        break

    if valor < 0:
        print("numero invalido")
        continue

    soma += valor
    quantidade += 1
