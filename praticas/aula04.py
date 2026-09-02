# listas
# aprendizado sobre listas e elementos

notas = [7.0, 9.0, 6.0, 8]
#         0    1    2   3
#        -4   -3   -2  -1
# ordem dos elementos do indice

if len(notas) > 10:
    print(notas[10])
else:
    print(f"A lista tem um total de {len(notas)} elementos.")

frutas = ["banana", "maca", "uva", "laranja"]

print(frutas[0])
print(frutas[-1])

# -------------------------------------------------------------

lista = [24, 47, 87, 3, 63, 38, 65, 34]

print(lista)
lista[2] = 870
print(lista)

# troca de elemento do indice
# usar variavel[posicao_do_indice] = novo indice

# -------------------------------------------------------------

# adicionar itens: .append() e .insert()
# insert fura a fila
# append vai pro final da fila


cidades = ["cabo", "jaboatao", "recife", "olinda"]
print(cidades[0], cidades[-1])
print(len(cidades))
cidades[1] = "igarassu"
print(cidades)

print("fim da parte 1")

convidados = ["alex", "mario", "lucas", "fernando", "pedro"]
print(convidados)
convidados.append("joao")
print(convidados)
convidados.insert(0, "gustavo")
print(convidados)
convidados.remove("mario")
print(convidados)
convidados.pop(1)
print(convidados)
nome = input("digite o nome do convidado: ").lower()
if nome in convidados:
    print(f"{nome} está na lista!")
else:
    print(f"{nome} não está na lista.")
print(len(convidados))
print(convidados[0], convidados[-1])

# --------------------------------------------------------------

# .sort() == ordena a lista crescente
# .reverse() == reverte a lista independente se esta ordenada
# .copy() copia a lista

notas = [14.6, 8.0, 7.9, 30.0, 2.0, 4.7]
notas.sort()
print(notas)
print(notas[0], notas[-1])
notas.sort(reverse=True)
print(notas)
notasx = notas.copy()
notasx.reverse()
print(f"original:{notas}")
print(f"cópia {notasx}")
