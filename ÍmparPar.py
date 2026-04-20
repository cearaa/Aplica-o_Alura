#Input e estrutura ímpar e par
numI = int(input("Insira um número inteiro: "))
if numI % 2 == 0:
    print("O número é par.\n")
else:
    print("O número é ímpar.\n")

#Regras de negócio para idade e input
idade = int(input("Insira sua idade: "))
if idade >= 0 and idade <= 13:
    print("Você é uma criança")
elif idade >= 13 and idade <= 18:
    print("Você é um adolescente")
else:
    print("Você é um adulto")