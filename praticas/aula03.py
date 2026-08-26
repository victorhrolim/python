nome = input("digite o nome do motorista: ")
meta = int(input("quanto quer arrecadar no dia?: "))
corridas = int(input("quantas corridas pertende fazer?: "))
corrida1 = float("digite o valor arrecadado desta corrida: ")
corrida2 = float("digite o valor arrecadado desta corrida: ")
corrida3 = float("digite o valor arrecadado desta corrida: ")
corrida4 = float("digite o valor arrecadado desta corrida: ")
corrida5 = float("digite o valor arrecadado desta corrida: ")

total = corrida1 + corrida2 + corrida3 + corrida4 + corrida5

if total >= meta:
    print(f"o valor total arrecadado foi {total} a sua meta era de {meta}. parabéns {nome}!")
elif total == meta:
    print(f"o valor total arrecadado foi {total} a sua meta era de {meta}. foi no limite hein {nome}!")
else:
    print(f"o valor total arrecadado foi {total} a sua meta era de {meta}. faltou {total - meta}")
    print(f"boa sorte na proxima {nome}")

'''
soma +
multiplicação *
subtração - 
divisão /
divisão inteira //
resto da divisão %
potência **
'''

gols_nau = 0
gols_san = 0

gol = int(input("qual time fez o gol? [(1) nautico]/[(2) santa]: "))

if gol == 1:
    gols_nau +=1
    print("gol do náutico")
else:
    gols_san +=1
    print("gol do santa cruz")

var = input("o gol foi validado? [sim/nao]: ")

if var == "nao":
    if gol == 1:
        gols_nau -= 1
    else:
        gols_san -= 1
else:
    print("gol valido")

print(f"placar do jogo: Náutico {gols_nau} X {gols_san} Santa")

gol = int(input("qual time fez o gol? [(1) nautico]/[(2) santa]: "))

if gol == 1:
    gols_nau +=1
    print("gol do náutico")
else:
    gols_san +=1
    print("gol do santa cruz")

var = input("o gol foi validado? [sim/nao]: ")

if var == "nao":
    if gol == 1:
        gols_nau -= 1
        print("gol anulado")
    else:
        gols_san -= 1
        print("gol anulado")
else:
    print("gol valido")

print(f"placar do jogo: Náutico {gols_nau} X {gols_san} Santa")

if gols_san > gols_nau:
    print("santa ganhou")
elif gols_nau > gols_san:
    print("náutico ganhou")
else:
    print("empate")

print("fim do jogo.")
