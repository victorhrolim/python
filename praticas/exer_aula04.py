''' Victor Rolim - 10/09/2026 '''
# exercicio da aula 05
# bloco A

# a1
numero = 1
while numero <= 10:
    print(numero)
    numero += 1

# a2
nnumero = 10
while nnumero >= 1:
    print(nnumero)
    nnumero -= 1
print("Fogo!")

# a3
passo = 2
while passo <= 20:
    print(passo)
    passo += 2

# a4
N = int(input("digite um numero entre 0 e 9: "))
C = 1
while C <= 10:
    print(f"{N} x {C} = {N * C}")
    C += 1

# bloco B

# b1
vl = 0
soma = 0
while True:
    vl = int(input("digite um valor: "))
    soma += vl
    if vl == 0:
        break
    elif vl < 0:
        print("valor invalido")

print(f"o valor total é: {soma}")

# b2
while True:
    senha = input("digite sua senha: ").lower()
    if senha == "sair":
        break
    else:
        print("senha incorreta, tente novamente.")

print("programa encerrado.")

# b3
itens = 0

while True:
    preco = float(input("digite o preço do item: "))
    if preco == 0:
        break
    if preco < 0:
        print("invalido")
    else:
        itens += 1

print(f"o total de itens foi {itens}")

# bloco C

# c1
while True:
    opcao = int(input("Selecione uma frase:( [1] Dizer Olá | [2] Dizer Tchau | [0] Sair ) "))
    if opcao == 0:
        break
    if opcao == 1:
        print("Olá")
    elif opcao == 2:
        print("Tchau")
    else:
        print("Opção inválida")

# c2
for N in range (1, 51):
    if N % 3 == 0:
        continue
    print(N)

# c3
while True:
    num = int(input("digite um numero: "))
    if num < 0:
        print("negativo ignorado")
        continue
    if num == 0:
        break
    else:
        print(f"o dobro do valor é {num * 2} ")

# c4
for ND in range (1, 10001):
    if ND % 7 == 0 and ND % 5 == 0:
        print(f"o primeiro numero divisivel por 7 e 5 é: {ND}!")
        break

# bloco D

# d1
SN = 0
for Nm in range (1,101):
    SN += Nm
print(f"a soma dos numeros de 1 a 100 é: {SN}")

# d2
somA = 0
for _ in range(5):
    nota = float(input("Digite uma nota: "))
    somA += nota
media = somA / 5
print(f"Soma: {somA:.2f}")
print(f"Média: {media:.2f}")

# d3
somaa = 0
quant = 0
while True:
    seila = int(input("digite um valor: "))
    if seila == 0:
        break
    if seila < 0:
        print("valor invalido, digite um valor valido")
    somaa += quant
    quant += 1
mediaa = somaa / quant
print(f"a soma total é de {somaa:.2f}")
print(f"a quantidade de valores inseridos foram {quant:.2f}")
print(f"a media total dos valores foi de {mediaa:.2f}")
