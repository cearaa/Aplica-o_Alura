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
    main()

def opt_invalida():
    print('Opção inválida\n')

def escolher_opcao():
    try:
        escolha_num = int(input("Escolha uma opção: "))
        #print(f"Você escolheu a opcao: {escolha_num} ")
        if escolha_num == 1:
            print("Cadastrar Restaurante")
        elif escolha_num == 2:
            print("Listar Restaurantes")
        elif escolha_num == 3:
            print("Ativar Restaurante")
        elif escolha_num == 4:
            finalizar_app()
        else:
            opt_invalida()
    except:
        opt_invalida()

def main():
    os.system('cls')
    exibir_nprograma()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()