import os

restaurantes = ['Pizza', 'Sushi']

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
    print("2. Listar Restaurantes cadastrados")
    print("3. Ativar Restaurante")
    print("4. Sair\n")
def finalizar_app():
   exibir_subtitulo('Finalizando o app')
    print('Finalizando o app')
    main()

def voltar_ao_menu_principal():
    input("\nPressione ENTER para sair")
    main()
def opt_invalida():
    print('Opção inválida\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()
def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastrando novo restaurante')
    nome_restaurante = input("Insira o nome do restaurante que deseja cadastrar: ")
    restaurantes.append(nome_restaurante)
    print(f"O restaurante {nome_restaurante} foi cadastrado com sucesso!!\n")
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando restaurantes')
    for restaurante in restaurantes:
        print(f'.{restaurante}')
    voltar_ao_menu_principal()

def escolher_opcao():
    try:
        escolha_num = int(input("Escolha uma opção: "))
        #print(f"Você escolheu a opcao: {escolha_num} ")
        if escolha_num == 1:
            cadastrar_novo_restaurante()
        elif escolha_num == 2:
            listar_restaurantes()
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