import os

def exibir_nprograma():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░
""")
def exibir_opcoes():
    print("1. Cadastrar Restaurante")
    print("2. Listar Restaurantes")
    print("3. Ativar Restaurante")
    print("4. Sair\n")

def finalizar_app():
    os.system('cls')
    print('Finalizando o app')

def escolher_opcao():
    escolha_num = int(input("Escolha uma opcao: "))
    #print(f"Você escolheu a opcao: {escolha_num} ")
    if escolha_num == 1:
        print("Cadastrar Restaurante")
    elif escolha_num == 2:
        print("Listar Restaurantes")
    elif escolha_num == 3:
        print("Ativar Restaurante")
    else:
        finalizar_app()

def main():
    exibir_nprograma()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()