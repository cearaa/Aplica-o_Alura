#Input e estrutura ímpar e par
numI = int(input("Insira um número inteiro: "))
if numI % 2 == 0:
    print("O número é par.\n")
else:
    print("O número é ímpar.\n")

#Regras de negócio para idade e input
idade = int(input("Insira sua idade: "))
if idade >= 0 and idade <= 12:
    print("Você é uma criança")
elif idade >= 13 and idade < 18:
    print("Você é um adolescente\n")
else:
    print("Você é um adulto\n")

nome = input("Insira seu nome: ")
if nome == "Tárik":
    print("Esse sou eu!!\n")
senha = int(input("Insira sua senha: "))
if senha == 13 :
    print("Acesso permitido!!\n")
else:
    print("Senha errada amigão.\n")


x = float(int(input("Coordenadas do ponto x: ")))
y = float(int(input("Coordenadas do ponto y: ")))
if x > 0 and y > 0:
    print("Ponto no primeiro quadrante")
elif x <0 and y > 0:
    print("Ponto segundo quadrante")
elif x <0 and y < 0:
    print("Ponto terceiro quadrante")
elif x > 0 and y < 0:
    print("Ponto quarto quadrante")
else:
    print("Ponto localizado num eixo ou na origem")
