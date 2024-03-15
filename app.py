import os

restaurantes = [{'nome':'Sapore', 'categoria':'Japonesa', 'ativo':False},
                {'nome':'Pizza Mania', 'categoria':'Italiana', 'ativo':True},
                {'nome':'Vivenda do Camarão', 'categoria':'Nordestina', 'ativo':False}]

def exibir_nome_do_programa():
    ''' Essa função é exibir o nome do programa
    
    print: exibe nome
    '''
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
""")

def exibir_opcoes():
    ''' Essa função é responsavel por exibir as opções de menu ao usuario
    
    print: exibe opções
    '''
    print('1. Cadastrar restaurante')
    print('2. Listar Restaurantes')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    exibir_subtitulo('Obrigado por utilizar nossos serviços\n')

def voltar_ao_menu_principal():
    input('\nPressione uma tecla para retornar ao menu ')
    main()
    
def opcao_invalida():
    '''Essa função é responsavel por nao apresentar erro uando o caracter for invalido'''
    print('Opção invalida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    '''Essa função é responsavel por padronizar a exibição dos subtitulos'''
    os.system('clear')
    linha = '*' * (len(texto) + 4)
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    '''Essa função é responsavel por cadastrar um novo restaurante
    
    inputs:
    - Nome do Restaurante
    - Categoria do Restaurante
    
    outputs:
    - Adciona um novo restaurante a lista de restaurantes
    
    '''
    exibir_subtitulo('Bem-vindo(a) ao cadastro de novos Restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    
    voltar_ao_menu_principal()
    
def listar_restaurantes():
    '''Essa função é responsavel por listar todos os restaurantes cadastrados'''
    exibir_subtitulo('Lista dos restaurantes cadastrados')
    
    print(f'{'Nome do restaurante'.ljust(23)} | {'Categoria'.ljust(20)} | Status ')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f' - {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    
    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    ''' Essa função é responsavel por alternar o status do restaurante the full is deactivated'''
    exibir_subtitulo('Alterando o status do Restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o status: ')
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print(f'O restaurante {nome_restaurante} não foi encontrado!')
               
    voltar_ao_menu_principal()
            
def escolher_opcoes():
    '''Essa função é responsavel exibir as opções do menu'''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        # opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:       
        opcao_invalida()
        
def main():
    os.system('Clear')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()
    
if __name__ == '__main__':
    main()