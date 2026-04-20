#Input e estrutura ímpar e par
numI = int(input("Insira um número inteiro: "))
if numI % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

#Regras de negócio para idade e input
idade = int(input("Insira sua idade: "))
if idade >= 0 and idade <= 13:
    print("Criança")
elif idade >= 13 and idade <= 18:
    print("Adolescente")
else:
    print("Adulto")