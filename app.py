import os #biblioteca de códigos do python

restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False}, 
                {'nome':'Pizza Superma', 'categoria':'Pizza', 'ativo':True},
                {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}]



def exibir_nome_do_programa():
    '''Essa função é responsável por apresentar o o visual do nome do programa'''
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def exibir_opcoes():
    '''Essa função é responsável por apresentar a lista de menus para navegação do app'''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar estado dos restaurantes')
    print('4. Sair\n')

def finalizar_app(): #def é o comando para criar uma função: def = function
    '''Essa função é responsável por finalizar o programa quando usuário selecionar a opção determinada'''
    exibir_subtitulo('Finalizando o App')

def voltar_ao_menu_principal():
    '''Essa função é responsável por retornar o usuário até o menu principal'''
    input('\nDigite uma tecla para voltar ao menu: ')
    main()

def exibir_subtitulo(texto):
    '''Essa função é responsável por limpar o terminal e imprimir o design e os textos dos subtítulos'''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def opcao_invalida():
    '''Essa função é responsável por guiar o usuário ao menu principal quando o mesmo não seleciona um opção válidade'''
    voltar_ao_menu_principal()

def cadastrar_novo_restaurante():
    '''Essa função é responsável por cadastrar um novo restaurante'''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def listar_restaurantes():
    '''Essa função é responsável por listar informações dos restaurantes registrados'''
    exibir_subtitulo('Listando restaurantes')
    print(f'{'Nome do Restaurante'.ljust(22)} | {'Categoria'.ljust(20)}| Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    '''Essa função é responsável por alterar os status dos restaurantes'''
    exibir_subtitulo('ALterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado.')
        
        
    voltar_ao_menu_principal()


def escolher_opcoes():
    '''Essa função é responsável por registrar e enviar o usuário para a página escolhida por ele'''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        match opcao_escolhida:
            case 1:
                print('Cadastrar restaurante')
                cadastrar_novo_restaurante()
            case 2:
                print('Listar restaurantes')
                listar_restaurantes()
            case 3:
                alternar_estado_restaurante()
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()

def main():
    '''Essa função é responsável por apresentar o menu principal do programa'''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()