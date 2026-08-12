print("calcular a idade media dos amigos")

total_amigos = 3

idade1 = int(input("digite a idade do primeiro amigo: "))
idade2 = int(input("digite a idade do segundo amigo: "))
idade3 = int(input("digite a idade do terceiro amigo: "))

media = (idade1 + idade2 + idade3) / total_amigos

if media >= 18:
    print("A média de idade dos seus amigos juntos é de um adulto")

elif media >= 14:
    print("A média de idade dos seus amigos juntos é de um adolescente")

else:
    print("A média de idade dos seus amigos juntos é de uma criança")
